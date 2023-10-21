import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
phone = os.environ.get("PHONE")

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/login")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.NAME, "session_key").send_keys(username)
driver.find_element(By.NAME, "session_password").send_keys(password)
# Find element by css selector from form div button
driver.find_element(By.CSS_SELECTOR, "form div button").click()
time.sleep(3)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3610766780&f_LF=f_AL&geoId=106057199&keywords=python%20developer&location=Brasil&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, ".ember-view a").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "form input").click()
driver.find_element(By.CSS_SELECTOR, "form input").send_keys(phone)
driver.find_element(By.CSS_SELECTOR, "footer button").click()
time.sleep(5)

driver.close()


