import requests


def test_example():
    res = requests.get('https://google.com')
    assert res.status_code == 200
