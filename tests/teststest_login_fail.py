import os
from selenium.webdriver.common.by import By


def test_successful_login(driver):
    os.makedirs("screenshots", exist_ok=True)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.save_screenshot("screenshots/login_success.png")

    assert "inventory" in driver.current_url