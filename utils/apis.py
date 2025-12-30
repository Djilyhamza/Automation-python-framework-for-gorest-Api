import requests
import os
#commentt
class API:
    Base_URL = "https://gorest.co.in/public/v2/"

    def __init__(self):
        token = os.getenv("GOREST_TOKEN")


        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        return requests.get(self.Base_URL + endpoint, headers=self.headers)

    def post(self, endpoint, data):
        return requests.post(self.Base_URL + endpoint, headers=self.headers, json=data)

    def put(self, endpoint, data):
        return requests.put(self.Base_URL + endpoint, headers=self.headers, json=data)

    def delete(self, endpoint):
        return requests.delete(self.Base_URL + endpoint, headers=self.headers)
