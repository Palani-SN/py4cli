
import pytest
import os

cmd_dict = {
    # int
    'int_h': 'python scripts/use_int.py -h',
    'int_help': 'python scripts/use_int.py --help',
    'int': 'python scripts/use_int.py',
    'int_args': 'python scripts/use_int.py 10',
    'int_kwargs': 'python scripts/use_int.py -inp_int=10',

    # float
    'float_h': 'python scripts/use_float.py -h',
    'float_help': 'python scripts/use_float.py --help',
    'float': 'python scripts/use_float.py',
    'float_args': 'python scripts/use_float.py 10.0',
    'float_kwargs': 'python scripts/use_float.py -inp_float=10.0',

    # str
    'str_h': 'python scripts/use_str.py -h',
    'str_help': 'python scripts/use_str.py --help',
    'str': 'python scripts/use_str.py',
    'str_args': 'python scripts/use_str.py hello',
    'str_kwargs': 'python scripts/use_str.py -inp_str=hello',

    # list
    'list_h': 'python scripts/use_list.py -h',
    'list_help': 'python scripts/use_list.py --help',
    'list': 'python scripts/use_list.py',
    'list_args': 'python scripts/use_list.py [1,2,3]',
    'list_kwargs': 'python scripts/use_list.py -inp_list=[1,2,3]',

    # dict
    'dict_h': 'python scripts/use_dict.py -h',
    'dict_help': 'python scripts/use_dict.py --help',
    'dict': 'python scripts/use_dict.py',
    'dict_args': """python scripts/use_dict.py \"{'hello':'world'}\"""",
    'dict_kwargs': """python scripts/use_dict.py -inp_dict=\"{'hello':'world'}\"""",

    # bool
    'bool_h': 'python scripts/use_bool.py -h',
    'bool_help': 'python scripts/use_bool.py --help',
    'bool': 'python scripts/use_bool.py',
    'bool_args': 'python scripts/use_bool.py True',
    'bool_kwargs': 'python scripts/use_bool.py -inp_bool=True',

    # multi-args
    'multi_h': 'python scripts/multi_args.py -h',
    'multi_help': 'python scripts/multi_args.py --help',
    'multi': 'python scripts/multi_args.py',
    'multi_args': """python scripts/multi_args.py 10 10.0 Seven \"[10,10.0,'Seven']\" \"{'int':10,'float':10.0,'str':'Seven'}\" True""",
    'multi_kwargs': """python scripts/multi_args.py -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=\"[10,10.0,'Seven']\" -inp_dict=\"{'int':10,'float':10.0,'str':'Seven'}\" -inp_bool=True""",

    'multi_mix1': 'python scripts/multi_args.py 10 10.0 Seven',
    'multi_mix2': """python scripts/multi_args.py 10 10.0 Seven -inp_dict=\"{'int':10,'float':10.0,'str':'Seven'}\"""",
    'multi_mix3': """python scripts/multi_args.py -inp_dict=\"{'int':10,'float':10.0,'str':'Seven'}\"""",
}

cmd_vs_out = [ tuple([v, f'{k}.txt']) for k, v in cmd_dict.items() ]

cmd = None
file = None

@pytest.fixture(autouse = True, scope="function")
def fix_function():

    global cmd
    global file
    
    yield

    if os.path.exists(f'ref_files/{file}'):
        f1 = open(f'ref_files{os.sep}{file}', 'r')
        Ref_String = f1.read()
        f1.close()

        f2 = open(f'res_files{os.sep}{file}', 'r')
        Act_String = f2.read()
        f2.close()
        if file.endswith('_h.txt') or file.endswith('_help.txt'):
            for inp, out in zip(Ref_String.splitlines(), Act_String.splitlines()):
                if 'python' not in (inp+out):
                    assert(inp == out)
        else:
            assert(Ref_String == Act_String)

##########################################################################################################
## Single condition based tests for Solver 
##########################################################################################################

@pytest.mark.parametrize("args, fname", cmd_vs_out)
def test_os_calls(args, fname):

    global cmd
    global file
    cmd = args

    os.system(f"{cmd} > res_files{os.sep}{fname}")

    file = fname 
