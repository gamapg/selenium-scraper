from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation

driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" - incognito")
chromedriver_path = "C:\Users\Gama\Downloads\chromedriver_win32"

def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path, chrome_options=driver_option)

browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")