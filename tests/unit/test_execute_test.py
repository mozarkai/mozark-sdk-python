import unittest

from mozark_sdk.client import Client


class TestSchedule(unittest.TestCase):
    def test_start_test_execution(self):
        project_name = "sample project"
        app = "./abc-sample.apk"
        test_app = "./test-abc-sample.apk"

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
        test_parameters = {
            "testType": "app-automation",  # ?
            "maxTestDuration": 10,
            "testFramework": "android-uiautomator",  # ?
            "projectName": "5Gmark_android",  # ?
            "packageName": ""  # ?
        }
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
