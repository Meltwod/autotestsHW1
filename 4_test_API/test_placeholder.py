import pytest
import requests
import pprint

# https://jsonplaceholder.typicode.com/posts/1
def test_jsonplaceholder():
    print('\n')
    r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(pprint.pprint(r.json()))


# yandex search
def test_yandex(put_parser_fixture):
    r = requests.get(put_parser_fixture)
    assert r.status_code == 200
    if r.status_code == 200:
        print("Success!", "200!")