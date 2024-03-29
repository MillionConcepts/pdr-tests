import sys

import fire

import ix_interface
from utilz.ix_utilz import console_and_log


def execute_command(command, dataset, product_type=None):
    method = getattr(ix_interface, command)
    method(dataset, product_type)


def handle_call():
    if len(sys.argv) < 2:
        return ix_interface.ix_help()
    try:
        command = sys.argv[1]
        assert command in ix_interface.COMMANDS, (
            f"{command} not " f"in {ix_interface.COMMANDS}"
        )
    except (IndexError, AttributeError, AssertionError) as ex:
        print(ex)
        return ix_interface.ix_help()
    sys.argv = sys.argv[1:]
    console_and_log(f'----INITIATING IX {command}----', quiet=True)
    try:
        fire.Fire(getattr(ix_interface, command))
    except Exception as ex:
        console_and_log(f'unrecoverable exception: ({type(ex)}: {ex})')
        raise


if __name__ == "__main__":
    handle_call()
