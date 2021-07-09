import os
from distutils.util import strtobool

import chromedriver_binary
from selenium import webdriver


def create_browser():
    chromedriver_binary.add_chromedriver_to_path()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.headless = bool(strtobool(os.getenv("HEADLESS", "True")))
    return webdriver.Chrome(chrome_options=chrome_options)
