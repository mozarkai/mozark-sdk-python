import json
import requests


class TestAnalytics:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()

    def get_test_list(self, client=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        test_api_url = self.config.get("api_url") + "analytics/tests"
        # Fetch list of tests
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            test_list = test_list['body']
            return test_list
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def get_test_information(self, client=None, test_id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        test_api_url = self.config.get("api_url") + "analytics/tests/"+test_id+"/info"
        # Fetch info of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            test_list = test_list['body']
            return test_list
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def get_test_apis(self, client=None, test_id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        test_api_url = self.config.get("api_url") + "analytics/tests/"+test_id+"/app/resource/httpapi"
        # Fetch http apis of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            test_list = test_list['body']
            return test_list
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def get_test_testcases(self, client=None, test_id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        test_api_url = self.config.get("api_url") + "analytics/tests/"+test_id+"/testcases"
        # Fetch info of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            test_list = test_list['body']
            return test_list
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def get_test_events(self, client=None, test_id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        test_api_url = self.config.get("api_url") + "analytics/tests/"+test_id+"/app/events"
        # Fetch events of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            test_list = test_list['body']
            return test_list
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def get_test_kpis(self, client=None, test_id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        test_api_url = self.config.get("api_url") + "analytics/tests/"+test_id+"/app/kpi/experience"
        # Fetch kpis of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            test_list = test_list['body']
            return test_list
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def get_test_screenshot_list(self, client=None, test_id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "testId": test_id,
            "type": "screenshots"
        }
        test_api_url = self.config.get("api_url") + "testexecute/download"
        # Fetch screenshots of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            test_list = test_list['data']['list']
            return test_list
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def get_test_output_file_list(self, client=None, test_id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "testId": test_id,
            "type": "output"
        }
        test_api_url = self.config.get("api_url") + "testexecute/download"
        # Fetch screenshots of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            test_list = test_list['data']['list']
            return test_list
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def download_test_screenshot(self, client=None, test_id=None, file_name=None, output_file=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "testId": test_id,
            "type": "screenshots",
            "fileName": file_name
        }
        test_api_url = self.config.get("api_url") + "testexecute/download"
        # Fetch screenshots of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            test_list = test_list['data']['list']
            print(test_list['fileName'])
            print(test_list['url'])
            new_response = requests.get(test_list['url'])
            open(output_file, "wb").write(new_response.content)
            return "Downloaded "+file_name+" successfully"
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def download_test_output_file(self, client=None, test_id=None, file_name=None, output_file=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "testId": test_id,
            "type": "output",
            "fileName": file_name
        }
        print(str(new_params))
        test_api_url = self.config.get("api_url") + "testexecute/download"
        # Fetch screenshots of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            test_list = test_list['data']['list']
            print(str(test_list))
            print(test_list['fileName'])
            print(requests.utils.unquote(test_list['url']))
            new_response = requests.get(requests.utils.unquote(test_list['url']))
            open(output_file, "wb").write(new_response.content)
            return "Downloaded "+file_name+" successfully"
        else:
            return {"statusCode:": response.status_code, "message": response.text}



