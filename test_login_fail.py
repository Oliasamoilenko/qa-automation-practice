from selenium.webdriver.common.by import By

def test_login_fails_with_incorrect_password(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error_message.is_displayed()