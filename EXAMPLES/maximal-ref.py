
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

        self.__ref = self.__preproc()

        inp_file = pathlib.Path(inp)
        if not inp_file.exists():
            raise FileNotFoundError(inp_file.absolute())
        
        if inp_file.name.endswith(('.yml', '.yaml')):
            parsed = self.__parse_yml(inp_file)
        else:
            parsed = self.__parse_json(inp_file)

        self.__validate(inp_file, parsed)

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
            if 'args' not in v: v['args'] = []
            if 'kwargs' not in v: v['kwargs'] = {}
            mod[k] = v

        return mod
    
    def __validate(self, inp_file, parsed):

        self.inp = OrderedDict()
        actm = set(parsed.keys())
        refm = set(self.__ref.keys())
        if actm.issubset(refm):
            for func, params in parsed.items():
                args, kwargs = self.__solve_schema(func, self.__ref[func], params)
                if args != params['args']:
                    raise ValueError(f"[{inp_file.absolute()}] : {func}/args - Got {params['args']}, Expected {args}, Kindly Check")
                if kwargs != params['kwargs']:
                    raise ValueError(f"[{inp_file.absolute()}] : {func}/kwargs - Got {params['kwargs']}, Expected {kwargs}, Kindly Check")
                self.inp[func] = {'args': args, 'kwargs': kwargs}
        else:
            methods_available = sorted(list(refm))
            raise Exception(f"Undefined func names : {list(actm-refm)}, try using defined func names {methods_available} instead")
    
    def __solve_schema(self, func_name, func, inps):

        mod_args = []
        mod_kwargs = {}
        kwargs_started = False
        for i in range(len(func['args'])):
            kwargs_found = func['args'][i] in inps['kwargs'].keys()
            if kwargs_found:
                var_name = func['args'][i]
                type = func['kwargs'][var_name]['type']
                val = inps['kwargs'][var_name]
                mod_kwargs[var_name] = self.__type(func_name, var_name, type, val) 
                kwargs_started = True
            else:
                if len(mod_args) != len(inps['args']):
                    if kwargs_started:
                        raise SyntaxError(
                            f"positional argument follows keyword argument '{prev}'")
                    else:
                        var_name = func['args'][i]
                        type = func['kwargs'][var_name]['type']
                        val = inps['args'][i]
                        mod_args.append(self.__type(func_name, var_name, type, val))
            prev = func['args'][i]

        return mod_args, mod_kwargs
    
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
        else:
            return False, value

        # if dtype in [int, float]:
        #     try:
        #         type_casted_value = dtype(value)
        #         return True, type_casted_value
        #     except ValueError as err:
        #         return False, value
        # elif dtype in [list, dict, bool]:
        #     try:
        #         type_casted_value = ast.literal_eval(value)
        #         return (dtype == type(type_casted_value)), type_casted_value
        #     except (SyntaxError, ValueError, Exception) as err:
        #         return False, value
        # elif dtype in [inspect._empty]:
        #     type_casted_value = value
        #     return True, type_casted_value

    def _exec(self):

        self.out = OrderedDict()
        for func, params in self.inp.items():
            args = params['args']
            kwargs = params['kwargs']
            self.out[func] = getattr(self, func)(*args, **kwargs)
    
class vscaled_args(gen_parser):

    # example multi_args template function with multiple arguments of different types
    def multi_args1(self, 
            inp_int: int = 6,
            inp_float: float = 6.0,
            inp_str: str = "Six",
            inp_list: list = [6, 6.0, "Six"],
            inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"},
            inp_bool: bool = False) -> dict:
        """
        Six arguments of different data type can be passed
        any value of the respective data type can be passed for specific argument. for defaults refer above
        the function returns a dict containing all the arguments and its values.

        cmds :

            1. python <__file__> ~<__func__> 10 10.0 "Seven" "[10, 10.0, 'Seven']" "{'int':10, 'float':10.0, 'str':'Seven'}" True
            2. python <__file__> ~<__func__> -inp_int=10 -inp_float=10.0 -inp_str="Seven" -inp_list="[10, 10.0, 'Seven']" -inp_dict="{'int':10, 'float':10.0, 'str':'Seven'}" -inp_bool=True
        """
        return {
                'inp_int': inp_int,
                'inp_float': inp_float,
                'inp_str': inp_str,
                'inp_list': inp_list,
                'inp_dict': inp_dict,
                'inp_bool': inp_bool
            }
    
    # example multi_args template function with multiple arguments of different types
    def multi_args2(self, 
            inp_int: int = 6,
            inp_float: float = 6.0,
            inp_str: str = "Six",
            inp_list: list = [6, 6.0, "Six"],
            inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"},
            inp_bool: bool = False) -> dict:
        """
        Six arguments of different data type can be passed
        any value of the respective data type can be passed for specific argument. for defaults refer above
        the function returns a dict containing all the arguments and its values.

        cmds :

            1. python <__file__> ~<__func__> 10 10.0 "Seven" "[10, 10.0, 'Seven']" "{'int':10, 'float':10.0, 'str':'Seven'}" True
            2. python <__file__> ~<__func__> -inp_int=10 -inp_float=10.0 -inp_str="Seven" -inp_list="[10, 10.0, 'Seven']" -inp_dict="{'int':10, 'float':10.0, 'str':'Seven'}" -inp_bool=True
        """
        return {
                'inp_int': inp_int,
                'inp_float': inp_float,
                'inp_str': inp_str,
                'inp_list': inp_list,
                'inp_dict': inp_dict,
                'inp_bool': inp_bool
            }
    
    # example multi_args template function with multiple arguments of different types
    def multi_args3(self, 
            inp_int: int = 6,
            inp_float: float = 6.0,
            inp_str: str = "Six",
            inp_list: list = [6, 6.0, "Six"],
            inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"},
            inp_bool: bool = False) -> dict:
        """
        Six arguments of different data type can be passed
        any value of the respective data type can be passed for specific argument. for defaults refer above
        the function returns a dict containing all the arguments and its values.

        cmds :

            1. python <__file__> ~<__func__> 10 10.0 "Seven" "[10, 10.0, 'Seven']" "{'int':10, 'float':10.0, 'str':'Seven'}" True
            2. python <__file__> ~<__func__> -inp_int=10 -inp_float=10.0 -inp_str="Seven" -inp_list="[10, 10.0, 'Seven']" -inp_dict="{'int':10, 'float':10.0, 'str':'Seven'}" -inp_bool=True
        """
        return {
                'inp_int': inp_int,
                'inp_float': inp_float,
                'inp_str': inp_str,
                'inp_list': inp_list,
                'inp_dict': inp_dict,
                'inp_bool': inp_bool
            }
    
    # example multi_args template function with multiple arguments of different types
    def multi_args4(self, 
            inp_int: int = 6,
            inp_float: float = 6.0,
            inp_str: str = "Six",
            inp_list: list = [6, 6.0, "Six"],
            inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"},
            inp_bool: bool = False) -> dict:
        """
        Six arguments of different data type can be passed
        any value of the respective data type can be passed for specific argument. for defaults refer above
        the function returns a dict containing all the arguments and its values.

        cmds :

            1. python <__file__> ~<__func__> 10 10.0 "Seven" "[10, 10.0, 'Seven']" "{'int':10, 'float':10.0, 'str':'Seven'}" True
            2. python <__file__> ~<__func__> -inp_int=10 -inp_float=10.0 -inp_str="Seven" -inp_list="[10, 10.0, 'Seven']" -inp_dict="{'int':10, 'float':10.0, 'str':'Seven'}" -inp_bool=True
        """
        return {
                'inp_int': inp_int,
                'inp_float': inp_float,
                'inp_str': inp_str,
                'inp_list': inp_list,
                'inp_dict': inp_dict,
                'inp_bool': inp_bool
            }
    
    # example multi_args template function with multiple arguments of different types
    def multi_args5(self, 
            inp_int: int = 6,
            inp_float: float = 6.0,
            inp_str: str = "Six",
            inp_list: list = [6, 6.0, "Six"],
            inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"},
            inp_bool: bool = False) -> dict:
        """
        Six arguments of different data type can be passed
        any value of the respective data type can be passed for specific argument. for defaults refer above
        the function returns a dict containing all the arguments and its values.

        cmds :

            1. python <__file__> ~<__func__> 10 10.0 "Seven" "[10, 10.0, 'Seven']" "{'int':10, 'float':10.0, 'str':'Seven'}" True
            2. python <__file__> ~<__func__> -inp_int=10 -inp_float=10.0 -inp_str="Seven" -inp_list="[10, 10.0, 'Seven']" -inp_dict="{'int':10, 'float':10.0, 'str':'Seven'}" -inp_bool=True
        """
        return {
                'inp_int': inp_int,
                'inp_float': inp_float,
                'inp_str': inp_str,
                'inp_list': inp_list,
                'inp_dict': inp_dict,
                'inp_bool': inp_bool
            }
    
    # example multi_args template function with multiple arguments of different types
    def multi_args6(self, 
            inp_int: int = 6,
            inp_float: float = 6.0,
            inp_str: str = "Six",
            inp_list: list = [6, 6.0, "Six"],
            inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"},
            inp_bool: bool = False) -> dict:
        """
        Six arguments of different data type can be passed
        any value of the respective data type can be passed for specific argument. for defaults refer above
        the function returns a dict containing all the arguments and its values.

        cmds :

            1. python <__file__> ~<__func__> 10 10.0 "Seven" "[10, 10.0, 'Seven']" "{'int':10, 'float':10.0, 'str':'Seven'}" True
            2. python <__file__> ~<__func__> -inp_int=10 -inp_float=10.0 -inp_str="Seven" -inp_list="[10, 10.0, 'Seven']" -inp_dict="{'int':10, 'float':10.0, 'str':'Seven'}" -inp_bool=True
        """
        return {
                'inp_int': inp_int,
                'inp_float': inp_float,
                'inp_str': inp_str,
                'inp_list': inp_list,
                'inp_dict': inp_dict,
                'inp_bool': inp_bool
            }
    
    # example multi_args template function with multiple arguments of different types
    def multi_args7(self, 
            inp_int: int = 6,
            inp_float: float = 6.0,
            inp_str: str = "Six",
            inp_list: list = [6, 6.0, "Six"],
            inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"},
            inp_bool: bool = False) -> dict:
        """
        Six arguments of different data type can be passed
        any value of the respective data type can be passed for specific argument. for defaults refer above
        the function returns a dict containing all the arguments and its values.

        cmds :
        
            1. python <__file__> ~<__func__> 10 10.0 "Seven" "[10, 10.0, 'Seven']" "{'int':10, 'float':10.0, 'str':'Seven'}" True
            2. python <__file__> ~<__func__> -inp_int=10 -inp_float=10.0 -inp_str="Seven" -inp_list="[10, 10.0, 'Seven']" -inp_dict="{'int':10, 'float':10.0, 'str':'Seven'}" -inp_bool=True
        """
        return {
                'inp_int': inp_int,
                'inp_float': inp_float,
                'inp_str': inp_str,
                'inp_list': inp_list,
                'inp_dict': inp_dict,
                'inp_bool': inp_bool
            }
    
if __name__ == '__main__':

    import sys
    import json

    print(sys.argv)
    obj = vscaled_args('use_mod_json_cnf.json')
    obj._exec()
    print("")
    if obj.out:
        out_dict = obj.out.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=False), type(obj.out))
    else:
        print(obj.out, type(obj.out))