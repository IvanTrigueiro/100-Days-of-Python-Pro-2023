from os import environ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

SIMILAR_ACCOUNT = "shiachticasananda"
USERNAME = environ.get("INSTA_USERNAME")
PASSWORD = environ.get("INSTA_PASSWORD")


class InstaFollower:
    def __init__(self):
        # Driver Options
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        # Driver Initialization
        self.driver = webdriver.Chrome(options=self.options)

    def login(self):
        # Navigate to Instagram
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)
        # Username
        self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
        # Password
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        # Click on Login
        self.driver.find_element(By.CSS_SELECTOR, "div button div").click()
        sleep(5)

    def find_followers(self):
        # Navigate to Profile Page
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        self.driver.maximize_window()
        sleep(3)
        # Click on Follow Button
        follow_button = self.driver.find_element(By.XPATH, "//li[2]/a/span")
        number_of_followers = int(follow_button.get_attribute("title").replace(".", ""))
        follow_button.click()
        sleep(1)
        follower_accounts = self.driver.find_element(By.CSS_SELECTOR, "div._aano")
        sleep(5)
        # Scroll Down until the end
        for i in range(int(5)):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_accounts)
            sleep(3)

    def follow(self):
        # Find all followers
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano div div div div button")
        for button in all_buttons:
            # Follow each account
            try:
                button.click()
                sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]")
                cancel_button.click()

