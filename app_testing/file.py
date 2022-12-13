import logging


class File:
    api_access_token = None

    def __init__(self, api_access_token=None):
        self.api_access_token = api_access_token
        pass

    def __upload(self, project_name=None, file_path=None, file_category=None):
        logging.info("Project Name: " + project_name)
        logging.info("File Path: " + file_path)
        logging.info("File Category: " + file_category)
        pass

    def upload_android_application(self, project_name=None, file_path=None):
        file_category = "android-application"
        self.__upload(project_name, file_path, file_category)
        pass

    def upload_android_native_test_application(self, project_name=None, file_path=None):
        file_category = "android-test-application"
        self.__upload(project_name, file_path, file_category)
        pass

    def upload_ios_application(self, project_name=None, file_path=None):
        file_category = "ios-application"
        self.__upload(project_name, file_path, file_category)
        pass

    def upload_ios_native_test_application(self, project_name=None, file_path=None):
        file_category = "ios-test-application"
        self.__upload(project_name, file_path, file_category)
        pass

    def list_files(self, search_filter=None):
        pass
