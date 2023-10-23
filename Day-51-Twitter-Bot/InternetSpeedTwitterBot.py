from os import environ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = environ.get("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        sleep(3)
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        sleep(50)
        self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a").click()
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        self.driver.maximize_window()
        sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span").click()
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input").click()
        self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input").send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input").send_keys(Keys.ENTER)
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").click()
        self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(Keys.ENTER)
        sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div").click()
        self.driver.find_element(By.CLASS_NAME, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div").send_keys(f"I am getting {self.down} down and {self.up} up")
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div").send_keys(Keys.ENTER)

