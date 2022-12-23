from pathlib import Path
import requests
from datetime import tzinfo, timedelta, datetime
from app_testing.device import Device
from app_testing.client import Client


class TZ(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=5, minutes=30)

class Schedule:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()
        self.device = None
        self.NSTime = None
        self.ExcType = None

    def selectDeviceForSchedule(self):
        device = Device()
        list_device = device.get_device()
        self.device = list_device
        return self.device

    def scheduleTime(self):
        tz = TZ()
        starttime = datetime(2022, 12, 25, 1, 12, 40, tzinfo=tz).isoformat()
        endtime = datetime(2022, 12, 25, 10, 10, 40, tzinfo=tz).isoformat()
        interval = 10
        self.NSTime = {
            "startTime": starttime,
            "endTime": endtime,
            "interval": interval
        }
        self.ExcType = "SCHEDULE"
        return self.NSTime, self.ExcType
    #
    # def nowTime(self):
    #     tz = TZ()
    #     starttime = datetime(2022, 12, 25, 1, 12, 40, tzinfo=tz).isoformat()
    #     self.NSTime = {
    #         "startTime": starttime
    #     }
    #     self.ExcType = "NOW"
    #     return self.NSTime, self.ExcType

    def makeSchedule(self):
        if self.ExcType == "NOW":
            self.NSTime
        else:
            self.NSTime

        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        data = {
            "deviceId": self.device,
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
            "scheduleConfiguration": self.NSTime,
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
            "applicationUrl": "https://development-ios-application.s3.ap-south-1.amazonaws.com/bitbar-ios-sample.ipa",
            "testApplicationUrl": "https://development-ios-application.s3.ap-south-1.amazonaws.com/bitbar-ios-sample.ipa",
            "executionType": self.ExcType
        }

        select_device_url = "https://development-api.mozark.ai/testexecute/schedules"
        response = requests.post(select_device_url, json=data, headers=new_headers)
        return response

