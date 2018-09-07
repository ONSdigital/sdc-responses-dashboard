import os

from selenium import webdriver


def create_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")

    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser



browser = create_browser()
