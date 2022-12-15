from pathlib import Path

import requests


class File:
    config = None
    calculate_md5 = True

    def __init__(self, client=None, calculate_md5=True):
        self.config = client.get_config()
        self.calculate_md5 = calculate_md5

    def get_file_md5(self, filepath=None):
        import hashlib
        md5_hash = ''
        with open(filepath, "rb") as f:
            bytes = f.read()  # read file as bytes
            readable_hash = hashlib.md5(bytes).hexdigest()
            md5_hash = readable_hash
        return md5_hash

    def __upload(self, data=None, files=None):
        new_headers = {'Authorization': "Bearer " + self.config.get("api_access_token"),
                       'Content-Type': 'application/json'}

        file_api_url = self.config.get("api_url") + "testexecute/files"
        # Leg 1 - get the s3 file upload URL
        response = requests.post(file_api_url, json=data, headers=new_headers)

        if response.status_code == 200:
            print("Leg 1 - response: " + response.text)
            if response.json()['status'] == 409:
                print("Leg 1 - File already exists")
                return
        else:
            print("Error: Leg 1" + response.text)
            return

        s3_file_upload_url = response.json()['data']['uploadUrl']

        # Leg 2 - upload the file using s3 upload URL
        response = requests.put(s3_file_upload_url, files=files)

        if response.status_code == 200:
            print("File uploaded successfully: " + s3_file_upload_url)
        else:
            print("Error uploading file")

    def upload_android_application(self, project_name=None, file_path=None):
        file_category = "android-application"
        # self.__upload(project_name, file_path, file_category)
        pass

    def upload_android_native_test_application(self, project_name=None, file_path=None):
        path_object = Path(file_path)
        filename = path_object.name
        data = {
            "fileName": filename,
            "fileCategory": "android-test-application",
            "userName": self.config.get("username"),
            "projectName": project_name
        }

        if self.calculate_md5 == True:
            md5 = self.get_file_md5(file_path)
            data["md5sum"] = md5
        else:
            print("no md5 sum")

        file_object = open(file_path, 'rb')
        files = {'file': file_object}
        self.__upload(data, files)
        file_object.close()

    def upload_ios_application(self, project_name=None, file_path=None):
        file_category = "ios-application"
        # self.__upload(project_name, file_path, file_category)
        pass

    def upload_ios_native_test_application(self, project_name=None, file_path=None):
        file_category = "ios-test-application"
        #self.__upload(project_name, file_path, file_category)
        pass

    def list_files(self, search_filter=None):
        pass
