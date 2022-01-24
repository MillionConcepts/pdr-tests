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

file_information = {'odf': {'database': geomro,
                            "fn_must_contain": ['.odf'],
                            "url_must_contain": ['/odf/'],  # this is probably unnecessary, but it's here anyway
                            "label": "D"},
                    'rsr': {'database': geomro,
                            "fn_must_contain": ['.1a1'],
                            "url_must_contain": ['/rsr/'],
                            "label": "D"},
                    'tnf': {'database': geomro,
                            'fn_must_contain': ['.tnf'],
                            'url_must_contain': ['/tnf/'],  # same thing here
                            "label": "D"},
                    'rsdmap': {'database': geomro,
                               'fn_must_contain': ['.img'],
                               'url_must_contain': ['/rsdmap/'],
                               "label": "D"},
                    'shadr': {'database': geomro,
                              'fn_must_contain': ['.tab'],
                              'url_must_contain': ['/shadr/'],
                              "label": "D"},
                    'shbdr': {'database': geomro,
                              'fn_must_contain': ['.dat'],
                              'url_must_contain': ['/shbdr/'],
                              "label": "D",
                              },
                    }
