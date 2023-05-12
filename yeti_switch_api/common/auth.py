from requests.auth import AuthBase
from requests import post
import json


class Auth(AuthBase):
    def __init__(self, url, login=None, password=None):
        self.login = login
        self.password = password
        self.token = None
        self.url = url

    def __call__(self, r):
        if self.token is None:
            self.token = self.__get_token()

        r.headers["Authorization"] = self.token
        return r

    def refresh_token(self):
        self.token = self.__get_token()

    def __get_token(self):
        payload = {"auth": {"username": self.login, "password": self.password}}
        header = {"Content-type": "application/json"}
        response = post(f"{self.url}/auth", data=json.dumps(payload), headers=header)
        response.raise_for_status()
        access_token = json.loads(response.text)
        return access_token["jwt"]
