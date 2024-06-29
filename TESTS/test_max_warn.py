
import re
import json
from collections import OrderedDict
from maximal_scripts.demo import demo

def test_file_not_found():

    try:
        obj = demo("demo.py dummy.yml".split())
    except FileNotFoundError as err:
        print(str(err))
        assert str(err).endswith(('.yml', '.yaml', '.json'))

def test_empty_yml():

    obj = demo("demo.py maximal_scripts/empty.yml".split())
    assert obj.returned == OrderedDict()

def test_none_yml():

    try:
        obj = demo("demo.py maximal_scripts/none.yml".split())
    except TypeError as err: 
        assert re.match("(.+) missing (.+) required positional arguments: (.+)", str(err))

def test_empty_json():

    try:
        obj = demo("demo.py maximal_scripts/empty.json".split())
    except SyntaxError as err:
        print(str(err))
        assert str(err).endswith(('.yml', '.yaml', '.json'))

def test_none_json():

    obj = demo("demo.py maximal_scripts/none.json".split())
    assert obj.returned == OrderedDict()

def test_err_yml():

    try:
        obj = demo("demo.py maximal_scripts/error.yml".split())
    except SyntaxError as err:
        assert str(err).endswith(('.yml', '.yaml', '.json'))

def test_func_err():

    try:
        obj = demo("demo.py maximal_scripts/func_err.yml".split())
    except Exception as err:
        assert re.match(f"Undefined func names : (.+), try using defined func names (.+) instead", str(err))

def test_type_err1():

    try:
        obj = demo("demo.py maximal_scripts/type_err1.yml".split())
    except ValueError as err:
        assert re.match("(.+) Expected '(.+)' value for '(.+)' in kwargs of method '(.+)', got '(.+)' of '(.+)' instead", str(err))

def test_type_err2():

    try:
        obj = demo("demo.py maximal_scripts/type_err2.yml".split())
    except Exception as err:
        assert re.match("Unsupported argument data type : '(.+)', try using basic types \\(int, float, str, list, dict, bool\\) instead", str(err))
