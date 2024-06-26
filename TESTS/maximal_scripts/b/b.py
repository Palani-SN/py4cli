from py4cli.maximal import cnf_parser

try:
    from .ba.ba import BA
    from .bb.bb import BB
except:
    from ba.ba import BA
    from bb.bb import BB

class B(cnf_parser):

    # Path of files ba & bb to be passed in as arguments
    def subclasses(self, ba:str, bb:str):
        """
        b.yml:

            subclasses:
                ba: ba.yml
                bb: bb.yml

        b.json:

            {
                "subclasses": {
                    "ba": "ba.json",
                    "bb": "bb.json"
                }
            }

        cmds:
            1. python <__file__> b.yml
            2. python <__file__> b.json
        """
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