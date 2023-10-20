from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver_options = Options()
# Keep the browser open until driver.quit()
driver_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driver_options)
driver.maximize_window()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Find cookie
cookie = driver.find_element(By.ID, "cookie")

# Get upgrade item ids
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

# To count time
timeout = time.time() + 5
five_min = time.time() + 60 * 5




while True:
    cookie.click()
    if time.time() > timeout:
        # Convert <b> into integer prices
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create a dictionary of store items and prices
        cookies_upgrades = {}
        for n in range(len(item_prices)):
            cookies_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie money
        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        # Find upgrades that we can afford now
        affordable_upgrades = {}
        for price, item_id in cookies_upgrades.items():
            if price <= cookie_count:
                affordable_upgrades[price] = item_id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element(By.ID, to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break




