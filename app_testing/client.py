import logging


class Client:
    api_access_token = None

    def login(self, username=None, password=None):
        login_url = "https://cognito-idp.ap-south-1.amazonaws.com/"
        logging.info("Login URL: " + login_url)
        self.api_access_token = "Dummy Token"
        return self.api_access_token

