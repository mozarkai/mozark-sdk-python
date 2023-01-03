import json
import requests


class TestAnalytics:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()

    def get_test_execution_info_full(self, test_id=None):

        test_info = self.get_test_information(test_id=test_id)
        kpi = self.get_test_kpis(test_id=test_id)
        events = self.get_test_events(test_id=test_id)
        testcases = self.get_test_testcases(test_id=test_id)

        test_information = {
            "test_info": test_info,
            "testCases": testcases,
            "userExperienceKpis": kpi,
            "events": events,
        }
        # print("\n test_info: ", test_information)
        # print("\n testinfo: ", test_info)
        # print("\n event: ", test_full_info["events"]["events"])
        return test_information

    def get_test_list(self, from_date_time=None, to_date_time=None):
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

    def get_test_information(self, test_id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        test_api_url = self.config.get("api_url") + "analytics/tests/" + test_id + "/info"
        # Fetch info of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            test_info = test_list['body']
            print("sffsf:  ", test_info)
            test_information = {
                "testUUID": test_info['uuid']['testId'],
                "testStartDateTime": test_info['testStartTime'],
                "testEndDateTime": test_info['testEndTime'],
                "projectName": test_info['projectName'],
                "applicationFileName": test_info['appVersion'],
                "testApplicationFileName": test_info['scriptName'],
                "deviceSerial": test_info['deviceSerial'],
                "deviceMake": "",
                "deviceModel": test_info['deviceName'],
                "deviceCity": test_info['deviceLocation'],
                "deviceCountry": "",
                "deviceNetwork": test_info['deviceNetwork'],
                "devicePlatform": test_info['deviceOSVersion'],
                "deviceOSVersion": test_info['deviceOSVersion'],
                "deviceNetworkOperator": test_info['operator'],
                "testStatus": test_info['testStatus'],
                "testStatusDescription": test_info['testCaseSummary'],
                "testCasesTotal": test_info['testCaseSummary']['total'],
                "testCasesPassed": test_info['testCaseSummary']['passed'],
                "testCasesFailed": test_info['testCaseSummary']['failed'],

            }

            return test_information
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def get_test_testcases(self, test_id=None):
        testcaselist = []
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        test_api_url = self.config.get("api_url") + "analytics/tests/" + test_id + "/testcases"
        # Fetch info of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            testcases = test_list['body']
            for i in range(len(testcases['testCases'])):
                testCaseName = testcases['testCases'][i]['testCaseName']
                testCaseResult = testcases['testCases'][i]['status']
                testCaseStartDateTime = ""
                testCaseEndDateTime = ""

                testcases_info = {
                    "testCaseName": testCaseName,
                    "testCaseResult": testCaseResult,
                    "testCaseStartDateTime": testCaseStartDateTime,
                    "testCaseEndDateTime": testCaseEndDateTime,
                }
                testcaselist.append(testcases_info)

            return testcaselist
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def get_test_events(self, test_id=None):
        eventexp = []
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        test_api_url = self.config.get("api_url") + "analytics/tests/" + test_id + "/app/events"
        # Fetch events of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            events = test_list['body']
            for i in range(len(events["events"])):
                eventname = events["events"][i]['eventName']
                eventdatetime = events["events"][i]['time']
                testcasename = events["events"][i]['testCase']

                event_info = {
                    "eventName": eventname,
                    "eventDateTime": eventdatetime,
                    "testCaseName": testcasename
                }
                eventexp.append(event_info)
            return eventexp
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def get_test_kpis(self, test_id=None):
        userexperiancekpi = []

        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        test_api_url = self.config.get("api_url") + "analytics/tests/" + test_id + "/app/kpi/experience"
        # Fetch kpis of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            kpi = test_list['body']
            for i in range(len(kpi["experience"])):
                kpiname = kpi["experience"][i]['kpiName']
                kpivalue = kpi["experience"][i]['value']
                testcasename = ""

                kpi_info = {"kpiName": kpiname,
                            "kpiValue": kpivalue,
                            "testCaseName": testcasename
                            }
                userexperiancekpi.append(kpi_info)
            return userexperiancekpi
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def get_test_apis(self, test_id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
        }
        test_api_url = self.config.get("api_url") + "analytics/tests/" + test_id + "/app/resource/httpapi"
        # Fetch http apis of test
        response = requests.get(test_api_url, params=new_params, headers=new_headers)
        if response.status_code == 200:
            test_list = json.loads(response.text)
            test_list = test_list['body']
            return test_list
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def get_test_screenshot_list(self, test_id=None):
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

    def get_test_output_file_list(self, test_id=None):
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

    def download_test_screenshot(self, test_id=None, file_name=None, output_file=None):
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
            return "Downloaded " + file_name + " successfully"
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def download_test_output_file(self, test_id=None, file_name=None, output_file=None):
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
            return "Downloaded " + file_name + " successfully"
        else:
            return {"statusCode:": response.status_code, "message": response.text}
