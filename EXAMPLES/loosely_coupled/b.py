from py4cli.maximal import cnf_parser

from ba import BA
from bb import BB

class B(cnf_parser):

    def subclasses(self, ba:str, bb:str):

        results = {}
        results["ret_ba"] = BA(ba).returned
        results["ret_bb"] = BB(bb).returned
        return results 
    
if __name__ == '__main__':

    import sys
    import json

    print(sys.argv)
    obj = B()
    print("")
    if obj.returned:
        out_dict = obj.returned.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=False), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))