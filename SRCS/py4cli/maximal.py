
import sys
import inspect
import __main__
from collections import OrderedDict
import pathlib
from typing import Union
import yaml
from yaml.loader import SafeLoader
import json

class cnf_parser:

    def __init__(self, inp: Union[list, str] =sys.argv) -> None:
        
        self.returned = OrderedDict()
        self.__parse(inp)

    def __preproc(self):

        methods = {}
        for name, obj in inspect.getmembers(self, predicate=inspect.ismethod):
            if not name.startswith('_'):
                sign = inspect.signature(obj)
                args = []
                kwargs = {}
                for key, val in sign.parameters.items():
                    if val.default == inspect._empty:
                        kwargs[key] = {
                            'value': val.default,
                            'type': val.annotation}
                    else:
                        kwargs[key] = {
                            'value': val.default,
                            'type': val.annotation
                            }
                    args.append(key)
                    methods[name] = {
                        'args': args,
                        'kwargs': kwargs,
                        'ret_type': sign.return_annotation
                    }
        return methods

    def __parse(self, inp):

        reference = self.__preproc()

        if (type(inp) == list and len(inp) == 2):

            if inp[1] in ['-h', '--help']:
                print(f"class : {self.__class__.__name__}")
                for ref in reference.keys():
                    self.__doc(ref)

            if (inp[1].endswith(('yml', 'json', 'yaml'))):
                inp_file = pathlib.Path(inp[1])
                self.__proc(reference, inp_file)

        if (type(inp) == str and inp.endswith(('yml', 'json', 'yaml'))):
            inp_file = pathlib.Path(inp)
            self.__proc(reference, inp_file)

    def __proc(self, reference, inp_file):

        if not inp_file.exists():
            raise FileNotFoundError(inp_file.absolute())
        
        if inp_file.name.endswith(('.yml', '.yaml')):
            parsed = self.__parse_yml(inp_file)
        else:
            parsed = self.__parse_json(inp_file)

        self.__validate(inp_file, reference, parsed)

    def __parse_json(self, inp_file):

        with open(inp_file.absolute(), 'r') as file:
            try:
                raw = json.load(file)
            except json.JSONDecodeError as err:
                raise SyntaxError(f'{err} in {inp_file.absolute()}')

        # preserving sequnce order
        if raw:
            ordered = OrderedDict(raw)
        else:
            ordered = OrderedDict()
        parsed = self.__edit(ordered)
        return parsed

    def __parse_yml(self, inp_file):

        # parsing from file
        with open(inp_file.absolute(), 'r') as stream:
            try:
                raw = yaml.load(stream, Loader=SafeLoader)
            except yaml.YAMLError as err:
                raise SyntaxError(f'{err} in {inp_file.absolute()}')

        # preserving sequnce order
        if raw:
            ordered = OrderedDict(raw)
        else:
            ordered = OrderedDict()
        parsed = self.__edit(ordered)
        return parsed
    
    def __edit(self, ord):

        mod = OrderedDict()
        for k, v in ord.items():
            if v == None:
                v = {}
            mod[k] = v

        return mod
    
    def __validate(self, inp_file, reference, parsed):

        actm = set(parsed.keys())
        refm = set(reference.keys())
        if actm.issubset(refm):
            for func, params in parsed.items():
                schema = reference[func]
                args = []
                kwargs = self.__solve_schema(inp_file, func, schema, params)
                self.returned[func] = getattr(self, func)(*args, **kwargs)
                if schema['ret_type'] != inspect._empty and type(self.returned) != schema['ret_type']:
                    print(
                        f"WARNING : '{func}' returns '{type(self.returned)}', but defined to return '{schema['ret_type']}'")
        else:
            methods_available = sorted(list(refm))
            raise Exception(f"Undefined func names : {list(actm-refm)}, try using defined func names {methods_available} instead")
    
    def __solve_schema(self, inp_file, func_name, func, inps):

        mod_kwargs = {}
        for key, val in inps.items():
            var_name = key
            type = func['kwargs'][key]['type']
            mod_kwargs[key] = self.__type(inp_file, func_name, var_name, type, val)

        return mod_kwargs
    
    def __type(self, inp_file, func_name, var_name, dtype, value):

        if dtype in [str, int, float, list, dict, bool, inspect._empty]:
            if (dtype == inspect._empty) or (type(value) == dtype):
                type_casted_value = value
            else:
                raise ValueError(f"[{inp_file.absolute()}] : Expected '{dtype}' value for '{var_name}' in kwargs of method '{func_name}', got '{value}' of '{type(value)}' instead")
        else:
            raise Exception(f"Unsupported argument data type : '{dtype}', try using basic types (int, float, str, list, dict, bool) instead")
        
        return type_casted_value
    
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
