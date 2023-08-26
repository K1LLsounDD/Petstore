import requests
from requests import Response


class BaseApi:

    @staticmethod
    def get(path):
        response: Response = requests.get(path)
        return response


    @staticmethod
    def post(path, body):
        response: Response = requests.post(path, json=body)
        return response

    @staticmethod
    def post_only_path(path):
        response: Response = requests.post(path)
        return response


    @staticmethod
    def put(path, body):
        response: Response = requests.put(path, json=body)
        return response


    @staticmethod
    def delete(path):
        response: Response = requests.delete(path)
        return response