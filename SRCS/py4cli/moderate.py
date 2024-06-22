
import sys
import re
import inspect
import ast
import __main__
from collections import OrderedDict
import pathlib
from sys import argv

import yaml
from yaml.loader import SafeLoader
import json

###### GENERIC PARSER ######

class gen_parser():

    def __init__(self, inps=sys.argv):

        methods = []
        self.returned = None
        for name, obj in inspect.getmembers(self, predicate=inspect.ismethod):
            if not name.startswith('_'):
                methods.append(name)
        methods = sorted(methods)

        if len(inps) == 2 and (inps[1] in ['-h', '--help']):
            for method in methods:
                self.__doc(method)
        elif len(inps) == 1 and inps[0].endswith('.py'):
            print("Methods available for use, is listed below")
            print(json.dumps([ f"~{x}" for x in methods], indent=2, sort_keys=True))
        else:
            code_flow = self._parse_inps(inps)
            if code_flow == None or code_flow == {}:
                print("Methods available for use, is listed below")
                print(json.dumps([ f"~{x}" for x in methods], indent=2, sort_keys=True))
            else:
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
        args_schema = self._inps2schema(func_name, inp_args)
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

        inp = str_inp.rstrip()
        if 'python' in inp:
            for key, value in replacements.items():
                inp = inp.replace(key, value)

        return inp
    
###### ARG PARSER ######

class arg_parser(gen_parser):

    def __init__(self, inps=sys.argv):
        super().__init__(inps)

    def _parse_inps(self, inps):

        inp_args = inps[1:]
        head = 0
        code_flow = OrderedDict()
        for i in range(len(inp_args)+1):
            if (i == len(inp_args)) or (head != i and inp_args[i].startswith("~")):
                func_name = inp_args[head][1:]
                func_args = inp_args[(head+1):i]
                code_flow[func_name] = func_args
                head = i

        return code_flow
    
    def _inps2schema(self, def_func_name, argv):

        args_schema = self.__args2schema(def_func_name, argv)
        return args_schema

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

###### CNF PARSER ######

# class cnf_parser(gen_parser):

#     def __init__(self, inps=sys.argv):
#         super().__init__(inps)

#     def _parse_inps(self, inps):
    
#         code_flow = {}
#         inp_file = pathlib.Path(inps[1])

#         if not inp_file.exists():
#             raise FileNotFoundError(inp_file.absolute())
        
#         if inp_file.name.endswith(('.yml', '.yaml')):
#             with open(inp_file.absolute(), 'r') as stream:
#                 try:
#                     cnfs2dict = yaml.load(stream, Loader=SafeLoader)
#                 except yaml.YAMLError as err:
#                     print(f'{err} in {inp_file.absolute()}')
#         elif inp_file.name.endswith('.json'):
#             with open(inp_file.absolute(), 'r') as file:
#                 cnfs2dict = json.load(file)

#         return OrderedDict(cnfs2dict) if cnfs2dict else cnfs2dict
    
#     def _inps2schema(self, def_func_name, argv):

#         args_schema = self.__cnfs2schema(def_func_name, argv)
#         return args_schema

#     def __cnfs2schema(self, func_name, inp_args):

#         if inp_args == None: inp_args = {'args': [], 'kwargs': {}}
#         else:
#             if 'args' not in inp_args:
#                 inp_args.update({'args': []})
#             if 'kwargs' not in inp_args:
#                 inp_args.update({'kwargs': {}})
#         func_dict = {func_name: inp_args}
#         return func_dict