from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    error_message = (By.XPATH, "//p[contains(@class,'alert-content-text')]")

    def load(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
