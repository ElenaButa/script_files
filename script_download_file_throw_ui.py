from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



options = webdriver.ChromeOptions()

prefs= {

    "download.default.directory": "С:\qaguru\pythonProject333",
    "download/prompt_for_download": False
}

options.add_experimental_option("prefs", prefs)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=options))

browser.config.driver = driver


browser.open('https://demoqa.com/upload-download')
browser.element('#downloadButton').click()
time.sleep(5)