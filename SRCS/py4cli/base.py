
import inspect
import ast
import sys


class py4cli_base():

    def __init__(self, argv=sys.argv):

        assert self.__class__.__name__ != "py4cli", "To be used as a parent classes."
        args = []
        kwargs = {}
        keywrd_arg = False
        file_name, method_name, arg_strs = argv[0], argv[1], argv[2:]
        for i in range(len(arg_strs)):
            key, value = None, None
            if (i < len(arg_strs)-1 and ("-" in arg_strs[i] or "--" in arg_strs[i])):
                key, value = arg_strs[i], arg_strs[i+1]
                if (key.startswith("--")):
                    kwargs[key[2:]] = value
                else:
                    kwargs[key[1:]] = value
                keywrd_arg = True
            elif(i > 0 and ("-" in arg_strs[i-1] or "--" in arg_strs[i-1])):
                continue
            else:
                if(keywrd_arg):
                    raise SyntaxError(
                        "positional argument follows keyword argument")
                else:
                    args.append(arg_strs[i])

        assert method_name in self.__class__.__dict__.keys(
        ), "method name should be defined in derived class"
        for name, object in self.__class__.__dict__.items():
            if str(type(object)) == "<class 'function'>":
                signature = inspect.signature(object)
                if(name == method_name):
                    idx = 0
                    for var, data_type in signature.parameters.items():
                        if(var != "self"):
                            if data_type.annotation != data_type.empty and data_type.annotation != str:
                                if(idx >= len(args) and var in kwargs.keys()):
                                    converted = ast.literal_eval(kwargs[var])
                                    assert type(
                                        converted) == data_type.annotation, f"Input should be of type {data_type.annotation}"
                                    kwargs[var] = converted
                                elif(idx >= len(args)):
                                    pass
                                else:
                                    converted = ast.literal_eval(args[idx])
                                    assert type(
                                        converted) == data_type.annotation, f"Input should be of type {data_type.annotation}"
                                    args[idx] = converted
                            idx += 1
                    result = object(self, *args, **kwargs)
                    break
        if signature.return_annotation != signature.empty:
            assert type(
                result) == signature.return_annotation, "Return type should be same as per function definition"
            print(result)


if __name__ == "__main__":

    py4cli_base()
