import json

import requests


class Project:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()

    def create_project(self, client=None, project_name=None, project_description=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        data = {
            "name": project_name,
            "description": project_description
        }
        project_api_url = self.config.get("api_url") + "testexecute/projects"
        response = requests.post(project_api_url, json=data, headers=new_headers)
        return response.text
        # pass

    def get_projects(self, client=None, project_name=None, project_description=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "name": project_name,
            "description": project_description
        }
        project_api_url = self.config.get("api_url") + "testexecute/projects"
        # Fetch list of projects
        response = requests.get(project_api_url,  params=new_params, headers=new_headers)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp['data']['list']
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}
        # return response.text
        # pass

