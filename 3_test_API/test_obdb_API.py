import pytest
import requests
import pprint


def test_search_brewery(base_adress_url):
    r = requests.get(base_adress_url + '/random')
    assert r.status_code == 200
    if r.status_code == 200:
        print("Success!", r.status_code)


def test_search_brewery_save(base_adress_url, put_parser_fixture):
    i = 0
    r = requests.get(base_adress_url + '/search?query=' + put_parser_fixture[0] + '&per_page=' + put_parser_fixture[1])
    json_r = r.json()
    while i < int(put_parser_fixture[1]):
        test_r = json_r[i]
        print(test_r['website_url'])
        if test_r['website_url'] != None:
            print("Pub have site!")
        else:
            # Есть бар без сайта!
            assert test_r['website_url'] != None
        i += 1
    print("Complete! All pubs have site!")


def test_brewery_param(base_adress_url, put_parser_fixture):
    i = 0
    r = requests.get(base_adress_url + '?by_type=' + str(put_parser_fixture[2][0]) + '&per_page=' + str(put_parser_fixture[2][1]))
    json_r = r.json()
    print(pprint.pprint(json_r))
    while i < int(put_parser_fixture[2][1]):
        test_r = json_r[i-1]
        print(test_r['brewery_type'])
        if test_r['brewery_type'] == str(put_parser_fixture[2][0]):
            print(str(put_parser_fixture[2][0]), "pub!")
        else:
            # Тип бара не совпадает
            assert test_r['brewery_type'] == str(put_parser_fixture[2][0])
        i += 1


def test_page_br(base_adress_url):
    r = requests.get(base_adress_url + '/?page=10&per_page=2')
    assert r.status_code == 200
    if r.status_code == 200:
        print("Success!", r.status_code)