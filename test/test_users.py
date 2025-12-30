import pytest
from utils.apis import API
from conftest import load_new_user_data
from conftest import load_update_user_data
from utils.apis import  API

import os
import uuid


@pytest.fixture(scope="module")
def apis():
    return API()


def test_get_user_validation(apis):
    response = apis.get("users")
    assert response.status_code == 200

def test_post_user(apis, load_new_user_data):
    test_data = load_new_user_data
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    test_data["email"] = unique_email
    response = apis.post("users", test_data)
    print(response.json())
    assert response.status_code == 201


def test_update_user(apis,user_id, load_update_user_data ):
    payload = load_update_user_data
    response = apis.put(f"users/{user_id}", payload)
    assert response.status_code == 200


def test_delete_user(apis, user_id):
    response = apis.delete(f"users/{user_id}")
    assert response.status_code == 204