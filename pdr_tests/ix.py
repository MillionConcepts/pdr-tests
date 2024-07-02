"""
Tool for sorting and indexing PDS data and testing that PDR
can still read that data.

For details of each action use 'ix <action> --help'.
"""

import sys

from pdr_tests import ix_interface
from pdr_tests.utilz.ix_utilz import console_and_log
from pdr_tests.utilz.cli_utilz import CLIDispatcher


def cli_main():
    cli = CLIDispatcher(__doc__, ix_interface)
    cli.parse_args().run()


if __name__ == "__main__":
    sys.exit(cli_main())
