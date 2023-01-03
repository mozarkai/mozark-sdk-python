import unittest

from mozark_sdk.client import Client


class TestSchedule(unittest.TestCase):
    def test_start_test_execution(self):

        client = Client()
        client.login()
        test_configuration = {
            "captureHAR": False,
            "captureCPUMetrics": False,
            "captureMemoryMetrics": False,
            "captureBatteryMetrics": True,
            "captureGraphicsMetrics": False,
            "captureDeviceScreenShots": True,
            "recordDeviceScreen": False,
            "captureDeviceNetworkPackets": True,
            "captureAutomationLogs": True,
            "captureSystemDebugLogs": True,
            "captureLiveLogs": True
        }
        test_configuration = {
            "captureBatteryMetrics": True,
            "captureDeviceScreenShots": True,
            "captureDeviceNetworkPackets": True,
            "captureAutomationLogs": True,
            "captureSystemDebugLogs": True,
            "captureLiveLogs": True
        }
        # test_parameters = {
        #     "testType": "app-automation",  # ?
        #     "maxTestDuration": 10,
        #     "testFramework": "android-uiautomator",  # ?
        #     "projectName": "5Gmark_android",  # ?
        #     "packageName": ""  # ?
        # }
        test_parameters = {
            "maxTestDuration": 10
        }

        response = client.start_test_execution(project_name="5Gmark_android",
                                               test_framework="android-uiautomator",
                                               application_file_name="fivegmark-debug.apk",
                                               test_application_file_name="fivegmark-debug-androidTest_1.apk",
                                               devices=["RF8R70LNY6W"],
                                               test_configuration=test_configuration,
                                               test_parameters=test_parameters
                                               )

        print(response)

    def test_schedule_info(self):
        client = Client()
        client.login()

        response = client.get_test_schedule_info(schedule_id="e36fc5ad-0cd0-41d3-ad9a-7adbd677e9c1")

        print(response)

    def test_info(self):
        client = Client()
        client.login()

        response = client.get_test_info(test_id="26b96d95-1c67-4bfe-9d99-159b0ef64c62")

        print(response)

    def test_schedule(self):
        client = Client()
        client.login()
        test_configuration = {
            "captureHAR": False,
            "captureCPUMetrics": False,
            "captureMemoryMetrics": False,
            "captureBatteryMetrics": True,
            "captureGraphicsMetrics": False,
            "captureDeviceScreenShots": True,
            "recordDeviceScreen": False,
            "captureDeviceNetworkPackets": True,
            "captureAutomationLogs": True,
            "captureSystemDebugLogs": True,
            "captureLiveLogs": True
        }
        test_configuration = {
            "captureBatteryMetrics": True,
            "captureDeviceScreenShots": True,
            "captureDeviceNetworkPackets": True,
            "captureAutomationLogs": True,
            "captureSystemDebugLogs": True,
            "captureLiveLogs": True
        }
        # test_parameters = {
        #     "testType": "app-automation",  # ?
        #     "maxTestDuration": 10,
        #     "testFramework": "android-uiautomator",  # ?
        #     "projectName": "5Gmark_android",  # ?
        #     "packageName": ""  # ?
        # }
        test_parameters = {
            "maxTestDuration": 10
        }
        response = client.schedule_test_execution(project_name="5Gmark_android",
                                                  test_framework="android-uiautomator",
                                                  application_file_name="fivegmark-debug.apk",
                                                  test_application_file_name="fivegmark-debug-androidTest_1.apk",
                                                  devices=["RF8R70LNY6W"],
                                                  test_configuration=test_configuration,
                                                  test_parameters=test_parameters,
                                                  start_date_time="2023-01-03T22:00:00.333658+05:30",
                                                  end_date_time="2023-01-03T23:00:00.333658+05:30",
                                                  interval=15
                                                  )

        print(response)

    def test_delete_schedule(self):
        client = Client()
        client.login()

        response = client.delete_test_schedule(schedule_id="450eeee0-3197-4d8d-a9e9-54939f97bd20")

        print(response)

    def test_schedule_list(self):
        client = Client()
        client.login()

        response = client.get_test_schedule_list()

        print(response)
