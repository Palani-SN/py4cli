
import sys
import json
from basic_usage import multi_args

print(sys.argv)
obj = multi_args()
print("")
obj.returned['inp_set'] = set(obj.returned['inp_set'])
print(json.dumps(obj.returned, indent=2, sort_keys=True))