import json
import requests
from mozark_sdk.device import Device


class Tray:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()
        self.client = client

    def create_tray(self, platform=None, tray_name=None, device_list=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        data = {
            "trayName": tray_name,
            "devices": device_list,
            "platform": platform
        }
        tray_api_url = self.config.get("api_url") + "tray/create"
        response = requests.post(tray_api_url, json=data, headers=new_headers)
        if response.status_code == 200 and response.json()["body"]["message"] == "Tray Created Successfully":
            return "Success"
        else:
            return "Failure: tray with name " + tray_name + " already exists."

    def get_tray_info(self, tray_name=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        tray_api_url = self.config.get("api_url") + "tray/list"
        # Get list of tray created
        response = requests.get(tray_api_url, params=new_params, headers=new_headers)
        print(json.loads(response.text)['body']['trays'][0]["trayName"],
              len(json.loads(response.text)['body']['trays']))
        devices = {}
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            # print("tray name: ", my_resp['body']['trays'][0]["trayName"])
            for j in range(len(json.loads(response.text)['body']['trays'])):

                if my_resp['body']['trays'][j]["trayName"] == tray_name:
                    print("tray name: ", tray_name)
                    for i in range(len(my_resp['body']['trays'][j]["devices"])):
                        device_id = my_resp['body']['trays'][j]["devices"][i]
                        platform = my_resp['body']['trays'][j]["platform"]

                        device_obj = Device(client=self.client)
                        device = device_obj.get_devices(platform=platform, device_serial=device_id)
                        devices[my_resp['body']['trays'][0]["devices"][i]] = device
                    my_resp = {"tray_info": my_resp['body']['trays'][j], 'device_info': devices}
                    return my_resp
            else:
                return "Failure: tray with name " + tray_name + " not exists."
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def update_tray(self, tray_name=None, device_list=None):
        # PUT
        # https://hotstar-api.mozark.ai/tray/update?trayid=7eed6665-f470-4b91-81aa-bc399f0f325a
        # {devices: ["RF8R70LNY6W", "RZ8R31QDBZF"]}
        pass
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "trayid": tray_name
        }
        data = {
            "devices": device_list
        }
        tray_api_url = self.config.get("api_url") + "tray/update"
        response = requests.put(tray_api_url, json=data, headers=new_headers, params=new_params)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp['body']['message']
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def delete_tray(self, tray_name=None):
        # DELETE
        # https://hotstar-api.mozark.ai/tray/delete?trayid=bd7670e1-a54d-4db6-a007-b0af8cead544
        # pass
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}

        tray_list_api_url = self.config.get("api_url") + "tray/list"

        response = requests.get(tray_list_api_url, headers=new_headers)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            # print(len(my_resp['body']['trays']))
            for j in range(len(my_resp['body']['trays'])):
                if my_resp['body']['trays'][j]["trayName"] == tray_name:

                    tray_id = my_resp['body']['trays'][j]["trayID"]

                    new_params = {
                        "trayid": tray_id
                    }
                    tray_delete_api_url = self.config.get("api_url") + "tray/delete"
                    # Fetch list of files uploaded
                    response = requests.delete(tray_delete_api_url, params=new_params, headers=new_headers)
                    if response.status_code == 200:
                        my_resp = json.loads(response.text)
                        my_resp = my_resp['body']['message']
                        return my_resp
                    else:
                        return {"statusCode:": response.status_code, "message": response.text}
            else:
                return "Failure: tray with name " + tray_name + " not exists."
        # return response.text

    def get_tray_list(self):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        tray_api_url = self.config.get("api_url") + "tray/list"
        # Get list of tray created
        response = requests.get(tray_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp['body']['trays']
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}

# def list_tray(self):
#     new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
#                    'Content-Type': 'application/json'}
#     new_params = {
#     }
#     tray_api_url = self.config.get("api_url") + "tray/list"
#     # Get list of tray created
#     response = requests.get(tray_api_url, params=new_params, headers=new_headers)
#     if response.status_code == 200:
#         my_resp = json.loads(response.text)
#         my_resp = my_resp['body']['trays']
#         return my_resp
#     else:
#         return {"statusCode:": response.status_code, "message": response.text}
