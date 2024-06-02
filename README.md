# py4cli 

- Python for Command Line Interface development ( scalable argument parser ).
- Argument Parser for developing Command Line Tools, that is scalable as per need.
- Check out the example code in repo ( https://github.com/Palani-SN/py4cli ) for reference.

## Installation

- use pip command to install the library, refer pypi page : https://pypi.org/project/py4cli/

```
  python -m pip install py4cli
  
```

## Minimal

- minimal arg parser that can pass on the cli arguments to parse_args class method arguments as per the declarative type definition.
- Sample code as shown below can read arguments in specified type as per function signature. (refer **use_minimal.py** under **EXAMPLES/**)

```python

from py4cli.minimal import arg_parser

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
        Six arguments of different data type can be passed
        any value of the respective data type can be passed for specific argument. for defaults refer above
        the function returns a dict containing all the arguments and its values.

        cmds :
            1. python <__file__> 10 10.0 Seven [10,10.0,'Seven'] {'int':10,'float':10.0,'str':'Seven'} True
            2. python <__file__> -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,'Seven'] -inp_dict={'int':10,'float':10.0,'str':'Seven'} -inp_bool=True
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
    obj = multi_args()
    print("")
    if obj.returned:
        out_dict = obj.returned.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=True), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))

```

- To get help on how to use the script, execute **python use_minimal.py -h** or **python use_minimal.py --help** which will generate the doc content based on the comments in script as shown below.

```output

(py4cli) D:\GitRepos\py4cli\EXAMPLES>python use_minimal.py --help
['use_minimal.py', '--help']

 | > def parse_args
 |
 |  Description :
 |
 |    example parse_args template function with multiple arguments of different types
 |
 |  Arguments :
 |
 |   -inp_int: int = 6
 |   -inp_float: float = 6.0
 |   -inp_str: str = 'Six'
 |   -inp_list: list = [6, 6.0, 'Six']
 |   -inp_dict: dict = {'int': 6, 'float': 6.0, 'str': 'Six'}
 |   -inp_bool: bool = False
 |
 |  Usage :
 |
 |    Six arguments of different data type can be passed
 |    any value of the respective data type can be passed for specific argument. for defaults refer above
 |    the function returns a dict containing all the arguments and its values.
 |
 |    cmds :
 |    1. python use_minimal.py 10 10.0 Seven [10,10.0,'Seven'] {'int':10,'float':10.0,'str':'Seven'} True
 |    2. python use_minimal.py -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,'Seven'] -inp_dict={'int':10,'float':10.0,'str':'Seven'} -inp_bool=True
 |
 | -> dict (Returnable)

None <class 'NoneType'>

```

- The commands specified can be used to alter the values as command line arguments to the script.

```
output

(py4cli) D:\GitRepos\py4cli\EXAMPLES>python use_minimal.py
['use_minimal.py']

{
  "inp_bool": false,
  "inp_dict": {
    "float": 6.0,
    "int": 6,
    "str": "Six"
  },
  "inp_float": 6.0,
  "inp_int": 6,
  "inp_list": [
    6,
    6.0,
    "Six"
  ],
  "inp_str": "Six"
} <class 'dict'>

(py4cli) D:\GitRepos\py4cli\EXAMPLES>python use_minimal.py 100 100.0 "parse args example function call" [1,2,3,4,5,6]
['use_minimal.py', '100', '100.0', 'parse args example function call', '[1,2,3,4,5,6]']

{
  "inp_bool": false,
  "inp_dict": {
    "float": 6.0,
    "int": 6,
    "str": "Six"
  },
  "inp_float": 100.0,
  "inp_int": 100,
  "inp_list": [
    1,
    2,
    3,
    4,
    5,
    6
  ],
  "inp_str": "parse args example function call"
} <class 'dict'>

(py4cli) D:\GitRepos\py4cli\EXAMPLES>python use_minimal.py -inp_int=100 -inp_float=100.0 -inp_str="parse args example function call" -inp_list=[1,2,3,4,5,6]
['use_minimal.py', '-inp_int=100', '-inp_float=100.0', '-inp_str=parse args example function call', '-inp_list=[1,2,3,4,5,6]']

{
  "inp_bool": false,
  "inp_dict": {
    "float": 6.0,
    "int": 6,
    "str": "Six"
  },
  "inp_float": 100.0,
  "inp_int": 100,
  "inp_list": [
    1,
    2,
    3,
    4,
    5,
    6
  ],
  "inp_str": "parse args example function call"
} <class 'dict'>

(py4cli) D:\GitRepos\py4cli\EXAMPLES>python use_minimal.py 100 100.0 -inp_str="parse args example function call" -inp_list=[1,2,3,4,5,6]
['use_minimal.py', '100', '100.0', '-inp_str=parse args example function call', '-inp_list=[1,2,3,4,5,6]']

{
  "inp_bool": false,
  "inp_dict": {
    "float": 6.0,
    "int": 6,
    "str": "Six"
  },
  "inp_float": 100.0,
  "inp_int": 100,
  "inp_list": [
    1,
    2,
    3,
    4,
    5,
    6
  ],
  "inp_str": "parse args example function call"
} <class 'dict'>

```

## Moderate 

- Vertically scalable version of minimal arg parser, aimed at use case like, hyper parameter tuning.
- Sample code as shown below can read arguments in specified type as per function signature. (refer **use_moderate.py** under **EXAMPLES/**)

```python
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
            1. python <__file__> 10 10.0 Seven [10,10.0,'Seven'] {'int':10,'float':10.0,'str':'Seven'} True
            2. python <__file__> -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,'Seven'] -inp_dict={'int':10,'float':10.0,'str':'Seven'} -inp_bool=True
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
            1. python <__file__> 10 10.0 Seven [10,10.0,'Seven'] {'int':10,'float':10.0,'str':'Seven'} True
            2. python <__file__> -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,'Seven'] -inp_dict={'int':10,'float':10.0,'str':'Seven'} -inp_bool=True
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
        print(json.dumps(out_dict, indent=2, sort_keys=True), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))

```

- To get help on how to use the script, execute **python use_moderate.py -h** or **python use_moderate.py --help** which will generate the doc content based on the comments in script as shown below.

```output

(py4cli) D:\GitRepos\py4cli\EXAMPLES>python use_moderate.py
['use_moderate.py']
Methods available for use, is listed below
[
  "~multi_args1",
  "~multi_args2"
]

None <class 'NoneType'>

(py4cli) D:\GitRepos\py4cli\EXAMPLES>python use_moderate.py --help
['use_moderate.py', '--help']

 | > def multi_args1
 |
 |  Description :
 |
 |    example multi_args template function with multiple arguments of different types
 |
 |  Arguments :
 |
 |   -inp_int: int = 6
 |   -inp_float: float = 6.0
 |   -inp_str: str = 'Six'
 |   -inp_list: list = [6, 6.0, 'Six']
 |   -inp_dict: dict = {'int': 6, 'float': 6.0, 'str': 'Six'}
 |   -inp_bool: bool = False
 |
 |  Usage :
 |
 |    Six arguments of different data type can be passed
 |    any value of the respective data type can be passed for specific argument. for defaults refer above
 |    the function returns a dict containing all the arguments and its values.
 |
 |    cmds :
 |    1. python use_moderate.py 10 10.0 Seven [10,10.0,'Seven'] {'int':10,'float':10.0,'str':'Seven'} True
 |    2. python use_moderate.py -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,'Seven'] -inp_dict={'int':10,'float':10.0,'str':'Seven'} -inp_bool=True
 |
 | -> dict (Returnable)

 | > def multi_args2
 |
 |  Description :
 |
 |    example multi_args template function with multiple arguments of different types
 |
 |  Arguments :
 |
 |   -inp_int: int = 6
 |   -inp_float: float = 6.0
 |   -inp_str: str = 'Six'
 |   -inp_list: list = [6, 6.0, 'Six']
 |   -inp_dict: dict = {'int': 6, 'float': 6.0, 'str': 'Six'}
 |   -inp_bool: bool = False
 |
 |  Usage :
 |
 |    Six arguments of different data type can be passed
 |    any value of the respective data type can be passed for specific argument. for defaults refer above
 |    the function returns a dict containing all the arguments and its values.
 |
 |    cmds :
 |    1. python use_moderate.py 10 10.0 Seven [10,10.0,'Seven'] {'int':10,'float':10.0,'str':'Seven'} True
 |    2. python use_moderate.py -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,'Seven'] -inp_dict={'int':10,'float':10.0,'str':'Seven'} -inp_bool=True
 |
 | -> dict (Returnable)

None <class 'NoneType'>

```

- The commands specified can be used to alter the values as command line arguments to the script. The methods can be selected with appropriate arguments as per definition, and the order of execution of the methods is also controllable. For illustration purpose only two methods [multi_args1, multi_args2] is defined which can be scaled to number of functions, as much as python supports.

```
output

(py4cli) D:\GitRepos\py4cli\EXAMPLES>python use_moderate.py ~multi_args1 100 100.0 "multi_args1 example function call" [1,2,3,4,5,6
] ~multi_args2 -inp_int=100 -inp_float=100.0 -inp_str="multi_args2 example function call" -inp_list=[1,2,3,4,5,6]
['use_moderate.py', '~multi_args1', '100', '100.0', 'multi_args1 example function call', '[1,2,3,4,5,6]', '~multi_args2', '-inp_int=100', '-inp_float=100.0', '-inp_str=multi_args2 example function call', '-inp_list=[1,2,3,4,5,6]']

{
  "multi_args1": {
    "inp_bool": false,
    "inp_dict": {
      "float": 6.0,
      "int": 6,
      "str": "Six"
    },
    "inp_float": 100.0,
    "inp_int": 100,
    "inp_list": [
      1,
      2,
      3,
      4,
      5,
      6
    ],
    "inp_str": "multi_args1 example function call"
  },
  "multi_args2": {
    "inp_bool": false,
    "inp_dict": {
      "float": 6.0,
      "int": 6,
      "str": "Six"
    },
    "inp_float": 100.0,
    "inp_int": 100,
    "inp_list": [
      1,
      2,
      3,
      4,
      5,
      6
    ],
    "inp_str": "multi_args2 example function call"
  }
} <class 'dict'>

```

## Maximal (in progress)

- Horizontally scalable version of minimal arg parser, aimed at use case like, workflow development for testing & debug needs.
