
import sys
import re
import inspect
import ast
import __main__

class arg_parser():

    def __init__(self, argv:list=sys.argv):

        methods = []
        self.returned = {}
        for name, obj in inspect.getmembers(self, predicate=inspect.ismethod):
            if not name.startswith('_'):
                methods.append(name)
        methods = sorted(methods)

        def_func_name = 'parse_args'
        if def_func_name in methods:
            if len(argv) == 2 and (argv[1] in ['-h', '--help']):
                self.__doc(def_func_name)
            else:
                func_schema = self.__func2schema(def_func_name)
                args_schema = self.__args2schema(def_func_name, argv[1:])
                args, kwargs = self.__solve_schema(func_schema[def_func_name], args_schema[def_func_name])
                self.returned = self.__func(def_func_name, args, kwargs)
                if func_schema['ret_type'] != inspect._empty and type(self.returned) != func_schema['ret_type']:
                    print(
                        f"WARNING : '{def_func_name}' returns '{type(self.returned)}', but defined to return '{func_schema['ret_type']}'")
        else:
            raise Exception(f"func name : '{def_func_name}' is not defined")

    def __func(self, func, args, kwargs):

        returned = getattr(self, func)(*args, **kwargs)
        return returned

    def __type(self, var_name, dtype, value):

        if dtype in [str, int, float, list, dict, bool, inspect._empty]:
            casted, casted_value = self.__validate_and_typecast(dtype, value)
            if casted:
                type_casted_value = casted_value
            else:
                raise ValueError(f"Expected '{dtype}' value for '{var_name}' in kwargs of method 'parse_args', got '{value}' instead")
        else:
            raise Exception(f"Unsupported argument data type : '{dtype}', try using basic types (int, float, str, list, dict, bool) instead")
        
        return type_casted_value

    def __validate_and_typecast(self, dtype, value):

        if type(value) == dtype:
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

    def __solve_schema(self, func, inps):

        mod_args = []
        for i in range(len(inps['args'])):
            var_name = func['args'][i]
            type = func['kwargs'][var_name]['type']
            val = inps['args'][i]
            mod_args.append(self.__type(var_name, type, val))

        mod_kwargs = {}
        for key, val in inps['kwargs'].items():
            var_name = key
            type = func['kwargs'][key]['type']
            mod_kwargs[key] = self.__type(var_name, type, val)

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
            kwargs_found = re.match("^-(\\S+)=(\\S.+)$", inp_args[i])
            if kwargs_found:
                key, value = kwargs_found.groups()
                kwargs[key] = value
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
                print(f" |    { self.__mult_repl(docs[0], {'<__file__>': __main__.__file__}) }  ")
            else:
                print(f" |    { self.__mult_repl(docs[0], {'<__file__>': __main__.__file__}) }  ")
                for i in range(1, len(docs)-1):
                    print(f" |    { self.__mult_repl(docs[i], {'<__file__>': __main__.__file__}) } ")
                print(f" |    { self.__mult_repl(docs[-1], {'<__file__>': __main__.__file__}) }  ")
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

        inp = str_inp.rstrip()
        if 'python' in inp:
            for key, value in replacements.items():
                inp = inp.replace(key, value)

        return inp