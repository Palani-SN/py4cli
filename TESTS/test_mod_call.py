import pytest

#single args import 
from moderate_scripts.basic_usage import vscaled_args

multi_arg_vs_ret = [ 
    ("basic_usage.py -h".split(), None),
    ("basic_usage.py --help".split(), None),
    ("basic_usage.py ~single_bool True ~single_dict {'Empty':'Empty'} ~single_float 10.0 ~single_int 10 ~single_list ['Empty'] ~single_str Empty".split(), {
        "single_bool": True,
        "single_dict": {
            "Empty": "Empty"
        },
        "single_float": 10.0,
        "single_int": 10,
        "single_list": [
            "Empty"
        ],
        "single_str": "Empty"
    }),
    ("basic_usage.py ~single_bool -inp_bool=True ~single_dict -inp_dict={'Empty':'Empty'} ~single_float -inp_float=10.0 ~single_int -inp_int=10 ~single_list -inp_list=['Empty'] ~single_str -inp_str=Empty".split(), {
        "single_bool": True,
        "single_dict": {
            "Empty": "Empty"
        },
        "single_float": 10.0,
        "single_int": 10,
        "single_list": [
            "Empty"
        ],
        "single_str": "Empty"
    }),
    ("basic_usage.py ~multi_args -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,'Seven'] -inp_dict={'int':10,'float':10.0,'str':'Seven'} -inp_bool=True".split(), {
        "multi_args": {
            "inp_bool": True,
            "inp_dict": {
                "float": 10.0,
                "int": 10,
                "str": "Seven"
            },
            "inp_float": 10.0,
            "inp_int": 10,
            "inp_list": [
                10,
                10.0,
                "Seven"
            ],
            "inp_str": "Seven"
        }
    })
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
## vscaled_args
##########################################################################################################

@pytest.mark.parametrize("arg, ret", multi_arg_vs_ret)
def test_vscaled_args(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = vscaled_args(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

