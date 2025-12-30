import json

import pytest
from datetime import datetime
import os
from utils.apis import API

import uuid


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    now = datetime.now().strftime("%Y%m%d-%H%M%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

def pytest_configure(config):
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)



@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("starting")
    yield
    print("End")

@pytest.fixture
def load_new_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__), "data", "Post_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
        return data


@pytest.fixture
def load_update_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__), "data", "Patch_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
        return data




pytest.fixture(scope="module")
def apis():
    return API()

@pytest.fixture(scope="module")
def user_id(apis):
    payload = {
        "name": "Test User",
        "gender": "male",
        "email": f"{uuid.uuid4().hex[:8]}@gmail.com",
        "status": "active"
    }

    response = apis.post("users", payload)
    assert response.status_code == 201

    user_id = response.json()["id"]
    yield user_id

    # Cleanup
    apis.delete(f"users/{user_id}")