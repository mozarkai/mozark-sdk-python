import os
import logging
import datetime
from mozark_sdk.client import Client
from unittest import TestCase
import pytz


class TestStartTestExecution(TestCase):

    def test_test_now(self):
        client = Client()
        client.login()
        project_name = "5Gmark_android"
        test_app_url = "https://development-app-testing.s3.ap-south-1.amazonaws.com/android-application/netflix-debug.apk"
        app_url = "https://development-app-testing.s3.ap-south-1.amazonaws.com/android-application/hotstar.apk"
        device_list = ["RF8R70LNY6W"]
        test_configuration = client.get_supported_test_configuration(platform='android')
        test_parameters = client.get_default_test_parameters()
        test_parameters['projectName'] = project_name
        print(test_configuration)
        print(test_parameters)
        # status = client.start_test_execution(devices=device_list, application_url=app_url,
        #                                      test_application_url=test_app_url, test_configuration=test_configuration,
        #                                      test_parameters=test_parameters)
        # print(status)
        time_format = "%Y-%m-%dT%H:%M:%S"
        start_time = datetime.datetime(2023, 1, 5, 2, 12, 40)
        end_time = datetime.datetime(2023, 1, 6, 1, 11, 40)
        start_time = start_time.strftime(time_format)
        end_time = end_time.strftime(time_format)
        interval = 10
        schedule_conf = {
            "startTime": start_time+"+05:30",
            "endTime": end_time+"+05:30",
            "interval": interval
        }
        print(schedule_conf)
        status = client.schedule_test_execution(devices=device_list, application_url=app_url,
                                                test_application_url=test_app_url,
                                                test_configuration=test_configuration,
                                                test_parameters=test_parameters,
                                                schedule_configuration=schedule_conf)
        print(status)
        # schedule_list = client.get_test_schedule_list()
        # print(schedule_list)
        # schedule_id = "a5945197-7a00-48e1-9fee-fd07be69f023"
        # client.get_test_schedule_info(schedule_id=schedule_id)
        # message = client.cancel_test_schedule(schedule_id="a5945197-7a00-48e1-9fee-fd07be69f023")
        # print(message)
