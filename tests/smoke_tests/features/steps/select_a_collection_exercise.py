import time

from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app.common.survey_metadata import _filter_ready_collection_exercises
from tests.collection_exercise_controller import get_collection_exercise_list
from selenium.webdriver.support import expected_conditions as EC
from tests.functional.setup import browser
from tests.test_config import TestConfig


@given('there is at least one live collection exercise')
def wait_on_collection_exercise(_):
        for retry in range(TestConfig.MAX_COLLECTION_EXERCISE_RETRIES):
            if _filter_ready_collection_exercises(get_collection_exercise_list()):
                return
            else:
                time.sleep(60)
        raise TimeoutError


@given('The user has selected a survey')
def clicking_on_survey(_):
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-id="survey_table"]')))
    browser.find_elements_by_css_selector('[data-id="survey_table"] tr')[0].click()


@then('They are shown at least one collection exercise')
def get_first_row_on_collex_modal(_):
    rows = browser.find_elements_by_css_selector('[data-id="survey_table"] tr')
    assert rows[0].text != 'No data available'
