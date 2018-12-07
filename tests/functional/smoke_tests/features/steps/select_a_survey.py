from behave import given, then

from tests.functional.test_config import TestConfig


@given('the user has navigated to the dashboard homepage')
@given('the user is on the dashboard homepage')
def navigating_to_homepage(context):
    context.browser.get(f'{TestConfig.DASHBOARD_URL}/dashboard')


@then('they can see a list containing at least one survey')
def get_first_row_on_survey_modal(context):
    # Check there is at least one survey displayed in the menu
    rows = context.browser.find_elements_by_css_selector('[data-id="survey-table"] tr')
    assert rows[0].text != 'No data available'
