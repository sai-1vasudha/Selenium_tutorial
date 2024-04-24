import pytest



@pytest.mark.smoke
@pytest.mark.regression
def test_Demo1():
    name = 'sai vasudha'
    assert name.upper() == "SAI VASUDHA"

@pytest.mark.regression
def test_Demo2():
    a, b = 10, 5
    c = a + b
    assert c == 15

@pytest.mark.smoke
def test_Demo3():
    subname  = 'PYTHON'
    assert subname.lower() == 'python'

@pytest.mark.regression
def test_Sample1():
    a = 10
    assert a*a == 100

@pytest.mark.regression
def test_Demo5():

    str = 'Python'

    count = len(str)

    assert count == 6

@pytest.mark.smoke
@pytest.mark.regression
def test_Sample2():

    str1,str2 = "Sai","vasudha"
    str3 = str1 + str2
    assert str3 == "Saivasudha"
