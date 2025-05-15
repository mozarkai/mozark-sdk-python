import json
from pathlib import Path

import requests


class JobRunner:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()

    def add_device(self, device_parameter=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}

        if device_parameter["platform"] == "living-room":
            device_parameter["platform"] = "TV"
        # print(device_parameter)
        device_api_url = self.config.get("api_url") + "v1/testexecute/devices"
        response = requests.post(device_api_url, json=device_parameter, headers=new_headers)
        print(response.json())
        try:
            if response.json()["status"] == 200 and response.json()["message"] == "Success":
                return "Success"
            else:
                return "Failure: Device with name " + device_parameter["serial"] + " already exists."
        except KeyError:
            return "Failure: Device with name " + device_parameter["serial"] + " already exists."

    def get_testsuite(self, test_filename=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        if test_filename:
            testsuite_api_url = f"{self.config.get('api_url')}job-runner/testsuite/{test_filename}"
        else:
            testsuite_api_url = self.config.get("api_url") + "job-runner/testsuite"

        response = requests.get(testsuite_api_url, headers=new_headers)
        testsuite_list = response.json()
        return testsuite_list

    def get_job(self, id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        # Check if an ID is provided, and append it to the URL
        if id:
            job_api_url = f"{self.config.get('api_url')}job-runner/job/{id}"
        else:
            job_api_url = self.config.get("api_url") + "job-runner/job"
            # Fetch list of testsuite
        response = requests.get(job_api_url,  headers=new_headers)
        job_list = response.json()
        return job_list
