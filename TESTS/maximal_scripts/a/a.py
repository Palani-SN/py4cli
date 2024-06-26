from py4cli.maximal import cnf_parser

try:
    from .aa.aa import AA
    from .ab.ab import AB
except:
    from aa.aa import AA
    from ab.ab import AB

class A(cnf_parser):

    # Path of files aa & ab to be passed in as arguments
    def subclasses(self, aa:str, ab:str):
        """
        a.yml:

            subclasses:
                aa: aa.yml
                ab: ab.yml

        a.json:

            {
                "subclasses": {
                    "aa": "aa.json",
                    "ab": "ab.json"
                }
            }

        cmds:
            1. python <__file__> a.yml
            2. python <__file__> a.json
        """
        results = {}
        results["ret_aa"] = AA(aa).returned
        results["ret_ab"] = AB(ab).returned
        return results 
    
if __name__ == '__main__':

    import sys
    import json

    print(sys.argv)
    obj = A()
    print("")
    if obj.returned:
        out_dict = obj.returned.copy()
        print(json.dumps(out_dict, indent=2, sort_keys=False), type(obj.returned))
    else:
        print(obj.returned, type(obj.returned))