import json
from pathlib import Path

import requests


class File:
    config = None
    calculate_md5 = True

    def __init__(self, client=None, calculate_md5=True):
        self.config = client.get_config()
        self.calculate_md5 = calculate_md5

    def get_file_md5(self, client=None, filepath=None):
        import hashlib
        md5_hash = ''
        with open(filepath, "rb") as f:
            file_bytes = f.read()  # read file as bytes
            readable_hash = hashlib.md5(file_bytes).hexdigest()
            md5_hash = readable_hash
        return md5_hash

    def __upload(self, client=None, data=None, files=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}

        file_api_url = self.config.get("api_url") + "testexecute/files"
        # Leg 1 - get the s3 file upload URL
        response = requests.post(file_api_url, json=data, headers=new_headers)

        if response.status_code == 200:
            print("Leg 1 - response: " + response.text)
            if response.json()['status'] == 409:
                print("Leg 1 - File already exists")
                return response.status_code, "File already exists"
        else:
            print("Error: Leg 1" + response.text)
            return response.status_code, response.text

        s3_file_upload_url = response.json()['data']['uploadUrl']

        # Leg 2 - upload the file using s3 upload URL
        response = requests.put(s3_file_upload_url, files=files)

        if response.status_code == 200:
            print("File uploaded successfully: " + s3_file_upload_url)
            return "File uploaded successfully"
        else:
            print("Error uploading file")
            return {"statusCode:": response.status_code, "message": response.text}

    def upload_native_package(self, client=None, project_name=None, file_path=None, file_category=None):
        path_object = Path(file_path)
        filename = path_object.name
        data = {
            "fileName": filename,
            "fileCategory": file_category,
            "userName": self.config.get("username"),
            "projectName": project_name
        }

        if self.calculate_md5:
            md5 = self.get_file_md5(filepath=file_path)
            data["md5sum"] = md5
        else:
            print("no md5 sum")

        file_object = open(file_path, 'rb')
        files = {'file': file_object}
        status_message = self.__upload(data=data, files=files)
        file_object.close()
        return status_message

    def list_files(self, client=None, file_category=None, project_name=None, file_name=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "fileCategory": file_category,
            "fileStatus": "processed",
            "projectName": project_name,
            "fileName": file_name
        }
        file_api_url = self.config.get("api_url") + "testexecute/files"
        # Fetch list of files uploaded
        response = requests.get(file_api_url,  params=new_params, headers=new_headers)
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp['data']['list']
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}
        # return response.status_code, response.text

    def delete_file(self, client=None, file_id=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}
        new_params = {
            "fileId": file_id
        }
        file_api_url = self.config.get("api_url") + "testexecute/files"
        # Fetch list of files uploaded
        response = requests.delete(file_api_url, params=new_params, headers=new_headers)
        # return response.text
        if response.status_code == 200:
            my_resp = json.loads(response.text)
            my_resp = my_resp['message']
            return my_resp
        else:
            return {"statusCode:": response.status_code, "message": response.text}

    def upload_android_application(self, client=None, project_name=None, file_path=None):
        file_category = "android-application"
        status_message = self.upload_native_package(self, project_name, file_path, file_category)
        return status_message

    def upload_android_native_test_application(self, client=None, project_name=None, file_path=None):
        file_category = "android-test-application"
        status_message = self.upload_native_package(self, project_name, file_path, file_category)
        return status_message

    def upload_ios_application(self, client=None, project_name=None, file_path=None):
        file_category = "ios-application"
        # self.__upload(project_name, file_path, file_category)
        # pass
        status_message = self.upload_native_package(project_name, file_path, file_category)
        return status_message

    def upload_ios_native_test_application(self, client=None, project_name=None, file_path=None):
        file_category = "ios-test-application"
        status_message = self.upload_native_package(project_name, file_path, file_category)
        return status_message

    def list_android_application(self, client=None, project_name=None, file_name=None):
        file_category = "android-application"
        status_message = self.list_files(project_name, file_name)
        return status_message

    def list_android_native_test_application(self, client=None, project_name=None, file_name=None):
        file_category = "android-test-application"
        status_message = self.list_files(project_name, file_name)
        return status_message

    def list_ios_application(self, client=None, project_name=None, file_name=None):
        file_category = "ios-application"
        status_message = self.list_files(project_name, file_name)
        return status_message

    def list_ios_native_test_application(self, client=None, project_name=None, file_name=None):
        file_category = "ios-test-application"
        status_message = self.list_files(project_name, file_name)
        return status_message
