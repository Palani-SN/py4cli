
from py4cli.maximal import cnf_parser

from a import A
from b import B

class demo(cnf_parser):

    def classes(self, a:str, b:str):

        results = {}
        results["ret_a"] = A(a).returned
        results["ret_b"] = B(b).returned
        return results 
    
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