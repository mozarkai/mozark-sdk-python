import configparser
from pathlib import Path

import requests


class Client:
    config = None

    def __init__(self):
        self.set_config()

    def set_config(self):
        config = configparser.ConfigParser()
        config_file = Path.home() / ".mozark" / "config"
        config.read(config_file)
        api_url = config.get("default", "MOZARK_APP_TESTING_URL")
        username = config.get("default", "MOZARK_APP_TESTING_USERNAME")
        password = config.get("default", "MOZARK_APP_TESTING_PASSWORD")
        client_id = config.get("default", "MOZARK_APP_TESTING_CLIENTID")
        config = {"username": username, "password": password, "api_url": api_url, "client_id": client_id}
        self.config = config

    def get_config(self):
        return self.config

    def login(self):
        new_headers = {'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth',
                       'Content-Type': 'application/x-amz-json-1.1'}

        login_url = "https://cognito-idp.ap-south-1.amazonaws.com/"

        data = {
            "AuthParameters": {
                "USERNAME": self.config.get("username"),
                "PASSWORD": self.config.get("password")
            },
            "AuthFlow": "USER_PASSWORD_AUTH",
            "ClientId": self.config.get("client_id")
        }

        resp = requests.post(login_url, json=data, headers=new_headers)
        api_access_token = resp.json()['AuthenticationResult']['IdToken']
        self.config["api_access_token"] = api_access_token

    def logout(self):
        pass

    # Project
    def create_project(self, project_name=None):
        pass

    def get_project_info(self, project_name=None):
        pass

    def rename_project(self, project_name_old=None, project_name_new=None):
        pass

    def delete_project(self, project_name=None):
        pass

    def get_project_list(self):
        pass

    # Android Application

    def upload_android_application(self, project_name=None, file_path=None):
        pass

    def get_android_application_info(self, file_name=None):
        pass

    def rename_android_application(self, file_name_old=None, file_name_new=None):
        pass

    def delete_android_application(self, file_name=None):
        pass

    def get_android_application_list(self):
        pass

    # iOS Application
    def upload_ios_application(self, project_name=None, file_path=None):
        pass

    def get_ios_application_info(self, file_name=None):
        pass

    def rename_ios_application(self, file_name_old=None, file_name_new=None):
        pass

    def delete_ios_application(self, file_name=None):
        pass

    def get_ios_application_list(self):
        pass

    # Android Native Test Application

    def upload_android_native_test_application(self, project_name=None, file_path=None):
        pass

    def get_android_native_test_application_info(self, file_name=None):
        pass

    def rename_android_native_test_application(self, file_name_old=None, file_name_new=None):
        pass

    def delete_android_native_test_application(self, file_name=None):
        pass

    def get_android_native_test_application_list(self):
        pass

    # iOS Application
    def upload_ios_native_test_application(self, project_name=None, file_path=None):
        pass

    def get_ios_native_test_application_info(self, file_name=None):
        pass

    def rename_ios_native_test_application(self, file_name_old=None, file_name_new=None):
        pass

    def delete_ios_native_test_application(self, file_name=None):
        pass

    def get_ios_native_test_application_list(self):
        pass

    # Device

    def get_device_info(self, device_serial=None):
        pass

    def get_device_busy_slots(self, devices=None):
        pass

    def get_android_device_list(self):
        pass

    def get_ios_device_list(self):
        pass

    def get_living_room_device_list(self):
        pass

    def create_tray(self, tray_name=None):
        pass

    def get_tray_info(self, tray_name=None):
        pass

    def rename_tray(self, tray_name_old=None, tray_name_new=None):
        pass

    def delete_tray(self, tray_name=None):
        pass

    def get_device_list_by_tray(self, tray_name=None):
        pass

    # Test Configuration & Test Parameters

    def get_supported_test_configuration(self, platform=None):
        pass

    def get_mandatory_test_parameters(self, platform=None):
        pass

    # Test Execution

    def start_test_execution(self,
                             devices=None,
                             application_name=None,
                             test_application_name=None,
                             test_framework=None,
                             test_configuration=None,
                             test_parameters=None
                             ):
        pass

    def abort_test_execution(self, test_id=None):
        pass

    def schedule_test_execution(self,
                                devices=None,
                                application_name=None,
                                test_application_name=None,
                                test_framework=None,
                                test_configuration=None,
                                test_parameters=None,
                                test_start_datetime=None,
                                test_end_datetime=None,
                                interval=None
                                ):
        pass

    def get_test_schedule_info(self, schedule_id=None):
        pass

    def cancel_test_schedule(self, schedule_id=None):
        pass

    def get_test_schedule_list(self):
        pass

    # Test Analytics
    def get_test_execution_info_full(self, test_id=None):
        pass

    def get_test_execution_info_by_section(self, test_id=None, section=None):
        # Section = test_info, test_configuration, test_case_summary, test_cases, test_output_artifacts, events
        # KPIs,
        pass



