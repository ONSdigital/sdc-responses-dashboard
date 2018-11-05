from behave import then, when
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@when('They click on an collection exercise period')
def click_on_collex(context):
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'collex-datatable')))
    context.browser.find_elements_by_id('collex-datatable')[0].click()


@then('They can view report figures on that collection exercise')
def get_report_figures(context):
    try:
        assert context.browser.find_element_by_id('downloads-counter').text.isdigit()
        assert context.browser.find_element_by_id('uploads-counter').text.isdigit()
        assert context.browser.find_element_by_id('accounts-pending-counter').text.isdigit()
        assert context.browser.find_element_by_id('sample-size-counter').text.isdigit()
    except NoSuchElementException:
        assert context.browser.find_element_by_id('accounts-created-counter').text.isdigit()
        assert context.browser.find_element_by_id('accounts-pending-counter').text.isdigit()
        assert context.browser.find_element_by_id('not-started-counter').text.isdigit()
        assert context.browser.find_element_by_id('in-progress-counter').text.isdigit()
        assert context.browser.find_element_by_id('completed-counter').text.isdigit()
        assert context.browser.find_element_by_id('sample-size-counter').text.isdigit()
