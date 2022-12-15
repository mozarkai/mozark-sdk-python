import os
import logging
from app_testing.client import Client
from app_testing.project import Project
from app_testing.file import File

from unittest import TestCase


class TestStartTestExecution(TestCase):

    def test_start_test_execution_now(self):
        logging.basicConfig(filename='mozark-app-testing.log', level=logging.INFO)
        client = Client()

        # login
        client.login()

        # Create Project
        project_name = "Sample Project Name"
        project = Project(client=client)
        project.create_project(project_name)

        # Upload Android Application
        android_application = "./5gmark.apk"
        file = File(client=client)
        file.upload_android_application(project_name=project_name, file_path=android_application)
