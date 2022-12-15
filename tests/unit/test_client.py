from unittest import TestCase
import configparser
from pathlib import Path
from app_testing.client import Client


class TestClient(TestCase):
    def test_config_read(self):
        config = configparser.ConfigParser()
        config_file = Path.home() / ".mozark" / "config"
        config.read(config_file)
        api_url = config.get("default", "MOZARK_APP_TESTING_URL")
        username = config.get("default", "MOZARK_APP_TESTING_USERNAME")
        password = config.get("default", "MOZARK_APP_TESTING_PASSWORD")
        client_id = config.get("default", "MOZARK_APP_TESTING_CLIENTID")

    def test_init_object(self):
        client = Client()
        api_url, username, password = client.get_config()
        print(api_url, username, password)
