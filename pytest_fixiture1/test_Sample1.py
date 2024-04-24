import pytest


@pytest.mark.usefixtures("setup1")
def test_case1():
    print('testcase1')


@pytest.mark.usefixtures("setup1")
def test_case2():
    print("testcase2")