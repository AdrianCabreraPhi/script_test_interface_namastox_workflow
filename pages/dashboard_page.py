

class DashboardPage:
    def __init__(self,page):
        self.page = page
        self.button_to_show_options = page.locator("#menubtn")
        self.btn_to_open_modal_new_ra = page.get_by_role("button",name="New")
        self.name_ra_input = page.locator("#newRA").get_by_placeholder("name")
        self.create_ra_button = page.get_by_role("button",name="Create")
    
    def show_options(self):
        self.button_to_show_options.click()
    
    def open_modal_new_ra(self):
        self.btn_to_open_modal_new_ra.click()
    
    def create_new_ra(self,name):
        self.name_ra_input.fill(name)
        self.create_ra_button.click()
    

    
    




