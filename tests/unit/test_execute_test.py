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
            "maxTestDuration": 10,
        }
        # devices = "10BD2509DR004G0"
        devices = ["RZCW111X0HN"]
        response = client.start_test_execution(project_name="Phonepe_RC",
                                               test_framework="android-uiautomator",
                                               application_file_name="amar-media-fragment-local-sdk.apk",
                                               test_application_file_name="PP_J09_AppLaunch_RC.apk",
                                               devices=devices,
                                               test_configuration=test_configuration,
                                               test_parameters=test_parameters
                                               )

        print("52..:", response)

    def test_schedule_info(self):
        client = Client()
        client.login()

        response = client.get_test_schedule_info(schedule_id="3fb33497-398a-471b-9041-6eea98721d1f")

        print(response)

    def test_info(self):
        client = Client()
        client.login()

        response = client.get_test_info(test_id="a5c7e7c5-1bb4-4f9c-b850-662b9ee5ef6d")

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
        devices=["RZCW111X0HN"]
        response = client.schedule_test_execution(project_name="Phonepe_RC",
                                                  test_framework="android-uiautomator",
                                                  application_file_name="amar-media-fragment-local-sdk.apk",
                                                  test_application_file_name="PP_J09_AppLaunch_RC.apk",
                                                  devices=devices,
                                                  test_configuration=test_configuration,
                                                  test_parameters=test_parameters,
                                                  start_date_time="2024-07-26T11:59:00+05:30",
                                                  end_date_time="2024-07-26T12:17:00+05:30",
                                                  interval=10
                                                  )

        print(response)

    def test_delete_schedule(self):
        client = Client()
        client.login()

        response = client.delete_test_schedule(schedule_id="fcbcc527-1b8c-4bf8-88d6-c05188a1bc2d")

        print(response)

    def test_schedule_list(self):
        client = Client()
        client.login()

        response = client.get_test_schedule_list()

        print(response)

    def test_update_schedule(self):
        client = Client()
        client.login()
        schedule_id = "f0abd6ea-83db-46ca-99b3-d5bcb6931d6c"
        update_data = {
            "testParameters": {
                "packageName": "1111"
            }
        }
        response = client.update_schedule(data=update_data, schedule_id=schedule_id)
        print(response)

    def test_update_test(self):
        client = Client()
        client.login()
        test_id = "a1c2e491-78be-47a1-aed8-7ca242b6a579"
        update_data = {
            "testParameters": {
                "packageName": "0000"
            }
        }
        response = client.update_test(data=update_data, test_id=test_id)
        print(response)

    def test_start_test_execution_robot(self):
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
            "maxTestDuration": 10,
            "visualMonitoringEnabled": True,
            "testExecution": "roboticArm",
            "appVersion": "12.0",
            "accountType": "retail"
        }

        response = client.start_test_execution(project_name="Fund_Transfer",
                                               test_framework="appium-python",
                                               application_file_name="",
                                               test_application_file_name="IOS_DeletePayee_J5.zip",
                                               visual_test_application = "KBank_TH_A53_J2.zip",
                                               devices=["00008110-000674113E9B801R"],
                                               test_configuration=test_configuration,
                                               test_parameters=test_parameters
                                               )

        print(response)
