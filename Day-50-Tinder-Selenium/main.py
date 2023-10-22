from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
from os import environ

login = environ.get("EMAIL")
password = environ.get("PASSWORD")

driver_options = Options()
driver_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driver_options)
driver.get("https://www.tinder.com.br")
sleep(1)

driver.find_element(By.ID, "details-button").click()
sleep(1)
driver.find_element(By.ID, "proceed-link").click()
sleep(6)

driver.find_element(By.LINK_TEXT, "Entrar").click()
sleep(1)
driver.find_element(By.XPATH,
                    "//*[@id='s-561743307']/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button").click()
sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
sleep(1)

driver.find_element(By.NAME, "email").send_keys(login)
driver.find_element(By.NAME, "pass").send_keys(password)
driver.find_element(By.NAME, "login").click()

driver.switch_to.window(base_window)
sleep(6)

# Allow location
allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

# Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

# Allow cookies
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    # Add a 1-second delay between likes.
    sleep(1)

    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()
