import os
import logging
from mozark_sdk.client import Client
from unittest import TestCase


class TestTray(TestCase):

    def test_create_tray(self):
        client = Client()
        client.login()

        device_list = ["RF8R70LNY6W"]
        response = client.create_tray(platform="android", tray_name="Sample_Tray_11", device_list=device_list)
        print("\n 1 create tray : ", response)

    def test_get_tray_info(self):
        client = Client()
        client.login()
        response = client.get_tray_info(tray_name="ioS")
        print("\n 2 get tray info : ", response)

    def test_get_tray_list(self):
        client = Client()
        client.login()
        response = client.get_tray_list()
        print("\n 3 get tray list : ", response)

    def test_update_tray(self):
        client = Client()
        client.login()
        device_list = ["RF8R70LNY6W", "RZ8R31QDBZF"]
        response = client.update_tray(tray_name="Sample_Tray_10", device_list=device_list)
        print("\n 4 update tray by device : ", response)

    def test_delete_tray(self):

        client = Client()
        client.login()
        response = client.delete_tray(tray_name="Sample_Tray_11")
        print("\n 5 delete tray by name : ", response)
