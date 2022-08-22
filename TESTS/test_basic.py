
import pytest
from basic import basic_use


def test_basic():

    basic_use(["basic.py"])

def test_list_as_input():

    basic_use(["basic.py", "~get_dtypes"])
