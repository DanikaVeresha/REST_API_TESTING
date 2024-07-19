"""
Task:
For https://gorest.co.in/, write test(s) to check post creation.
User, for who post will be created, should be created for test and removed after test
Post format: {'title': '<POST_TITLE>', 'body': '<POST_BODY>'}
You could write it in one file
"""
import requests


def test_status_code_for_requests_create_publication(
        main_url, headers, publication_data, user):
    """
    1. Create user for test
    2. Get user from the response
    3. Get iD new user
    4. Create publication for this user by user ID
    Check status code for requests create publication
    5. After testing delete user
    """
    assert user is not None
    create_user_publication = requests.post(
        f'{main_url}/{user}/posts', headers=headers, json=publication_data)
    assert create_user_publication.status_code == 201


def test_status_code_for_requests_get_publication(
        main_url, headers, publication_data, user):
    """
    1. Create user for test
    2. Get user from the response
    3. Get iD new user
    4. Create publication for this user by user ID
    5. Get publication for this user by user ID
    Check status code for requests get publication
    6. After testing delete user
    """
    assert user is not None
    requests.post(f'{main_url}/{user}/posts', headers=headers, json=publication_data)
    get_user_publication = requests.get(f'{main_url}/{user}/posts', headers=headers)
    assert get_user_publication.status_code == 200


def test_publication_data(
        main_url, headers, publication_data, user):
    """
    1. Create user for test
    2. Get user from the response
    3. Get iD new user
    4. Create publication for this user by user ID
    5. Get publication for this user by user ID
    Check TITLE on correctness for publication
    Check BODY on correctness for publication
    6. After testing delete user
    """
    assert user is not None
    requests.post(f'{main_url}/{user}/posts', headers=headers, json=publication_data)
    get_user_publication = requests.get(f'{main_url}/{user}/posts', headers=headers)
    assert get_user_publication.json()[0]['title'] == publication_data['title']
    assert get_user_publication.json()[0]['body'] == publication_data['body']


def test_status_code_for_requests_get_publication_after_user_delete(
        main_url, headers, publication_data, user_id):
    """
    1. Create user for test
    2. Get user from the response
    3. Get iD new user
    4. Create publication for this user by user ID
    5. Delete user
    5. Get publication for this user by user ID which was deleted
    Check status code for requests get publication after user delete
    """
    assert user_id is not None
    requests.post(f'{main_url}/{user_id}/posts', headers=headers, json=publication_data)
    requests.delete(f'{main_url}/{user_id}', headers=headers)
    get_user_publication = requests.get(f'{main_url}/{user_id}/posts', headers=headers)
    assert get_user_publication.status_code == 200


def test_publication_data_for_requests_get_publication_after_user_delete(
        main_url, headers, publication_data, user_id):
    """
    1. Create user for test
    2. Get user from the response
    3. Get iD new user
    4. Create publication for this user by user ID
    5. Delete user
    5. Get publication for this user by user ID which was deleted
    Check data of publication for requests get publication after user delete
    """
    assert user_id is not None
    requests.post(f'{main_url}/{user_id}/posts', headers=headers, json=publication_data)
    requests.delete(f'{main_url}/{user_id}', headers=headers)
    get_user_publication = requests.get(f'{main_url}/{user_id}/posts', headers=headers)
    assert get_user_publication.json() == []











