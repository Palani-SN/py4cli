from py4cli.minimal import cnf_parser

# Multiple arguments example

class multi_cnfs(cnf_parser):

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

        files :
        
            use_min_yml_cnf.yml

            args: [100, 100.0]
            kwargs:
                inp_str: "Hello from YML"
                inp_list: [1, 2, 3, 4, 5, 6]
                inp_dict: { "Hello": "World", "from": "YML" }
                inp_bool: True

            use_min_json_cnf.json

            {
                "args": [100, 100.0],
                "kwargs": {
                    "inp_str": "Hello From JSON",
                    "inp_list": [1, 2, 3, 4, 5, 6],
                    "inp_dict": {"Hello": "World", "from": "JSON"},
                    "inp_bool": true
                }
            }

            1. python <__file__> use_min_yml_cnf.yml
            2. python <__file__> use_min_json_cnf.json
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
    obj = multi_cnfs()
    print("")
    if obj.returned:
        out_dict = obj.returned.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=True), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))
