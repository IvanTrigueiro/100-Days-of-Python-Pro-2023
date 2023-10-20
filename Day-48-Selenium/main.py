from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

webdriver_chrome_path = "C:/Users/Ivan/Documents/chromedriver-win64/chromedriver.exe"
chrome_options = Options()
# Keep the browser open until driver.quit()
# chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# about = driver.find_element(By.ID, "about")
# print(about.text)
#
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.get_attribute("href"))
#
# bug_link = driver.find_element(By.XPATH, "//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(bug_link.get_attribute("href"))

##### Challenge #####
# # Find the date of the next Python conference by CSS selector
# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_times = [event.get_attribute("datetime").split("T")[0] for event in event_times]
# # Find the name of the next Python conference by CSS selector
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul a")
# event_names = [name.text for name in event_names]
#
# events = {}
# for i in range(len(event_times)):
#     events[i] = {
#         "time": event_times[i],
#         "name": event_names[i]
#     }
#
# print(events)

driver.quit()
