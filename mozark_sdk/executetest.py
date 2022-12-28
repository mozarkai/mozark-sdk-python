import json
from pathlib import Path
import requests


class TestExecute:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()

    # def execute_now(self, devices=None, schedule=None):
    #     pass
    #
    # def schedule(self, devices=None, schedule=None):
    #     pass

    # def make_schedule(self, list_device=None, app_name=None, test_app_name=None, time_schedule=None, type_exe=None):
    #     new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
    #                    'Content-Type': 'application/json'}
    #     data = {
    #         "deviceId": list_device,
    #         "testConfiguration": {
    #             "captureHAR": True,
    #             "captureCPUMetrics": True,
    #             "captureMemoryMetrics": False,
    #             "captureBatteryMetrics": True,
    #             "captureGraphicsMetrics": False,
    #             "captureDeviceScreenShots": False,
    #             "recordDeviceScreen": False,
    #             "captureDeviceNetworkPackets": False
    #         },
    #         "scheduleConfiguration": time_schedule,
    #         "testAction": {
    #             "pre": {},
    #             "post": {}
    #         },
    #         "testParameters": {
    #             "maxTestDuration": 600,
    #             "testFramework": "android-uiautomator",
    #             "testRuntime": "robot",
    #             "projectName": "test"
    #         },
    #         "applicationUrl": app_name,
    #         "testApplicationUrl": test_app_name,
    #         "executionType": type_exe
    #     }
    #
    #     select_device_url = "https://development-api.mozark.ai/testexecute/schedules"
    #     response = requests.post(select_device_url, json=data, headers=new_headers)
    #     return response

    def execute_test(self, client=None, device_list=None, test_configuration={}, schedule_configuration={},
                     test_parameters={},
                     execution_type=None, application_url=None, application_test_url=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        data = {
            "deviceId": device_list,
            "testConfiguration": test_configuration,
            "scheduleConfiguration": schedule_configuration,
            "testAction": {
                "pre": {},
                "post": {}
            },
            "testParameters": test_parameters,
            "applicationUrl": application_url,
            "testApplicationUrl": application_test_url,
            "executionType": execution_type
        }
        test_api_url = self.config.get("api_url") + "testexecute/schedules"
        response = requests.post(test_api_url, json=data, headers=new_headers)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp['data']
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}
        # return response.status_code, response.text

    def list_schedules(self, client=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        test_api_url = self.config.get("api_url") + "testexecute/schedules"
        # Fetch list of schedules
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp['data']['list']
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}
        # return response.status_code, response.text

    def delete_schedule(self, client=None, schedule_id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "scheduleId": schedule_id
        }
        test_api_url = self.config.get("api_url") + "testexecute/schedules"
        # Delete schedule
        response = requests.delete(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp["message"]
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}
        # return response.text

    def abort_test(self, client=None, test_id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        data = {
            "testId": test_id
        }
        test_api_url = self.config.get("api_url") + "testexecute/tests"
        # abort test
        response = requests.put(test_api_url, json=data, headers=new_headers)
        return response.text

    def schedule_test(self, client=None, device_list=None, schedule_configuration={}, test_configuration={},
                      test_parameters={}, application_url=None, application_test_url=None):
        # schedule_configuration = {
        #     "startTime": start_time,
        #     "endTime": end_time,
        #     "interval": interval
        # }
        # test_parameters = {
        #     "maxTestDuration": max_duration,
        #     "testFramework": test_framework,
        #     "projectName": project_name
        # }
        execution_type = "SCHEDULE"
        status_message = self.execute_test(device_list=device_list, test_configuration=test_configuration,
                                           schedule_configuration=schedule_configuration,
                                           test_parameters=test_parameters, execution_type=execution_type,
                                           application_url=application_url,
                                           application_test_url=application_test_url)
        return status_message

    def test_now(self, client=None, device_list=None, test_configuration={}, test_parameters={},
                 application_url=None, application_test_url=None):
        schedule_configuration = {}
        # test_parameters = {
        #     "maxTestDuration": max_duration,
        #     "testFramework": test_framework,
        #     "projectName": project_name
        # }
        execution_type = "NOW"
        status_code, status_message = self.execute_test(device_list=device_list, test_configuration=test_configuration,
                                                        schedule_configuration=schedule_configuration,
                                                        test_parameters=test_parameters, execution_type=execution_type,
                                                        application_url=application_url,
                                                        application_test_url=application_test_url)
        return status_message
