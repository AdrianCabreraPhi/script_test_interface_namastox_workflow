
class LoginPage:
    def __init__(self,page):
        self.page = page
        self.url = "https://namastox.upf.edu/auth/realms/namastox/protocol/openid-connect/auth?client_id=namastox-client&redirect_uri=https://namastox.upf.edu/callback&response_type=code&scope=openid%20profile%20email"
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#kc-login")
    
    def navigate(self):
        self.page.goto(self.url)
    
    def login(self,user,password):
        self.username_input.fill(user) 
        self.password_input.fill(password)
        self.login_button.click()
    
    def is_logged(self):
        try:
            self.page.get_by_text("Select RA").wait_for(state="visible",timeout=5000)
            return True
        except:
            return False



        
