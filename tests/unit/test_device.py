from unittest import TestCase
import json
from mozark_sdk.client import Client


class TestDevice(TestCase):

    def test_get_device_list(self):
        client = Client()
        client.login()
        response = client.get_device_list(platform="android")
        print(json.dumps(response))

        response = client.get_device_list(platform="ios")
        print(json.dumps(response))

        response = client.get_device_list(platform="living-room")
        print(json.dumps(response))

        response = client.get_device_list()
        print(json.dumps(response))

    def test_get_device_info(self):
        client = Client()
        client.login()
        response = client.get_device_list(platform="android")
        print(json.dumps(response))

        response = client.get_device_list(device_serial="e3a2211901a618a832d92b5cecec27ca049f0a0d")
        print(json.dumps(response))
