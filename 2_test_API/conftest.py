import pytest


@pytest.fixture(params=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def get_param_fixture(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--put",
        action="store",
        default="chow",
        help="This is part for url test api"
    )
    parser.addoption(
        "--amount",
        action="store",
        default="5",
        help="This is part for url test api"
    )


@pytest.fixture
def put_parser_fixture(request):
    breed_test = ['akita', 'african', 'beagle', 'boxer', 'chow', 'coonhound', 'clumber', 'dhole', 'eskimo', 'havanese']
    return request.config.getoption("--put"), breed_test, request.config.getoption("--amount")


@pytest.fixture()
def url_set_fixture(put_parser_fixture):
    base_adress_rnd = 'https://dog.ceo/api/breeds/image/random'
    base_adress_breed = 'https://dog.ceo/api/breed/' + put_parser_fixture[0] + '/images/random'
    base_adress_amount = 'https://dog.ceo/api/breeds/image/random/' + put_parser_fixture[2]
    return base_adress_breed, base_adress_rnd, base_adress_amount

@pytest.fixture()
def url_set_breeds_fixture(put_parser_fixture, get_param_fixture):
    get_param = put_parser_fixture[1]
    base_adress_breeds = 'https://dog.ceo/api/breed/' + get_param[get_param_fixture-1] + '/images/random'
    return base_adress_breeds



