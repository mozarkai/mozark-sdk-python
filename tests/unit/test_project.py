from unittest import TestCase
from mozark_sdk.client import Client


class TestProject(TestCase):
    def test_create_project(self):
        project_name = "Sample Android Project"
        project_description = "Sample Android Project Description"
        client = Client()
        client.login()

        response = client.create_project(project_name=project_name, project_description=project_description)
        self.assertEqual(response, "Success")
        response = client.create_project(project_name=project_name, project_description=project_description)
        self.assertEqual(response, "Failure: Project with "+project_name+" already exists.")

    def test_get_project_info(self):
        project_name = "Sample Android Project"
        client = Client()
        client.login()

        response = client.get_project_info(project_name=project_name)
        print(response)
        self.assertEqual(response["projectName"], project_name)

        project_name = "Sample Android Projectt"
        response = client.get_project_info(project_name=project_name)
        self.assertEqual(response, "Failure: Project with name `" + project_name + "` not found.")

    def test_delete_project(self):
        project_name = "Sample Android Project"
        client = Client()
        client.login()

        response = client.delete_project(project_name=project_name)
        self.assertEqual(response, "Success")

        response = client.delete_project(project_name=project_name)
        self.assertEqual(response, "Failure: Project with name `" + project_name + "` not found.")

    def test_get_project_list(self):
        client = Client()
        client.login()

        project_list = client.get_project_list()
        print(project_list)
