import random
import string
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility


class UpdateInvestmentPortfolios:
    def __init__(self, driver):
      self.driver = driver

    def click_on_the_edit_option(self):
        """
        Clicks on the 'خصص المحفظة' (Customize Portfolio) button using Accessibility ID.
        """
        try:
            print("Waiting for the 'خصص المحفظة' (Customize Portfolio) button to appear...")
            edit_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "خصص المحفظة"),
                timeout=10
            )
            if edit_button:
                print("'خصص المحفظة' button found. Clicking now...")
                edit_button.click()
                print("Click on 'خصص المحفظة' successful.")
            else:
                pytest.fail("Failed to find the 'خصص المحفظة' button.")
        except Exception as e:
            pytest.fail(f"Exception while clicking on 'خصص المحفظة': {e}")

    def click_on_name_field_and_remove_to_update(self):
        """
        Clicks on the portfolio name field, removes the existing name,
        and enters a new randomly generated name.
        """
        try:
            print("Searching for the portfolio name EditText field...")
            name_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, "//android.widget.EditText"),
                timeout=10
            )
            if not name_field:
                pytest.fail("Portfolio name EditText field not found.")
            print("Clicking on the EditText field...")
            name_field.click()
            print("Clearing existing portfolio name...")
            name_field.clear()
            # Generate a random name (e.g., 'PortfolioABX3')
            random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
            new_name = f"Portfolio{random_suffix}"
            print(f"Typing new portfolio name: {new_name}")
            name_field.send_keys(new_name)
            print("New portfolio name entered successfully.")
            #  store the new name for later verification
            self.updated_portfolio_name = new_name
        except Exception as e:
            pytest.fail(f"Exception while updating portfolio name: {e}")

    def click_on_the_view_to_hide_keyboard(self):
        """
        Taps on the ScrollView to hide the keyboard.
        """
        try:
            print("Attempting to tap on the ScrollView to hide the keyboard...")
            scroll_view = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, "//android.widget.ScrollView"),
                timeout=10
            )
            if not scroll_view:
                pytest.fail("ScrollView element not found for hiding keyboard.")
            scroll_view.click()
            print("Tapped on ScrollView successfully. Keyboard should now be hidden.")
            # Optional: explicitly hide keyboard in case it's still visible
            try:
                self.driver.hide_keyboard()
                print("Keyboard hidden successfully.")
            except Exception:
                print("Keyboard was already hidden or no keyboard to hide.")
        except Exception as e:
            pytest.fail(f"Exception while trying to hide keyboard: {e}")

    def click_on_icon_to_update(self):
        """
        Clicks on the update icon located inside the ScrollView.
        """
        try:
            print("Searching for the update icon inside ScrollView...")
            update_icon = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View/android.widget.ImageView[1]"),
                timeout=10
            )
            if not update_icon:
                pytest.fail("Update icon not found inside ScrollView.")
            print("Update icon found. Performing click action...")
            update_icon.click()
            print("Click on update icon successful. Proceeding to the next step...")
        except Exception as e:
            pytest.fail(f"Exception while clicking on update icon: {e}")

    def click_on_save_button(self):
        """
        Clicks on the 'حفظ التغييرات' (Save Changes) button using Accessibility ID.
        """
        try:
            print("Waiting for the 'حفظ التغييرات' (Save Changes) button to appear...")
            save_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "حفظ التغييرات"),
                timeout=10
            )
            if not save_button:
                pytest.fail("Failed to find the 'حفظ التغييرات' (Save Changes) button.")
            print("'حفظ التغييرات' button found. Clicking now...")
            save_button.click()
            print("Click on 'حفظ التغييرات' successful. Proceeding to the next step...")
        except Exception as e:
            pytest.fail(f"Exception while clicking on 'حفظ التغييرات': {e}")

    def click_on_success_update_button(self):
        """
        Clicks on the 'تسجيل الدخول' (Login) button using Accessibility ID.
        Typically used after a successful portfolio update or confirmation screen.
        """
        try:
            print("Waiting for the 'تسجيل الدخول' (Login) button to appear...")
            login_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "تسجيل الدخول"),
                timeout=10
            )
            if not login_button:
                pytest.fail("Failed to find the 'تسجيل الدخول' (Login) button.")
            print("'تسجيل الدخول' button found. Clicking now...")
            login_button.click()
            print("Click on 'تسجيل الدخول' successful. Proceeding to the next screen...")
        except Exception as e:
            pytest.fail(f"Exception while clicking on 'تسجيل الدخول': {e}")
