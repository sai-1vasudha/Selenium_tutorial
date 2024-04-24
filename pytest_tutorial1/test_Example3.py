import pytest


@pytest.mark.sanity
def test_Sample4():

    assert 5*5 == 25

@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_Demo7():

    assert  100/5 == 20.0


@pytest.mark.regression
def test_Sample5():

    assert 25 == 25