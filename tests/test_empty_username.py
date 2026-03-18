from selenium.webdriver.common.by import By

def test_empty_username(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Username is required" in error