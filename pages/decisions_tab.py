

class DecisionsTab:
    def __init__(self,page):
        self.page = page
        self.tab_button = page.get_by_role("tab", name="Decisions")
        self.selector = page.locator("#selectPendingDecision")
        self.justification_textarea = page.locator("#justification")
        self.option_yes = page.locator("#inlineRadioDecision1")
        self.submit_button = page.locator("#decisionForm").get_by_role("button", name="Submit")
    
    def navigate(self):
        self.tab_button.click()
    
    def first_option_text(self):
        return self.page.locator("#selectPendingDecision option").first.inner_text()

    def submit(self):
        self.submit_button.wait_for(state="visible",timeout=5000)
        self.submit_button.click()


