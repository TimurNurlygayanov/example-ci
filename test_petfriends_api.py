#
# PetFriends project was created by Timur Nurlygaianov
# to provide basic environment for eduction of QA engineers
#
# More about PetFriends API:
# https://petfriends1.herokuapp.com/apidocs/
#

import requests


def test_get_api_key():
    """ Get API Key and check the length of the key. """

    url = 'https://petfriends1.herokuapp.com/api/key'
    res = requests.get(url, headers={'email': 'api@mail.ru',
                                     'password': 'test'})
    data = res.json()

    assert res.status_code == 200
    assert len(data['key']) == 56


def test_get_api_key_wrong_user():
    """ Try to get API Key with wrong user and make sure
        we can't get the key.
    """

    url = 'https://petfriends1.herokuapp.com/api/key'
    res = requests.get(url, headers={'email': 'api2@mail.ru',
                                     'password': 'TEST'})

    assert res.status_code == 403


def test_get_list_of_pets():
    """ Get list of pets and make sure it is not empty. """

    # Get API key
    url = 'https://petfriends1.herokuapp.com/api/key'
    res = requests.get(url, headers={'email': 'api@mail.ru',
                                     'password': 'test'})
    api_key = res.json()['key']

    # Get list of pets (API returns only latest 100 elements)
    url = 'https://petfriends1.herokuapp.com/api/pets'
    res = requests.get(url, headers={'auth_key': api_key})
    all_pets = res.json()['pets']

    # Make sure that list of pets contains 100 elements
    assert len(all_pets) == 100


def test_delete_pet():
    """ Delete some pet from the list of my pets. """

    url = 'https://petfriends1.herokuapp.com/api/key'
    res = requests.get(url, headers={'email': 'api@mail.ru',
                                     'password': 'test'})
    api_key = res.json()['key']

    # Create new pet
    url = 'https://petfriends1.herokuapp.com/api/create_pet_simple'
    res = requests.post(url, headers={'auth_key': api_key},
                        json={'name': 'Bob', 'animal_type': 'Dog', 'age': 5})
    pet_id_to_delete = res.json()['id']

    # Get list of my pets to make sure new pet is in list
    url = 'https://petfriends1.herokuapp.com/api/pets?filter=my_pets'
    res = requests.get(url, headers={'auth_key': api_key})
    all_pets = res.json()['pets']
    all_pets_ids = [pet['id'] for pet in all_pets]

    assert pet_id_to_delete in all_pets_ids

    # Delete pet
    url = 'https://petfriends1.herokuapp.com/api/pets/{0}'
    res = requests.delete(url.format(pet_id_to_delete),
                          headers={'auth_key': api_key})

    # Get list of my pets
    url = 'https://petfriends1.herokuapp.com/api/pets?filter=my_pets'
    res = requests.get(url, headers={'auth_key': api_key})
    all_pets = res.json()['pets']
    all_pets_ids = [pet['id'] for pet in all_pets]

    assert pet_id_to_delete not in all_pets_ids
