import sys
from basic_usage import single_bool

print(sys.argv)
obj = single_bool()
print("")
print(obj.returned, type(obj.returned))