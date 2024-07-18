"""
For https://gorest.co.in/, write test(s) to check post creation.
User, for who post will be created, should be created for test and removed after test
Post format: {'title': '<POST_TITLE>', 'body': '<POST_BODY>'}
You could write it in one file
"""
import requests


def test_status_code_for_requests_create_publication(
        main_url, headers, user_data, publication_data, user
):
    assert user is not None
    create_user_publication = requests.post(
        f'{main_url}/{user}/posts', headers=headers, json=publication_data)
    assert create_user_publication.status_code == 201


def test_status_code_for_requests_get_publication(
        main_url, headers, user_data, publication_data, user
):
    assert user is not None
    create_user_publication = requests.post(
        f'{main_url}/{user}/posts', headers=headers, json=publication_data)
    get_user_publication = requests.get(f'{main_url}/{user}/posts', headers=headers)
    assert get_user_publication.status_code == 200


def test_publication_data(
        main_url, headers, user_data, publication_data, user
):
    assert user is not None
    create_user_publication = requests.post(
        f'{main_url}/{user}/posts', headers=headers, json=publication_data)
    get_user_publication = requests.get(f'{main_url}/{user}/posts', headers=headers)
    assert get_user_publication.json()[0]['title'] == publication_data['title']
    assert get_user_publication.json()[0]['body'] == publication_data['body']


def test_status_code_for_requests_get_publication_after_user_delete(
        main_url, headers, user_data, publication_data, user_deleted
):
    assert user_deleted is not None
    create_user_publication = requests.post(
        f'{main_url}/{user_deleted}/posts', headers=headers, json=publication_data)
    delete_user = requests.delete(f'{main_url}/{user_deleted}', headers=headers)
    get_user_publication = requests.get(f'{main_url}/{user_deleted}/posts', headers=headers)
    assert get_user_publication.status_code == 200


def test_publication_data_for_requests_get_publication_after_user_delete(
        main_url, headers, user_data, publication_data, user_deleted
):
    create_user_publication = requests.post(
        f'{main_url}/{user_deleted}/posts', headers=headers, json=publication_data)
    delete_user = requests.delete(f'{main_url}/{user_deleted}', headers=headers)
    get_user_publication = requests.get(f'{main_url}/{user_deleted}/posts', headers=headers)
    assert get_user_publication.json() == []



