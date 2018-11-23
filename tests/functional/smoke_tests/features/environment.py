from tests.functional.setup import create_browser


def before_all(context):
    context.browser = create_browser()


def after_all(context):
    context.browser.quit()
