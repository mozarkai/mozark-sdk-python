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

        response = client.get_device_list(device_serial="5200d8204e1")
        print(json.dumps(response))

    def test_add_device(self):
        client = Client()
        client.login()
        device_parameter = {
            "brand": "Samsung",
            "modelName": "Galaxy S22",
            "serial": "5200d8204e1",
            "platform": "android",
            "osVersion": "12",
            "sdkVersion": ["31", "32"],
            "modelNumber": "SM-A107F",
            "deviceParameters": {
                "controllerId": "App-xp",
                "city": "Mumbai",
                "country": "",
                "network": ""
            }
        }
        response = client.add_device(device_parameter=device_parameter)
        print(json.dumps(response))

    # def test_delete_device(self):
    #     client = Client()
    #     client.login()
    #     response = client.(device_parameter=device_parameter)
    #     print(json.dumps(response))
