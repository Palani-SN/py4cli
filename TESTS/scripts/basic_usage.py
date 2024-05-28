
import pandas as pd
from py4cli.minimal import arg_parser

# Single argument examples

class single_int(arg_parser):

    # example parse_args template function with single argument of type <int>
    def parse_args(self, inp_int: int = 0) -> int:
        """
        inp_int is variable of type <int>
        any integer value can be passed for the argument, while the default is 0
        the function returns the same arg value as type <int> 

        cmds :
            1. python <__file__> 10
            2. python <__file__> -inp_int=10
        """
        return inp_int
    
class single_float(arg_parser):

    # example parse_args template function with single argument of type <float>
    def parse_args(self, inp_float: float = 0.0) -> float:
        """
        inp_float is variable of type <float>
        any floating point value can be passed for the argument, while the default is 0.0
        the function returns the same arg value as type <float> 

        cmds :
            1. python <__file__> 10.0
            2. python <__file__> -inp_float=10.0
        """
        return inp_float
    
class single_str(arg_parser):

    # example parse_args template function with single argument of type <str>
    def parse_args(self, inp_str: str = "None") -> str:
        """
        inp_str is variable of type <str>
        any string value can be passed for the argument, while the default is "None"
        the function returns the same arg value as type <str> 

        cmds :
            1. python <__file__> Empty
            2. python <__file__> -inp_str=Empty
        """
        return inp_str
    
class single_list(arg_parser):

    # example parse_args template function with single argument of type <list>
    def parse_args(self, inp_list: list = [None]) -> list:
        """
        inp_list is variable of type <list>
        any list value can be passed for the argument, while the default is [None]
        the function returns the same arg value as type <list> 

        cmds :
            1. python <__file__> ["Empty"]
            2. python <__file__> -inp_list=["Empty"]
        """
        return inp_list
    
# class single_tuple(arg_parser):

#     # example parse_args template function with single argument of type <tuple>
#     def parse_args(self, inp_tuple: tuple = (None,)) -> tuple:
#         """
#         inp_tuple is variable of type <tuple>
#         any tuple value can be passed for the argument, while the default is (None,)
#         the function returns the same arg value as type <tuple> 

#         cmds :
#             1. python <__file__> ("Empty",)
#             2. python <__file__> -inp_tuple=("Empty",)
#         """
#         return inp_tuple
    
# class single_set(arg_parser):

#     # example parse_args template function with single argument of type <set>
#     def parse_args(self, inp_set: set = {None}) -> set:
#         """
#         inp_set is variable of type <set>
#         any set value can be passed for the argument, while the default is {None}
#         the function returns the same arg value as type <set> 

#         cmds :
#             1. python <__file__> {'Empty'}
#             2. python <__file__> -inp_set={'Empty'}
#         """
#         return inp_set
    
class single_dict(arg_parser):

    # example parse_args template function with single argument of type <dict>
    def parse_args(self, inp_dict: dict = {None:None}) -> dict:
        """
        inp_dict is variable of type <dict>
        any dict value can be passed for the argument, while the default is {None: None}
        the function returns the same arg value as type <dict> 

        cmds :
            1. python <__file__> {"Empty":"Empty"}
            2. python <__file__> -inp_dict={"Empty":"Empty"}
        """
        return inp_dict
    
class single_bool(arg_parser):

    # example parse_args template function with single argument of type <bool>
    def parse_args(self, inp_bool: bool = False) -> bool:
        """
        inp_bool is variable of type <bool>
        any bool value can be passed for the argument, while the default is False
        the function returns the same arg value as type <dict> 

        cmds :
            1. python <__file__> True
            2. python <__file__> -inp_bool=True
        """
        return inp_bool
    
# Multiple arguments example

class multi_args(arg_parser):

    # example parse_args template function with multiple arguments of different types
    def parse_args(self, 
            inp_int: int = 6,
            inp_float: float = 6.0,
            inp_str: str = "Six",
            inp_list: list = [6, 6.0, "Six"],
            inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"},
            inp_bool: bool = False) -> dict:
        """
        Seven arguments of different data type can be passed
        any value of the respective data type can be passed for specific argument. for defaults refer above
        the function returns a json string containing all the arguments and its values.

        cmds :
            1. python <__file__> 10 10.0 Seven [10,10.0,'Seven'] (10,10.0,'Seven') {10,10.0,'Seven'} {'int':10,'float':10.0,'str':'Seven'} True
            2. python <__file__> -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,'Seven'] -inp_tuple=(10,10.0,'Seven') -inp_set={10,10.0,'Seven'} -inp_dict={'int':10,'float':10.0,'str':'Seven'} -inp_bool=True
        """
        return {
                'inp_int': inp_int,
                'inp_float': inp_float,
                'inp_str': inp_str,
                'inp_list': inp_list,
                'inp_dict': inp_dict,
                'inp_bool': inp_bool
            }
        
# Warnings check

class warn_ret_type(arg_parser):

    # example parse_args template function for testing if warning is getting printed.
    # return type warning will be printed if there is a mismatch between expected dtype and returned dtype.
    # warning will only be printed and will not halt the execution flow.
    def parse_args(self, 
            inp_bool: int = False) -> str:
        """
        inp_bool is variable of type <bool>
        any bool value can be passed for the argument, while the default is False
        the function returns the same arg value as type <dict> 

        cmds :
            1. python <__file__> True
            2. python <__file__> -inp_bool=True
        """
        return inp_bool
    
class warn_wo_ret_typ_def(arg_parser):

    # example parse_args template function with multiple arguments of different types
    def parse_args(self, 
            inp_bool):
        """
        inp_bool is variable of type <bool>
        any bool value can be passed for the argument, while the default is None
        the function returns the same arg value as type <dict> 

        cmds :
            1. python <__file__> True
            2. python <__file__> -inp_bool=True
        """
        return inp_bool
    
class warn_no_support_typ_arg(arg_parser):

    # example parse_args template function with multiple arguments of different types
    def parse_args(self, 
            inp_df: pd.DataFrame) -> None:
        """
        example defined for checking if exception is getting raised, will not return any output as the definition is not valid
        """
        return inp_df
    
class warn_on_arg_order(arg_parser):

    # example parse_args template function with multiple arguments of different types
    def parse_args(self, 
            inp_bool1: bool, inp_bool2: bool) -> tuple:
        """
        example defined for checking if exception is getting raised, will not return any output as the definition is not valid
        """
        return inp_bool1, inp_bool2