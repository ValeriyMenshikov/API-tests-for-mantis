from pony.orm import *
from model.project import Project


class ORMFixture:
    db = Database()

    class ORMProject(db.Entity):
        _table_ = 'mantis_project_table'
        id = PrimaryKey(int, column='id')
        name = Optional(str, column='name')
        description = Optional(str, column='description')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_projects_to_model(self, projects):
        def convert(project):
            return Project(id=str(project.id), project_name=project.name, description=project.description)

        return list(map(convert, projects))

    @db_session
    def get_projects_list(self):
        return self.convert_projects_to_model(select(g for g in ORMFixture.ORMProject))
