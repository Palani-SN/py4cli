
import sys
import json
from basic_usage import multi_args

print(sys.argv)
obj = multi_args()
print("")
if obj.returned:
    out_dict = obj.returned.copy()
    print(out_dict['inp_set'])
    print("")
    del out_dict['inp_set']
    print(json.dumps(out_dict, indent=2, sort_keys=True))
else:
    print(obj.returned)