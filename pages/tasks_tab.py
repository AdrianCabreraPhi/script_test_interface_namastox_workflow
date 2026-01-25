

class TasksTab:
    def __init__(self,page):
        self.page = page
        self.selector = page.locator("#selectPendingResult")
        self.tab_button = page.get_by_role("tab", name="Tasks")
        self.report_textarea = page.locator("#report")
        self.open_modal_method_button = page.get_by_role("button", name="Add method")
        self.method_modal = page.locator("#methodModal")
        self.add_method_button = self.method_modal.get_by_role("button", name="Add", exact=True)
        self.close_method_modal_button = self.method_modal.locator("#btncloseImportTableModal")
        self.open_modal_add_value_button = page.get_by_role("button", name="Add value")
        self.add_value_modal = page.locator("#extraInformation")
        self.selector_method = page.locator("#method")
        self.add_value_button = self.add_value_modal.get_by_role("button", name="Add", exact=True)
        self.close_add_value_modal_button  =  self.add_value_modal.locator("#btncloseImportTableModal")
        self.submit_button = page.locator("#taskForm").get_by_role("button", name="Submit")

    def first_task_text(self):
        return self.page.locator("#selectPendingResult option").first.inner_text()

    def navigate(self):
        self.tab_button.click()
        self.page.wait_for_load_state("networkidle")
    
    def complete_method_form(self):
        self.method_modal.locator("#name").fill("te2e")
        self.method_modal.locator("#description").fill("te2e")
        self.method_modal.locator("#link").fill("te2e")
        self.method_modal.locator("#sensitivity").fill("1")
        self.method_modal.locator("#specificity").fill("1")
        self.method_modal.locator("#sd").fill("1")
    
    def complete_add_value_form(self):
          self.add_value_modal.locator("#parameter").fill("te2e")
          self.add_value_modal.locator("#value").fill("te2e")

    def add_method(self):
        self.add_method_button.click()
    
    def close_modal(self):
        self.close_method_modal_button.click()
    
    def add_value(self):
        self.add_value_button.click()
    
    def close_add_value_modal(self):
        self.close_add_value_modal_button.click()



