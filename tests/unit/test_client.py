from unittest import TestCase
import configparser
from pathlib import Path

from mozark_sdk.client import Client


class TestClient(TestCase):
    def test_config_read(self):
        config = configparser.ConfigParser()
        config_file = Path.home() / ".mozark" / "config"
        config.read(config_file)
        api_url = config.get("default", "MOZARK_APP_TESTING_URL")
        username = config.get("default", "MOZARK_APP_TESTING_USERNAME")
        password = config.get("default", "MOZARK_APP_TESTING_PASSWORD")
        client_id = config.get("default", "MOZARK_APP_TESTING_CLIENTID")
        print("1. ", username, "2. ", password, "3. ", api_url, "4. ", client_id)

    def test_test_configuration(self):
        client = Client()
        config = client.get_supported_test_configuration(platform="living-room")
        print(config)
