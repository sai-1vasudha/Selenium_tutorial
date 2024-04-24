import pytest


@pytest.mark.regression
def test_Demo6():

    assert  5+5 == 10


@pytest.mark.sanity
@pytest.mark.smoke
def test_Sample3():
    assert 15-5 == 10