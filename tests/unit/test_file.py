import logging
import unittest

from app_testing.file import File


class TestFile(unittest.TestCase):
    def test_upload_android_application(self):
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        file = File()
        file.upload_android_application(project_name="Sample Android Project", file_path="./sample.apk")
        self.assertEqual(True, False)
