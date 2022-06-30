
import sys
import re
import inspect
import ast


class cli_router():

    def __init__(self, argv=sys.argv):

        derived_class = self.__class__.__name__
        base_class = cli_router.__name__
        if derived_class != base_class:
            if argv[1].startswith("--"):
                method_name = argv[1][2:]
            else:
                raise SyntaxError(
                    f"function name should precede positional arguments, eg : --run")
            method_obj = getattr(self, method_name)
            if inspect.ismethod(method_obj):
                args, kwargs = self.__get_args(
                    argv[2:], inspect.signature(method_obj))
                method_obj(*args, **kwargs)
            else:
                raise SyntaxError(
                    f"class {derived_class} derived from {base_class} should have method 'run' defined")
        else:
            raise SyntaxError(
                f"{base_class} should be used as parent class only")

    def __get_args(self, inp_args, sign):

        args = []
        kwargs = {}
        kwargs_started = False
        ordered_type_list = list(sign.parameters.items())
        ordered_type_dict = dict(sign.parameters.items())
        for i in range(len(inp_args)):
            kwargs_found = re.match("^-(\\S+)=(\\S+)$", inp_args[i])
            if kwargs_found:
                key, value = kwargs_found.groups()
                kwarg_type = ordered_type_dict[key].annotation if key in ordered_type_dict.keys(
                ) else None
                if kwarg_type and kwarg_type != str:
                    kwarg_val = ast.literal_eval(value)
                    if(type(kwarg_val) != kwarg_type):
                        raise SyntaxError(
                            f"Input for {key} should be of type {kwarg_type.__name__}")
                else:
                    kwarg_val = value
                kwargs[key] = kwarg_val
                kwargs_started = True
            else:
                if kwargs_started:
                    raise SyntaxError(
                        f"positional argument follows keyword argument {key}")
                else:
                    arg_type = ordered_type_list[i][1].annotation if i < len(
                        ordered_type_list) else None
                    if arg_type and arg_type != str:
                        arg_key = ordered_type_list[i][0]
                        arg_val = ast.literal_eval(inp_args[i])
                        if(type(arg_val) != arg_type):
                            raise SyntaxError(
                                f"Input for {arg_key} should be of type {arg_type.__name__}")
                    else:
                        arg_val = inp_args[i]
                    args.append(arg_val)

        return args, kwargs


if __name__ == "__main__":

    cli_router()
