
import sys
import re
import inspect
import ast
import pickle

class cli_router():

    def __init__(self, argv=sys.argv):

        derived_class = self.__class__.__name__
        base_class = cli_router.__name__
        self.returned = None
        if derived_class != base_class:

            if len(argv) > 1:

                if argv[1].startswith("~"):
                    method_name = argv[1][1:]
                else:
                    raise SyntaxError(
                        f"function name should precede positional arguments, eg : ~run")

                if not method_name.startswith("_"):

                    method_obj = getattr(self, method_name)

                    if inspect.ismethod(method_obj):

                        sign = inspect.signature(method_obj)
                        args, kwargs = self.__get_args(argv[2:], sign)
                        self.returned = method_obj(*args, **kwargs)
                        if sign.return_annotation == pickle:
                            print(f"writing pickle file as '{method_name}.pkl'")
                            with open(f'{method_name}.pkl', 'wb') as handle:
                                pickle.dump(self.returned, handle, protocol=pickle.HIGHEST_PROTOCOL)

                    else:
                        raise SyntaxError(
                            f"class {derived_class} derived from {base_class} should have method '{method_name}' defined")

                else:
                    raise SyntaxError(
                        f"~{method_name} : not supported, method name should not start with underscore, i.e _ ")

            else:
                self._help()
        else:
            raise SyntaxError(
                f"{base_class} should be used as parent class only")

    def __get_args(self, inp_args, sign):

        args = []
        kwargs = {}
        kwargs_started = False
        ordered_type_list = list(sign.parameters.items())
        ordered_type_dict = dict(sign.parameters.items())
        for i in range(len(inp_args)):
            kwargs_found = re.match("^-(\\S+)=(\\S+)$", inp_args[i])
            if kwargs_found:
                key, value = kwargs_found.groups()
                kwarg_type = ordered_type_dict[key].annotation if key in ordered_type_dict.keys(
                ) else None
                if kwarg_type and kwarg_type != str:
                    kwarg_val = ast.literal_eval(value)
                    if(type(kwarg_val) != kwarg_type):
                        raise SyntaxError(
                            f"Input for {key} should be of type {kwarg_type.__name__}")
                else:
                    kwarg_val = value
                kwargs[key] = kwarg_val
                kwargs_started = True
            else:
                if kwargs_started:
                    raise SyntaxError(
                        f"positional argument follows keyword argument {key}")
                else:
                    arg_type = ordered_type_list[i][1].annotation if i < len(
                        ordered_type_list) else None
                    if arg_type and arg_type != str:
                        arg_key = ordered_type_list[i][0]
                        arg_val = ast.literal_eval(inp_args[i])
                        if(type(arg_val) != arg_type):
                            raise SyntaxError(
                                f"Input for {arg_key} should be of type {arg_type.__name__}")
                    else:
                        arg_val = inp_args[i]
                    args.append(arg_val)

        return args, kwargs

    def __func(self, name, obj):

        print(f" > ~{name} ")
        print(f" |    ")

        func_comments = inspect.getcomments(obj)
        if func_comments:
            print(" |  Description :")
            print(f" |    ")
            comments = func_comments.splitlines()
            if len(comments) == 1:
                print(f" |    { comments[0].replace('#', '').strip() }  ")
            else:
                print(f" |    { comments[0].replace('#', '').strip() }  ")
                for i in range(1,len(comments)-1):
                    print(f" |    { comments[i].replace('#', '').strip() } ")
                print(f" |    { comments[-1].replace('#', '').strip() }  ")
            print(f" |    ")

        sign = inspect.signature(obj)
        args = [str(val) for var, val in sign.parameters.items()]
        if args:
            print(" |  Arguments :")
            print(f" |    ")
            for arg in args:
                print(f" |   -{arg}")
            print(f" |    ")

        func_docs = inspect.getdoc(obj)
        if func_docs:
            print(" |  Usage :")
            print(f" |    ")
            docs = func_docs.splitlines()
            if len(docs) == 1:
                print(f" |    { docs[0].strip() }  ")
            else:
                print(f" |    { docs[0].strip() }  ")
                for i in range(1,len(docs)-1):
                    print(f" |    { docs[i].strip() } ")
                print(f" |    { docs[-1].strip() }  ")
            print(f" |    ")

        if sign.return_annotation != sign.empty:
            if sign.return_annotation == pickle:
                print(f" | -> {sign.return_annotation.__name__} (Writable as '{name}.pkl')")
            elif sign.return_annotation == None:
                print(f" | -> {None} (Returnable)")
            else:
                print(f" | -> {sign.return_annotation.__name__} (Returnable)")

        # print(inspect.getdoc(obj))
        # return {
        #     "comment": comment.rstrip('\n') if comment else None,
        #     "docs": inspect.getdoc(obj),
        #     "args": [str(val) for var, val in sign.parameters.items()],
        #     "ret": sign.return_annotation.__name__ if sign.return_annotation else None
        # }

    def _help(self, func: str = None):

        if func:
            
            func_obj = getattr(self, func)
            if inspect.ismethod(func_obj):
                print()
                self.__func(func, func_obj)
        else:
            method_list = filter(
                lambda tup: not tup[0].startswith("_"),
                inspect.getmembers(self, predicate=inspect.ismethod)
            )
            print()
            for name, obj in method_list:
                self.__func(name, obj)
                print()



if __name__ == "__main__":

    cli_router()
