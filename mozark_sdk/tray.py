import json
import requests


class Tray:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()

    def create_tray(self, client=None, name=None, platform=None, device_list=None):
        # POST
        # https://hotstar-api.mozark.ai/tray/create
        # {trayName: "hcvdh", devices: ["G4N1EL04114400M3"]}
        # pass
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        data = {
            "trayName": name,
            "devices": device_list,
            "platform": platform
        }
        project_api_url = self.config.get("api_url") + "tray/create"
        response = requests.post(project_api_url, json=data, headers=new_headers)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp['body']['message']
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}
        # return response.status_code, response.text

    def list_tray(self, client=None):
        # GET
        # https://hotstar-api.mozark.ai/tray/list
        # pass
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
        # return response.text

    def get_tray_info(self, client=None, tray_id=None):
        # GET
        # https://hotstar-api.mozark.ai/tray/devices?trayid=7eed6665-f470-4b91-81aa-bc399f0f325a
        # pass
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "trayid": tray_id
        }
        tray_api_url = self.config.get("api_url") + "tray/devices"
        # Get tray details
        response = requests.get(tray_api_url, params=new_params, headers=new_headers)
        print(response.text)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp['body']
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}
        # return response.text

    def update_tray(self, client=None, tray_id=None, device_list=None):
        # PUT
        # https://hotstar-api.mozark.ai/tray/update?trayid=7eed6665-f470-4b91-81aa-bc399f0f325a
        # {devices: ["RF8R70LNY6W", "RZ8R31QDBZF"]}
        pass
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "trayid": tray_id
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
        # return response.text

    def delete_tray(self, client=None, tray_id=None):
        # DELETE
        # https://hotstar-api.mozark.ai/tray/delete?trayid=bd7670e1-a54d-4db6-a007-b0af8cead544
        # pass
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "trayid": tray_id
        }
        tray_api_url = self.config.get("api_url") + "tray/delete"
        # Fetch list of files uploaded
        response = requests.delete(tray_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp['body']['message']
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}
        # return response.text
