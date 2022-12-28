import logging
import unittest

from app_testing.file import File
from app_testing.client import Client


class TestFile(unittest.TestCase):
    def test_upload_android_application(self):
        logging.basicConfig(filename='mozark-app-testing.log', level=logging.INFO)
        file = File()
        file.upload_android_application(project_name="Sample Android Project", file_path="./sample.apk")
        self.assertEqual(True, False)

    def test_upload_android_test_application(self):
        logging.basicConfig(filename='mozark-app-testing.log', level=logging.INFO)

        client = Client()
        # login using the credentials configured in ~/.mozark/config
        client.login()

        # pass client object to reuse the configuration and api access token, default send md5 sum of the file
        file = File(client=client)

        # upload file
        file.upload_android_native_test_application(project_name="5Gmark_Android", file_path="./5gmark.apk")

        # pass client object to reuse the configuration and api access token, do not send the md5sum
        file = File(client=client, calculate_md5=False)

        # upload file
        file.upload_android_native_test_application(project_name="5Gmark_Android", file_path="./5gmark.apk")

        self.assertEqual(True, True)

    def test_md5(self):
        import hashlib

        filename = "./5gmark.apk"
        md5_hash = ''
        with open(filename, "rb") as f:
            bytes = f.read()  # read file as bytes
            readable_hash = hashlib.md5(bytes).hexdigest()
            md5_hash = readable_hash
        self.assertEqual("e7c961a45858f45c05e0c3ca7d9fe061", md5_hash)
