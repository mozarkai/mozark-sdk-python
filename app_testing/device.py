import json
from pathlib import Path

import requests


class Device:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()

    # def get_device(self, client=None):
    #     get_device_url = "https://development-api.mozark.ai/testexecute/devices?deviceParameters.controllerId=Staging NUC"
    #     new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
    #                    'Content-Type': 'application/json'}
    #     response = requests.get(get_device_url, headers=new_headers)
    #     if response.status_code == 200:
    #         Name = response.json()['data']['list'][0]['brand']
    #         DeviceId = response.json()['data']['list'][0]['serial']
    #         City = response.json()['data']['list'][0]['deviceParameters']['city']
    #         DeviceStatus = response.json()['data']['list'][0]['deviceParameters']['deviceStatus']
    #         # deviceStaus =response.json()['data']['list'][0]['deviceStatus']
    #
    #         if DeviceStatus == 'unavailable':
    #             print(f'{Name} device with {City} location and serial ID {DeviceId} is {DeviceStatus}')
    #         else:
    #             pass
    #
    #         return DeviceId

    def add_device(self, client=None, project_name=None):
        pass

    def get_devices(self, client=None, platform=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "platform": platform
        }
        device_api_url = self.config.get("api_url") + "testexecute/devices"
        # Fetch list of devices
        response = requests.get(device_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp['data']['list']
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}
        # return response.status_code, response.text

    def get_lr_devices(self, client=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        device_api_url = self.config.get("api_url") + "tv/devices"
        # Fetch list of devices
        response = requests.get(device_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp['data']['list']
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}
        # return response.status_code, response.text



