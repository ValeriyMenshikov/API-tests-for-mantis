from model.project import Project


def test_delete_first_project(app, orm):
    if len(orm.get_projects_list()) == 0:
        new_project = Project(project_name='project_name1',
                              status='release',
                              inherit_global=True,
                              view_status='private',
                              description='description2')
        app.project.create(new_project)
    old_projects = orm.get_projects_list()
    app.project.delete()
    new_project = orm.get_projects_list()
    assert len(old_projects) - 1 == len(new_project)


def test_delete_first_project_soap(app, orm):
    username = 'Administrator'
    password = 'root'
    if len(app.soap.get_project_list(username, password)) == 0:
        new_project = Project(project_name='project_name1',
                              status='release',
                              inherit_global=True,
                              view_status='private',
                              description='description2')
        app.project.create(new_project)
    old_projects = app.soap.get_project_list(username, password)
    app.project.delete()
    new_project = app.soap.get_project_list(username, password)
    assert len(old_projects) - 1 == len(new_project)