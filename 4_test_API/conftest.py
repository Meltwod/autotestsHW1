import pytest


# parser.addoption(
#         "--search",
#         action="store",
#         default="dog",
#         help="Search for breweries based on a search term"
#     )

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="url, default - ya.ru"
    )


@pytest.fixture()
def put_parser_fixture(request):
    return request.config.getoption("--url")

