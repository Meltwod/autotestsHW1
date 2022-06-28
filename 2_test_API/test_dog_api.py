import pytest
import requests
import pprint


# url_set_fixture[0] - put url
# url_set_fixture[1] - rnd url

# 10 test api status
def test_get_image(get_param_fixture, url_set_fixture):
    r = requests.get(url_set_fixture[1])
    assert r.status_code == 200
    if r.status_code == 200:
        print("Success!", r.status_code)
    else:
        print("Error: ", r.status_code)
    print("----------Json----------")
    print(pprint.pprint(r.json()))


def test_put_breeds_image(put_parser_fixture, url_set_fixture, get_param_fixture):
    r = requests.get(url_set_fixture[0])
    assert r.status_code == 200
    if r.status_code == 200:
        print("Success!", r.status_code)
        print(pprint.pprint(r.json()))


def test_param_breeds_image(put_parser_fixture, url_set_breeds_fixture):
    r = requests.get(url_set_breeds_fixture)
    assert r.status_code == 200
    if r.status_code == 200:
        print("Success!", r.status_code)
        print(pprint.pprint(r.json()))


def test_amount_breeds_image(put_parser_fixture, url_set_fixture):
    r = requests.get(url_set_fixture[2])
    json_r = r.json()
    test_r = json_r['message']
    assert r.status_code == 200
    print(r.json())
    print("Количество выведенных картинок", len(test_r))


