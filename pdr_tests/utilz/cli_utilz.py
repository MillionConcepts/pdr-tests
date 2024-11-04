"""
Helper functions for implementing a command line interface.
"""


import argparse
import inspect
import numbers
import sys
import typing

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
NoneType = type(None)


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


def _pspec_parser(
    param: Parameter,
    parse_fn: Optional[Callable[[str], Any]],
) -> Callable[[str], Any]:
    """
    Subroutine of ParamSpec.__init__.  Derives the function to use to
    parse an argument from a string.

    TODO: List arguments (nargs='*', nargs='+') are not currently
    supported and would help move away from expecting the user to type
    list and dict literals for some options (see ix_interface.py for
    examples).  Well, you can specify a parse function, but then that
    parse function is going to get called on the *list*, which is not
    the right API (it should instead map the parse function / type
    constructor over the list).
    """
    if parse_fn is not None:
        return parse_fn

    name = param.name
    annotation = param.annotation
    default = param.default

    if annotation is Parameter.empty:
        raise ValueError(
            f"{name}: need a type annotation or a parse function"
        )
    if annotation is Any:
        raise ValueError(
            f"{name}: parse function required when type is Any"
        )

    origin = typing.get_origin(annotation)
    if origin is None:
        return annotation

    if origin is Union:
        # Optional[T] aka Union[T, None] is supported, provided the
        # default is None.  Other Union types require a parse function.
        args = typing.get_args(annotation)
        if default is None and len(args) == 2:
            a, b = args
            if a is NoneType and b is not NoneType:
                return b
            if b is NoneType and a is not NoneType:
                return a
        raise ValueError(
            f"{name}: parse function required when type is {annotation}"
        )

    if origin in (list, tuple):
        raise NotImplementedError(
            f"{name}: sorry, not implemented: list parameters"
        )

    raise ValueError(
        f"{name}: don't know how to parse into {annotation}"
    )


class ParamSpec:
    """
    A paramspec defines how to parse one or more command line args into
    a single parameter to some function.  It does this by specifying how
    to call argparse.ArgumentParser.add_argument so that the argument
    parser will parse those arguments into that parameter.  As much
    information as possible is derived from the parameter's name, kind
    (positional, keyword, rest, etc), type annotation, and defaults.
    Only argument types actually used in ix_interface.py are supported.

    The parameter's name will be the name used in the argparse.Namespace
    object returned by parse_args, and also at least one of the names
    it is known by on the command line (except for boolean options that
    default to True, see below).

    Parameters with defaults are optional, parameters with no default
    are required.  This cannot be overridden; in particular you cannot
    specify a mandatory --option.

    By default, a positional-only or positional/keyword parameter will
    be mapped to either a zero-one or one-exactly positional command
    line argument, depending on whether it has a default.  A positional
    rest parameter (*args) will be mapped to a zero-or-more positional
    command line argument.  Keyword-only arguments will be mapped to
    options.  Some of this can be overridden, see below.

    Each command line argument will be converted to an appropriate
    type, based on the declared type of the parameter that receives it.
    For mandatory parameters the conversion target is simply the
    declared type; for optional parameters, it's the non-None
    alternative (i.e. the T in Optional[T]), and for parameters that
    can receive more than one argument, it's the sequence item type.
    The parser can be overridden, see below.

    Boolean parameters have special handling:

    `flag: bool = False` specifies a zero-argument, normally-off
    toggle option spelled `--flag`.

    `flag: bool = True` specifies a zero-argument, normally-*on*
    toggle option spelled `--no-flag`.  Note that in this case the
    Python parameter name (`flag`) will be different from the primary
    command line option name (`--no-flag`).

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

      parse:  Callable which parses the value as desired.  Exceptions
              (of any variety, unlike how argparse does it) will be
              interpreted as signaling some kind of syntax error.
              Must return a value consistent with the type declared
              for the parameter (possibly modified by the effects of
              e.g. nargs='+').

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
        self.parse_arg = _pspec_parser(param, parse)

        spec = {
            "help": help,
            "dest": param.name
        }
        if param.default is not Parameter.empty:
            spec["default"] = param.default
        if const is not None:
            spec["const"] = const

        if nargs is not None:
            spec["nargs"] = nargs
        if choices is not None:
            l_choices = choices if isinstance(choices, list) else list(choices)
            if len(l_choices) > 0:
                spec["choices"] = l_choices

        if action is not None:
            spec["action"] = action
        elif self.parse_arg is bool:
            if spec.get("default", False) is True:
                spec["action"] = "store_false"
                spec["help"] = neg_help
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

        # The name to be used in error messages is the first entry in names
        # that is not a short option.  This will normally be closely related
        # to self.arg_name.
        self.diag_name = next(n for n in self.names
                              if not (len(n) == 2 and n[0] == '-'))

        if metavar is not None:
            spec["metavar"] = metavar
        elif not is_option:
            # For positional arguments, the adjusted parameter name must
            # be specified as 'metavar', and *not* as a positional arg
            # to add_argument, or we will get either an assertion
            # failure in add_argument, or a Namespace object some of
            # whose data cannot be accessed via .attribute.  This has
            # been reported as a bug in argparse at least three times:
            # * https://github.com/python/cpython/issues/59330
            # * https://github.com/python/cpython/issues/95100
            # * https://github.com/python/cpython/issues/117834
            spec["metavar"] = self.names.pop(0)
            assert not self.names

        self.spec = spec

    def add_to_parser(self, ap: argparse.ArgumentParser):
        ap.add_argument(*self.names, **self.spec)


class CLIPreparedCall:
    """
    A prepared call to a function, with all its arguments parsed from
    the command line.  Call run() to actually call the function.

    The return value of the function will be adapted to a process
    exit code, as follows:
       None, True, 0, or "" -> silent successful exit (0)
       False                -> silent unsuccessful exit (1)
       any nonzero number   -> silent unsuccessful exit (clamped to the
                               range [1, 127] and truncated to an int)
       any nonempty string  -> printed to stderr with a newline appended,
                               exit 1
       any other object     -> repr() printed to stderr with a newline
                               appended, exit 1
       any Exception thrown -> str() printed to stderr, with a traceback
                               if print_tracebacks is true, exit 2

    run() does not exit, it returns the exit code.
    """
    def __init__(self, print_traceback, fn, args, kwargs):
        self.print_traceback = print_traceback
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self) -> int:
        """
        Run the wrapped function.
        """
        try:
            rv = self.fn(*self.args, **self.kwargs)
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
            if self.print_traceback:
                import traceback
                traceback.print_exc()
            else:
                xtype = type(e).__name__
                xmsg = str(e)
                if not xmsg:
                    sys.stderr.write(f"{xtype}\n")
                elif xmsg.startswith(xtype):
                    sys.stderr.write(f"{xmsg}\n")
                else:
                    sys.stderr.write(f"{xtype}: {xmsg}\n")

            return 2


class CLIAction:
    """
    Wraps a function and adapts it to take its arguments from the
    command line.  The function's arguments must all have type
    annotations.

    As much information as possible is pulled from the function's type
    signature and docstring; the remainder comes from the "argspec"
    dict, which should have keys matching the function's arguments,
    and values that are dicts of additional arguments to pass to
    argparse.ArgumentParser.add_argument.  There must at least be
    a "help" entry in argspec for each argument; see ParamSpec
    for specifics of what else you can put in argspec.

    It is OK for argspec to have keys that don't correspond to any
    function argument; they will be ignored.  Function arguments
    without matching argspec entries, on the other hand, are an error.
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
        self.ap = None

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
        self.ap = ap
        ap.set_defaults(_subcommand=self)
        for arg in self.argspec:
            arg.add_to_parser(ap)

    def postprocess_args(
        self,
        args: argparse.Namespace,
    ) -> CLIPreparedCall:
        pargs = []
        kwargs = {}
        print_traceback = not not getattr(args, 'debug', False)
        for param in self.argspec:
            rawval = getattr(args, param.arg_name)
            if isinstance(rawval, str) and param.parse_arg is not str:
                try:
                    val = param.parse_arg(rawval)
                except Exception as e:
                    dname = param.diag_name
                    if param.is_option:
                        self.ap.error(f"invalid argument to {dname}: {e}")
                    else:
                        self.ap.error(f"invalid {dname}: {e}")
            else:
                val = rawval
            if param.is_option:
                kwargs[param.arg_name] = val
            else:
                pargs.append(val)

        return CLIPreparedCall(print_traceback, self.fn, pargs, kwargs)


class CLIActionDecorator:
    """
    Decorator which attaches CLIAction instances to callables, with
    support for sharing argspecs across commands.  See CLIAction for
    what an "argspec" is.
    """
    def __init__(self):
        self.common_argspecs = {}

    def add_common_argspecs(self, **specs):
        """
        Record each of the SPECS as a shared argspec: action instances
        will automatically use these specs for any options that they
        don't have their own spec for.
        """
        for name, spec in specs.items():
            if name in self.common_argspecs:
                self.common_argspecs[name].update(spec)
            else:
                self.common_argspecs[name] = spec

    def __call__(self, fn=None, /, **argspec):
        """
        Decorate 'fn' with ARGSPEC plus any shared options.
        The odd signature accommodates being called either as
        @cli_action or as @cli_action(...).
        """
        def do_decorate(fn):
            """
            Subroutine of __call__ that actually does the decorating.
            """
            action = CLIAction(fn, merged_spec)
            setattr(fn, 'cli_action', action)
            return fn

        if fn is None:
            merged_spec = self.common_argspecs.copy()
            merged_spec.update(argspec)
            return do_decorate
        else:
            assert not argspec
            merged_spec = self.common_argspecs
            return do_decorate(fn)


cli_action = CLIActionDecorator()


class CLIDispatcher:
    """
    An instance of this class is responsible for parsing command
    line arguments to one of a set of actions and dispatching to the
    appropriate runner function.  Actions are defined by scanning
    one or more modules for callables decorated with @cli_action.
    """

    def __init__(self, description, *modules):
        ap = argparse.ArgumentParser(description=description)
        ap.add_argument("--debug", action="store_true",
                        help="Enable Python-level debugging")
        cmds = ap.add_subparsers(required=True, metavar="action")
        for m in modules:
            for name, obj in m.__dict__.items():
                if callable(obj) and hasattr(obj, 'cli_action'):
                    obj.cli_action.add_to_parser(cmds)
        self.ap = ap

    def parse_args(self, arguments = None):
        """
        Parse command line arguments from sys.argv.
        If ARGUMENTS is not None, it should be a list of strings;
        command line arguments are parsed from that list *instead of*
        from sys.argv.
        """
        args = self.ap.parse_args(arguments)
        return args._subcommand.postprocess_args(args)
