import requests


class JsonRequest:

    def __init__(self):
        self.headers = {
            'Content-Type': 'text/plain'
        }

    def get(self, url, data):

        content = requests.get(url, headers=self.headers, data=data).json()
        return content

    def post(self, url, data):

        content = requests.post(url, headers=self.headers, data=data).json()
        return content
