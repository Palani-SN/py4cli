
import pytest
import os

cmd_dict = {

    # help
    'mod_h': 'python moderate_scripts/basic_usage.py -h',
    'mod_help': 'python moderate_scripts/basic_usage.py --help',

    # int
    'mod_int': 'python moderate_scripts/basic_usage.py ~single_int',
    'mod_int_args': 'python moderate_scripts/basic_usage.py ~single_int 10',
    'mod_int_kwargs': 'python moderate_scripts/basic_usage.py ~single_int -inp_int=10',

    # float
    'mod_float': 'python moderate_scripts/basic_usage.py ~single_float',
    'mod_float_args': 'python moderate_scripts/basic_usage.py ~single_float 10.0',
    'mod_float_kwargs': 'python moderate_scripts/basic_usage.py ~single_float -inp_float=10.0',

    # str
    'mod_str': 'python moderate_scripts/basic_usage.py ~single_str',
    'mod_str_args': 'python moderate_scripts/basic_usage.py ~single_str hello',
    'mod_str_kwargs': 'python moderate_scripts/basic_usage.py ~single_str -inp_str=hello',

    # list
    'mod_list': 'python moderate_scripts/basic_usage.py ~single_list',
    'mod_list_args': 'python moderate_scripts/basic_usage.py ~single_list [1,2,3]',
    'mod_list_kwargs': 'python moderate_scripts/basic_usage.py ~single_list -inp_list=[1,2,3]',

    # dict
    'mod_dict': 'python moderate_scripts/basic_usage.py ~single_dict',
    'mod_dict_args': """python moderate_scripts/basic_usage.py ~single_dict \"{'hello':'world'}\"""",
    'mod_dict_kwargs': """python moderate_scripts/basic_usage.py ~single_dict -inp_dict=\"{'hello':'world'}\"""",

    # bool
    'mod_bool': 'python moderate_scripts/basic_usage.py ~single_bool',
    'mod_bool_args': 'python moderate_scripts/basic_usage.py ~single_bool True',
    'mod_bool_kwargs': 'python moderate_scripts/basic_usage.py ~single_bool -inp_bool=True',

    # multi-args
    'mod_multi': 'python moderate_scripts/basic_usage.py ~multi_args',
    'mod_multi_args': """python moderate_scripts/basic_usage.py ~multi_args 10 10.0 Seven \"[10,10.0,'Seven']\" \"{'int':10,'float':10.0,'str':'Seven'}\" True""",
    'mod_multi_kwargs': """python moderate_scripts/basic_usage.py ~multi_args -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=\"[10,10.0,'Seven']\" -inp_dict=\"{'int':10,'float':10.0,'str':'Seven'}\" -inp_bool=True""",

    'mod_multi_mix1': 'python moderate_scripts/basic_usage.py ~multi_args 10 10.0 Seven',
    'mod_multi_mix2': """python moderate_scripts/basic_usage.py ~multi_args 10 10.0 Seven -inp_dict=\"{'int':10,'float':10.0,'str':'Seven'}\"""",
    'mod_multi_mix3': """python moderate_scripts/basic_usage.py ~multi_args -inp_dict=\"{'int':10,'float':10.0,'str':'Seven'}\"""",

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
