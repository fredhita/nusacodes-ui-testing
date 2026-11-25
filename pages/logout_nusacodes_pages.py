from locators.nusacode_locator import locator

class LogoutPage:
    def __init__(self, page):
        self.page = page
        
    def click_button_logout(self):
        self.page.locator(locator.button_logout).click()
        
    def button_daftar(self):
        return self.page.get_by_role("link", name="Daftar", exact=True)