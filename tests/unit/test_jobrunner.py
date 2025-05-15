from unittest import TestCase
import json
from mozark_sdk.client import Client


class Testjobrunner(TestCase):

    def test_get_testsuite_list(self):
        client = Client()
        client.login()
        response = client.get_testsuite_list(test_filename="test.csv")
        print("12..",json.dumps(response))

        response = client.get_testsuite_list()
        print(json.dumps(response))

    def test_get_job_list(self):
        client = Client()
        client.login()
        response = client.get_job_list(id="7f320a39-4a24-4c9f-b72e-dc2bc1cf48c4")
        print("21..",json.dumps(response))

        response = client.get_job_list()
        print(json.dumps(response))

