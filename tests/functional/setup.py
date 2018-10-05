from selenium import webdriver


def create_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.headless = True
    return webdriver.Chrome(chrome_options=chrome_options)


browser = create_browser()
