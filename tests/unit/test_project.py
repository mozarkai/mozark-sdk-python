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
        self.assertEqual(response, "Failure: Project already exists")

    def test_get_project_info(self):
        project_name = "Sample Android Project"
        client = Client()
        client.login()

        response = client.get_project_info(project_name=project_name)
        self.assertEqual(response["projectName"], project_name)

        project_name = "Sample Android Projectt"
        response = client.get_project_info(project_name=project_name)
        self.assertEqual(response, "Failure: Project with name `" + project_name + "` not found.")
