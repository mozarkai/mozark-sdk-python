from pathlib import Path
from unittest import TestCase
import requests
from app_testing.client import Client
from app_testing.device import Device


class TestDevice(TestCase):

    def test_list_device(self):
        device = Device()
        list_device = device.get_device()
        print(list_device)
