from py4cli.maximal import cnf_parser

class BA(cnf_parser):

    # params baa, bab, bac, bad to be passed in as arguments
    def sub_func(self, baa:dict, bab:dict, bac:dict, bad:dict):
        """
        ba.yml:

            sub_func:
                baa: { "k1": "v1", "k2": "v2", "k3": "v3" }
                bab: { "k1": "v1", "k2": "v2", "k3": "v3" }
                bac: { "k1": "v1", "k2": "v2", "k3": "v3" }
                bad: { "k1": "v1", "k2": "v2", "k3": "v3" }

        ba.json:

            {
                "subfunc": {
                    "baa": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    },
                    "bab": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    },
                    "bac": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    },
                    "bad": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                    }
                }
            }

        cmds:
            1. python <__file__> ba.yml
            2. python <__file__> bb.json
        """
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