
import pytest
import os

cmd_dict = {
    # int
    'min_int_h': 'python minimal_scripts/use_int.py -h',
    'min_int_help': 'python minimal_scripts/use_int.py --help',
    'min_int': 'python minimal_scripts/use_int.py',
    'min_int_args': 'python minimal_scripts/use_int.py 10',
    'min_int_kwargs': 'python minimal_scripts/use_int.py -inp_int=10',

    # float
    'min_float_h': 'python minimal_scripts/use_float.py -h',
    'min_float_help': 'python minimal_scripts/use_float.py --help',
    'min_float': 'python minimal_scripts/use_float.py',
    'min_float_args': 'python minimal_scripts/use_float.py 10.0',
    'min_float_kwargs': 'python minimal_scripts/use_float.py -inp_float=10.0',

    # str
    'min_str_h': 'python minimal_scripts/use_str.py -h',
    'min_str_help': 'python minimal_scripts/use_str.py --help',
    'min_str': 'python minimal_scripts/use_str.py',
    'min_str_args': 'python minimal_scripts/use_str.py hello',
    'min_str_kwargs': 'python minimal_scripts/use_str.py -inp_str=hello',

    # list
    'min_list_h': 'python minimal_scripts/use_list.py -h',
    'min_list_help': 'python minimal_scripts/use_list.py --help',
    'min_list': 'python minimal_scripts/use_list.py',
    'min_list_args': 'python minimal_scripts/use_list.py [1,2,3]',
    'min_list_kwargs': 'python minimal_scripts/use_list.py -inp_list=[1,2,3]',

    # dict
    'min_dict_h': 'python minimal_scripts/use_dict.py -h',
    'min_dict_help': 'python minimal_scripts/use_dict.py --help',
    'min_dict': 'python minimal_scripts/use_dict.py',
    'min_dict_args': """python minimal_scripts/use_dict.py \"{'hello':'world'}\"""",
    'min_dict_kwargs': """python minimal_scripts/use_dict.py -inp_dict=\"{'hello':'world'}\"""",

    # bool
    'min_bool_h': 'python minimal_scripts/use_bool.py -h',
    'min_bool_help': 'python minimal_scripts/use_bool.py --help',
    'min_bool': 'python minimal_scripts/use_bool.py',
    'min_bool_args': 'python minimal_scripts/use_bool.py True',
    'min_bool_kwargs': 'python minimal_scripts/use_bool.py -inp_bool=True',

    # multi-args
    'min_multi_h': 'python minimal_scripts/multi_args.py -h',
    'min_multi_help': 'python minimal_scripts/multi_args.py --help',
    'min_multi': 'python minimal_scripts/multi_args.py',
    'min_multi_args': """python minimal_scripts/multi_args.py 10 10.0 Seven \"[10,10.0,'Seven']\" \"{'int':10,'float':10.0,'str':'Seven'}\" True""",
    'min_multi_kwargs': """python minimal_scripts/multi_args.py -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=\"[10,10.0,'Seven']\" -inp_dict=\"{'int':10,'float':10.0,'str':'Seven'}\" -inp_bool=True""",

    'min_multi_mix1': 'python minimal_scripts/multi_args.py 10 10.0 Seven',
    'min_multi_mix2': """python minimal_scripts/multi_args.py 10 10.0 Seven -inp_dict=\"{'int':10,'float':10.0,'str':'Seven'}\"""",
    'min_multi_mix3': """python minimal_scripts/multi_args.py -inp_dict=\"{'int':10,'float':10.0,'str':'Seven'}\"""",
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
