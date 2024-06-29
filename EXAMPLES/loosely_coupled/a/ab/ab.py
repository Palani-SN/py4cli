from py4cli.maximal import cnf_parser

class AB(cnf_parser):

    # params aba, abb, abc, abd to be passed in as arguments
    def sub_func(self, aba:dict, abb:dict, abc:dict, abd:dict):
        """
        ab.yml:

            sub_func:
                aba: { "k1": "v1", "k2": "v2", "k3": "v3" }
                abb: { "k1": "v1", "k2": "v2", "k3": "v3" }
                abc: { "k1": "v1", "k2": "v2", "k3": "v3" }
                abd: { "k1": "v1", "k2": "v2", "k3": "v3" }

        ab.json:

            {
                "subfunc": {
                    "aba": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    },
                    "abb": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    },
                    "abc": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    },
                    "abd": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    }
                }
            }

        cmds:
            1. python <__file__> ab.yml
            2. python <__file__> ab.json
        """
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