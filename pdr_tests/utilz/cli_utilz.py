"""
Helper functions for implementing a command line interface.
"""


import argparse
import inspect
import numbers
import sys

from inspect import Parameter, Signature
from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Optional,
    Tuple,
    Union,
)


def _pspec_arity(
    kind: inspect._ParameterKind,
    default: Any,
    nargs: Union[None, int, str]
) -> Tuple[Union[None, int, str], bool]:
    """
    Subroutine of ParamSpec.__init__.  Report whether a parameter
    should be treated as a positional or an option argument.
    Also, adjust 'nargs' if necessary.
    """
    # We trust 'nargs' supplied by the user.  argparse infers an
    # appropriate 'nargs' in most cases if one is not supplied.
    if kind in (Parameter.POSITIONAL_ONLY,
                Parameter.POSITIONAL_OR_KEYWORD):
        is_option = False
        if nargs is None and default is not Parameter.empty:
            nargs = '?'

    elif kind == Parameter.VAR_POSITIONAL:
        is_option = False
        if nargs is None:
            nargs = '*'

    elif kind == Parameter.KEYWORD_ONLY:
        is_option = True

    elif kind == Parameter.VAR_KEYWORD:
        raise ValueError("`**kwargs` parameters are not supported")
    else:
        raise ValueError(f"{kind.name} parameters are not supported")

    return nargs, is_option


def _pspec_names(
    name: str,
    sopts: Union[None, str, Iterable[str]],
    lopts: Union[None, str, Iterable[str]],
    is_option: bool
) -> List[str]:
    """
    Subroutine of ParamSpec.__init__.  Computes the names list for
    a call to ArgumentParser.add_argument.
    """
    def adjust_name(n, prefix):
        short = ({ "": False, "--": False, "-": True })[prefix]
        if (
                " " in n
                or not n.isprintable()
                or n.startswith("_")
                or n.startswith("-")
                or (short and len(n) != 1)
                or (not short and len(n) < 2)
        ):
            label = ({
                "": "positional argument name",
                "-": "short option",
                "--": "long option",
            })[prefix]
            raise ValueError(f"{n!r} cannot be used as a {label}")
        return prefix + n.replace("_", "-")

    if is_option:
        names = set()
        names.add(adjust_name(name, "--"))

        if lopts is None:
            pass
        elif isinstance(lopts, str):
            names.add(adjust_name(lopts, "--"))
        else:
            names.update(adjust_name(l, "--") for l in lopts)

        if sopts is None:
            pass
        elif isinstance(sopts, str):
            names.add(adjust_name(sopts, "-"))
        else:
            names.update(adjust_name(s, "-") for s in sopts)

        return sorted(names, key = lambda n: (n.startswith("--"), n))
    else:
        if sopts is not None or lopts is not None:
            raise ValueError(
                "positional arguments can only have one name"
            )
        return [adjust_name(name, "")]


class ParamSpec:
    """
    A paramspec defines how to parse one or more command line
    arguments into a single parameter to some function.  It does this
    by specifying how to call argparse.ArgumentParser.add_argument
    so that the ArgumentParser will parse those arguments into that
    parameter.  As much information as possible is derived from the
    parameter's name, type annotation, and defaults:

      - Parameters with defaults are optional, parameters with no
        default are required.  This cannot be overridden; in
        particular you cannot specify a mandatory --option.

      - By default, a positional-only or positional/keyword parameter
        will be mapped to either a zero-one or one-exactly positional
        command line argument, depending on whether it has a default.
        A positional rest parameter (*args) will be mapped to a
        zero-or-more positional command line argument.  Keyword-only
        arguments will be mapped to options.  Some of this can be
        overridden, see below.

      - The parameter's type will be used as the conversion type for
        add_argument, unless you override it, see below.

      - The parameter's name will be the name used in the argparse.Namespace
        object returned by parse_args, and also at least one of the
        names it is known by on the command line.

      - Appropriate argparse action, nargs, and const settings are
        deduced from the type and default if possible.  In particular,
        `flag: bool = False/True` is sufficient to set up --flag as a
        zero-argument boolean option whose default is false or true.

    The keyword arguments to __init__ supply additional information
    that may be required:

      help:   --help description of the parameter.  Required.
              Use argparse.SUPPRESS if you don't want the parameter
              to be documented.

      short:  None, a one-character string, or a list of one-character
              strings, specifying short options to be mapped to this
              parameter (e.g. short="x" means -x maps to this parameter).
              None, or an empty list, mean this parameter should not
              correspond to any short options.  It is an error to specify
              short option names for a positional argument.

      long:   None or a list of strings, specifying *additional* long
              options to be mapped to this parameter (besides the name).
              It is an error to specify long option names for a positional
              argument.

      parse:  Parser callable to supply as the type argument to
              add_argument.  Must return a value consistent with the
              type declared for the parameter (possibly modified by
              the effects of e.g. nargs='+').

      action, nargs, const, choices, metavar:
              Override the values used for these arguments to
              add_argument.  See argparse documentation for details.
    """
    def __init__(
        self,
        param: Parameter,
        *,
        help: str,
        neg_help: Optional[str] = None,
        metavar: Optional[str] = None,
        short: Union[None, str, Iterable[str]] = None,
        long: Union[None, str, Iterable[str]] = None,
        parse: Optional[Callable[[str], Any]] = None,
        action: Optional[str] = None,
        nargs: Union[None, int, str] = None,
        const: Optional[Any] = None,
        choices: Optional[Iterable[Any]] = None,
    ):
        nargs, is_option = _pspec_arity(param.kind, param.default, nargs)
        self.names = _pspec_names(param.name, short, long, is_option)
        self.arg_name = param.name
        self.is_option = is_option

        spec = {
            "help": help,
            "dest": param.name
        }
        if neg_help is not None:
            spec["neg_help"] = neg_help
        if metavar is not None:
            spec["metavar"] = metavar
        elif not is_option:
            # for positional arguments, the adjusted parameter name has
            # to be specified as 'metavar', and *not* as a positional
            # argument to .add_argument(), or we will get either an
            # assertion failure in .add_argument, or a Namespace object
            # some of whose data cannot be accessed via .attribute.
            # see https://github.com/python/cpython/issues/117834
            # and
            spec["metavar"] = self.names.pop(0)
            assert not self.names

        if nargs is not None:
            spec["nargs"] = nargs
        if parse is not None:
            spec["type"] = parse
        elif param.annotation is not Parameter.empty:
            spec["type"] = param.annotation
        if choices is not None:
            l_choices = choices if isinstance(choices, list) else list(choices)
            if len(l_choices) > 0:
                spec["choices"] = l_choices

        if param.default is not Parameter.empty:
            spec["default"] = param.default
        if const is not None:
            spec["const"] = const

        if action is not None:
            spec["action"] = action
        elif spec["type"] is bool:
            del spec["type"]
            if spec.get("default", False) is True:
                spec["action"] = "store_false"
                spec["help"] = spec["neg_help"]
                for i in range(len(self.names)):
                    if (
                            self.names[i].startswith("--")
                            and not self.names[i].startswith("--no-")
                    ):
                        self.names[i] = "--no-" + self.names[i][2:]
            else:
                spec["action"] = "store_true"
                for i in range(len(self.names)):
                    if self.names[i].startswith("--no-"):
                        self.names[i] = "--" + self.names[i][5:]
            spec.pop("neg_help", None)

        self.spec = spec

    def add_to_parser(self, ap: argparse.ArgumentParser):
        ap.add_argument(*self.names, **self.spec)


class CLIAction:
    """
    Wraps a function and adapts it to take its arguments from the command
    line.  As much information as possible is pulled from the function's
    type signature and docstring; the remainder comes from the "argspec"
    dictionary, which should have keys matching the function's arguments,
    and values that are dictionaries of additional arguments to pass to
    argparse.ArgumentParser.add_argument.  It is OK for this dictionary
    to have keys that don't correspond to any function argument; they
    will be ignored.  Function arguments with no matching argspec entry,
    on the other hand, are an error.
    """

    def __init__(self, fn, argspec):
        if not callable(fn):
            raise TypeError(f'{fn!r} is not callable')
        self.fn = fn
        self.cmd_name = fn.__name__.replace('_', '-')
        self.cmd_help = inspect.getdoc(fn)
        self.argspec = [
            ParamSpec(param, **argspec[param.name])
            for param in inspect.signature(fn).parameters.values()
        ]

    def add_to_parser(self, sp: argparse._SubParsersAction) -> None:
        """
        Add this subcommand to a top-level argument parser.
        The SP argument must be an object returned by
        argparse.ArgumentParser.add_subparsers.

        After calling parse_args() on the top-level argument parser,
        call sys.exit(args._subcommand.run(args)) where `args` is the
        namespace object returned by parse_args.
        """
        ap = sp.add_parser(
            self.cmd_name,
            help=self.cmd_help
        )
        ap.set_defaults(_subcommand=self)
        for arg in self.argspec:
            arg.add_to_parser(ap)

    def run(self, args: argparse.Namespace) -> int:
        """
        Run the wrapped function, supplying arguments from 'args'.

        The return value of the function will be adapted to a process
        exit code, as follows:
           None, True, 0, or "" -> silent successful exit (0)
           False                -> silent unsuccessful exit (1)
           any nonzero number   -> silent unsuccessful exit (clamped to the
                                   range [1, 127] and truncated to an int)
           any nonempty string  -> printed to stderr with a newline appended,
                                   exit 1
           any other object     -> repr() printed to stderr, exit 1
           any Exception thrown -> str() printed to stderr, with backtrace
                                  if args.debug exists and is truthy, exit 2
        """
        import pprint
        pprint.pprint(args.__dict__)

        pargs = []
        kwargs = {}
        for param in self.argspec:
            if param.is_option:
                kwargs[param.arg_name] = getattr(args, param.arg_name)
            else:
                pargs.append(getattr(args, param.arg_name))

        pprint.pprint({
            "call": self.fn.__name__,
            "p": pargs,
            "k": kwargs
        })
        #sys.exit(0)

        try:
            rv = self.fn(*pargs, **kwargs)
            if rv is None or rv is True or rv == 0 or rv == "":
                return 0
            elif rv is False:
                return 1
            elif isinstance(rv, numbers.Real):
                return max(1, min(127, round(rv)))
            elif isinstance(rv, str):
                sys.stderr.write(f"{rv}\n")
                return 1
            else:
                sys.stderr.write(f"{repr(rv)}\n")
                return 1

        except Exception as e:
            if getattr(args, 'debug', False):
                import traceback
                traceback.print_exc()
            else:
                sys.stderr.write(f"{e}\n")
            return 2


def cli_action(**argspec):
    """
    Decorator which attaches a CLIAction instance to a callable.
    See CLIAction for details of the argspec.
    """
    def cli_action_inner(fn):
        subcommand = CLIAction(fn, argspec)
        setattr(fn, 'cli_command', subcommand)
        return fn
    return cli_action_inner


class CLIDispatcher:
    """
    An instance of this class is responsible for parsing command
    line arguments to one of a set of actions and dispatching to the
    appropriate runner function.  Actions are defined by scanning
    one or more modules for callables decorated with @cli_action.
    """

    def __init__(self, description, *modules):
        ap = argparse.ArgumentParser(description=description)
        cmds = ap.add_subparsers(
            required=True,
            metavar="<action>",
            title="actions"
        )
        for m in modules:
            for name, obj in m.__dict__.items():
                if callable(obj) and hasattr(obj, 'cli_command'):
                    obj.cli_command.add_to_parser(cmds)
        self.ap = ap

    def parse_args(self):
        return self.ap.parse_args()

    def run(self, args: argparse.Namespace) -> int:
        return args._subcommand.run(args)
