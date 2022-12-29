import os
import logging
from mozark_sdk.client import Client
from unittest import TestCase


class File(TestCase):

    def test_file_functionalities(self):
        client = Client()
        client.login()
        project_list = client.get_project_list()
        print(project_list)
        project_name = project_list[0]['name']
        print(project_name)

        # message = client.upload_android_application(project_name=project_name, file_path='/Users/sumitkumargupta/development/bitbucket/app-testing-api/docs/samples/app-qosi5gmark-debug.apk')
        # print(message)
        android_app_list = client.get_android_application_list(project_name=project_name)
        print(android_app_list)
        # ios_app_list = client.get_ios_application_list(project_name=project_name)
        # print(ios_app_list)
        android_app_details = client.get_android_application_info(file_name='app-qosi5gmark-debug.apk')
        print(android_app_details)

        test_app_list = client.get_android_native_test_application_list(project_name=project_name)
        print(test_app_list)

        # message = client.delete_android_application(file_id="6d3d9a7f-e551-46ed-b375-cf4521de8f8c")
        # print(message)
