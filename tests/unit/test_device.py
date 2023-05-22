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
              "modelName": "Galaxy M20",
              "serial": "3401868eba0a16fd",
              "platform": "android",
              "osVersion": "8.1.0",
              "modelNumber": "",
              "sdkVersion": [
                "31",
                "32"
              ],
              "deviceParameters": {
                "controllerId": "dubai-mac-1",
                "city": "Dubai",
                "country": "United Arab Emirates",
                "network": "",
                "liveLog": "https://{TenantName}}-logs.mozark.ai:10024",
                "deviceStatus": "free",
                "appiumPort": "4933",
                "mjpegServerPort": "1047",
                "systemPort": "8224",
                "chromedriverPort": "8024"
              },
              "logParameters": {
                "serverIpAddress": "{TenantName}}-logs.mozark.ai",
                "serverUserName": "ubuntu",
                "port": "10024",
                "mitmPort": "8024"
              }
            }
        response = client.add_device(device_parameter=device_parameter)
        print(json.dumps(response))

    # def test_delete_device(self):
    #     client = Client()
    #     client.login()
    #     response = client.(device_parameter=device_parameter)
    #     print(json.dumps(response))
