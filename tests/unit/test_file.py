import json
import logging
import unittest

from mozark_sdk.client import Client


class TestFile(unittest.TestCase):

    def test_build_upload_application(self):
        client = Client()
        client.login()
        project_name = "Phonepe_RC"
        file_path="5gmark.apk"
        testType = "app-automation"
        self.application = client.upload_application(file_category="android-application", project_name=project_name,
                                                     file_path=file_path)
        response = self.application
        print(response)

    def test_script_upload_application(self):
        client = Client()
        client.login()
        project_name = "test2"
        file_path="5gmark.apk"
        response = client.upload_application(file_category="android-test-application",
                                             project_name=project_name,
                                             file_path=file_path)
        print(response)

    def test_get_application_info(self):
        client = Client()
        client.login()

        response = client.get_application_info(file_name="5gmark.apk")
        print(response)
        response = client.get_application_info(file_name="5gmark.apk")
        print(response)

    def test_delete_application(self):
        client = Client()
        client.login()
        response = client.delete_application(file_name="5gmark.apk")
        print(response)

    def test_get_application_list(self):
        # Android
        project_name = "for_icici"

        client = Client()
        client.login()

        response = client.get_application_list(file_category='android-application', project_name=project_name)
        print(json.dumps(response))

        project_name = 'Sample_ios_Project'
        response = client.get_application_list(file_category='ios-application', project_name=project_name)
        print(json.dumps(response))

        response = client.get_application_list()
        print(json.dumps(response))

    def test_get_application_list_all(self):
        # Android
        client = Client()
        client.login()

        response = client.get_application_list_all()
        print(json.dumps(response))

    def test_get_native_application_info(self):
        client = Client()
        client.login()

        response = client.get_native_test_application_info(file_name="netflix-androidTest.apk")
        print(json.dumps(response))
        response = client.get_native_test_application_info(file_name="5gmark_script.ipa")
        print(json.dumps(response))

    def test_get_native_application_list(self):
        # Android
        project_name = "sample project name"

        client = Client()
        client.login()

        response = client.get_native_test_application_list(file_category='android-test-application',
                                                           project_name=project_name)
        print(json.dumps(response))

        response = client.get_native_test_application_list()
        print(json.dumps(response))

    def test_md5(self):
        import hashlib

        filename = "./tests/unit/5gmark.apk"
        md5_hash = ''
        with open(filename, "rb") as f:
            bytes = f.read()  # read file as bytes
            readable_hash = hashlib.md5(bytes).hexdigest()
            md5_hash = readable_hash
        self.assertEqual("e7c961a45858f45c05e0c3ca7d9fe061", md5_hash)
