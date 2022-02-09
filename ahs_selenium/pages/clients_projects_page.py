from .base_page import BasePage
from .locators.locators import ClientsProjectsPageLocators


class ClientsProjectsPage(BasePage):
    def should_be_clients_projects_page_text(self):
        assert self.is_element_present(*ClientsProjectsPageLocators.CLIENTS_PROJECTS_TEXT), \
            "Clients&Projects text doesn't appear!"
        assert self.browser.find_element(*ClientsProjectsPageLocators.CLIENTS_PROJECTS_TEXT).text == \
               "Clients & projects", "Incorrect Clients&Projects page!"
