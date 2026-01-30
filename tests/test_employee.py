from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from utils.config import BASE_URL, USERNAME, PASSWORD

def test_add_employee(setup):
    driver = setup
    login = LoginPage(driver)
    pim = PIMPage(driver)

    login.load(BASE_URL)
    login.login(USERNAME, PASSWORD)

    pim.go_to_pim()
    emp_id = pim.add_employee("Wendell Ann", "Nocido")

    assert emp_id is not None
