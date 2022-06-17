
import json

from py4cli.base import py4cli_base


class basic_use(py4cli_base):

    def get_dtypes(self, inp_int: int = 6,
                   inp_float: float = 6.0,
                   inp_str: str = "Six",
                   inp_list: list = [6, 6.0, "Six"],
                   inp_tuple: tuple = (6, 6.0, "Six"),
                   inp_set: set = {6, 6.0, "Six"},
                   inp_dict: dict = {'int': 6, 'float': 6.0, 'str': "Six"}) -> str:

        output = {
            "int": inp_int,
            "float": inp_float,
            "str": inp_str,
            "list": inp_list,
            "tuple": inp_tuple,
            # "set": inp_set,
            "dict": inp_dict
        }
        return json.dumps(output, indent=2, sort_keys=True)


if __name__ == "__main__":

    basic_use()
