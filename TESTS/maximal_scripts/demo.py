
from py4cli.maximal import cnf_parser
import pandas as pd

from maximal_scripts.a.a import A
from maximal_scripts.b.b import B

class demo(cnf_parser):

    # Path of files a & b to be passed in as arguments
    def classes(self, a:str, b:str):
        """python <__file__> demo.yml or python <__file__> demo.json"""
        # """
        # demo.yml:

        #     classes:
        #         a: a.yml
        #         b: b.yml

        # demo.json:

        #     {
        #         "classes": {
        #             "a": "a.json",
        #             "b": "b.json"
        #         }
        #     }

        # cmds:
        #     1. python <__file__> demo.yml
        #     2. python <__file__> demo.json
        # """
        results = {}
        results["ret_a"] = A(a).returned
        results["ret_b"] = B(b).returned
        return results 
    
    def err_on_df(self, df: pd.DataFrame):

        return None
    
if __name__ == '__main__':

    import sys
    import json

    print(sys.argv)
    obj = demo()
    print("")
    if obj.returned:
        out_dict = obj.returned.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=False), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))