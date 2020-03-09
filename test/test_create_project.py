from model.project import Project


def test_create_project(app, orm):
    old_projects = orm.get_projects_list()
    new_project = Project(project_name='project_name',
                          status='release',
                          inherit_global=True,
                          view_status='private',
                          description='description')
    app.project.create(new_project)
    new_projects = orm.get_projects_list()
    assert len(old_projects) + 1 == len(new_projects)