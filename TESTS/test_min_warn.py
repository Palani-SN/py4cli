
import re
from minimal_scripts.basic_usage import warn_ret_type
from minimal_scripts.basic_usage import warn_wo_ret_typ_def
from minimal_scripts.basic_usage import warn_no_support_typ_arg
from minimal_scripts.basic_usage import warn_on_arg_order
from minimal_scripts.basic_usage import warn_on_undef_parse_args

def test_warn_ret_type1(capsys):

    obj = warn_ret_type("basic_usage.py --help".split())
    print(obj.returned)

def test_warn_ret_type2(capsys):

    obj = warn_ret_type("basic_usage.py".split())
    out, err = capsys.readouterr()
    assert re.match("WARNING : '(.+)' returns '(.+)', but defined to return '(.+)'", out)
    assert(False == obj.returned)
    print(obj.returned)

def test_warn_ret_type3():

    try:
        obj = warn_ret_type("basic_usage.py -inp_bool=50.456".split())
    except Exception as err:
        print(str(err))
        assert re.match("Expected '(.+)' value for '(.+)' in kwargs of method '(.+)', got '(.+)' instead", str(err))

def test_warn_wo_ret_typ_def1():

    obj = warn_wo_ret_typ_def("basic_usage.py --help".split())
    assert(None == obj.returned)
    print(obj.returned)

def test_warn_wo_ret_typ_def2():

    obj = warn_wo_ret_typ_def("basic_usage.py None".split())
    assert('None' == obj.returned)
    print(obj.returned)

def test_warn_no_support_typ_arg1(capsys):

    obj = warn_no_support_typ_arg("basic_usage.py --help".split())
    print(obj.returned)

def test_warn_no_support_typ_arg2():

    try:
        obj = warn_no_support_typ_arg("basic_usage.py None".split())
    except Exception as err:
        print(str(err))
        assert re.match("Unsupported argument data type : '(.+)', try using basic types \\(int, float, str, list, dict, bool\\) instead", str(err))

def test_warn_on_arg_order1(capsys):

    obj = warn_on_arg_order("basic_usage.py --help".split())
    print(obj.returned)

def test_warn_on_arg_order2():

    try:
        obj = warn_on_arg_order("basic_usage.py -inp_bool1=True False".split())
    except Exception as err:
        print(str(err))
        assert re.match("positional argument follows keyword argument '(.+)'", str(err))

def test_warn_on_arg_order3():

    try:
        obj = warn_on_arg_order("basic_usage.py -inp_bool1=hello -inp_bool2=[1,2,3,4,5,6]".split())
    except Exception as err:
        print(str(err))
        assert re.match("Expected '(.+)' value for '(.+)' in kwargs of method '(.+)', got '(.+)' instead", str(err))

def test_warn_on_undef_parse_args():

    try:
        obj = warn_on_undef_parse_args("basic_usage.py --help".split())
    except Exception as err:
        print(str(err))
        assert re.match("func name : '(.+)' is not defined", str(err))