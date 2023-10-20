from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver_options = Options()
# Keep the browser open until driver.quit()
driver_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driver_options)
driver.maximize_window()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # article_count.click()
#
# click_species = driver.find_element(By.LINK_TEXT, "Wikispecies")
# click_species.click()
#
# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

# ### Challenge ###
# driver.get("https://secure-retreat-92358.herokuapp.com")
#
# first_name = driver.find_element(By.NAME, "fName")
# first_name.send_keys("Regnum")
#
# last_name = driver.find_element(By.NAME, "lName")
# last_name.send_keys("Animalia")
#
# email = driver.find_element(By.NAME, "email")
# email.send_keys("regnum@animalia.com")
#
# submit_button = driver.find_element(By.CLASS_NAME, "btn")
# submit_button.click()

