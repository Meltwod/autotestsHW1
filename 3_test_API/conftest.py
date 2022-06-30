import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--search",
        action="store",
        default="dog",
        help="Search for breweries based on a search term"
    )
    parser.addoption(
        "--per_page",
        action="store",
        default="5",
        help="Number of breweries to return each call"
    )
    parser.addoption(
        "--mode",
        action="store",
        default="1",
        help="1 - Large/5, 2 - Brewpub/4, 3 - bar/3"
    )


@pytest.fixture(params=[1, 2, 3, 4, 5])
def test_amount(request):
    return request.param


@pytest.fixture()
def put_parser_fixture(request):
    mode = [('large', 5), ('brewpub', 4), ('bar', 3)]
    return request.config.getoption("--search"), request.config.getoption("--per_page"), mode[int(request.config.getoption("--mode"))-1]


@pytest.fixture()
def base_adress_url():
    base_adress_url = 'https://api.openbrewerydb.org/breweries'
    return base_adress_url
