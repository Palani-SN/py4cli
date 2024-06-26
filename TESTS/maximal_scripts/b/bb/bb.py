from py4cli.maximal import cnf_parser

class BB(cnf_parser):

    # params bba, bbb, bbc, bbd to be passed in as arguments
    # return type explicitly specified as None, for test coverage of warning
    # return type explicitly specified as None, for test coverage of warning
    # return type explicitly specified as None, for test coverage of warning
    def sub_func(self, bba:dict, bbb:dict, bbc:dict, bbd:dict) -> None:
        """
        bb.yml:

            sub_func:
                bba: { "k1": "v1", "k2": "v2", "k3": "v3" }
                bbb: { "k1": "v1", "k2": "v2", "k3": "v3" }
                bbc: { "k1": "v1", "k2": "v2", "k3": "v3" }
                bbd: { "k1": "v1", "k2": "v2", "k3": "v3" }

        bb.json:

            {
                "subfunc": {
                    "bba": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    },
                    "bbb": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    },
                    "bbc": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    },
                    "bbd": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    }
                }
            }

        cmds:
            1. python <__file__> bb.yml
            2. python <__file__> bb.json
        """
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