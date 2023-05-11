from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
import pandas as pd

driver_option = webdriver.ChromeOptions()
driver_option.add_argument("--incognito")
chromedriver_path = r"C:\Users\Gama\Downloads\chromedriver_win32"

def create_webdriver():
    return webdriver.Chrome(service=Service(chromedriver_path), options=driver_option)

browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")

projects = browser.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']")

# Extract information for each project
project_list = {}
for proj in projects:
    proj_name = proj.text
    proj_url = proj.find_element(By.XPATH, ".//a").get_attribute("href")
    project_list[proj_name] = proj_url

browser.quit()

# Extracting data
project_df = pd.DataFrame.from_dict(project_list, orient = 'index')
# Manipulate the table
project_df['project_name'] = project_df.index
project_df.columns = ['project_url', 'project_name']
project_df = project_df.reset_index(drop=True)
project_df.to_csv('project_list.csv')