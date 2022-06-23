import random
import pytest
import math


@pytest.fixture
def print_hi_fixture():
    print("Hello, pytest! It's my first test with you!")


@pytest.fixture()
def return_rnd_number_fixture():
    return random.randint(9, 10)


class math_test_class:
    def __init__(self, x, y):
        self.x = x
        self.y = y


@pytest.fixture(scope="module")
def math_test_fixture():
    return math_test_class(x=50, y=25)


@pytest.fixture(scope="module")
def hello_module_fixture(math_test_fixture):
    print("Start module")
    yield
    print("50+25=", math_test_fixture.x + math_test_fixture.y)
    print("It's end module!")


@pytest.fixture(scope="session")
def hello_session_fixture():
    print("Hi session")
    yield
    print("End Session")


@pytest.fixture(params=[1, 2, 3, 4])
def param_fixture(request):
    return request.param


@pytest.fixture()
def list_fixture():
    l = [1]
    l.extend([2, 3, 4])
    return l
