import configparser
from pathlib import Path

import requests


class Client:
    config = None

    def __init__(self):
        self.set_config()

    def set_config(self):
        config = configparser.ConfigParser()
        config_file = Path.home() / ".mozark" / "config"
        config.read(config_file)
        api_url = config.get("default", "MOZARK_APP_TESTING_URL")
        username = config.get("default", "MOZARK_APP_TESTING_USERNAME")
        password = config.get("default", "MOZARK_APP_TESTING_PASSWORD")
        client_id = config.get("default", "MOZARK_APP_TESTING_CLIENTID")
        config = {"username": username, "password": password, "api_url": api_url, "client_id": client_id}
        self.config = config

    def get_config(self):
        return self.config

    def login(self):
        new_headers = {'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth',
                       'Content-Type': 'application/x-amz-json-1.1'}

        login_url = "https://cognito-idp.ap-south-1.amazonaws.com/"

        data = {
            "AuthParameters": {
                "USERNAME": self.config.get("username"),
                "PASSWORD": self.config.get("password")
            },
            "AuthFlow": "USER_PASSWORD_AUTH",
            "ClientId": self.config.get("client_id")
        }

        resp = requests.post(login_url, json=data, headers=new_headers)
        api_access_token = resp.json()['AuthenticationResult']['IdToken']
        self.config["api_access_token"] = api_access_token

