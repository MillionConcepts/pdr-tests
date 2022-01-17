"""These should be database file names that contain the relevant file information from the spider/scrapers."""
geomro = 'geomro_size_corrected.csv'

"""This is a dictionary of information about each file type:
    dataset: the name of the dataset type (this will be the name of the folder these data are downloaded into
    and the name of the dataset in datasets.py for testing
    database_file: the database file that contains the file information for this data type. for some mission this will
    all be the same, others are spread out between nodes or scraping sessions
    fn_must_contain: a list of strings that must be in this file name to differentiate it from the other types in the
    database file
    url_must_contain: an optional additional list of strings that must be in the url to differentiate this from other
    types in the database file."""

file_information = {'EDR': {'database': geomro,
                            "fn_must_contain": ['.img'],
                            "url_must_contain": ['/edr/'],
                            "label": "D"},
                    'CDR': {'database': geomro,
                            "fn_must_contain": ['.img'],
                            "url_must_contain": ['/cdr/'],
                            "label": "D"},
                    'DDR': {'database': geomro,
                            'fn_must_contain': ['.img'],
                            'url_must_contain': ['/ddr/'],
                            "label": "D"},
                    'LDR': {'database': geomro,
                            'fn_must_contain': ['.img'],
                            'url_must_contain': ['/ldr/'],
                            "label": "D"},
                    'TRDR': {'database': geomro,
                             'fn_must_contain': ['.img'],
                             'url_must_contain': ['/trdr/'],
                             "label": "D"},
                    'MRDR': {'database': geomro,
                             'fn_must_contain': ['.img'],
                             'url_must_contain': ['/mrdr/'],
                             "label": "D",
                             },
                    'TER': {'database': geomro,
                            'fn_must_contain': ['.img'],
                            'url_must_contain': ['/ter/'],
                            "label": "D"
                            },
                    'MTRDR': {'database': geomro,
                              'fn_must_contain': ['.img'],
                              'url_must_contain': ['/mtrdr/'],
                              "label": "D",
                              },
                    'speclib': {'database': geomro,
                                'fn_must_contain': ['.tab'],
                                'url_must_contain': ['speclib-v1', '/data/'],
                                'label': "A"},
                    'typespec': {'database': geomro,
                                 'fn_must_contain': ['.tab'],
                                 'url_must_contain': ['typespec-v1', '/data/'],
                                 'label': "D"},
                    }
