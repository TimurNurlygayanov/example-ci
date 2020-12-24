import requests


def test():
    res = requests.get('https://mail.ru')
    assert res.status_code == 200
