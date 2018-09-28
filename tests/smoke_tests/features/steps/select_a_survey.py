from behave import given, then

from tests.functional.setup import browser

from tests.test_config import TestConfig


@given('The user has navigated to the dashboard homepage')
@given('the user is on the dashboard homepage')
def navigating_to_homepage(_):
    browser.get(TestConfig.DASHBOARD_URL)


@then('They can see a list containing at least one survey')
def get_first_row_on_survey_modal(_):
    rows = browser.find_elements_by_css_selector('[data-id="survey_table"] tr')
    assert rows[0].text != 'No data available'
