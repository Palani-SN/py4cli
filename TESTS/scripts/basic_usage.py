

from py4cli.minimal import arg_parser

# Single argument examples

class single_int(arg_parser):

    # example parse_args template function with single argument of type <int>
    def parse_args(self, inp_int: int = 0) -> int:
        """
        inp_int is variable of type <int>
        any integer value can be passed for the argument, while the default is 0
        the function returns the same arg value as type <int> 

        cmd :
            1. python basic_usage.py 10
            2. python basic_usage.py -inp_int=10
        """
        return inp_int
    
class single_float(arg_parser):

    # example parse_args template function with single argument of type <float>
    def parse_args(self, inp_float: float = 0.0) -> float:
        """
        inp_float is variable of type <float>
        any floating point value can be passed for the argument, while the default is 0.0
        the function returns the same arg value as type <float> 

        cmd :
            1. python basic_usage.py 10.0
            2. python basic_usage.py -inp_float=10.0
        """
        return inp_float
    
class single_str(arg_parser):

    # example parse_args template function with single argument of type <str>
    def parse_args(self, inp_str: str = "None") -> str:
        """
        inp_str is variable of type <str>
        any string value can be passed for the argument, while the default is "None"
        the function returns the same arg value as type <str> 

        cmd :
            1. python basic_usage.py Empty
            2. python basic_usage.py -inp_str=Empty
        """
        return inp_str
    
class single_list(arg_parser):

    # example parse_args template function with single argument of type <list>
    def parse_args(self, inp_list: list = [None]) -> list:
        """
        inp_list is variable of type <list>
        any list value can be passed for the argument, while the default is [None]
        the function returns the same arg value as type <list> 

        cmd :
            1. python basic_usage.py ["Empty"]
            2. python basic_usage.py -inp_list=["Empty"]
        """
        return inp_list
    
class single_tuple(arg_parser):

    # example parse_args template function with single argument of type <tuple>
    def parse_args(self, inp_tuple: tuple = (None,)) -> tuple:
        """
        inp_tuple is variable of type <tuple>
        any tuple value can be passed for the argument, while the default is (None,)
        the function returns the same arg value as type <tuple> 

        cmd :
            1. python basic_usage.py ("Empty",)
            2. python basic_usage.py -inp_tuple=("Empty",)
        """
        return inp_tuple
    
class single_set(arg_parser):

    # example parse_args template function with single argument of type <set>
    def parse_args(self, inp_set: set = {None}) -> set:
        """
        inp_set is variable of type <set>
        any set value can be passed for the argument, while the default is {None}
        the function returns the same arg value as type <set> 

        cmd :
            1. python basic_usage.py {'Empty'}
            2. python basic_usage.py -inp_set={'Empty'}
        """
        return inp_set
    
class single_dict(arg_parser):

    # example parse_args template function with single argument of type <dict>
    def parse_args(self, inp_dict: dict = {None:None}) -> dict:
        """
        inp_dict is variable of type <dict>
        any dict value can be passed for the argument, while the default is zero {None: None}
        the function returns the same arg value as type <dict> 

        cmd :
            1. python basic_usage.py {"Empty":"Empty"}
            2. python basic_usage.py -inp_dict={"Empty":"Empty"}
        """
        return inp_dict
    
# Multiple arguments example

class multi_args(arg_parser):

    # example parse_args template function with multiple arguments of different types
    def parse_args(self, 
            inp_int: int = 6,
            inp_float: float = 6.0,
            inp_str: str = "Six",
            inp_list: list = [6, 6.0, "Six"],
            inp_tuple: tuple = (6, 6.0, "Six"),
            inp_set: set = {"Six"},
            inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"}) -> dict:
        """
        Seven arguments of different data type can be passed
        any value of the respective data type can be passed for specific argument. for defaults refer above
        the function returns a json string containing all the arguments and its values.

        cmds :
            1. python basic_usage.py 10 ^
                                10.0 ^
                                Seven ^
                                [10,10.0,'Seven'] ^
                                (10,10.0,'Seven') ^
                                {10,10.0,'Seven'} ^
                                {'int':10,'float':10.0,'str':'Seven'}

            2. python basic_usage.py -inp_int=10 ^
                                    -inp_float=10.0 ^
                                    -inp_str=Seven ^
                                    -inp_list=[10,10.0,'Seven'] ^
                                    -inp_tuple=(10,10.0,'Seven') ^
                                    -inp_set={10,10.0,'Seven'} ^
                                    -inp_dict={'int':10,'float':10.0,'str':'Seven'}
        """
        return {
                'inp_int': inp_int,
                'inp_float': inp_float,
                'inp_str': inp_str,
                'inp_list': inp_list,
                'inp_tuple': inp_tuple,
                'inp_set': inp_set,
                'inp_dict': inp_dict
            }
        