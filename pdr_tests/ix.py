from clize import run

import ix_interface


def execute_command(command, dataset, product_type=None):
    method = getattr(ix_interface, command)
    method(dataset, product_type)


if __name__ == "__main__":
    run(execute_command)
