import pytest
from collections import OrderedDict
#single args import 
from maximal_scripts.demo import demo
from maximal_scripts.a.aa.aa import AA
from maximal_scripts.a.ab.ab import AB
from maximal_scripts.b.ba.ba import BA
from maximal_scripts.b.bb.bb import BB

demo_arg_vs_ret = [ 
    ("demo.py".split(), OrderedDict()),
    ("demo.py -h".split(), OrderedDict()),
    ("demo.py --help".split(), OrderedDict()),
    ("demo.py maximal_scripts/demo.yml".split(), OrderedDict({
            "classes": {
              "ret_a": {
                "subclasses": {
                  "ret_aa": {
                    "sub_func": {
                      "ret_aaa": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_aab": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_aac": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_aad": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      }
                    }
                  },
                  "ret_ab": {
                    "sub_func": {
                      "ret_aba": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_abb": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_abc": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_abd": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      }
                    }
                  }
                }
              },
              "ret_b": {
                "subclasses": {
                  "ret_ba": {
                    "sub_func": {
                      "ret_baa": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_bab": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_bac": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_bad": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      }
                    }
                  },
                  "ret_bb": {
                    "sub_func": {
                      "ret_bba": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_bbb": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_bbc": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_bbd": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      }
                    }
                  }
                }
              }
            }
          }
        )
    ),
("demo.py maximal_scripts/demo.json".split(), OrderedDict({
            "classes": {
              "ret_a": {
                "subclasses": {
                  "ret_aa": {
                    "sub_func": {
                      "ret_aaa": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_aab": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_aac": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_aad": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      }
                    }
                  },
                  "ret_ab": {
                    "sub_func": {
                      "ret_aba": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_abb": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_abc": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_abd": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      }
                    }
                  }
                }
              },
              "ret_b": {
                "subclasses": {
                  "ret_ba": {
                    "sub_func": {
                      "ret_baa": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_bab": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_bac": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_bad": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      }
                    }
                  },
                  "ret_bb": {
                    "sub_func": {
                      "ret_bba": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_bbb": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_bbc": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      },
                      "ret_bbd": {
                        "k1": "v1",
                        "k2": "v2",
                        "k3": "v3"
                      }
                    }
                  }
                }
              }
            }
          }
        )
    )
]

aa_arg_vs_ret = [
    ("demo.py".split(), OrderedDict()),
    ("demo.py -h".split(), OrderedDict()),
    ("demo.py --help".split(), OrderedDict()),
]

ab_arg_vs_ret = [
    ("demo.py".split(), OrderedDict()),
    ("demo.py -h".split(), OrderedDict()),
    ("demo.py --help".split(), OrderedDict()),
]

ba_arg_vs_ret = [
    ("demo.py".split(), OrderedDict()),
    ("demo.py -h".split(), OrderedDict()),
    ("demo.py --help".split(), OrderedDict()),
]

bb_arg_vs_ret = [
    ("demo.py".split(), OrderedDict()),
    ("demo.py -h".split(), OrderedDict()),
    ("demo.py --help".split(), OrderedDict()),
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

@pytest.mark.parametrize("arg, ret", demo_arg_vs_ret)
def test_demo_args(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = demo(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

@pytest.mark.parametrize("arg, ret", aa_arg_vs_ret)
def test_aa_args(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = AA(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

@pytest.mark.parametrize("arg, ret", ab_arg_vs_ret)
def test_ab_args(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = AB(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

@pytest.mark.parametrize("arg, ret", ba_arg_vs_ret)
def test_ba_args(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = BA(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

@pytest.mark.parametrize("arg, ret", bb_arg_vs_ret)
def test_bb_args(arg, ret):

    global args_in
    global OBJ
    global returned

    args_in = arg
    OBJ = BB(args_in)
    returned = ret

    print("")
    if returned != OBJ.returned:
        print(f"{args_in} : Expected({returned}) != Actual({OBJ.returned})")
    else:
        print(f"{args_in} : Expected({returned}) == Actual({OBJ.returned})")
    print("")

