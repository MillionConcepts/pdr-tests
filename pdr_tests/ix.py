import sys

from clize import run

import ix_interface


def execute_command(command, dataset, product_type=None):
    method = getattr(ix_interface, command)
    method(dataset, product_type)


if __name__ == "__main__":
    try:
        command = sys.argv[1]
        assert command in ix_interface.COMMANDS, print(f"{command} not in {ix_interface.COMMANDS}")
        run(getattr(ix_interface, command), args=sys.argv[1:])
    except (IndexError, AttributeError, AssertionError) as ex:
        print(ex)
        ix_interface.ix_help()

