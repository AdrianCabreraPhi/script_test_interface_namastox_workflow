
import random
from playwright.sync_api import expect


# test E2E to prove that the workflow can be run from the beginning to finish
def test_workflow(auth_page,dashboard_page,general_information_tab,tasks_tab,decisions_tab):
    TEST_NAME = f"Test_{random.randrange(10000)}"
    TEXT = f"{TEST_NAME} E2E FROM SCRIPT IN PYTHON"
    print(F"--- Executing {TEST_NAME} ---")
    # --- Step Create RA --- #
    dashboard_page.show_options()
    dashboard_page.open_modal_new_ra()
    dashboard_page.create_new_ra(TEST_NAME)

    # --- Step General information: add molecule too --- #
    # check if general information is visible
    expect(general_information_tab.title_label).to_be_visible()
    general_information_tab.title(TEXT)
    general_information_tab.open_modal_add_mol()
    general_information_tab.substance_name("ibuprofen")
    general_information_tab.autocomplete()
    expect(general_information_tab.smiles_input).not_to_be_empty() # check if field SMILES is autocompleted
    general_information_tab.add_mol()
    general_information_tab.close_modal()
    expect(general_information_tab.modal).to_be_hidden() # wait to confirm modal is closed
    
    # --- Choose workflow --- #
    workflows_names = general_information_tab.selector_workflows.all_inner_texts()
    workflows_names = ''.join(workflows_names).split("\n")[:-1]
    if workflows_names:
         print("Choose which workflow do you want to test:")
         for i , workflow in enumerate(workflows_names):
              print(f"{i}) {workflow}")
         idx_workflow = -4
         while idx_workflow not in range(0,len(workflows_names)):
              try:
                  idx_workflow = int(input("Introduce number of workflow: "))
              except:
                 pass
         workflow_selected = workflows_names[idx_workflow]
         general_information_tab.selector_workflows.select_option(label=workflow_selected)

    general_information_tab.submit()
    expect(general_information_tab.page.get_by_text(TEXT)).to_be_visible() # wait text is visible in overview


    while True:
      tasks_tab.navigate()

      try:
            tasks_tab.selector.wait_for(state="visible", timeout=5000)
            has_tasks = True
      except:
            has_tasks = False # no tasks available

      if has_tasks:
            print(f"Processing task {tasks_tab.first_task_text()}...")
            tasks_tab.selector.click()

            expect(tasks_tab.report_textarea.or_(tasks_tab.open_modal_method_button).first).to_be_visible()

            if tasks_tab.report_textarea.is_visible():
                  tasks_tab.report_textarea.press_sequentially(TEXT, delay=1)
            else:
                  tasks_tab.open_modal_method_button.click()
                  expect(tasks_tab.method_modal).to_be_visible()

                  tasks_tab.complete_method_form() # complete with random data method form
                  tasks_tab.add_method()
                  tasks_tab.close_modal()
                  expect(tasks_tab.method_modal).to_be_hidden()

                  tasks_tab.open_modal_add_value_button.click()
                  expect(tasks_tab.add_value_modal).to_be_visible()
               
                  tasks_tab.selector_method.first.click()
                  tasks_tab.complete_add_value_form()
                  tasks_tab.add_value()
                  tasks_tab.close_add_value_modal()
                  expect(tasks_tab.add_value_modal).to_be_hidden()

           
            expect(tasks_tab.submit_button).to_be_enabled()
            tasks_tab.submit_button.click()
            tasks_tab.page.wait_for_timeout(1000)
            continue 

      decisions_tab.navigate()

      try:
            decisions_tab.selector.wait_for(state="visible", timeout=5000)
            has_decisions = True
      except:
            has_decisions = False # no decisions available

      if has_decisions:
            print(f"Processing decision {decisions_tab.first_option_text()}...")
            decisions_tab.selector.click()
            expect(decisions_tab.justification_textarea).to_be_visible()
            decisions_tab.justification_textarea.press_sequentially(TEXT, delay=1)

            # random decision yes/no to go through different parts of the workflow
            if random.randrange(2) == 1:
                 decisions_tab.option_yes.click()
                 expect(decisions_tab.option_yes).to_be_checked()

            decisions_tab.submit()
            decisions_tab.page.wait_for_timeout(1000)
            continue 

      if not has_tasks and not has_decisions:
            print("¡Completed! No more tasks in workflow")
            break

            

            




    








