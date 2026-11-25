from pages.login_nusacode_pages import LoginPage
from data.nusacode_data import LOGIN_DATA
from utils.config import *
from fixtures.browser import page

def test_login_using_valid_data(page):
    login_page = LoginPage(page)
    page.goto("https://nusacodes.com/")
    login_page.click_button_login_member()
    login_page.fill_email("alcaponeeeyy@gmail.com")
    login_page.fill_password("Ekadita41!")
    login_page.click_button_login()
    login_page.click_button_ok()
    success_login = login_page.validate_name()
    assert success_login == "Eka Dhita"

def test_login_using_invalid_data(page):
    login_page = LoginPage(page)
    page.goto("https://nusacodes.com/")
    login_page.click_button_login_member()
    login_page.fill_email("invalid@gmail.com")
    login_page.fill_password("Invalid123!")
    login_page.click_button_login()
    

def test_login_using_valid_dataIMPORT(page):
    login_page = LoginPage(page)
    page.goto(URL_PROD)
    login_page.click_button_login_member()
    login_page.fill_email(LOGIN_DATA["valid_user"]["email"])
    login_page.fill_password(LOGIN_DATA["valid_user"]["password"])
    login_page.click_button_login()
    login_page.click_button_ok()
    success_login = login_page.validate_name()
    assert success_login == (LOGIN_DATA["valid_user"]["name"])