import pytest
import os
from conftest import DEBUG

cmd_list = [

    'python scripts/use_int.py -h',
    'python scripts/use_float.py -h',
    'python scripts/use_str.py -h',
    'python scripts/use_list.py -h',
    'python scripts/use_tuple.py -h',
    'python scripts/use_set.py -h',
    'python scripts/use_dict.py -h',
    'python scripts/multi_args.py -h',

    'python scripts/use_int.py --help',
    'python scripts/use_float.py --help',
    'python scripts/use_str.py --help',
    'python scripts/use_list.py --help',
    'python scripts/use_tuple.py --help',
    'python scripts/use_set.py --help',
    'python scripts/use_dict.py --help',
    'python scripts/multi_args.py --help',

    'python scripts/use_int.py',
    'python scripts/use_float.py',
    'python scripts/use_str.py',
    'python scripts/use_list.py',
    'python scripts/use_tuple.py',
    'python scripts/use_set.py',
    'python scripts/use_dict.py',
    'python scripts/multi_args.py',

    'python scripts/use_int.py 10',
    'python scripts/use_float.py 10.0',
    'python scripts/use_str.py hello',
    'python scripts/use_list.py [1,2,3]',
    'python scripts/use_tuple.py (1,2,3)',
    'python scripts/use_set.py {1,2,3,1,2,3}',
    'python scripts/use_dict.py {\'hello\':\'world\'}',
    'python scripts/multi_args.py 10 10.0 Seven [10,10.0,\'Seven\'] (10,10.0,\'Seven\') {1,2,3,1,2,3} {\'int\':10,\'float\':10.0,\'str\':\'Seven\'}',

    'python scripts/use_int.py -inp_int=10',
    'python scripts/use_float.py -inp_float=10.0',
    'python scripts/use_str.py -inp_str=hello',
    'python scripts/use_list.py -inp_list=[1,2,3]',
    'python scripts/use_tuple.py -inp_tuple=(1,2,3)',
    'python scripts/use_set.py -inp_set={1,2,3,1,2,3}',
    'python scripts/use_dict.py -inp_dict={\'hello\':\'world\'}',
    'python scripts/multi_args.py -inp_int=10 -inp_float=10.0 -inp_str=Seven -inp_list=[10,10.0,\'Seven\'] -inp_tuple=(10,10.0,\'Seven\') -inp_set={1,2,3,1,2,3} -inp_dict={\'int\':10,\'float\':10.0,\'str\':\'Seven\'}',

    'python scripts/multi_args.py 10 10.0 Seven',
    'python scripts/multi_args.py 10 10.0 Seven -inp_dict={\'int\':10,\'float\':10.0,\'str\':\'Seven\'}',
    'python scripts/multi_args.py -inp_set={1,2,3,1,2,3} -inp_dict={\'int\':10,\'float\':10.0,\'str\':\'Seven\'}',
]

cmd_vs_out = [ tuple([cmd_list[i], f'single_{i+1}.txt']) for i in range(len(cmd_list))]

cmd = None
file = None

@pytest.fixture(autouse = True, scope="function")
def fix_function():

    global cmd
    global file
    
    yield

    if os.path.exists(f'ref_files/{file}'):
        f1 = open(f'ref_files/{file}', 'r')
        Ref_String = f1.read()
        f1.close()

        f2 = open(f'res_files/{file}', 'r')
        Act_String = f2.read()
        f2.close()
        assert(Ref_String == Act_String)

##########################################################################################################
## Single condition based tests for Solver 
##########################################################################################################

@pytest.mark.parametrize("args, fname", cmd_vs_out)
def test_os_calls(args, fname):

    global cmd
    global file
    cmd = args

    os.system(f"{cmd} > res_files/{fname}")

    file = fname 
