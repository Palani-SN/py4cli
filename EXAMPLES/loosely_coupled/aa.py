from py4cli.maximal import cnf_parser

class AA(cnf_parser):

    def sub_func(self, aaa:dict, aab:dict, aac:dict, aad:dict):

        results = {}
        results["ret_aaa"] = aaa
        results["ret_aab"] = aab
        results["ret_aac"] = aac
        results["ret_aad"] = aad
        return results 
    
if __name__ == '__main__':

    import sys
    import json

    print(sys.argv)
    obj = AA()
    print("")
    if obj.returned:
        out_dict = obj.returned.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=False), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))