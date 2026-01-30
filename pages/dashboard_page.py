from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    user_dropdown = (By.CLASS_NAME, "oxd-userdropdown-tab")
    logout_button = (By.LINK_TEXT, "Logout")

    def is_dashboard_visible(self):
        return "dashboard" in self.driver.current_url.lower()

    def logout(self):
        self.driver.find_element(*self.user_dropdown).click()
        self.driver.find_element(*self.logout_button).click()
