import pytest
from pages.login_nusacode_pages import LoginPage
from data.nusacode_data import LOGIN_DATA
from utils.config import URL_PROD
from playwright.sync_api import expect
    
@pytest.fixture   
def login(page):
    login_page = LoginPage(page)
    page.goto(URL_PROD)
    login_page.click_button_login_member()
    login_page.fill_email(LOGIN_DATA["valid_user"]["email"])
    login_page.fill_password(LOGIN_DATA["valid_user"]["password"])
    login_page.click_button_login()
    login_page.click_button_ok()
    expect(login_page.name_locator()).to_have_text(LOGIN_DATA["valid_user"]["name"])
    return page