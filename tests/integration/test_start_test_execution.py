import os
import logging
from app_testing.client import Client
from app_testing.project import Project
from app_testing.file import File
from app_testing.executetest import TestExecute
from app_testing.device import Device
from unittest import TestCase
from datetime import tzinfo, timedelta, datetime
from zoneinfo import ZoneInfo


class TestStartTestExecution(TestCase):
    def test_schedule_test(self):
        client = Client()

        client.login()

        msg = client.create_project(project_name="Sample Project", project_description="Sample Project Description")

        if msg != "Success":
            print("Raise Error")

        msg = client.upload_android_application(project_name="Sample Project", file_path="./5gmark.apk")

        if msg != "Success":
            print("Raise Error")

        msg = client.upload_android_native_test_application(project_name="Sample Project", file_path="./5gmark.apk")

        if msg != "Success":
            print("Raise Error")

        devices = ["abc", "xyz"]

        test_configuration = {
            "captureDeviceScreenShots": True,
            "recordDeviceScreen": True,
            "captureAutomationLogs": True,
            "captureSystemDebugLogs": True
        }
        test_parameters = {
            "maxTestDuration": 5,
            # "testFramework": "android-uiautomator",
            # "projectName": "5Gmark_Android", client.get_project_info()
            # "testRunnerName": "androidx.test.runner.AndroidJUnitRunner", - client.get_file_info()
            # "testCodePackageName": "com.example.fivegmark.test", - client.get_file_info()
            # "packageName": "com.example.fivegmark" - client.get_file_info()
        }
        start_datetime = datetime()
        end_datetime = datetime()
        msg = client.schedule_test_execution(devices=devices,
                                             application_name="5gmark.apk",
                                             test_application_name="5gmark.apk",
                                             test_framework="android-uiautomator",
                                             test_configuration=test_configuration,
                                             test_parameters=test_parameters,
                                             start_datetime=start_datetime,
                                             end_datetime=end_datetime,
                                             interval=30
                                             )

        if msg["message"] != "Success":
            print("Raise Error")

        schedule_id = msg["scheduleId"]

        test_ids = client.get_test_schedule_info(schedule_id)

        for test_id in test_ids:
            msg = client.get_test_execution_info_full(test_id=test_id)



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

        # Device List
        device = Device(client=client)
        list_device = device.get_device()

        # Schedule Time
        # type_exe = "NOW"
        type_exe = "SCHEDULE"
        now_time = datetime.now(tz=ZoneInfo('Asia/Kolkata')).isoformat()
        start_time = datetime(2022, 12, 29, 2, 12, 40, tzinfo=ZoneInfo('Asia/Kolkata'))
        end_time = datetime(2022, 12, 30, 1, 11, 40, tzinfo=ZoneInfo('Asia/Kolkata'))
        interval = 10
        time_diff = ((end_time - start_time).total_seconds()) / 60
        schedule = TestExecute(client=client)
        if type_exe == "NOW":
            time_schedule = {"startTime": now_time}
            res = schedule.make_schedule(list_device=list_device, app_name=android_application,
                                         test_app_name=android_application, time_schedule=time_schedule,
                                         type_exe=type_exe)
            print(res.json())
            print(list_device, type_exe, time_schedule)
        else:
            try:
                if time_diff > 0 and time_diff > interval:
                    time_schedule = {"startTime": start_time.isoformat(), "endTime": end_time.isoformat(),
                                     "interval": interval}
                    res = schedule.make_schedule(list_device=list_device, app_name=android_application,
                                                 test_app_name=android_application, time_schedule=time_schedule,
                                                 type_exe=type_exe)
                    print(res.json())
                    print(list_device, type_exe, time_schedule)
                else:
                    print("Start Time Should be less than End Time and check interval also")
            except:
                print("Start Time Should be less than End Time")
