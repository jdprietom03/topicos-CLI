import json
import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json" 
        }

    def get(self, endpoint, data = None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, data = json.dumps(data), headers=self.headers)
        return response

    def put(self, endpoint, data):
        self.headers["Content-Type"] = "multipart/form-data"
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, data=data, headers=self.headers)
        return response

    def list(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response

    def search(self, endpoint, query_params):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=query_params)
        return response
