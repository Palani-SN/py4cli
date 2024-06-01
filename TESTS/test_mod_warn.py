
import re
from moderate_scripts.basic_usage import vscaled_args

def test_warn_ret_type2(capsys):

    obj = vscaled_args("basic_usage.py ~warn_ret_type -inp_bool=50".split())
    out, err = capsys.readouterr()
    assert re.match("WARNING : '(.+)' returns '(.+)', but defined to return '(.+)'", out)
    assert(50 == obj.returned['warn_ret_type'])
    print(obj.returned)

def test_warn_wo_ret_typ_def2():

    obj = vscaled_args("basic_usage.py ~warn_wo_ret_typ_def None".split())
    assert('None' == obj.returned['warn_wo_ret_typ_def'])
    print(obj.returned)

def test_warn_no_support_typ_arg2():

    try:
        obj = vscaled_args("basic_usage.py ~warn_no_support_typ_arg None".split())
    except Exception as err:
        print(str(err))
        assert re.match("Unsupported argument data type : '<(.+)>', try using basic types \\(int, float, str, list, dict, bool\\) instead", str(err))

def test_warn_on_arg_order2():

    try:
        obj = vscaled_args("basic_usage.py ~warn_on_arg_order -inp_bool1=True False".split())
    except Exception as err:
        print(str(err))
        assert re.match("positional argument follows keyword argument '(.+)'", str(err))

def test_warn_on_undef_parse_args():

    try:
        obj = vscaled_args("basic_usage.py ~dummy_func -dummy_inp=10".split())
    except Exception as err:
        print(str(err))
        assert re.match(f"Undefined func names : (.+), try using defined func names (.+) instead", str(err))