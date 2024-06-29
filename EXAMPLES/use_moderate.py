from py4cli.moderate import arg_parser

# Multiple arguments example

class vscaled_args(arg_parser):

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
    obj = vscaled_args()
    print("")
    if obj.returned:
        out_dict = obj.returned.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=False), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))