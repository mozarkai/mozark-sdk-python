from pathlib import Path
import requests


class TestExecute:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()

    def execute_now(self, devices=None, schedule = None):
        pass

    def schedule(self, devices=None, schedule=None):
        pass
    def make_schedule(self, list_device=None, app_name=None, test_app_name=None, time_schedule=None, type_exe=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        data = {
            "deviceId": list_device,
            "testConfiguration": {
                "captureHAR": True,
                "captureCPUMetrics": True,
                "captureMemoryMetrics": False,
                "captureBatteryMetrics": True,
                "captureGraphicsMetrics": False,
                "captureDeviceScreenShots": False,
                "recordDeviceScreen": False,
                "captureDeviceNetworkPackets": False
            },
            "scheduleConfiguration": time_schedule,
            "testAction": {
                "pre": {},
                "post": {}
            },
            "testParameters": {
                "maxTestDuration": 600,
                "testFramework": "android-uiautomator",
                "testRuntime": "robot",
                "projectName": "test"
            },
            "applicationUrl": app_name,
            "testApplicationUrl": test_app_name,
            "executionType": type_exe
        }

        select_device_url = "https://development-api.mozark.ai/testexecute/schedules"
        response = requests.post(select_device_url, json=data, headers=new_headers)
        return response
