from functools import partial
from pathlib import Path
from re import Pattern
from typing import Optional, Union

import pandas as pd
from dustgoggles.structures import unnest
from hostess.directory import do_magic, index_breadth_first, LSFrame
from multidict import MultiDict
from rich.progress import Progress

import pdr


def open_attached(fn):
    return pdr.read(fn, label_fn=fn, skip_existence_check=True)


def scan_headers(
    root: Union[str, Path] = None,
    manifest: Optional[LSFrame] = None,
    path_regex: Optional[Union[str, Pattern]] = None,
    attached_labels: bool = True,
    level_sep: str = "",
    magic: bool = False,
    **read_kwargs
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    construct a DataFrame from the metadata of all products in a directory
    tree or a preconstructed DataFrame of paths.

    Example of usage:

        >>> meta, files, glitches = scan_headers(
        ...     root='pdr_tests/data',
        ...     path_regex='.*IMG.*',
        ...     attached_labels=False,
        ...     magic=True
        ... )
        scanning... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
        >>> meta['INSTRUMENT_NAME'].unique()[3:5]
        array(['REAR HAZARD AVOIDANCE CAMERA LEFTSTRING B',
            'FRONT HAZARD AVOIDANCE CAMERA LEFTSTRING B'], dtype=object)
        >>> glitches.iloc[10].to_dict()
        {'path': 'data/ch1/M3_L2/M3T20090418T074719_V01_RFL.IMG',
         'err': "ValueError: Can't load this product's metadata: 'utf-8' codec
             can't decode byte 0xc0 in position 1: invalid start byte, <class
             'UnicodeDecodeError'>"}
        >>> files['info'].unique()[38:43]
        array(['Targa image data 16 x 16 x 16 +16 +16 "\\020"',
           'DOS 2.0-3.2 backed up sequence 47 of file /',
           'PDP-11 UNIX/RT ldp',
           'Tower/XP rel 2 object not stripped - version 505',
           'TTComp archive data; binary; 4K dictionary'], dtype=object)

        >>> np.nanmean(
        ...     meta[
        ...         meta.columns[meta.columns.str.match('.*IMAGE.*LINES.*')]
        ...     ]
        ...     .replace('NULL', 'nan')
        ...     .values.astype(float)
        ...     .ravel()
        ... )
        1722.8669796557122

    Args:
        root: root of directory tree to scan. this or path_df must be given.
        path_regex: if not None, scan only files matching this regex.
        manifest: DataFrame of paths to scan. this or root must be given.
        attached_labels: if True, assume all labels are attached. improves
            scanning speed, but obviously requires labels to be attached.
        level_sep: optional extra separator character to distinguish levels
            of nested label structures in output column names (will be added
            to a '_')
        magic: if True, add filetype information, as given by `file`, to the
            file manifest. may be very slow or not work on some systems.
        **read_kwargs: additional kwargs to pass to pdr.read

    Returns:
        tuple whose elements are:
            0: DataFrame containing flattened metadata from all readable files
            1: file manifest DataFrame
            2: DataFrame with information on failed reads
    """
    if root is None and manifest is None:
        raise TypeError(
            "must pass a root directory or a preconstructed TreeFrame"
        )
    if manifest is None:
        manifest = pd.DataFrame(index_breadth_first(root))
    if len(manifest) == 0:
        raise FileNotFoundError("no files in tree")
    manifest = manifest.loc[manifest['directory'] == False]
    if path_regex is not None:
        manifest = manifest.loc[manifest['path'].str.match(path_regex)]
        if len(manifest) == 0:
            raise FileNotFoundError("no files in tree match regex")
    if magic is True:
        manifest = do_magic(manifest)
    if attached_labels is True:
        reader = partial(open_attached, **read_kwargs)
    else:
        reader = partial(pdr.read, skip_existence_check=True, **read_kwargs)
    glitched, metadatas = [], []
    with Progress() as progress:
        scan_task = progress.add_task(
            "[green]scanning...", total=len(manifest)
        )
        n = 0
        for _, product in manifest.iterrows():
            try:
                metadata = reader(product['path']).metadata
                if len(metadata) == 0:
                    glitched.append(
                        {'path': product['path'], 'err': 'no metadata found'}
                    )
                else:
                    metadata['path'] = product['path']
                    metadatas.append(metadata)
                del metadata
            except KeyboardInterrupt:
                raise
            except Exception as ex:
                glitched.append(
                    {
                        'path': product['path'],
                        'err': f'{type(ex).__name__}: {ex}'
                    }
                )
            if n % 100 == 0:
                progress.update(scan_task, advance=100)
            n += 1
        flat = pd.DataFrame([
            unnest(metadata, mtypes=(dict, MultiDict), escape=level_sep)
            for metadata in metadatas
        ])
        for c in flat.columns:
            try:
                flat[c] = flat[c].str.strip('"')
            except AttributeError:
                continue
        return flat.copy(), manifest, pd.DataFrame(glitched)
