from .base_page import BasePage
from .locators import CreatePersonModalLocators


class CreatePersonModal(BasePage):
    def should_be_create_person_modal(self, ):
        assert self.is_element_present(*CreatePersonModalLocators.CREATE_NEW_PERSON_TEXT), "Text in top doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.UPLOAD_PHOTO), "Upload photo field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.UPLOAD_OTHER_CV), \
            "Upload other cv field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ENTER_AKVELON_CV), \
            "Enter Akvelon CV field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.FIRST_NAME), "First name field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.LAST_NAME), "Last name field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.MIDDLE_NAME), "Middle name field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.RECRUITER), "Recruiter field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ROLES), "Roles field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.OFFICE), "Office field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.COUNTRY), "Country field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CITY), "City field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CONTEXT_COMMENT), \
            "Context comment field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.SALARY_TEXT), "Salary field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ENGLISH_LEVEL), "English level field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ENGLISH_COMMENT), \
            "English comment field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.PRIMARY_SKILL), "primary skills field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.PRIMARY_SKILL_GRADE), \
            "primary skills grade field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CONFIRMED_SKILL_CHECKBOX), \
            "confirmed skills field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ADD_PRIMARY_SKILL), "Add skills field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.OTHER_SKILL), "Other skills field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.RESIDENCE_COUNTRY), "Residences field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.RESIDENCE_TYPE), \
            "Residences type field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ADD_RESIDENCE), "Add Residence field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.WANT_RELOCATE), "Want relocate field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.WANT_RELOCATE_COMMENT), \
            "Want relocate comment field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.ADD_ONE_MORE_CONTACT), \
            "Add contact field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CONTACT_TYPE), "Contact type field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CONTACT_VALUE), "Contact value field doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CREATE_PERSON_BUTTON), \
            "CREATE_PERSON_BUTTON doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CANCEL_CREATE_PERSON_BUTTON), \
            "CANCEL_CREATE_PERSON_BUTTON doesn't appear!"
        assert self.is_element_present(*CreatePersonModalLocators.CROSS_EXIT), "Exit cross doesn't appear!"
