import sys
import re
import inspect
import json
import ast
# import pickle
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml


class route_args():

    def __init__(self, argv=sys.argv):

        def_func_name = 'parse_args'
        if len(argv) == 1:
            self.returned = None
            self.__doc(def_func_name)
        else:
            func_schema = self.__func2schema(def_func_name)
            args_schema = self.__args2schema(def_func_name, argv[1:])
            args, kwargs = self.__solve_schema(
                func_schema[def_func_name], args_schema[def_func_name])
            if inspect.ismethod(getattr(self, def_func_name)):
                self.returned = self.__func(def_func_name, args, kwargs)
                if type(self.returned) != func_schema['ret_type']:
                    print(
                        f"WARNING : '{def_func_name}' returns '{type(self.returned).__name__}', but defined to return '{func_schema['ret_type'].__name__}'")

        # print(args)
        # print(kwargs)
        # print(self.returned)

    def __func(self, func, args, kwargs):

        returned = getattr(self, func)(*args, **kwargs)
        return returned

    def __type(self, dtype, value):

        if dtype == str:
            return value

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

    def __solve_schema(self, func, inps):

        mod_args = []
        for i in range(len(inps['args'])):
            type = func['kwargs'][func['args'][i]]['type']
            val = inps['args'][i]
            mod_args.append(self.__type(type, val))

        mod_kwargs = {}
        for key, val in inps['kwargs'].items():
            type = func['kwargs'][key]['type']
            val = val['value']
            mod_kwargs[key] = self.__type(type, val)

        return mod_args, mod_kwargs

    def __func2schema(self, func_name):

        sign = inspect.signature(getattr(self, func_name))
        args = []
        kwargs = {}
        for key, val in sign.parameters.items():
            if val.default == inspect._empty:
                kwargs[key] = {'value': '_empty',
                               'type': val.annotation}
            else:
                kwargs[key] = {'value': val.default,
                               'type': val.annotation}
            args.append(key)

        if sign.return_annotation == inspect._empty:
            ret_anno = '_empty'
        else:
            ret_anno = sign.return_annotation

        func_dict = {
            func_name: {
                'args': args,
                'kwargs': kwargs
            },
            'ret_type': ret_anno
        }
        return func_dict

    def __args2schema(self, func_name, inp_args):

        args = []
        kwargs = {}
        kwargs_started = False
        for i in range(len(inp_args)):
            kwargs_found = re.match("^-(\\S+)=(\\S+)$", inp_args[i])
            if kwargs_found:
                key, value = kwargs_found.groups()
                kwargs[key] = {'value': value}
                kwargs_started = True
            else:
                if kwargs_started:
                    raise SyntaxError(
                        f"positional argument follows keyword argument {key}")
                else:
                    args.append(inp_args[i])

        func_dict = {func_name: {'args': args, 'kwargs': kwargs}}
        return func_dict

    def __doc(self, name):

        print()
        print(f" | > def {name} ")
        print(f" |    ")
        obj = getattr(self, name)
        func_comments = inspect.getcomments(obj)
        if func_comments:
            print(" |  Description :")
            print(f" |    ")
            comments = func_comments.splitlines()
            if len(comments) == 1:
                print(f" |    { comments[0].replace('#', '').strip() }  ")
            else:
                print(f" |    { comments[0].replace('#', '').strip() }  ")
                for i in range(1, len(comments)-1):
                    print(f" |    { comments[i].replace('#', '').strip() } ")
                print(f" |    { comments[-1].replace('#', '').strip() }  ")
            print(f" |    ")

        sign = inspect.signature(obj)
        args = [str(val) for var, val in sign.parameters.items()]
        if args:
            print(" |  Arguments :")
            print(f" |    ")
            for arg in args:
                print(f" |   -{arg}")
            print(f" |    ")

        func_docs = inspect.getdoc(obj)
        if func_docs:
            print(" |  Usage :")
            print(f" |    ")
            docs = func_docs.splitlines()
            if len(docs) == 1:
                print(f" |    { docs[0].strip() }  ")
            else:
                print(f" |    { docs[0].strip() }  ")
                for i in range(1, len(docs)-1):
                    print(f" |    { docs[i].strip() } ")
                print(f" |    { docs[-1].strip() }  ")
            print(f" |    ")

        if sign.return_annotation != sign.empty:
            if sign.return_annotation == None:
                print(f" | -> {None} (Returnable)")
            else:
                print(
                    f" | -> {sign.return_annotation.__name__} (Returnable)")


if __name__ == '__main__':

    class arg_ex1(route_args):

        # python minimal.py 3 4.5 Seven [1,2,3,4,5,6] ('hello','world') {'hello':'world'} True
        # python minimal.py -inp_int=3 -inp_float=4.5 -inp_str=Seven -inp_list=[1,2,3,4,5,6] -int_tuple=('hello','world') -inp_dict={'hello':'world'} -inp_bool=True
        def parse_args(self, inp_int: int = 6,
                       inp_float: float = 6.0,
                       inp_str: str = "Six",
                       inp_list: list = [6, 6.0, "Six"],
                       inp_tuple: tuple = (6, 6.0, "Six"),
                       inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"},
                       inp_bool: bool = False) -> str:
            """
            hello
            nice
            now
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
            return json.dumps(output, indent=2, sort_keys=True)
            # return output

        # def parse_args(self, a, b: int, c: str = 'hello'):

        #     print(a, b, c)
        #     return (a, b, c)

        # def parse_args(self, *args: list, **kwargs: dict):

        #     pass

    obj = arg_ex1()
    print(obj.returned)