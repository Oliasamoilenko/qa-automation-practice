from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    time.sleep(2)

    assert "Google" in driver.title

    driver.find_element(By.NAME, "q")

    print("Success! Google homepage loaded.")

    time.sleep(2)

finally:
    driver.quit()