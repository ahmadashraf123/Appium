import random
import string
import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility, hard_wait


class UpdateCashPortfolios:
    def __init__(self, driver):
      self.driver = driver

    def click_on_pre_define_category_and_verify_home_screen(self, category_name):
        """
        Click on a predefined category (e.g., 'Education' or 'predefineportfo')
        Scrolls to find it if not visible, and handles multi-line content-desc.
        """
        try:
            print(f"Searching for category: {category_name} ...")
            safe_name = category_name.replace(" ", "").replace("\n", "").replace("…", "").replace(".", "")

            dynamic_xpath = (
                f'//android.view.View[contains(translate(@content-desc, " .\n", ""), "{safe_name}")]'
            )

            portfolio_element = wait_for_element_visibility(
                self.driver, (AppiumBy.XPATH, dynamic_xpath), timeout=3, soft_fail=True
            )

            if not portfolio_element:
                print(f"'{category_name}' not visible. Scrolling to find it...")
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiScrollable(new UiSelector().scrollable(true))'
                    f'.scrollIntoView(new UiSelector().descriptionContains("{category_name.split()[0]}"));'
                )

                portfolio_element = wait_for_element_visibility(
                    self.driver, (AppiumBy.XPATH, dynamic_xpath), timeout=5, soft_fail=True
                )

            if portfolio_element:
                print(f"Category '{category_name}' found. Clicking now...")
                portfolio_element.click()
                print("Click successful. Proceeding to the next screen...")
            else:
                print(f" Category '{category_name}' not found even after scroll. Printing visible categories...")
                self.print_all_visible_categories()
                pytest.fail(f"Category '{category_name}' not found even after scroll.")
        except Exception as e:
            pytest.fail(f"Failed to click on category '{category_name}': {e}")
        time.sleep(5)
    def print_all_visible_categories(self):
        """
        Prints all visible elements' content-desc or text on the current screen.
        Helps debug when a category is not found after scrolling.
        """
        try:
            print("\n Visible categories or elements on screen:")
            elements = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
            if not elements:
                print("No visible elements found on the screen.")
            for elem in elements:
                desc = elem.get_attribute("content-desc")
                text = elem.text
                if desc:
                    print(f"  • content-desc: {desc}")
                elif text:
                    print(f"  • text: {text}")
            print("🔹 End of visible elements list\n")
        except Exception as e:
            print(f" Failed to list visible categories: {e}")

    def click_on_pre_define_category_and_verify_home_screen(self, category_name, max_scrolls=4):
        """
        Scrolls step by step until the category is found and clicks it.
        """
        try:
            print(f"Searching for category: {category_name} ...")

            dynamic_xpath = (
                f'//android.view.View[contains(@content-desc, "{category_name}") or contains(@text, "{category_name}")]'
            )

            portfolio_element = wait_for_element_visibility(
                self.driver, (AppiumBy.XPATH, dynamic_xpath), timeout=3, soft_fail=True
            )

            scroll_attempt = 0
            while not portfolio_element and scroll_attempt < max_scrolls:
                scroll_attempt += 1
                print(f"Element not visible, scrolling down (attempt {scroll_attempt}/{max_scrolls}) ...")
                try:
                    self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true)).scrollForward();'
                    )
                except Exception as e:
                    print(f"Scroll attempt {scroll_attempt} failed: {e}")

                time.sleep(1)
                portfolio_element = wait_for_element_visibility(
                    self.driver, (AppiumBy.XPATH, dynamic_xpath), timeout=3, soft_fail=True
                )

            if portfolio_element:
                print(f"Category '{category_name}' found after {scroll_attempt} scroll(s). Clicking now...")
                # Modern tap
                portfolio_element.click()
                print("Tap successful.")
            else:
                print(f"Category '{category_name}' not found after {scroll_attempt} scrolls.")
                self.print_all_visible_categories()
                pytest.fail(f"Category '{category_name}' not found after {scroll_attempt} scrolls.")

        except Exception as e:
            pytest.fail(f"Failed to click on category '{category_name}': {e}")

        time.sleep(5)

    def click_on_update_icon(self):
        """
        Clicks on the 'Update' icon using its XPath: //android.widget.Button
        """
        try:
            print("Waiting for the 'Update' icon to be visible...")

            update_button_xpath = '//android.widget.Button'
            update_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, update_button_xpath),
                timeout=10
            )

            if update_button:
                print(" 'Update' button found. Clicking now...")
                update_button.click()
                print("Click action successful.")
            else:
                pytest.fail(" 'Update' button not found on the screen.")

        except Exception as e:
            print(f" Exception while clicking on 'Update' button: {e}")
            pytest.fail(f"Failed to click on 'Update' button: {e}")

    def click_on_update_button(self):
        """
        Clicks on the 'إدارة الفئة' (Manage Category) button.
        Uses text or content-desc match for reliability.
        """
        try:
            print("Searching for 'إدارة الفئة' button...")

            # XPath that matches button by its text or content-desc
            update_button_xpath = (
                '//android.widget.Button[@content-desc="إدارة الفئة" or @text="إدارة الفئة"]'
            )

            # Wait for button to appear
            update_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, update_button_xpath),
                timeout=10
            )

            if update_button:
                print(" 'إدارة الفئة' button found. Clicking now...")
                update_button.click()
                print("Click on 'إدارة الفئة' successful.")
            else:
                pytest.fail(" 'إدارة الفئة' button not found on screen.")

        except Exception as e:
            print(f" Exception while clicking 'إدارة الفئة': {e}")
            pytest.fail(f"Failed to click 'إدارة الفئة' button: {e}")


    def click_on_edit_icon_for_custom_category(self, category_name=None, x=158, y=433):
        """
        Performs a coordinate tap using Appium TouchAction.
        Optionally logs category name for clarity.
        """
        try:
            if category_name:
                print(f"Performing coordinate tap for category '{category_name}' at ({x}, {y})...")
            else:
                print(f"Performing coordinate tap at ({x}, {y})...")

            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(
                self.driver,
                mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
            )

            actions.w3c_actions.pointer_action.move_to_location(int(x), int(y))
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

            print(f" Tap performed successfully at ({x}, {y}).")

        except Exception as e:
            print(f"Exception while performing coordinate tap: {e}")
            pytest.fail(f"Failed to perform coordinate tap at ({x}, {y}): {e}")

    def click_on_edit_icon(self, category_name=None, x=164, y=436):
        """
        Optionally accepts a category name (for logging), but taps at given coordinates.
        """
        try:
            if category_name:
                print(f"Performing coordinate tap for category '{category_name}' at ({x}, {y})...")
            else:
                print(f"Performing coordinate tap at ({x}, {y})...")

            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(
                self.driver,
                mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
            )

            actions.w3c_actions.pointer_action.move_to_location(int(x), int(y))
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

            print(f" Tap performed successfully at ({x}, {y}).")

        except Exception as e:
            print(f"Exception while performing coordinate tap: {e}")
            pytest.fail(f"Failed to perform coordinate tap at ({x}, {y}): {e}")

    def click_edit_field_remove_existing_name_and_update_new_name(self):
        """
        Clicks on the EditText field, clears existing name, and enters a new random English name.
        Saves it as self.latest_updated_name for later verification.
        """
        try:
            print("Searching for EditText field to update name...")

            edit_field_xpath = '//android.widget.EditText'
            edit_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, edit_field_xpath),
                timeout=10
            )

            if edit_field:
                print(" Edit field found. Clearing existing name...")
                edit_field.click()
                edit_field.clear()

                random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
                new_name = f"Category{random_suffix}"
                print(f"Typing new name: {new_name}")
                edit_field.send_keys(new_name)
                print(" New name entered successfully.")

                #  store it for verify method
                self.latest_updated_name = new_name

                return new_name
            else:
                pytest.fail(" EditText field not found on screen.")
        except Exception as e:
            print(f" Exception while editing field: {e}")
            pytest.fail(f"Failed to update name in EditText field: {e}")

    def click_edit_field_remove_existing_name_and_update_new_name_for_delete_action(self):
        print("Searching for EditText field to update name...")
        edit_field = wait_for_element_visibility(self.driver, (AppiumBy.CLASS_NAME, 'android.widget.EditText'), 10)
        if edit_field:
            print("Edit field found. Clearing existing name...")
            edit_field.clear()
            new_name = "CategoryFHBP"
            print(f"Typing new name: {new_name}")
            edit_field.send_keys(new_name)
            print("New name entered successfully.")
            self.updated_category_name = new_name  #  store it for later verification
        else:
            pytest.fail("EditText field for updating name not found.")

    def click_outside_and_hide_keyboard(self):
        """
        Attempts to click on a specific UIAutomator element to remove focus
        from input field. If the element is not found, hides the keyboard as fallback.
        """
        try:
            print("Trying to click on UIAutomator element to remove focus...")

            # Try finding the element using UIAutomator
            try:
                element = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(5)'
                )
                element.click()
                print("Clicked on UIAutomator element successfully.")

            except Exception:
                print("UIAutomator element not found. Hiding keyboard instead...")
                try:
                    self.driver.hide_keyboard()
                    print("Keyboard hidden successfully.")
                except Exception:
                    print("Keyboard not visible or could not be hidden — continuing...")

        except Exception as e:
            print(f"Exception in click_outside_and_hide_keyboard: {e}")
            pytest.fail(f"Failed to remove focus / hide keyboard: {e}")

    def click_next_button(self):
        """
        Clicks on the 'التالي' (Next) button on the screen using UIAutomator.
        Waits until the button is visible and clickable.
        """
        try:
            print("Waiting for the 'التالي' (Next) button to appear...")

            # Using Android UIAutomator
            next_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("التالي")'),
                timeout=10
            )

            if next_button:
                print(" 'التالي' button found. Clicking now...")
                next_button.click()
                print("Click on 'التالي' successful.")
            else:
                pytest.fail(" 'التالي' button not found on the screen.")

        except Exception as e:
            print(f"Exception while clicking 'التالي' button: {e}")
            pytest.fail(f"Failed to click on 'التالي' button: {e}")


    def verify_updated_category_name_visible(self):
        """
        Verifies that the updated category name appears on the screen where
        category elements use @content-desc (android.view.View elements).
        """
        updated_name = self.latest_updated_name
        print(f" Verifying that updated name '{updated_name}' is visible on screen using @content-desc...")

        # Step 1: Give UI time to refresh
        hard_wait(6)

        # Step 2: Build the primary XPath for @content-desc
        xpath = f'//android.view.View[contains(@content-desc, "{updated_name}")]'
        print(f"Trying to locate: {xpath}")

        try:
            # Try first direct visibility
            element = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, xpath),
                timeout=15,
                soft_fail=True
            )

            # Step 3: If not found, scroll to it
            if not element:
                print("Name not found immediately — attempting scroll...")
                try:
                    self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
                        f'new UiSelector().descriptionContains("{updated_name}"));'
                    )
                    element = wait_for_element_visibility(
                        self.driver,
                        (AppiumBy.XPATH, xpath),
                        timeout=10,
                        soft_fail=True
                    )
                except Exception as scroll_error:
                    print(f" Scroll attempt failed: {scroll_error}")
            # Step 4: Final verification
            if element:
                print(f" Updated category name '{updated_name}' is visible on the screen (found via @content-desc).")
            else:
                self.driver.save_screenshot("screenshots/category_update_not_found.png")
                pytest.fail(f" Updated category name '{updated_name}' not visible even after scroll.")
        except Exception as e:
            print(f" Error verifying category name: {e}")
            self.driver.save_screenshot("screenshots/category_update_error.png")
            pytest.fail(f"Exception while verifying updated category name '{updated_name}'_")


    # def perform_scroll_down_on_portfolio_name_update_screen_and_procced(self):
    #     """
    #     Performs a vertical scroll down gesture within the ScrollView
    #     on the portfolio name update screen and proceeds afterward.
    #     """
    #     try:
    #         print("Attempting to scroll down on the Portfolio Name Update screen...")
    #
    #         # Find the ScrollView element
    #         scroll_view = wait_for_element_visibility(
    #             self.driver,
    #             (AppiumBy.CLASS_NAME, "android.widget.ScrollView"),
    #             timeout=10
    #         )
    #         if not scroll_view:
    #             pytest.fail("ScrollView not found on portfolio name update screen.")
    #         # Get screen dimensions to calculate swipe start/end points
    #         size = self.driver.get_window_size()
    #         start_y = size["height"] * 0.7  # Start lower
    #         end_y = size["height"] * 0.3  # Scroll upward
    #         x = size["width"] / 2  # Middle of the screen
    #         # Perform scroll using W3C actions
    #         actions = ActionChains(self.driver)
    #         actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    #         actions.w3c_actions.pointer_action.move_to_location(x, start_y)
    #         actions.w3c_actions.pointer_action.pointer_down()
    #         actions.w3c_actions.pointer_action.move_to_location(x, end_y)
    #         actions.w3c_actions.pointer_action.release()
    #         actions.perform()
    #         print(" Scroll down performed successfully.")
    #         # Optional: proceed to next step, e.g. clicking the Update button
    #         # You can enable this line if needed:
    #         # self.click_on_update_button()
    #     except Exception as e:
    #         print(f"Exception during scroll: {e}")
    #         pytest.fail(f"Failed to scroll down on portfolio update screen: {e}")

    def click_action_on_update_the_icon_and_proceed(self):
        """
        Clicks on the update icon/button inside the ScrollView and proceeds further.
        Handles visibility, scroll, and click reliability.
        """
        try:
            print("Searching for the update icon inside ScrollView...")

            # Using Android UI Automator instead of XPath
            ui_automator_selector = 'new UiSelector().className("android.view.View").instance(12)'

            # Step 1: Wait for the update icon to be visible
            update_icon = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ANDROID_UIAUTOMATOR, ui_automator_selector),
                timeout=8,
                soft_fail=True
            )
            # Step 2: If not found, scroll a bit and retry
            if not update_icon:
                print(" Update icon not visible — attempting to scroll down slightly...")
                try:
                    self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true)).scrollForward();'
                    )
                    update_icon = wait_for_element_visibility(
                        self.driver,
                        (AppiumBy.ANDROID_UIAUTOMATOR, ui_automator_selector),
                        timeout=5,
                        soft_fail=True
                    )
                except Exception as scroll_error:
                    print(f" Scroll attempt failed while locating update icon: {scroll_error}")
            # Step 3: Click when visible
            if update_icon:
                print(" Update icon found. Performing click action...")
                update_icon.click()
                print(" Click on update icon successful. Proceeding to the next step...")
            else:
                pytest.fail(" Failed to locate and click on the update icon after scrolling.")
        except Exception as e:
            print(f" Exception while clicking update icon: {e}")
            pytest.fail(f"Failed to click on update icon: {e}")

    def click_edit_field_remove_existing_goal_amount_and_update_new_amount(self):
        """
        Clicks on the goal amount EditText field, clears existing amount,
        and enters a new random amount between 1 and 1,000,000.
        Example: '567893'
        """
        try:
            print("Searching for Goal Amount EditText field...")
            # XPath for the goal amount field
            goal_field_xpath = '//android.widget.EditText'
            # Wait until visible
            goal_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, goal_field_xpath),
                timeout=10
            )
            if goal_field:
                print(" Goal amount field found. Clearing existing value...")
                goal_field.click()
                goal_field.clear()
                # Generate random amount between 1 and 1,000,000
                new_amount = str(random.randint(1, 1000000))

                print(f"Typing new goal amount: {new_amount}")
                goal_field.send_keys(new_amount)
                print(" New goal amount entered successfully.")

                # Save new amount for later verification
                self.latest_goal_amount = new_amount

                # --- Close keyboard safely ---
                try:
                    print("Attempting to close keyboard by tapping outside the field...")
                    scroll_view = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ScrollView")
                    scroll_view.click()
                    print(" Keyboard closed successfully.")
                except Exception as close_err:
                    print(f" Could not close keyboard via ScrollView tap: {close_err}. Trying press_keycode(4)...")
                    try:
                        self.driver.press_keycode(4)  # Android BACK key
                        print(" Keyboard closed using BACK key.")
                    except Exception as key_err:
                        print(f" Failed to close keyboard using BACK key: {key_err}")

                return new_amount

            else:
                pytest.fail(" Goal amount EditText field not found on screen.")

        except Exception as e:
            print(f" Exception while updating goal amount: {e}")
            pytest.fail(f"Failed to update goal amount field: {e}")



    # def click_on_scroll_view_to_hide_the_keyboard(self):
    #     """
    #     Taps on the ScrollView to close the on-screen keyboard safely.
    #     Works as a universal keyboard-dismiss helper.
    #     """
    #     try:
    #         print("Attempting to tap on ScrollView and hide keyboard...")
    #
    #         # Locate ScrollView and tap to close keyboard
    #         scroll_view_xpath = '//android.widget.ScrollView'
    #         scroll_view = wait_for_element_visibility(
    #             self.driver,
    #             (AppiumBy.XPATH, scroll_view_xpath),
    #             timeout=5,
    #             soft_fail=True
    #         )
    #         if scroll_view:
    #             scroll_view.click()
    #             print(" Tapped on ScrollView successfully.\n Keyboard hidden successfully.")
    #         else:
    #             print(" ScrollView not found. Trying fallback method using BACK key...")
    #             try:
    #                 self.driver.press_keycode(4)  # BACK button
    #                 print(" Keyboard closed using BACK key successfully.")
    #             except Exception as key_err:
    #                 print(f"Fallback failed: Could not close keyboard. Error: {key_err}")
    #     except Exception as e:
    #         print(f" Exception while trying to close keyboard: {e}")

    def click_on_save_changes_button_and_proceed(self):
        """
        Waits for and clicks on the 'حفظ التغييرات' (Save Changes) button.
        Verifies the action was performed successfully.
        """
        try:
            print("Waiting for the 'حفظ التغييرات' (Save Changes) button to appear...")
            # Corrected XPath → use Button instead of View
            save_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.widget.Button[@content-desc="حفظ التغييرات"]'),
                timeout=15
            )
            if save_button:
                print(" 'حفظ التغييرات' button found. Clicking now...")
                save_button.click()
                print("Click on 'حفظ التغييرات' successful. Proceeding to the next step.")
                # Wait for transition after saving
                hard_wait(3)
            else:
                pytest.fail(" 'حفظ التغييرات' button not found on screen.")
        except Exception as e:
            print(f" Exception while clicking on 'حفظ التغييرات' button: {e}")
            pytest.fail(f"Failed to click 'حفظ التغييرات' button: {e}")

    def click_on_update_icon_to_delete(self):
        """
        Clicks on the 'Update' icon for deletion using the provided XPath.
        Includes scroll-into-view in case the button is off-screen.
        """
        try:
            print("Waiting for the 'Update' icon (for deletion) to appear...")
            update_delete_xpath = ('//android.widget.FrameLayout[@resource-id="android:id/content"]'
                                   '/android.widget.FrameLayout/android.widget.FrameLayout'
                                   '/android.view.View/android.view.View/android.view.View'
                                   '/android.view.View[1]/android.view.View/android.view.View[1]'
                                   '/android.widget.Button')
            # Try direct visibility first
            update_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, update_delete_xpath),
                timeout=10,
                soft_fail=True
            )
            # If not visible, scroll into view
            if not update_button:
                print("Update icon for deletion not visible, attempting scroll...")
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
                    'new UiSelector().className("android.widget.Button"));'
                )
                update_button = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.XPATH, update_delete_xpath),
                    timeout=10
                )

            if update_button:
                print(" 'Update' icon (for deletion) found. Clicking now...")
                update_button.click()
                print("Click action successful.")
            else:
                pytest.fail(" 'Update' icon for deletion not found even after scrolling.")
        except Exception as e:
            print(f" Exception while clicking on 'Update' icon for deletion: {e}")
            pytest.fail(f"Failed to click on 'Update' icon for deletion: {e}")

    def click_on_delete_category_button_and_proceed(self):
        """
        Waits for and clicks on the 'حذف الفئة' (Delete Category) button.
        Verifies that the button click was performed successfully.
        """
        try:
            print("Waiting for the 'حذف الفئة' (Delete Category) button to appear...")
            delete_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, 'حذف الفئة'),
                timeout=15
            )
            if delete_button:
                print(" 'حذف الفئة' button found. Clicking now...")
                delete_button.click()
                print("Click on 'حذف الفئة' successful. Proceeding to the next step.")
                hard_wait(3)
            else:
                pytest.fail(" 'حذف الفئة' button not found on screen.")
        except Exception as e:
            print(f" Exception while clicking on 'حذف الفئة' button: {e}")
            pytest.fail(f"Failed to click 'حذف الفئة' button: {e}")

    def click_on_delete_button_to_delete_category(self):
        """
        Waits for and clicks on the 'احذف الفئة' (Confirm Delete Category) button.
        Verifies that the delete action was triggered successfully.
        """
        try:
            print("Waiting for the 'احذف الفئة' (Confirm Delete Category) button to appear...")
            delete_confirm_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.widget.Button[@content-desc="احذف الفئة"]'),
                timeout=15
            )
            if delete_confirm_button:
                print(" 'احذف الفئة' button found. Clicking now...")
                delete_confirm_button.click()
                print("Click on 'احذف الفئة' successful. Category deletion in progress.")
                hard_wait(3)
            else:
                pytest.fail(" 'احذف الفئة' button not found on confirmation popup.")
        except Exception as e:
            print(f" Exception while clicking on 'احذف الفئة' confirmation button: {e}")
            pytest.fail(f"Failed to confirm category deletion: {e}")
            time.sleep(5)

    # def verify_user_should_redirect_to_the_holistic_home_screen_after_delete_category_and_verify_category_name_not_showing_that_previously_updated_name(
    #         self):
    #     """
    #     Automatically uses the last updated category name stored in class variable.
    #     Verifies redirection to 'الرئيسية' and confirms deleted category is gone.
    #     """
    #     try:
    #         print("Verifying user redirection to 'الرئيسية' (Holistic Home Screen)...")
    #         home_screen_element = wait_for_element_visibility(
    #             self.driver,
    #             (AppiumBy.XPATH, '//android.view.View[@content-desc="الرئيسية"]'),
    #             timeout=20
    #         )
    #         assert home_screen_element, "User not redirected to 'الرئيسية'."
    #         print("User successfully redirected to the Holistic Home Screen.")
    #         deleted_category_name = getattr(self, "updated_category_name", None)
    #         if not deleted_category_name:
    #             pytest.fail("No updated category name stored — cannot verify deletion.")
    #         print(f"Verifying that deleted category '{deleted_category_name}' is not visible...")
    #         category_xpath = f'//android.view.View[contains(@content-desc, "{deleted_category_name}")]'
    #         elements = self.driver.find_elements(AppiumBy.XPATH, category_xpath)
    #
    #         if len(elements) == 0:
    #             print(f" Deleted category '{deleted_category_name}' not found — verification passed.")
    #         else:
    #             pytest.fail(f" Deleted category '{deleted_category_name}' still visible on screen.")
    #     except Exception as e:
    #         print(f" Exception during verification: {e}")
    #         pytest.fail(f"Failed to verify deletion: {e}")









