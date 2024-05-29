
import pandas as pd
from py4cli.moderate import arg_parser

# vertically scaled argument examples

class vscaled_args(arg_parser):

    # example single_int template function with single argument of type <int>
    def single_int(self, inp_int: int = 0) -> int:
        """
        inp_int is variable of type <int>
        any integer value can be passed for the argument, while the default is 0
        the function returns the same arg value as type <int> 

        cmds :
            1. python <__file__> 10
            2. python <__file__> -inp_int=10
        """
        return inp_int
    
    # example single_float template function with single argument of type <float>
    def single_float(self, inp_float: float = 0.0) -> float:
        """
        inp_float is variable of type <float>
        any floating point value can be passed for the argument, while the default is 0.0
        the function returns the same arg value as type <float> 

        cmds :
            1. python <__file__> 10.0
            2. python <__file__> -inp_float=10.0
        """
        return inp_float
    
    # example single_str template function with single argument of type <str>
    def single_str(self, inp_str: str = "None") -> str:
        """
        inp_str is variable of type <str>
        any string value can be passed for the argument, while the default is "None"
        the function returns the same arg value as type <str> 

        cmds :
            1. python <__file__> Empty
            2. python <__file__> -inp_str=Empty
        """
        return inp_str
    
    # example single_list template function with single argument of type <list>
    def single_list(self, inp_list: list = [None]) -> list:
        """
        inp_list is variable of type <list>
        any list value can be passed for the argument, while the default is [None]
        the function returns the same arg value as type <list> 

        cmds :
            1. python <__file__> ["Empty"]
            2. python <__file__> -inp_list=["Empty"]
        """
        return inp_list
    
    # example single_dict template function with single argument of type <dict>
    def single_dict(self, inp_dict: dict = {None:None}) -> dict:
        """
        inp_dict is variable of type <dict>
        any dict value can be passed for the argument, while the default is {None: None}
        the function returns the same arg value as type <dict> 

        cmds :
            1. python <__file__> {"Empty":"Empty"}
            2. python <__file__> -inp_dict={"Empty":"Empty"}
        """
        return inp_dict
    
    # example single_bool template function with single argument of type <bool>
    def single_bool(self, inp_bool: bool = False) -> bool:
        """
        inp_bool is variable of type <bool>
        any bool value can be passed for the argument, while the default is False
        the function returns the same arg value as type <dict> 

        cmds :
            1. python <__file__> True
            2. python <__file__> -inp_bool=True
        """
        return inp_bool
    
    # example multi_args template function with multiple arguments of different types
    def multi_args(self, 
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
    
    # example warn_ret_type template function for testing if warning is getting printed.
    # return type warning will be printed if there is a mismatch between expected dtype and returned dtype.
    # warning will only be printed and will not halt the execution flow.
    def warn_ret_type(self, 
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
    
    # example warn_wo_ret_typ_def template function with multiple arguments of different types
    def warn_wo_ret_typ_def(self, 
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
    
    # example warn_no_support_typ_arg template function with multiple arguments of different types
    def warn_no_support_typ_arg(self, 
            inp_df: pd.DataFrame) -> None:
        """
        example defined for checking if exception is getting raised, will not return any output as the definition is not valid
        """
        return inp_df
    
    # example warn_on_arg_order template function with multiple arguments of different types
    def warn_on_arg_order(self, 
            inp_bool1: bool, inp_bool2: bool) -> tuple:
        """
        example defined for checking if exception is getting raised, will not return any output as the definition is not valid
        """
        return inp_bool1, inp_bool2
    
if __name__ == '__main__':

    import sys
    import json

    print(sys.argv)
    obj = vscaled_args()
    print("")
    if obj.returned:
        out_dict = obj.returned.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=True), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))