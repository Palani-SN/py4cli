from py4cli.maximal import cnf_parser

class BA(cnf_parser):

    def sub_func(self, baa:dict, bab:dict, bac:dict, bad:dict):

        results = {}
        results["ret_baa"] = baa
        results["ret_bab"] = bab
        results["ret_bac"] = bac
        results["ret_bad"] = bad
        return results 
    
if __name__ == '__main__':

    import sys
    import json

    print(sys.argv)
    obj = BA()
    print("")
    if obj.returned:
        out_dict = obj.returned.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=False), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))