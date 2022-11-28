from . import utils
import pytest


def test_add_func():
    with pytest.raises(TypeError) as excinfo:
        # print("------------------", excinfo.value)
        # assert excinfo == "concatenate"
        utils.add(2, "4")
        print("------------------", excinfo.value)

