from suds.client import Client
from suds import WebFault
from model.project import Project
import re


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            group_list = client.service.mc_projects_get_user_accessible(username, password)
            groups = []
            for i in group_list:
                id = re.search('(id = (.*$))', str(i), re.MULTILINE).groups()[1]
                project_name = re.search('(name = (.*$))', str(i), re.MULTILINE).groups()[1]
                description = re.search('(description = (.*$))', str(i), re.MULTILINE).groups()[1]
                groups.append(Project(id=id, project_name=project_name[1:-1], description=description[1:-1]))
            return groups
        except WebFault:
            return None
