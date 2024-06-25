from py4cli.maximal import cnf_parser

class AB(cnf_parser):

    def sub_func(self, aba:dict, abb:dict, abc:dict, abd:dict):

        results = {}
        results["ret_aba"] = aba
        results["ret_abb"] = abb
        results["ret_abc"] = abc
        results["ret_abd"] = abd
        return results 
    
if __name__ == '__main__':

    import sys
    import json

    print(sys.argv)
    obj = AB()
    print("")
    if obj.returned:
        out_dict = obj.returned.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=False), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))