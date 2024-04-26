import sys
import re
import inspect
# import json
import ast
# import pickle


class route_args():

    def __init__(self, argv=sys.argv):

        self.__exec(self.__parse(argv))

    def __parse(self, argv):

        print(f"script : {argv[0]}")
        inp_args = argv[1:]
        print(f"inp_args : {inp_args}")

        head = 0
        func_list = []
        for i in range(len(inp_args)+1):

            if (i == len(inp_args)) or (head != i and inp_args[i].startswith("--")):
                # print(f"func : {inp_args[head]}")
                mod_args = self.__func(inp_args[head:i])
                func_list.append(mod_args)
                head = i

        return func_list

    def __func(self, args):

        mod_args = {}
        for i in range(len(args)):
            kwargs_found = re.match("^-(\\S+)=(\\S+)$", args[i])
            if args[i].startswith("--") and inspect.ismethod(getattr(self, args[i][2:])):
                mod_args['name'] = args[i][2:]
                mod_args['args'] = []
                mod_args['kwargs'] = {}
                sign = inspect.signature(getattr(self, args[i][2:]))
                ordered_type_list = list(sign.parameters.items())
                ordered_type_dict = dict(sign.parameters.items())
                # print(ordered_type_list)
                # print(ordered_type_dict)
                kwargs_started = False
            elif kwargs_found:
                key, value = kwargs_found.groups()
                kwarg_type = ordered_type_dict[key].annotation if key in ordered_type_dict.keys(
                ) else None
                if kwarg_type and kwarg_type != str:
                    kwarg_val = self.__type(kwarg_type, value)
                    # print(key, value, kwarg_type, kwarg_val)
                else:
                    kwarg_val = value
                mod_args['kwargs'][key] = kwarg_val
                kwargs_started = True
            else:
                if kwargs_started:
                    raise SyntaxError(
                        f"positional argument follows keyword argument {key}")
                else:
                    arg_type = ordered_type_list[i-1][1].annotation if i-1 < len(
                        ordered_type_list) else None
                    if arg_type and arg_type != str:
                        arg_key = ordered_type_list[i-1][0]
                        arg_val = self.__type(arg_type, args[i])
                        # print(arg_key, args[i], arg_type, arg_val)
                    else:
                        arg_val = args[i]
                    mod_args['args'].append(arg_val)

        return mod_args

    def __type(self, dtype, value):

        if dtype in [int, float]:
            type_casted_value = dtype(value)
        elif dtype in [list, tuple, dict, bool]:
            type_casted_value = ast.literal_eval(value)
        elif dtype in [inspect._empty]:
            type_casted_value = value
        else:
            raise Exception(
                f"Unsupported argument data type : {dtype}, try using basic types ([int, float, list, tuple, dict]) instead")

        return type_casted_value

    def __exec(self, flow):

        # print(json.dumps(flow, indent=2))
        for func in flow:
            func['ret'] = getattr(self, func['name'])(
                *func['args'], **func['kwargs'])
        self.func_list = flow
        # print(json.dumps(flow, indent=2, sort_keys=True))


class arg_ex1(route_args):

    # python demo.py --get_dtypes -inp_int=10 -inp_float=12.5 -inp_str=hello -inp_list=[12,12.56,'hello'] -inp_tuple=(12,12.78,'crud') -inp_dict={'one':1,'two':2,'three':3} -inp_bool=False
    def get_dtypes(self, inp_int: int = 6,
                   inp_float: float = 6.0,
                   inp_str: str = "Six",
                   inp_list: list = [6, 6.0, "Six"],
                   inp_tuple: tuple = (6, 6.0, "Six"),
                   inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"},
                   inp_bool: bool = False) -> str:
        """get_dtypes
        get_dtypes
        get_dtypes
        get_dtypes
        get_dtypes
        get_dtypes
        """
        output = {
            "int": inp_int,
            "float": inp_float,
            "str": inp_str,
            "list": inp_list,
            "tuple": inp_tuple,
            "dict": inp_dict,
            "bool": inp_bool
        }
        # sample 1
        # print(output)
        # return json.dumps(output, indent=2, sort_keys=True)
        return output


if __name__ == '__main__':

    arg_ex1()
