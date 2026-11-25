from locators.nusacode_locator import locator

class LoginPage:
    def __init__(self, page):
        self.page = page
        
    def click_button_login_member(self):
        self.page.get_by_role(locator.button_login_member[0],name=locator.button_login_member[1]).click()
        
    def fill_email(self,email):
        self.page.get_by_label(locator.input_email[0],exact=locator.input_email[1]).fill(email)
        
    def fill_password(self,password):
        self.page.get_by_label(locator.input_password[0],exact=locator.input_password[1]).fill(password)
        
    def click_button_login(self):
        self.page.get_by_role(locator.button_login[0],name=locator.button_login[1],exact=locator.button_login[2]).click()
        
    def click_button_ok(self):
        self.page.get_by_role(locator.button_ok[0], name=locator.button_ok[1],exact=locator.button_ok[2]).click()
        
    def name_locator(self):
         return self.page.get_by_role("banner").get_by_role("heading")

    def validate_name(self):
         locator = self.name_locator()
         locator.wait_for(state="visible")
         return locator.text_content()
