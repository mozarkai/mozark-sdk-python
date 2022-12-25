import os
import logging
from app_testing.client import Client
from app_testing.project import Project
from app_testing.file import File
from app_testing.schedule import Schedule
from app_testing.device import Device
from unittest import TestCase
from datetime import tzinfo, timedelta, datetime
from zoneinfo import ZoneInfo


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

        # Device List
        device = Device(client=client)
        list_device = device.get_device()

        # Schedule Time
        # type_exe = "NOW"
        type_exe = "SCHEDULE"
        now_time = datetime.now(tz=ZoneInfo('Asia/Kolkata')).isoformat()
        start_time = datetime(2022, 12, 24, 2, 12, 40, tzinfo=ZoneInfo('Asia/Kolkata'))
        end_time = datetime(2022, 12, 25, 1, 11, 40, tzinfo=ZoneInfo('Asia/Kolkata'))
        interval = 10
        time_diff = ((end_time - start_time).total_seconds()) / 60
        schedule = Schedule(client=client)
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
