
import sys
import re
import inspect
import ast
import __main__
from collections import OrderedDict
import json

class arg_parser():

    def __init__(self, argv=sys.argv):

        methods = []
        self.returned = None
        for name, obj in inspect.getmembers(self, predicate=inspect.ismethod):
            if not name.startswith('_'):
                methods.append(name)
        methods = sorted(methods)

        if len(argv) == 2 and (argv[1] in ['-h', '--help']):
            for method in methods:
                self.__doc(method)
        elif len(argv) == 1 and argv[0].endswith('.py'):
            print("Methods available for use, is listed below")
            print(json.dumps([ f"~{x}" for x in methods], indent=2, sort_keys=True))
        else:
            inp_args = argv[1:]
            head = 0
            code_flow = OrderedDict()
            for i in range(len(inp_args)+1):
                if (i == len(inp_args)) or (head != i and inp_args[i].startswith("~")):
                    func_name = inp_args[head][1:]
                    func_args = inp_args[(head+1):i]
                    code_flow[func_name] = func_args
                    head = i

            def_set = set(methods)
            inv_set = set(code_flow.keys())
            if not inv_set.issubset(def_set):
                raise Exception(f"Undefined func names : {list(inv_set-def_set)}, try using defined func names {methods} instead")

            self.returned = {}
            for func, argv in code_flow.items():
                self.returned[func] = self.__solve_func(func, argv)

    def __solve_func(self, func_name, inp_args):

        returned = None
        func_schema = self.__func2schema(func_name)
        args_schema = self.__args2schema(func_name, inp_args)
        args, kwargs = self.__solve_schema(func_name, func_schema[func_name], args_schema[func_name])
        if inspect.ismethod(getattr(self, func_name)):
            returned = self.__func(func_name, args, kwargs)
            if func_schema['ret_type'] != inspect._empty and type(returned) != func_schema['ret_type']:
                print(
                    f"WARNING : '{func_name}' returns '{type(returned)}', but defined to return '{func_schema['ret_type']}'")
                
        return returned

    def __func(self, func, args, kwargs):

        returned = getattr(self, func)(*args, **kwargs)
        return returned

    def __type(self, func_name, var_name, dtype, value):

        if dtype in [str, int, float, list, dict, bool, inspect._empty]:
            casted, casted_value = self.__validate_and_typecast(dtype, value)
            if casted:
                type_casted_value = casted_value
            else:
                raise ValueError(f"Expected '{dtype}' value for '{var_name}' in kwargs of method '{func_name}', got '{value}' instead")
        else:
            raise Exception(f"Unsupported argument data type : '{dtype}', try using basic types (int, float, str, list, dict, bool) instead")
        
        return type_casted_value

    def __validate_and_typecast(self, dtype, value):

        if dtype == str:
            return True, value

        if dtype in [int, float]:
            try:
                type_casted_value = dtype(value)
                return True, type_casted_value
            except ValueError as err:
                return False, value
        elif dtype in [list, dict, bool]:
            try:
                type_casted_value = ast.literal_eval(value)
                return (dtype == type(type_casted_value)), type_casted_value
            except (SyntaxError, ValueError, Exception) as err:
                return False, value
        elif dtype in [inspect._empty]:
            type_casted_value = value
            return True, type_casted_value

    def __solve_schema(self, func_name, func, inps):

        mod_args = []
        for i in range(len(inps['args'])):
            var_name = func['args'][i]
            type = func['kwargs'][var_name]['type']
            val = inps['args'][i]
            mod_args.append(self.__type(func_name, var_name, type, val))

        mod_kwargs = {}
        for key, val in inps['kwargs'].items():
            var_name = key
            type = func['kwargs'][key]['type']
            val = val['value']
            mod_kwargs[key] = self.__type(func_name, var_name, type, val)

        return mod_args, mod_kwargs

    def __func2schema(self, func_name):

        sign = inspect.signature(getattr(self, func_name))
        args = []
        kwargs = {}
        for key, val in sign.parameters.items():
            if val.default == inspect._empty:
                kwargs[key] = {'value': val.default,
                               'type': val.annotation}
            else:
                kwargs[key] = {'value': val.default,
                               'type': val.annotation}
            args.append(key)

        func_dict = {
            func_name: {
                'args': args,
                'kwargs': kwargs
            },
            'ret_type': sign.return_annotation
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
                        f"positional argument follows keyword argument '{key}'")
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
                print(f" |    { self.__mult_repl(docs[0], {'<__file__>': __main__.__file__, '<__func__>': name}) }  ")
            else:
                print(f" |    { self.__mult_repl(docs[0], {'<__file__>': __main__.__file__, '<__func__>': name}) }  ")
                for i in range(1, len(docs)-1):
                    print(f" |    { self.__mult_repl(docs[i], {'<__file__>': __main__.__file__, '<__func__>': name}) } ")
                print(f" |    { self.__mult_repl(docs[-1], {'<__file__>': __main__.__file__, '<__func__>': name}) }  ")
            print(f" |    ")

        if sign.return_annotation != sign.empty:
            if sign.return_annotation == None:
                print(f" | -> {None} (Returnable)")
            else:
                print(
                    f" | -> {sign.return_annotation.__name__} (Returnable)")
        else:
            print(f" | -> Any (Returnable)")

    def __mult_repl(self, str_inp, replacements):

        inp = str_inp.strip()
        if 'python' in inp:
            for key, value in replacements.items():
                inp = inp.replace(key, value)

        return inp
