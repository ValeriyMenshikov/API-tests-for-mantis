from sys import maxsize

class Project:
    def __init__(self, id=None, project_name=None, status=None, inherit_global=None, view_status=None,
                 description=None):
        self.id = id
        self.project_name = project_name
        self.status = status
        self.inherit_global = inherit_global
        self.view_status = view_status
        self.description = description

    def __repr__(self, id=None, project_name=None, status=None, inherit_global=None, view_status=None,
                 description=None):
        return f'id={self.id} project_name={self.project_name} descrtiption={self.description}'

    def __eq__(self, other):
        return self.id == other.id, self.project_name == other.project_name, self.description == other.description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize