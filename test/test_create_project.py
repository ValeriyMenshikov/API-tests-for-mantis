import string
import random
from model.project import Project


def random_project_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ''.join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


def test_create_project(app, orm):
    old_projects = orm.get_projects_list()
    new_project = Project(project_name=random_project_name('project_name_', 10),
                          status='release',
                          inherit_global=True,
                          view_status='private',
                          description='description')
    app.project.create(new_project)
    new_projects = orm.get_projects_list()
    assert len(old_projects) + 1 == len(new_projects)
