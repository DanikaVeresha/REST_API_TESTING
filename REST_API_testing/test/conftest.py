"""
This file contains the fixtures that are used in the test cases.
"""

import pytest
import requests


@pytest.fixture(scope='session')
def main_url():
    return 'https://gorest.co.in/public/v2/users/'


@pytest.fixture(scope='session')
def headers():
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"
    }


@pytest.fixture(scope='session')
def user_data():
    return {
        'name': 'John Doe',
        'gender': 'male',
        'email': 'john@ce.com',
        'status': 'active'
    }


@pytest.fixture(scope='session')
def publication_data():
    return {
        'title': 'My Post',
        'body': 'This is my first post'
    }


@pytest.fixture()
def user(main_url, headers, user_data):
    requests.post(main_url, headers=headers, json=user_data)
    get_user = requests.get(main_url, headers=headers)
    get_user_id = get_user.json()[0]['id']
    yield get_user_id
    requests.delete(f'{main_url}/{get_user_id}', headers=headers)


@pytest.fixture()
def user_id(main_url, headers, user_data):
    requests.post(main_url, headers=headers, json=user_data)
    get_user = requests.get(main_url, headers=headers)
    get_user_id = get_user.json()[0]['id']
    return get_user_id











