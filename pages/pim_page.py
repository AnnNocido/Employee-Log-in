from selenium.webdriver.common.by import By
import time

class PIMPage:
    def __init__(self, driver):
        self.driver = driver

    pim_menu = (By.XPATH, "//span[text()='PIM']")
    add_button = (By.XPATH, "//button[contains(.,'Add')]")
    first_name = (By.NAME, "firstName")
    last_name = (By.NAME, "lastName")
    save_button = (By.XPATH, "//button[@type='submit']")
    employee_id = (By.XPATH, "//label[text()='Employee Id']/../following-sibling::div/input")

    def go_to_pim(self):
        self.driver.find_element(*self.pim_menu).click()

    def add_employee(self, first, last):
        self.driver.find_element(*self.add_button).click()
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        emp_id = self.driver.find_element(*self.employee_id).get_attribute("value")
        self.driver.find_element(*self.save_button).click()
        return emp_id
