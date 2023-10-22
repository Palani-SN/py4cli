
from minimal import route_args


class single_args(route_args):

    # example parse_args template function with single argument of type <int>
    def parse_args(self, inp_int: int = 0) -> int:
        """
        inp_int is variable of type <int>
        any integer value can be passed for the argument, while the default is zero <0>
        the function returns the same arg value as type <int> 

        cmd :
            1. python example_usage.py 10
            2. python example_usage.py -inp_int=10
        """
        return inp_int


if __name__ == '__main__':

    sa = single_args()
    if sa.returned:
        print(sa.returned)
