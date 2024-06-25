from py4cli.maximal import cnf_parser

class BB(cnf_parser):

    def sub_func(self, bba:dict, bbb:dict, bbc:dict, bbd:dict):

        results = {}
        results["ret_bba"] = bba
        results["ret_bbb"] = bbb
        results["ret_bbc"] = bbc
        results["ret_bbd"] = bbd
        return results 
    
if __name__ == '__main__':

    import sys
    import json

    print(sys.argv)
    obj = BB()
    print("")
    if obj.returned:
        out_dict = obj.returned.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=False), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))