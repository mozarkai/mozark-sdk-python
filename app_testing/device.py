from pathlib import Path

import requests


class Device:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()

    def get_device(self):
        get_device_url = "https://development-api.mozark.ai/testexecute/devices?deviceParameters.controllerId=Staging NUC"
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        response = requests.get(get_device_url, headers=new_headers)
        if response.status_code == 200:
            Name = response.json()['data']['list'][0]['brand']
            DeviceId = response.json()['data']['list'][0]['serial']
            City = response.json()['data']['list'][0]['deviceParameters']['city']
            DeviceStatus = response.json()['data']['list'][0]['deviceParameters']['deviceStatus']
            # deviceStaus =response.json()['data']['list'][0]['deviceStatus']

            if DeviceStatus == 'unavailable':
                print(f'{Name} device with {City} location and serial ID {DeviceId} is {DeviceStatus}')
            else:
                pass

            return DeviceId

    def add_device(self, project_name=None):
        pass


