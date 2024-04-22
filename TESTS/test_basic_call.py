import pytest

#single args import 
from scripts.basic_usage import single_int
from scripts.basic_usage import single_float
from scripts.basic_usage import single_str
from scripts.basic_usage import single_list
from scripts.basic_usage import single_tuple
from scripts.basic_usage import single_set
from scripts.basic_usage import single_dict
from scripts.basic_usage import multi_args

int_arg_vs_ret = [ 
    ("basic_usage.py -h".split(), None),
    ("basic_usage.py --help".split(), None),
    ("basic_usage.py".split(), 0),
    ("basic_usage.py 10".split(), 10),
    ("basic_usage.py -inp_int=10".split(), 10),
    ]

float_arg_vs_ret = [ 
    ("basic_usage.py -h".split(), None),
    ("basic_usage.py --help".split(), None),
    ("basic_usage.py".split(), 0.0),
    ("basic_usage.py 10.0".split(), 10.0),
    ("basic_usage.py -inp_float=10.0".split(), 10.0),
    ]

str_arg_vs_ret = [ 
    ("basic_usage.py -h".split(), None),
    ("basic_usage.py --help".split(), None),
    ("basic_usage.py".split(), "None"),
    ("basic_usage.py Empty".split(), 'Empty'),
    ("basic_usage.py -inp_str=Empty".split(), 'Empty'),
    ]

list_arg_vs_ret = [ 
    ("basic_usage.py -h".split(), None),
    ("basic_usage.py --help".split(), None),
    ("basic_usage.py".split(), [None]),
    ("basic_usage.py ['Empty']".split(), ['Empty']),
    ("basic_usage.py -inp_list=['Empty']".split(), ['Empty']),
    ]

tuple_arg_vs_ret = [ 
    ("basic_usage.py -h".split(), None),
    ("basic_usage.py --help".split(), None),
    ("basic_usage.py".split(), (None,)),
    ("basic_usage.py ('Empty',)".split(), ('Empty',)),
    ("basic_usage.py -inp_tuple=('Empty',)".split(), ('Empty',)),
    ]

set_arg_vs_ret = [ 
    ("basic_usage.py -h".split(), None),
    ("basic_usage.py --help".split(), None),
    ("basic_usage.py".split(), {None}),
    ("basic_usage.py {'Empty'}".split(), {'Empty'}),
    ("basic_usage.py -inp_set={'Empty'}".split(), {'Empty'}),
    ]

dict_arg_vs_ret = [ 
    ("basic_usage.py -h".split(), None),
    ("basic_usage.py --help".split(), None),
    ("basic_usage.py".split(), {None:None}),
    ("basic_usage.py {'Empty':'Empty'}".split(), {'Empty':'Empty'}),
    ("basic_usage.py -inp_dict={'Empty':'Empty'}".split(), {'Empty':'Empty'}),
    ]

multi_arg_vs_ret = [ 
    ("basic_usage.py -h".split(), None),
    ("basic_usage.py --help".split(), None),
    ("basic_usage.py".split(), {
                'inp_int': 6,
                'inp_float': 6.0,
                'inp_str': 'Six',
                'inp_list': [6, 6.0, "Six"],
                'inp_tuple': (6, 6.0, "Six"),
                'inp_set': {6, 6.0, "Six"},
                'inp_dict': {'int': 6, 'float': 6.0, 'str': "Six"}
            }),
    ("basic_usage.py 10 10.0 Seven".split(), {
                'inp_int': 10,
                'inp_float': 10.0,
                'inp_str': 'Seven',
                'inp_list': [6, 6.0, "Six"],
                'inp_tuple': (6, 6.0, "Six"),
                'inp_set': {6, 6.0, "Six"},
                'inp_dict': {'int': 6, 'float': 6.0, 'str': "Six"}
            }),
    ("basic_usage.py 10 10.0 Seven -inp_dict={'int':10,'float':10.0,'str':'Seven'}".split(), {
                'inp_int': 10,
                'inp_float': 10.0,
                'inp_str': 'Seven',
                'inp_list': [6, 6.0, "Six"],
                'inp_tuple': (6, 6.0, "Six"),
                'inp_set': {6, 6.0, "Six"},
                'inp_dict': {'int': 10, 'float': 10.0, 'str': "Seven"}
            }),
    ("basic_usage.py -inp_set={10,10.0,'Seven',10,10.0,'Seven'} -inp_dict={'int':10,'float':10.0,'str':'Seven'}".split(), {
                'inp_int': 6,
                'inp_float': 6.0,
                'inp_str': 'Six',
                'inp_list': [6, 6.0, "Six"],
                'inp_tuple': (6, 6.0, "Six"),
                'inp_set': {10, 10.0, "Seven"},
                'inp_dict': {'int': 10, 'float': 10.0, 'str': "Seven"}
            }),
    ("basic_usage.py 10 10.0 Seven [10,10.0,'Seven'] (10,10.0,'Seven') {10,10.0,'Seven'} {'int':10,'float':10.0,'str':'Seven'}".split(), {
                'inp_int': 10,
                'inp_float': 10.0,
                'inp_str': 'Seven',
                'inp_list': [10, 10.0, "Seven"],
                'inp_tuple': (10, 10.0, "Seven"),
                'inp_set': {10, 10.0, "Seven"},
                'inp_dict': {'int': 10, 'float': 10.0, 'str': "Seven"}
            }),
    ("basic_usage.py -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,'Seven'] -inp_tuple=(10,10.0,'Seven') -inp_set={10,10.0,'Seven'} -inp_dict={'int':10,'float':10.0,'str':'Seven'}".split(), {
                'inp_int': 10,
                'inp_float': 10.0,
                'inp_str': 'Seven',
                'inp_list': [10, 10.0, "Seven"],
                'inp_tuple': (10, 10.0, "Seven"),
                'inp_set': {10, 10.0, "Seven"},
                'inp_dict': {'int': 10, 'float': 10.0, 'str': "Seven"}
            }),
    ]

args_in = None
OBJ = None
returned = None

@pytest.fixture(autouse = True, scope="function")
def fix_function():

    global args_in
    global OBJ
    global returned
    
    yield

    assert(returned == OBJ.returned)

##########################################################################################################
## Single condition based tests for Solver 
##########################################################################################################

@pytest.mark.parametrize("arg, ret", int_arg_vs_ret)
def test_single_int(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = single_int(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

@pytest.mark.parametrize("arg, ret", float_arg_vs_ret)
def test_single_float(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = single_float(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

@pytest.mark.parametrize("arg, ret", str_arg_vs_ret)
def test_single_str(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = single_str(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

@pytest.mark.parametrize("arg, ret", list_arg_vs_ret)
def test_single_list(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = single_list(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

@pytest.mark.parametrize("arg, ret", tuple_arg_vs_ret)
def test_single_tuple(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = single_tuple(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

@pytest.mark.parametrize("arg, ret", set_arg_vs_ret)
def test_single_set(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = single_set(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

@pytest.mark.parametrize("arg, ret", dict_arg_vs_ret)
def test_single_dict(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = single_dict(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

@pytest.mark.parametrize("arg, ret", multi_arg_vs_ret)
def test_multi_args(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = multi_args(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

