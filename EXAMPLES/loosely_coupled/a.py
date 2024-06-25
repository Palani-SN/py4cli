from py4cli.maximal import cnf_parser

from aa import AA
from ab import AB

class A(cnf_parser):

    def subclasses(self, aa:str, ab:str):

        results = {}
        results["ret_aa"] = AA(aa).returned
        results["ret_ab"] = AB(ab).returned
        return results 
    
if __name__ == '__main__':

    import sys
    import json

    print(sys.argv)
    obj = A()
    print("")
    if obj.returned:
        out_dict = obj.returned.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=False), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))