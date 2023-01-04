from mozark_sdk.client import Client
from unittest import TestCase
from pathlib import Path


class TestTestAnalytics(TestCase):

    def test_get_test_list(self):
        client = Client()
        client.login()
        response = client.get_test_list(from_date_time=None, to_date_time=None)
        print("\n 1 get test list : ", response)

    def test_get_test_execution_info_full(self):
        client = Client()
        client.login()
        # test_id = '5a1126d2-9927-43fc-acda-61255b45ad3b'
        test_id = '95549b4f-24a0-4a9e-8520-2fbcf7db0f12'
        response = client.get_test_execution_info_full(test_id=test_id)
        print("\n 2 get test information : ", response)

    def test_get_test_information(self):
        client = Client()
        client.login()
        test_id = '95549b4f-24a0-4a9e-8520-2fbcf7db0f12'
        section = "screenshots"
        response = client.get_test_execution_info_by_section(test_id=test_id, section=section)
        print("\n 3 get test information : ", response)

    def test_download_by_section(self):
        client = Client()
        client.login()
        test_id = '95549b4f-24a0-4a9e-8520-2fbcf7db0f12'
        output_path = Path.home()/"down"
        section = 'output'
        file_name = 'battery.txt'
        # section = 'screenshots'
        # file_name = '2023-01-02T23-40-26-305650.jpg'
        response = client.download_by_section(test_id=test_id, section=section, file_name=file_name,
                                              output_path=output_path)
        print("\n 4 get test information : ", response)
