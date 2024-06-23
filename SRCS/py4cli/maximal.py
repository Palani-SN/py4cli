
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

class gen_parser:

    def __init__(self, inp:str) -> None:
        
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

        inp_file = pathlib.Path(inp)
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

        self.returned = OrderedDict()
        actm = set(parsed.keys())
        refm = set(reference.keys())
        if actm.issubset(refm):
            for func, params in parsed.items():
                schema = reference[func]
                args = []
                kwargs = self.__solve_schema(inp_file, func, schema, params)
                self.returned[func] = getattr(self, func)(*args, **kwargs)
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
            if type(value) == dtype:
                type_casted_value = value
            else:
                raise ValueError(f"[{inp_file.absolute()}] : Expected '{dtype}' value for '{var_name}' in kwargs of method '{func_name}', got '{value}' of '{type(value)}' instead")
        else:
            raise Exception(f"Unsupported argument data type : '{dtype}', try using basic types (int, float, str, list, dict, bool) instead")
        
        return type_casted_value