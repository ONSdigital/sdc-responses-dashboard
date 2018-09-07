from behave import then, when

from tests.functional.setup import browser
from config import DevelopmentConfig


@when('The user navigates to the home page')
def navigating_to_homepage(_):
    browser.get(f'http://{DevelopmentConfig.HOST}:{DevelopmentConfig.PORT}')


# @then('The user is shown a list of all available surveys')
# def show_list_of_surveys(_):
#     browser.find_element_by_class_name()
