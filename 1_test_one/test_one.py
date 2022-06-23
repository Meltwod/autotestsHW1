import pytest


def test_session_start_end(hello_session_fixture):
    pass


def test_pass():
    pass


def test_print():
    print("Hello, i'm test_print!")


def test_start_fixture(print_hi_fixture):
    pass


def test_random_int(return_rnd_number_fixture):
    assert return_rnd_number_fixture == 10
    if return_rnd_number_fixture == 10:
        print("WOW! return_rnd_number == 10! It's fantastic!")


def test_module_start_end(hello_module_fixture, math_test_fixture):
    assert (math_test_fixture.x / math_test_fixture.y) == 2
    if (math_test_fixture.x / math_test_fixture.y) == 2:
        print("50/25=2! It's True!")


def test_params_with_fixture(param_fixture):
    print(param_fixture)


@pytest.mark.parametrize("param_one", [1, 2, 3, 4])
def test_comb_params_with_fix(param_fixture, param_one):
    print(param_fixture, param_one)


def test_list_with_fixture(list_fixture):
    list_fixture.extend(['add', 'more', 'obj list', 'with', 'def'])
    print(list_fixture)


def test_list_plus(list_fixture):
    i = 3
    while i < 9:
        k = list_fixture[i]
        list_fixture.extend([k*2])
        i += 1
    print(list_fixture)




