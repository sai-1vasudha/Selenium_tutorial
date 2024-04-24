import pytest


@pytest.fixture(scope='module')
def setup():
    print('Browser is open')
    yield
    print('Browser is closed')


@pytest.fixture(scope='function')
def setup1():
    print('Browser is open')
    yield
    print('Browser is closed')



@pytest.fixture(scope='session')
def setup2():
    print('Browser is open')
    yield
    print('Browser is closed')


@pytest.fixture(scope='package')
def setup3():
    print('Browser is open')
    yield
    print('Browser is closed')