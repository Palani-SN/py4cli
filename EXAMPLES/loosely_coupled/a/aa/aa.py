from py4cli.maximal import cnf_parser

class AA(cnf_parser):

    # params aaa, aab, aac, aad to be passed in as arguments
    def sub_func(self, aaa:dict, aab:dict, aac:dict, aad:dict):
        """
        aa.yml:

            sub_func:
                aaa: { "k1": "v1", "k2": "v2", "k3": "v3" }
                aab: { "k1": "v1", "k2": "v2", "k3": "v3" }
                aac: { "k1": "v1", "k2": "v2", "k3": "v3" }
                aad: { "k1": "v1", "k2": "v2", "k3": "v3" }

        aa.json:

            {
                "subfunc": {
                    "aaa": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    },
                    "aab": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    },
                    "aac": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    },
                    "aad": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    }
                }
            }

        cmds:
            1. python <__file__> aa.yml
            2. python <__file__> aa.json
        """
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