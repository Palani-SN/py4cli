
import sys
import json
from basic_usage import multi_args

print(sys.argv)
obj = multi_args()
print("")
if obj.returned:
    out_dict = obj.returned.copy()
    print(json.dumps(out_dict, indent=2, sort_keys=True), type(obj.returned))
else:
    print(obj.returned, type(obj.returned))