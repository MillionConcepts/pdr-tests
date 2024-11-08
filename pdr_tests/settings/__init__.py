"""
Persistent configuration for pdr-tests.

To learn where to put a config file and what you can write in it,
consult the docstring for IxSettings and the comments above each of
IxSettings' data attributes.  The docstring for expand_path may also
be helpful.
"""

import dataclasses
import functools
import os
import sys
import typing
import warnings
import yaml

from dataclasses import dataclass, Field
from pathlib import Path
from typing import Any, Optional, TypeVar, Union

@functools.cache
def environ_path_with_default(var: str) -> Path:
    """
    Subroutine of (and mutually recursive with) expand_path.
    Look up VAR in os.environ.  If it is set with a nonempty
    value, return expand_path(os.environ[VAR]).  If it is
    not set or empty, substitute a default value if possible.
    """
    pth = os.environ.get(var, "")
    if pth:
        return expand_path(pth)

    if var == "HOME":
        return Path.home()
    if var == "XDG_CONFIG_HOME":
        return Path.home() / ".config"
    if var == "XDG_CACHE_HOME":
        return Path.home() / ".cache"
    if var == "PDR_TESTS_ROOT":
        return Path(__file__).parent.parent
    if var == "TMPDIR":
        return "/tmp"

    raise ValueError(f"env var {var} is not set")


def expand_path(pth: Union[Path, str]) -> Path:
    """
    Canonicalize a user-supplied path PTH.  Absolute paths are
    processed through Path.resolve but otherwise left unmolested.
    Relative paths are checked for several possible special first
    components, in this order:

    - If the first component is $NAME or ${NAME} where NAME is the
      name of an environment variable with a nonempty value, then the
      value of that environment variable is processed recursively
      through this function and the remainder of PTH is taken as
      relative to the result.  Certain environment variables have
      default values that are used if they are unset or empty,
      see environ_path_with_default.

    - If the first component is exactly '~' then the remainder of the
      path is resolved relative to the user's home directory (same as
      for $HOME).  ~user notation is not recognized.

    - If the first component is exactly '.' or '..' then the path
      *including* the first component is resolved relative to the
      current working directory.

    - All other paths are resolved relative to PDR_TESTS_ROOT.
      This behavior is deprecated; in the future such paths
      may be resolved relative to the current working directory instead.

    In all cases the final result is converted to an absolute
    physical path via Path.resolve().
    """

    if not isinstance(pth, Path):
        pth = Path(pth)
    if pth.is_absolute():
        return pth.resolve()

    first = pth.parts[0]

    if first == "~":
        return Path(Path.home(), *pth.parts[1:]).resolve()

    if first[0] == "$":
        var = first[1:]
        if var and var[0] == "{" and var[-1] == "}":
            var = var[1:-1]
        return Path(environ_path_with_default(var), *pth.parts[1:]).resolve()

    if first == "." or first == "..":
        return pth.resolve()

    warnings.warn(
        f"resolving {pth} relative to PDR_TESTS_ROOT - may change in the future"
    )
    return (environ_path_with_default("PDR_TESTS_ROOT") / pth).resolve()


class InvalidSettingError(Exception):
    """
    Exception thrown out of IxSettings.__init__ when a setting is invalid.
    """
    def __init__(
        self,
        *args: Any,
        setting: str,
        key: Optional[str] = None,
        **kwargs: Any
    ):
        super().__init__(*args, **kwargs)
        self.setting = setting
        self.key = key

    def __str__(self) -> str:
        if self.key is None:
            msg = f"invalid setting for {self.setting}"
        else:
            msg = f"invalid setting for {self.setting}[{self.key}]"
        if self.__cause__:
            msg += f": {self.__cause__}"
        return msg


def postprocess_field(field: Field, val: Any) -> Any:
    """
    Coerce VAL to the expected type of FIELD if possible.
    Throws InvalidSettingError if this is not possible.
    Only the field types actually used by IxSettings are implemented.
    """
    xtype = typing.get_origin(field.type)
    if xtype is None:
        xtype = field.type
    badkey = None
    try:
        if xtype is Path:
            if not isinstance(val, (Path, str)):
                raise TypeError("must be a Path or string")
            return expand_path(val)

        elif xtype is Union:
            # for the case we actually use, Optional[str],
            # no coercion will help
            valid_types = typing.get_args(field.type)
            if not isinstance(val, valid_types):
                options = ", ".join("None" if c is type(None)
                                    else c.__name__
                                    for c in valid_types)
                raise TypeError(f"must be one of: {options}")
            return val

        elif xtype is dict:
            # for the case we actually use, dict[str, str],
            # no coercion will help
            xkeytype, xvaltype = typing.get_args(field.type)
            for k, v in val.items():
                if not isinstance(k, xkeytype):
                    badkey = k
                    raise TypeError(
                        f"key must be a {xkeytype.__name__}"
                    )
                if not isinstance(v, xvaltype):
                    badkey = k
                    raise TypeError(
                        f"value must be a {xvaltype.__name__}"
                    )
            return val

        else:
            raise NotImplementedError(
                f"coercion to {field.type!r} for {field.name}"
            )

    except (TypeError, ValueError) as e:
        raise InvalidSettingError(setting=field.name, key=badkey) from e


# Return type of IxSettings.load. typing.Self is new in 3.11 so we can't use it.
IxSettingsT = TypeVar("IxSettingsT", bound="IxSettings")


@dataclass(frozen=True)
class IxSettings:
    """
    Attributes of this class are configurable settings for the 'ix' tool.

    To configure them, create a file $XDG_CONFIG_HOME/pdr/ix.conf
    (if you haven't set it, XDG_CONFIG_HOME defaults to ~/.config)
    containing a YAML document whose top-level construct is a mapping
    giving values for the settings you want to adjust.

    All Path-type attributes are processed through expand_path, meaning
    that environment variables and '~' can be used as the first component
    of each path; see that function for details.
    """

    #: Root of directory tree for dumping "browse products"
    #: (data products converted to easily inspectable formats)
    browse_root: Path = "$PDR_TESTS_ROOT/browse"

    #: Root of directory tree holding a local copy of the test corpus.
    data_root: Path = "$PDR_TESTS_ROOT/data"

    #: Directory containing manifest files, which catalogue the
    #: complete PDS archive
    manifest_dir: Path = "$PDR_TESTS_ROOT/node_manifests"

    #: Path to concatenated filename table used by ix find
    filename_table_path: Path = (
        "$PDR_TESTS_ROOT/node_manifests/filenames.parquet"
    )

    #: Directory to write tracker logs to.
    tracker_log_dir: Path = "$PDR_TESTS_ROOT/.tracker_logs"

    #: S3 bucket holding the complete test corpus.
    #: Currently used only by 'ix finalize'.
    test_corpus_bucket: Optional[str] = None

    #: Additional request headers to send when downloading
    #: PDS files over HTTP.  You should probably set User-Agent
    #: to a value that identifies you and distinguishes you from
    #: a generic python-based web crawler.
    headers: dict[str, str] = dataclasses.field(default_factory=dict)
    # n.b. @dataclass does not accept 'headers: dict[str, str] = {}'

    def __post_init__(self):
        """
        Post-init hook, ensures all field values have their expected
        types and resolves relative paths using expand_path.
        """
        for field in dataclasses.fields(self):
            object.__setattr__(
                self,
                field.name,
                postprocess_field(field, getattr(self, field.name))
            )

    @classmethod
    def load(cls: type, config: Union[str, Path, None] = None) -> IxSettingsT:
        """
        Factory method, creates a settings object from user configuration.

        If the file specified by 'config' exists, we load it as YAML,
        with the top-level object expected to be a dictionary.  When
        'config' is None, it defaults to $XDG_CONFIG_HOME/pdr/ix.conf.

        If that file does not exist, but $PDR_TESTS_ROOT/settings/user.py
        does, we load it as a Python module and copy its globals;
        since this is for backward compatibility, its location is not
        configurable.
        """
        params = {}
        source = None

        if config is None:
            config = expand_path("$XDG_CONFIG_HOME/pdr/ix.conf")
        try:
            with open(config, "rt") as fp:
                user_settings = yaml.safe_load(fp)
            for setting in dataclasses.fields(cls):
                if setting.name in user_settings:
                    params[setting.name] = user_settings[setting.name]
            source = config
        except FileNotFoundError:
            pass

        try:
            from pdr_tests.settings import user
            for setting in dataclasses.fields(cls):
                for name in [setting.name, setting.name.upper()]:
                    if hasattr(user, name):
                        params[setting.name] = getattr(user, name)
                        break
            source = user.__file__
        except ImportError:
            pass

        # Instantiating cls(**params) validates all the settings.
        # If it throws, we convert the exception to a warning, delete
        # the offending field, and retry.  This loop must eventually
        # terminate because params must eventually be empty.  Weeding
        # out all the bad settings this way is quadratic in the size
        # of params, but anyone who writes dozens of invalid settings
        # in their config file has only themselves to blame.
        while True:
            try:
                return cls(**params)
            except InvalidSettingError as e:
                sys.stderr.write(f"{source}: warning: {e}\n")
                if e.key is not None:
                    del params[e.setting][e.key]
                else:
                    del params[e.setting]


SETTINGS = IxSettings.load()
