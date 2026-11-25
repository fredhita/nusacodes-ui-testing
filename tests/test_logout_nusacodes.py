from pages.logout_nusacodes_pages import LogoutPage
from playwright.sync_api import expect

def test_logout(login):
    logout = LogoutPage(login)
    logout.click_button_logout()
    expect(logout.button_daftar()).to_be_visible()
