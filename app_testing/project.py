class Project:
    config = None

    def __init__(self, client=None):
        self.config = client.get_config()

    def create_project(self, project_name=None):
        pass

    def get_projects(self):
        pass
