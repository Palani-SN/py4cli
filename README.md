# py4cli 

- Python for Command Line Interface development ( scalable argument parser ).
- Argument Parser for developing Command Line Tools, that is scalable as per need.
- Check out the example code in repo ( https://github.com/Palani-SN/py4cli ) for reference.

## Minimal

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
            inp_tuple: tuple = (6, 6.0, "Six"),
            inp_set: set = {"Six"},
            inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"},
            inp_bool: bool = False) -> dict:
        """
        Seven arguments of different data type can be passed
        any value of the respective data type can be passed for specific argument. for defaults refer above
        the function returns a json string containing all the arguments and its values.

        cmds :
            1. python <__file__> 10 10.0 Seven [10,10.0,'Seven'] (10,10.0,'Seven') {1,2,3,1.0,2.0,3.0} {'int':10,'float':10.0,'str':'Seven'} True
            2. python <__file__> -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,'Seven'] -inp_tuple=(10,10.0,'Seven') -inp_set={1,2,3,1.0,2.0,3.0} -inp_dict={'int':10,'float':10.0,'str':'Seven'} -inp_bool=True
        """
        return {
                'inp_int': inp_int,
                'inp_float': inp_float,
                'inp_str': inp_str,
                'inp_list': inp_list,
                'inp_tuple': inp_tuple,
                'inp_set': inp_set,
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
        out_dict['inp_set'] = list(out_dict['inp_set'])
        print(json.dumps(out_dict, indent=2, sort_keys=True), type(obj.returned))

```

- To get help on how to use the script, execute **python use_minimal.py -h** or **python minimal.py --help** which will generate the doc content based on the comments in script as shown below.

```
output

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
 |   -inp_tuple: tuple = (6, 6.0, 'Six')
 |   -inp_set: set = {'Six'}
 |   -inp_dict: dict = {'int': 6, 'float': 6.0, 'str': 'Six'}
 |   -inp_bool: bool = False
 |
 |  Usage :
 |
 |    Seven arguments of different data type can be passed
 |    any value of the respective data type can be passed for specific argument. for defaults refer above
 |    the function returns a json string containing all the arguments and its values.
 |
 |    cmds :
 |    1. python use_minimal.py 10 10.0 Seven [10,10.0,'Seven'] (10,10.0,'Seven') {1,2,3,1.0,2.0,3.0} {'int':10,'float':10.0,'str':'Seven'} True
 |    2. python use_minimal.py -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,'Seven'] -inp_tuple=(10,10.0,'Seven') -inp_set={1,2,3,1.0,2.0,3.0} -inp_dict={'int':10,'float':10.0,'str':'Seven'} -inp_bool=True
 |
 | -> dict (Returnable)

```

- The commands specified can be used to alter the values as command line arguments to the script.

```
output

(py4cli) D:\GitRepos\py4cli\EXAMPLES>python use_minimal.py -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,'Seven'] -inp_tuple=(10,10.0,'Seven') -inp_set={1,2,3,1.0,2.0,3.0} -inp_dict={'int':10,'float':10.0,'str':'Seven'} -inp_bool=True
['use_minimal.py', '-inp_int=10', '-inp_float=10.0', '-inp_str=Seven', "-inp_list=[10,10.0,'Seven']", "-inp_tuple=(10,10.0,'Seven')", '-inp_set={1,2,3,1.0,2.0,3.0}', "-inp_dict={'int':10,'float':10.0,'str':'Seven'}", '-inp_bool=True']

{
  "inp_bool": true,
  "inp_dict": {
    "float": 10.0,
    "int": 10,
    "str": "Seven"
  },
  "inp_float": 10.0,
  "inp_int": 10,
  "inp_list": [
    10,
    10.0,
    "Seven"
  ],
  "inp_set": [
    1,
    2,
    3
  ],
  "inp_str": "Seven",
  "inp_tuple": [
    10,
    10.0,
    "Seven"
  ]
} <class 'dict'>

```

## Moderate (in progress)

- Vertically scalable version of minimal arg parser, aimed at use case like, hyper parameter tuning.

## Maximal (in progress)

- Horizontally scalable version of minimal arg parser, aimed at use case like, workflow development for testing & debug needs.
