import json
import requests


class TestAnalytics:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()

    def create_tray(self, name=None, device_list=None):
        #POST
        # https://hotstar-api.mozark.ai/tray/create
        # {trayName: "hcvdh", devices: ["G4N1EL04114400M3"]}
        pass

    def list_tray(self):
        #GET
        # https://hotstar-api.mozark.ai/tray/list
        pass

    def get_tray_info(self, tray_id=None):
        #GET
        # https://hotstar-api.mozark.ai/tray/devices?trayid=7eed6665-f470-4b91-81aa-bc399f0f325a
        pass

    def update_tray(self, tray_id=None, device_list=None):
        #PUT
        # https://hotstar-api.mozark.ai/tray/update?trayid=7eed6665-f470-4b91-81aa-bc399f0f325a
        # {devices: ["RF8R70LNY6W", "RZ8R31QDBZF"]}
        pass

    def delete_tray(self, tray_id):
        #DELETE
        #https://hotstar-api.mozark.ai/tray/delete?trayid=bd7670e1-a54d-4db6-a007-b0af8cead544
        pass