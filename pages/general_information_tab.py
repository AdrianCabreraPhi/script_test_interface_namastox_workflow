

class GeneralInformationTab:
    def __init__(self,page):
        self.page = page
        self.modal = page.locator("#exampleModal")
        self.title_label = page.get_by_text("Title:")
        self.title_input = page.get_by_role("textbox", name="Descriptive name for this study")
        self.open_modal_button = page.get_by_role("button",name="Add Molecule")
        self.close_modal_button = page.get_by_role("dialog",name="Add molecule",).get_by_label("Close")
        self.substance_name_input = page.locator("#substance_name")
        self.autocomplete_button = page.get_by_role("button",name="Autocomplete")
        self.smiles_input = page.locator("#substance_SMILES")
        self.add_mol_button = page.get_by_role("button",name="Add",exact=True)
        

    def title(self,text):
        self.title_input.fill(text)

    def open_modal_add_mol(self):
        self.open_modal_button.click()
    
    def substance_name(self,text):
        self.substance_name_input.fill(text)
    
    def autocomplete(self):
        self.autocomplete_button.click()
    def add_mol(self):
        self.add_mol_button.click()
    
    def close_modal(self):
        self.close_modal_button.click()

    





        