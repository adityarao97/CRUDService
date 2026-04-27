import requests


class HttpClient:

    @staticmethod
    def get(url, params=None, headers=None):
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def post(url, data=None, params=None, headers=None):
        response = requests.post(url, data=data, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
