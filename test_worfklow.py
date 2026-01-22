
import random
from playwright.sync_api import expect


# test E2E to prove that the workflow can be run from the beginning to finish
def test_workflow(auth_page):
    TEST_NAME = f"Test_{random.randrange(10000)}"
    TEXT = f"{TEST_NAME} E2E FROM SCRIPT IN PYTHON"
    print(F"--- Executing {TEST_NAME} ---")
    # --- Step Create RA --- #
    auth_page.locator("#menubtn").click()
    auth_page.get_by_role("button", name="New").click()
    auth_page.locator("#newRA").get_by_placeholder("name").fill(TEST_NAME)
    auth_page.get_by_role("button",name="Create").click()
    expect(auth_page.get_by_text("Title:")).to_be_visible()
    # --- Step General information: add molecule too --- #
    auth_page.get_by_role("textbox", name="Descriptive name for this study").fill(TEXT)
    auth_page.get_by_role("button",name="Add Molecule").click()
    auth_page.locator("#substance_name").fill("ibuprofen")
    auth_page.get_by_role("button",name="Autocomplete").click()
    expect(auth_page.locator("#substance_SMILES")).not_to_be_empty() # check if field SMILES is autocompleted
    auth_page.get_by_role("button",name="Add",exact=True).click()
    auth_page.get_by_role("dialog",name="Add molecule",).get_by_label("Close").click()
    expect(auth_page.locator("#exampleModal")).to_be_hidden() # wait to confirm modal is closed
    auth_page.get_by_role("button",name="Submit",).click()
    expect(auth_page.get_by_text(TEXT)).to_be_visible() # wait text is visible in overview
    tasks_tab = auth_page.get_by_role("tab", name="Tasks")

    while True:
      tasks_tab.click()
      auth_page.wait_for_load_state("networkidle")

      try:
            selector_task = auth_page.locator("#selectPendingResult")
            selector_task.wait_for(state="visible", timeout=5000)
            has_tasks = True
      except:
            has_tasks = False # no tasks available

      if has_tasks:
            text_first_option = auth_page.locator("#selectPendingResult option").first.inner_text()
            print(f"Processing task {text_first_option}...")
            selector_task.click() 
            textarea = auth_page.locator("#report")
            add_method = auth_page.get_by_role("button", name="Add method")

            expect(textarea.or_(add_method).first).to_be_visible()

            if textarea.is_visible():
                  textarea.press_sequentially(TEXT, delay=10)
            else:
                  add_method.click()
                  method_modal = auth_page.locator("#methodModal")
                  expect(method_modal).to_be_visible()
                  method_modal.locator("#name").fill("te2e")
                  method_modal.locator("#description").fill("te2e")
                  method_modal.locator("#link").fill("te2e")
                  method_modal.locator("#sensitivity").fill("1")
                  method_modal.locator("#specificity").fill("1")
                  method_modal.locator("#sd").fill("1")
                  method_modal.get_by_role("button", name="Add", exact=True).click()
                  method_modal.locator("#btncloseImportTableModal").click()
                  expect(method_modal).to_be_hidden()
                  add_value = auth_page.get_by_role("button", name="Add value")
                  add_value.click()
                  add_value_modal = auth_page.locator("#extraInformation")
                  expect(add_value_modal).to_be_visible()
                  select_method = auth_page.locator("#method")
                  select_method.first.click()
                  add_value_modal.locator("#parameter").fill("te2e")
                  add_value_modal.locator("#value").fill("te2e")
                  add_value_modal.get_by_role("button", name="Add", exact=True).click()
                  add_value_modal.locator("#btncloseImportTableModal").click()
                  expect(add_value_modal).to_be_hidden()

            
            submit_btn = auth_page.locator("#taskForm").get_by_role("button", name="Submit")
            expect(submit_btn).to_be_enabled()
            submit_btn.click()
            auth_page.wait_for_timeout(1000)
            continue 

      decisions_tab = auth_page.get_by_role("tab", name="Decisions")
      decisions_tab.click()

      try:
            selector_decision = auth_page.locator("#selectPendingDecision")
            selector_decision.wait_for(state="visible", timeout=5000)
            has_decisions = True
      except:
            has_decisions = False # no decisions available

      if has_decisions:
            text_first_option = auth_page.locator("#selectPendingDecision option").first.inner_text()
            print(f"Processing decision {text_first_option}...")
            selector_decision.click()
        
            textarea_dec = auth_page.locator("#justification")
            expect(textarea_dec).to_be_visible()
            textarea_dec.press_sequentially(TEXT, delay=10)

            # random decision yes/no to go through different parts of the workflow
            if random.randrange(2) == 1:
                 yes_checkbox = auth_page.locator("#inlineRadioDecision1")
                 yes_checkbox.click()
                 expect(yes_checkbox).to_be_checked()

            submit_btn = auth_page.locator("#decisionForm").get_by_role("button", name="Submit")
            expect(submit_btn).to_be_enabled()
            submit_btn.click()
            auth_page.wait_for_timeout(1000)
            continue 

      if not has_tasks and not has_decisions:
            print("¡Completed! No more tasks in workflow")
            break

            

            




    








