import configparser
from pathlib import Path

from mozark_sdk.file import File
from mozark_sdk.executetest import TestExecute
from mozark_sdk.device import Device
from mozark_sdk.testanalytics import TestAnalytics

import requests

from mozark_sdk.project import Project
from mozark_sdk.tray import Tray


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
        print(str(config))
        self.config = config

    def get_config(self):
        return self.config

    def login(self):
        new_headers = {'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth',
                       'Content-Type': 'application/x-amz-json-1.1'}

        login_url = "https://cognito-idp.ap-south-1.amazonaws.com/"
        print(login_url)
        data = {
            "AuthParameters": {
                "USERNAME": self.config.get("username"),
                "PASSWORD": self.config.get("password")
            },
            "AuthFlow": "USER_PASSWORD_AUTH",
            "ClientId": self.config.get("client_id")
        }
        print(str(data))
        resp = requests.post(login_url, json=data, headers=new_headers)
        api_access_token = resp.json()['AuthenticationResult']['IdToken']
        self.config["api_access_token"] = api_access_token
        print(str(self.config))

    def logout(self):
        pass

    # Project

    def create_project(self, project_name=None, project_description=None):
        """Create a new project
        Args:
            project_name (str): unique project name
            project_description (str): short description for a project

        Returns:
            message (str): 'Success' if successful, 'Failure' along with failure reason

            "Failure: Project with `{project_name}` already exists." - in case if project with the given name already exists
        """
        project = Project()
        status_message = project.create_project(project, project_name, project_description)
        return status_message
        # pass

    def get_project_info(self, project_name=None):
        """ Returns project information -
        Args:
            project_name (str): project name

        Returns:
            project (dict): contains projectName, projectDescription, and unique ID
            {
                "projectName": "",
                "projectDescription": "",
                "projectUUID": ""
            }
        """
        project = Project()
        status_message = project.get_projects(project, project_name)
        return status_message
        # pass

    # def rename_project(self, project_name_old=None, project_name_new=None):
    #     pass

    # def delete_project(self, project_name=None):
    #     """ Delete project with given project name
    #
    #     Args:
    #         project_name (str): project name
    #
    #     Returns:
    #         message (str): 'Success' if successful, 'Failure' along with failure reason
    #     """
    #     pass

    def get_project_list(self):
        """ Returns list of all projects

        Returns:
            projects (list): list of project dict

            [
                {
                    "projectName": "abc",
                    "projectDescription" : "abc desc",
                    "projectUUID": "aabbcc"
                },
                {
                    "projectName": "xyz",
                    "projectDescription": "xyz desc",
                    "projectUUID": "aabbcd"
                }
            ]

        """
        project = Project(client=self)
        status_message = project.get_projects(project)
        return status_message
        # pass

    # Android Application

    def upload_android_application(self, project_name=None, file_path=None):
        """ Upload android application(.apk) from given file path

        Args:
            project_name (str): Container project for the application
            file_path (str): relative or absolute path of the file

        Returns:
            message (str): 'Success' if uploaded successfully, 'Failure' along with failure reason

            "Failure: File with `{file_name}` already exists." - in case if file with checksum already exists
        """
        file = File(client=self)
        status = file.upload_android_application(project_name=project_name, file_path=file_path)
        return status

    def get_android_application_info(self, file_name=None):
        """ Returns android file information

        Args:
            file_name (str): unique file name

        Returns:
            fileinfo (dict): dictionary containing the metadata about the file

            {
                "fileName" : "",
                "fileCategory": "android-application",
                "md5": "",
                "fileURL": "",
                "fileUUID": "",
                "packageName": ""
            }
        """
        # pass
        file = File(client=self)
        app_list = file.list_android_application(file, file_name=file_name)
        return app_list

    # def rename_android_application(self, file_name_old=None, file_name_new=None):
    #     pass

    def delete_android_application(self, file_id=None):
        # pass
        file = File(client=self)
        status = file.delete_file(file, file_id=file_id)
        return status

    def get_android_application_list(self, project_name=None):
        """ Returns list of all android application file information

        Returns:
            fileinfo (list): dictionary containing the metadata about the file

            [
                {
                    "fileName" : "",
                    "fileCategory": "android-application",
                    "md5": "",
                    "fileURL": "",
                    "fileUUID": "",
                    "packageName": ""
                },
                {
                    "fileName" : "",
                    "fileCategory": "android-application",
                    "md5": "",
                    "fileURL": "",
                    "fileUUID": "",
                    "packageName": ""
                }
            ]
        """
        # pass
        file = File(client=self)
        app_list = file.list_android_application(file, project_name=project_name)
        return app_list

    # iOS Application
    def upload_ios_application(self, project_name=None, file_path=None):
        """ Upload ios application(.ipa) from given file path

        Args:
            project_name (str): Container project for the application
            file_path (str): relative or absolute path of the file

        Returns:
            message (str): 'Success' if uploaded successfully, 'Failure' along with failure reason

            "Failure: File with `{file_name}` already exists." - in case if file with checksum already exists
        """
        # pass
        file = File(client=self)
        status = file.upload_ios_application(project_name=project_name, file_path=file_path)
        return status

    def get_ios_application_info(self, file_name=None):
        """ Returns ios application file information

        Args:
            file_name (str): unique file name

        Returns:
            fileinfo (dict): dictionary containing the metadata about the file

            {
                "fileName" : "",
                "fileCategory": "ios-application",
                "md5": "",
                "fileURL": "",
                "fileUUID": "",
                "packageName": ""
            }
        """
        # pass
        file = File(client=self)
        app_list = file.list_ios_application(file, file_name=file_name)
        return app_list

    # def rename_ios_application(self, file_name_old=None, file_name_new=None):
    #     pass

    def delete_ios_application(self, file_id=None):
        # pass
        file = File(client=self)
        status = file.delete_file(file, file_id=file_id)
        return status

    def get_ios_application_list(self, project_name=None):
        """ Returns list of all ios application file information

        Returns:
            fileinfo (list): dictionary containing the metadata about the file

            [
                {
                    "fileName" : "",
                    "fileCategory": "ios-application",
                    "md5": "",
                    "fileURL": "",
                    "fileUUID": "",
                    "packageName": ""
                },
                {
                    "fileName" : "",
                    "fileCategory": "ios-application",
                    "md5": "",
                    "fileURL": "",
                    "fileUUID": "",
                    "packageName": ""
                }
            ]
        """
        # pass
        file = File(client=self)
        app_list = file.list_ios_application(file, project_name=project_name)
        return app_list

    # Android Native Test Application

    def upload_android_native_test_application(self, project_name=None, file_path=None):
        """ Upload android native test application(.apk) from given file path

        Args:
            project_name (str): Container project for the application
            file_path (str): relative or absolute path of the file

        Returns:
            message (str): 'Success' if uploaded successfully, 'Failure' along with failure reason

            "Failure: File with `{file_name}` already exists." - in case if file with checksum already exists
        """
        # pass
        file = File(client=self)
        status = file.upload_android_native_test_application(project_name=project_name, file_path=file_path)
        return status

    def get_android_native_test_application_info(self, file_name=None):
        """ Returns android native test application file information

        Args:
            file_name (str): unique file name

        Returns:
            fileinfo (dict): dictionary containing the metadata about the file

            {
                "fileName" : "",
                "fileCategory": "android-test-application",
                "md5": "",
                "fileURL": "",
                "fileUUID": "",
                "testCodePackageName": "",
                "testRunnerName": ""
            }
        """
        # pass
        file = File(client=self)
        app_list = file.list_android_native_test_application(file, file_name=file_name)
        return app_list

    # def rename_android_native_test_application(self, file_name_old=None, file_name_new=None):
    #     pass

    def delete_android_native_test_application(self, file_id=None):
        # pass
        file = File(client=self)
        status = file.delete_file(file, file_id=file_id)
        return status

    def get_android_native_test_application_list(self, project_name=None, file_name=None):
        """ Returns list of all android native test application file information

        Returns:
            fileinfo (list): dictionary containing the metadata about the file

            [
                {
                    "fileName" : "",
                    "fileCategory": "android-test-application",
                    "md5": "",
                    "fileURL": "",
                    "fileUUID": "",
                    "testCodePackageName": "",
                    "testRunnerName": ""
                },
                {
                    "fileName" : "",
                    "fileCategory": "android-test-application",
                    "md5": "",
                    "fileURL": "",
                    "fileUUID": "",
                    "testCodePackageName": "",
                    "testRunnerName": ""
                }
            ]
        """
        # pass
        file = File(client=self)
        app_list = file.list_android_native_test_application(file, project_name=project_name, file_name=file_name)
        return app_list

    # iOS Application
    def upload_ios_native_test_application(self, project_name=None, file_path=None):
        """ Upload ios native test application(.ipa) from given file path

        Args:
            project_name (str): Container project for the application
            file_path (str): relative or absolute path of the file

        Returns:
            message (str): 'Success' if uploaded successfully, 'Failure' along with failure reason

            "Failure: File with `{file_name}` already exists." - in case if file with checksum already exists
        """
        # pass
        file = File(client=self)
        status = file.upload_ios_native_test_application(project_name=project_name, file_path=file_path)
        return status

    def get_ios_native_test_application_info(self, file_name=None):
        """ Returns ios native test application file information

        Args:
            project_name (str): project names
            file_name (str): unique file name

        Returns:
            fileinfo (dict): dictionary containing the metadata about the file

            {
                "fileName" : "",
                "fileCategory": "ios-test-application",
                "md5": "",
                "fileURL": "",
                "fileUUID": "",
                "XCTestRunFileUrl": ""
            }
        """
        # pass
        file = File(client=self)
        status = file.list_ios_native_test_application(file_name=file_name)
        return status

    # def rename_ios_native_test_application(self, file_name_old=None, file_name_new=None):
    #     pass

    def delete_ios_native_test_application(self, file_id=None):
        # pass
        file = File(client=self)
        status = file.delete_file(file, file_id=file_id)
        return status

    def get_ios_native_test_application_list(self, project_name=None):
        """ Returns list of all ios native test application file information

        Returns:
            fileinfo (list): dictionary containing the metadata about the file

            [
                {
                    "fileName" : "",
                    "fileCategory": "ios-test-application",
                    "md5": "",
                    "fileURL": "",
                    "fileUUID": "",
                    "XCTestRunFileUrl": ""
                },
                {
                    "fileName" : "",
                    "fileCategory": "ios-test-application",
                    "md5": "",
                    "fileURL": "",
                    "fileUUID": "",
                    "XCTestRunFileUrl": ""
                }
            ]
        """
        # pass
        file = File(client=self)
        status = file.list_ios_native_test_application(project_name=project_name)
        return status

    # Device

    def get_device_info(self, device_serial=None):
        """ Returns device information given a device serial

        Args:
            device_serial (str): unique device serial

        Returns:
            device_info (dict): dictionary containing the information about the device

            {
                "deviceSerial": "",
                "deviceBrand": "",
                "deviceCity": "",
                "deviceCountry": "",
                "deviceModelName": "",
                "deviceModelNumber": "",
                "devicePlatform": "android | ios",
                "deviceOSVersion": "",
                "deviceSDKVersion": ["", ""],
                "deviceUUID": "",
                "deviceNetwork": ""
            }
        """
        pass

    # def get_device_busy_slots(self, devices=None):
    #     pass

    def get_android_device_list(self):
        """ Returns device information of all android devices

        Returns:
            device_info (list): list of dictionary containing the information about the device

            [
                {
                    "deviceSerial": "",
                    "deviceBrand": "",
                    "deviceCity": "",
                    "deviceCountry": "",
                    "deviceModelName": "",
                    "deviceModelNumber": "",
                    "devicePlatform": "android",
                    "deviceOSVersion": "",
                    "deviceSDKVersion": ["", ""],
                    "deviceUUID": "",
                    "deviceNetwork": ""
                },
                {
                    "deviceSerial": "",
                    "deviceBrand": "",
                    "deviceCity": "",
                    "deviceCountry": "",
                    "deviceModelName": "",
                    "deviceModelNumber": "",
                    "devicePlatform": "android",
                    "deviceOSVersion": "",
                    "deviceSDKVersion": ["", ""],
                    "deviceUUID": "",
                    "deviceNetwork": ""
                }
            ]
        """
        # pass
        device = Device(client=self)
        device_list = device.get_devices(device, "android")
        return device_list

    def get_ios_device_list(self):
        """ Returns device information of all iOS devices

        Returns:
            device_info (list): list of dictionary containing the information about the device

            [
                {
                    "deviceSerial": "",
                    "deviceBrand": "",
                    "deviceCity": "",
                    "deviceCountry": "",
                    "deviceModelName": "",
                    "deviceModelNumber": "",
                    "devicePlatform": "ios",
                    "deviceOSVersion": "",
                    "deviceSDKVersion": ["", ""],
                    "deviceUUID": "",
                    "deviceNetwork": ""
                },
                {
                    "deviceSerial": "",
                    "deviceBrand": "",
                    "deviceCity": "",
                    "deviceCountry": "",
                    "deviceModelName": "",
                    "deviceModelNumber": "",
                    "devicePlatform": "ios",
                    "deviceOSVersion": "",
                    "deviceSDKVersion": ["", ""],
                    "deviceUUID": "",
                    "deviceNetwork": ""
                }
            ]
        """
        # pass
        device = Device(client=self)
        device_list = device.get_devices(device, "ios")
        return device_list

    def get_living_room_device_list(self):
        """ Returns device information of all living room devices

        Returns:
            device_info (list): list of dictionary containing the information about the device

            [
                {
                    "deviceSerial": "",
                    "deviceBrand": "",
                    "deviceCity": "",
                    "deviceCountry": "",
                    "deviceModelName": "",
                    "deviceModelNumber": "",
                    "devicePlatform": "living-room",
                    "deviceOSVersion": "",
                    "deviceSDKVersion": ["", ""],
                    "deviceUUID": "",
                    "deviceNetwork": ""
                },
                {
                    "deviceSerial": "",
                    "deviceBrand": "",
                    "deviceCity": "",
                    "deviceCountry": "",
                    "deviceModelName": "",
                    "deviceModelNumber": "",
                    "devicePlatform": "living-room",
                    "deviceOSVersion": "",
                    "deviceSDKVersion": ["", ""],
                    "deviceUUID": "",
                    "deviceNetwork": ""
                }
            ]
        """
        # pass
        device = Device(client=self)
        device_list = device.get_lr_devices()
        return device_list

    def create_tray(self, tray_name=None, platform=None, device_list=None):
        """ Create tray for a given device platform category

        Args:
            tray_name (str): Unique tray name
            device_list (str): device list
            platform(str): type of devices

        Returns:
            message (str): 'Success' if tray is created successfully, 'Failure' along with failure reason

            "Failure: Tray with `{tray_name}` already exists" - in case if a tray with a given name already exists
        """
        # pass
        tray = Tray(client=self)
        status = tray.create_tray(name=tray_name, platform=platform, device_list=device_list)
        return status

    def get_tray_list(self):
        # pass
        tray = Tray(client=self)
        status = tray.list_tray()
        return status

    def update_tray_devices(self, tray_id=None, device_list=None):
        # pass
        tray = Tray(client=self)
        status = tray.update_tray(tray_id=tray_id, device_list=device_list)
        return status

    def delete_tray(self, tray_id=None):
        # pass
        tray = Tray(client=self)
        status = tray.delete_tray(tray_id=tray_id)
        return status

    def get_device_list_by_tray(self, tray_id=None):
        """ Returns device information of all devices added as part of a given tray

        Returns:
            device_info (list): list of dictionary containing the information about the device

            [
                {
                    "deviceSerial": "",
                    "deviceBrand": "",
                    "deviceCity": "",
                    "deviceCountry": "",
                    "deviceModelName": "",
                    "deviceModelNumber": "",
                    "devicePlatform": "android",
                    "deviceOSVersion": "",
                    "deviceSDKVersion": ["", ""],
                    "deviceUUID": "",
                    "deviceNetwork": ""
                },
                {
                    "deviceSerial": "",
                    "deviceBrand": "",
                    "deviceCity": "",
                    "deviceCountry": "",
                    "deviceModelName": "",
                    "deviceModelNumber": "",
                    "devicePlatform": "android",
                    "deviceOSVersion": "",
                    "deviceSDKVersion": ["", ""],
                    "deviceUUID": "",
                    "deviceNetwork": ""
                }
            ]
        """

        # pass
        tray = Tray(client=self)
        status = tray.get_tray_info(tray_id=tray_id)
        return status



    # Test Configuration & Test Parameters

    def get_supported_test_configuration(self, platform=None):
        mobile_test_configuration = {
            "captureHAR": False,
            "captureCPUMetrics": False,
            "captureMemoryMetrics": False,
            "captureBatteryMetrics": False,
            "captureGraphicsMetrics": False,
            "captureDeviceScreenShots": False,
            "recordDeviceScreen": False,
            "captureDeviceNetworkPackets": False
        }
        living_room_test_configuration = {
            "captureDeviceScreenShots": False,
            "recordDeviceScreen": False
        }
        if platform == "android":
            config = mobile_test_configuration
        elif platform == "ios":
            config = mobile_test_configuration
        elif platform == "living-room":
            config = living_room_test_configuration
        return mobile_test_configuration

    def get_default_test_parameters(self):
        test_parameters = {
            "maxTestDuration": 5,
            "testFramework": "android-uiautomator",
            "projectName": "",
        }
        return test_parameters

    def get_mandatory_test_parameters(self, platform=None):
        pass

    # Test Execution

    def start_test_execution(self,
                             devices=None,
                             application_url=None,
                             test_application_url=None,
                             test_configuration=None,
                             test_parameters=None
                             ):
        # pass
        action = TestExecute(client=self)
        status = action.test_now(device_list=devices, application_url=application_url,
                                 application_test_url=test_application_url,
                                 test_configuration=test_configuration, test_parameters=test_parameters)
        return status

    def abort_test_execution(self, test_id=None):
        pass

    def schedule_test_execution(self,
                                devices=None,
                                application_url=None,
                                test_application_url=None,
                                schedule_configuration=None,
                                test_configuration=None,
                                test_parameters=None,
                                ):
        """

        Args:
            devices:
            application_url:
            test_application_url:
            test_framework:
            test_configuration:
            test_parameters:
            test_start_datetime:
            test_end_datetime:
            interval:

        Returns:
            response (dict): unique schedule ID created if successful, else Error along with error message

            {
                "message" = "Success",
                "scheduleId" = ""
            }

        """
        action = TestExecute(client=self)
        status = action.schedule_test(device_list=devices, application_url=application_url,
                                      application_test_url=test_application_url,
                                      schedule_configuration=schedule_configuration,
                                      test_configuration=test_configuration, test_parameters=test_parameters)
        return status

    # def get_test_schedule_info(self, schedule_id=None):
    #     f"""
    #
    #     Args:
    #         schedule_id:
    #
    #     Returns:
    #         schedule_info (dict):
    #
    #         {
    #     "scheduleId" : "schedule_id",
    #             test_ids : [
    #                 "test_id1",
    #                 "test_id2",
    #                 "test_id3"
    #             ]
    #
    #         }
    #
    #     """
    #     pass

    def cancel_test_schedule(self, schedule_id=None):
        # pass
        action = TestExecute(client=self)
        status = action.delete_schedule(action, schedule_id=schedule_id)
        return status

    def get_test_schedule_list(self):
        # pass
        action = TestExecute(client=self)
        schedule_list = action.list_schedules(action)
        return schedule_list

    # Test Analytics

    def get_test_list(self):
        # pass
        analytics = TestAnalytics(client=self)
        test_list = analytics.get_test_list(analytics)
        return test_list

    def get_test_execution_info_full(self, test_id=None):
        analytics = TestAnalytics(client=self)
        test_info = analytics.get_test_information(analytics, test_id)
        test_cases = analytics.get_test_testcases(analytics, test_id)
        test_events = analytics.get_test_events(analytics, test_id)
        test_kpis = analytics.get_test_kpis(analytics, test_id)
        test_http_apis = analytics.get_test_apis(analytics, test_id)
        test_screenshots = analytics.get_test_screenshot_list(analytics, test_id)
        test_logs = analytics.get_test_output_file_list(analytics, test_id)

        return {
            "test_info": test_info,
            "test_cases": test_cases,
            "events": test_events,
            "kpis": test_kpis,
            "http_api": test_http_apis,
            "screenshots": test_screenshots,
            "logs": test_logs
        }

    def get_test_execution_info_by_section(self, test_id=None, section=None):
        # Section = test_info, test_configuration, test_case_summary, test_cases, test_output_artifacts, events
        # KPIs,
        # pass
        analytics = TestAnalytics(client=self)
        response = None
        if section == "test_info":
            response = analytics.get_test_information(analytics, test_id)
        elif section == "test_cases":
            response = analytics.get_test_testcases(analytics, test_id)
        elif section == "events":
            response = analytics.get_test_events(analytics, test_id)
        elif section == "kpis":
            response = analytics.get_test_kpis(analytics, test_id)
        elif section == "http_api":
            response = analytics.get_test_apis(analytics, test_id)
        elif section == "screenshots":
            response = analytics.get_test_screenshot_list(analytics, test_id)
        elif section == "logs":
            response = analytics.get_test_output_file_list(analytics, test_id)
        return response

    def download_test_screenshot(self, test_id=None, image_name=None, file_name=None):
        analytics = TestAnalytics(client=self)
        response = analytics.download_test_screenshot(test_id=test_id, file_name=image_name, output_file=file_name)
        return response

    def download_test_log(self, test_id=None, log_name=None, file_name=None):
        analytics = TestAnalytics(client=self)
        response = analytics.download_test_output_file(test_id=test_id, file_name=log_name, output_file=file_name)
        return response
