import requests


def test_get_api_key():
    """ Get API Key and check the length of the key. """

    url = 'https://petfriends1.herokuapp.com/api/key'
    res = requests.get(url, headers={'email': 'api@mail.ru',
                                     'password': 'test'})
    data = res.json()

    assert res.status_code == 200
    assert len(data['key']) == 20

