import requests


class Project:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()

    def create_project(self, project_name=None, project_description=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        data = {
            "name": project_name,
            "description": project_description
        }
        project_api_url = self.config.get("api_url") + "testexecute/projects"
        response = requests.post(project_api_url, json=data, headers=new_headers)
        return response.status_code, response.text
        # pass

    def get_projects(self, project_name=None, project_description=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "name": project_name,
            "description": project_description
        }
        project_api_url = self.config.get("api_url") + "testexecute/projects"
        # Fetch list of projects
        response = requests.get(project_api_url,  params=new_params, headers=new_headers)
        return response.status_code, response.text
        # pass

