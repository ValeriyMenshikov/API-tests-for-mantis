from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_link_text("Manage Projects")) > 0:
            self.app.open_manage_page()

    def open_manage_projects_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_xpath("//input[@value='Create New Project']")) > 0:
            self.open_manage_page()
            wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.change_field_value('name', project.project_name)
        self.change_select_field_value('status', project.status)
        self.activate_check_box('inherit_global', project.inherit_global)
        self.change_select_field_value('view_state', project.view_status)
        self.change_field_value('description', project.description)
        wd.find_element_by_css_selector('input.button').click()

    def delete(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_css_selector('tr.row-1 td a').click()
        wd.find_element_by_css_selector("input.button[value='Delete Project']").click()
        wd.find_element_by_css_selector("input.button[value='Delete Project']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def activate_check_box(self, field_name, parameter):
        wd = self.app.wd
        if parameter is not None:
            wd.find_element_by_name(field_name).click()