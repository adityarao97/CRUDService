from integrations.http_client import HttpClient


class PostsAPI:

    def __init__(self):
        self.http_client = HttpClient()
        self.BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_posts(self):
        url = self.BASE_URL + "/posts"
        response = self.http_client.get(url)
        return response
