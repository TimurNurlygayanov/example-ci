import requests


def test_example():
    res = requests.get('https://goigle.com')
    assert res.status_code == 200
