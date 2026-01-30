from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import BASE_URL, USERNAME, PASSWORD

def test_valid_login(setup):
    driver = setup
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.load(BASE_URL)
    login.login(USERNAME, PASSWORD)

    assert dashboard.is_dashboard_visible()


def test_invalid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.load(BASE_URL)
    login.login("wrong", "wrong")

    assert "Invalid credentials" in login.get_error_message()
