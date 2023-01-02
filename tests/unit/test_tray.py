import os
import logging
from mozark_sdk.client import Client
from unittest import TestCase


class TestTray(TestCase):

    def test_create_tray(self):
        client = Client()
        client.login()

        device_list = ["RF8R70LNY6W"]
        response = client.create_tray(platform="android", tray_name="Sample_Tray_10", device_list=device_list)
        print("\n 1 create tray : ", response)

    def test_get_tray_info(self):
        client = Client()
        client.login()
        response = client.get_tray_info(tray_name="Sample_Tray_10")
        print("\n 2 get tray info : ", response)

    def test_get_tray_list(self):
        client = Client()
        client.login()
        response = client.get_tray_list()
        print("\n 3 get tray list : ", response)

    def test_delete_tray(self):

        client = Client()
        client.login()
        response = client.delete_tray(tray_name="Sample_Tray_10")
        print("\n 5 delete tray by name : ", response)


    # def test_tray_functionalities(self):
    #     client = Client()
    #     # client.set_config()
    #     client.login()
    #     # device_list = client.get_android_device_list()
    #     # print(device_list)
    #     message = client.create_tray(tray_name='Sumit_Test', platform="android", device_list=["RF8R70LNY6W"])
    #     print(message)
    #     tray_list = client.get_tray_list()
    #     print(tray_list)
    #     tray_id = tray_list[0]['trayID']
    #     tray_info = client.get_device_list_by_tray(tray_id=tray_id)
    #     print(tray_info)
    #     message = client.update_tray_devices(tray_id=tray_id, device_list=[])
    #     print(message)
    #     tray_info = client.get_device_list_by_tray(tray_id=tray_id)
    #     print(tray_info)
    #     message = client.delete_tray(tray_id=tray_id)
    #     print(message)

        # Tray
        # Created
        # Successfully
        # [{'trayID': '1ef59c93-6877-4872-b05d-5d1168d83ffc', 'trayName': 'Sumit_Test', 'devices': ['RF8R70LNY6W'],
        #   'platform': 'android'}]
        # {"statusCode": 200, "body": [
        #     {"_id": "637b5bced97e6c00089bc8d6", "version": "1.0", "uuid": "41e69da7-596f-4e65-a9b7-76eb4375a36a",
        #      "brand": "Samsung", "modelName": "A32", "serial": "RF8R70LNY6W", "platform": "android", "osVersion": "11",
        #      "modelNumber": "", "sdkVersion": ["31", "32"],
        #      "deviceParameters": {"controllerId": "phuket-mac-1", "city": "Phuket", "country": "Thailand",
        #                           "network": "", "liveLog": "https://development-logs.mozark.ai:10028",
        #                           "deviceStatus": "free"},
        #      "logParameters": {"serverIpAddress": "development-logs.mozark.ai", "serverUserName": "ubuntu",
        #                        "port": "10028", "mitmPort": "8011"}}]}
        # [{'_id': '637b5bced97e6c00089bc8d6', 'version': '1.0', 'uuid': '41e69da7-596f-4e65-a9b7-76eb4375a36a',
        #   'brand': 'Samsung', 'modelName': 'A32', 'serial': 'RF8R70LNY6W', 'platform': 'android', 'osVersion': '11',
        #   'modelNumber': '', 'sdkVersion': ['31', '32'],
        #   'deviceParameters': {'controllerId': 'phuket-mac-1', 'city': 'Phuket', 'country': 'Thailand', 'network': '',
        #                        'liveLog': 'https://development-logs.mozark.ai:10028', 'deviceStatus': 'free'},
        #   'logParameters': {'serverIpAddress': 'development-logs.mozark.ai', 'serverUserName': 'ubuntu',
        #                     'port': '10028', 'mitmPort': '8011'}}]
        # Tray
        # Updated
        # Successfully
        # {"statusCode": 200, "body": []}
        # []
