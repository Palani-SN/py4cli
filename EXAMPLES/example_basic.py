from basic import basic_use

obj = basic_use(["basic.py"])
print(obj.returned)

obj = basic_use(["basic.py", "~get_dtypes"])
print(obj.returned)