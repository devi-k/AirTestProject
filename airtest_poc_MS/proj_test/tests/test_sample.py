import pytest
from proj_test.common import assertions

def test_1(proj_setup_fix):
    print("Inside test 1")
    assertions.assert_equal(5,5)


def test_2(proj_setup_fix):
    print("Inside test 2")
    assertions.assert_not_equal(5,6)

