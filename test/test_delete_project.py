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
