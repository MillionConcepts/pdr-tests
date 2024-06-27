"""
Tool for sorting and indexing PDS data and testing that PDR
can still read that data.

For details of each action use 'ix <action> --help'.
"""

import sys

from . import ix_interface
from .utilz.ix_utilz import console_and_log
from .utilz.cli_utilz import CLIDispatcher

def cli_main():
    cli = CLIDispatcher(__doc__, ix_interface)
    args = cli.parse_args()
    return cli.run(args)

if __name__ == "__main__":
    sys.exit(cli_main())
