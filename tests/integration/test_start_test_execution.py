import os
from app_testing.client import Client
from app_testing.project import Project
from app_testing.file import File

from unittest import TestCase


class TestStartTestExecution(TestCase):

    def test_start_test_execution_now(self):
        username = os.environ.get('MOZARK_APP_TESTING_USERNAME')
        password = os.environ.get('MOZARK_APP_TESTING_PASSWORD')
        client = Client()

        # login
        api_access_token = client.login(username=username, password=password)

        # Create Project
        project_name = "Sample Project Name"
        project = Project(api_access_token=self.api_access_token)
        project.create_project(project_name)

        # Upload Android Application
        android_application = "./sample.apk"
        file = File(api_access_token=self.api_access_token)
        file.upload_android_application(project_name=project_name, file_path=android_application)
