import requests
import json


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)

        return response.content

    def load_json(self):
        json_data = []
        data = json.loads(self.get_response_body())

        for data in data:
            json_data.append(data)

        return json_data
