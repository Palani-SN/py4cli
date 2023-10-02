
from demo import route_args


class example(route_args):

    def concat_str(self, inp1, inp2, inp3) -> int:

        # print(inp1, inp2, inp3)
        return (inp1 + inp2 + inp3)

    def add_int(self, inp1: int, inp2: int, inp3: int) -> int:

        # print(inp1, inp2, inp3)
        return (inp1 + inp2 + inp3)


if __name__ == '__main__':

    run = example()
    print("---")
    for func in run.func_list:
        print("func : ")
        print(f"    {func['name']}")
        print("args : ")
        if func['args']:
            for arg in func['args']:
                print(f"    - {arg} # {type(arg)}")
        else:
            print("    xxx")
        print("kwargs : ")
        if func['kwargs']:
            for key, val in func['kwargs'].items():
                print(f"    {key} : {val} # {type(val)}")
        else:
            print("    xxx")
        print("ret : ")
        print(f"    {func['ret']} # {type(func['ret'])}")
        print("---")
