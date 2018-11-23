from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given('the user has selected a survey')
@given('the user has chosen a survey')
def clicking_on_survey(context):
    # Wait for surveys menu to load
    WebDriverWait(context.browser, timeout=10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-id="survey_table"]')))

    # Click the first survey on the list
    context.browser.find_elements_by_css_selector('[data-id="survey_table"] tr')[0].click()


@then('they are shown at least one collection exercise')
@given("the user can see at least one live collection exercise")
def get_first_row_on_collex_modal(context):
    # Check there is at least one collection exercise displayed in the menu
    rows = context.browser.find_elements_by_css_selector('[data-id="survey_table"] tr')
    assert rows[0].text != 'No data available'
