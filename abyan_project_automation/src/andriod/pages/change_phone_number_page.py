import random
import re
import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webdriver import WebDriver

from abyan_project_automation.src.utils.randomdatagenerator import RandomDataGenerator
from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility


class ChangePhoneNumber:
    SETTING_BUTTON =(AppiumBy.ACCESSIBILITY_ID,"الإعدادات")
    ACCOUNT_BUTTON =(AppiumBy.ACCESSIBILITY_ID,"الحساب\nالملف الشخصي، ترقية مستثمر")
    ABOUT_NUMBER = (AppiumBy.ACCESSIBILITY_ID,"رقم الجوال\n533193463")  # change this locater every time if you change number
    CHANGE_PHONE_NO_INPUT_FIELD =(AppiumBy.CLASS_NAME,"android.widget.ImageView")
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'استمرار')
    OTP = (AppiumBy.XPATH, '//android.view.View[@content-desc="ادخل رمز التحقق"]/preceding-sibling::android.view.View[1]')
    OTP_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    IDCARD_INPUT_FIELD = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    BIRTHDAY_SELECT_FIELD = (AppiumBy.XPATH, '//android.widget.ImageView')
    MILADI_TAB = (AppiumBy.XPATH, '//android.view.View[@content-desc="ميلادي\nهجري"]')
    CONFIRM_DOB = (AppiumBy.ACCESSIBILITY_ID,'تأكيد التاريخ')
    CONTINUE_BUTTON_AFTER_DOB_SELECTION=(AppiumBy.ACCESSIBILITY_ID,'إستمر')
    ABSHER_OTP_SCREEN = (AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View')
    ABSHER_OTP_INPUT = (AppiumBy.XPATH, "//android.widget.EditText")
    HOME_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'الصفحة الرئيسية')
    PASSWORD_SCREEN_HEADER = (AppiumBy.ACCESSIBILITY_ID, "أدخل رمز المرور")
    PASSWORD_SCREEN_KEY_1 = (AppiumBy.ACCESSIBILITY_ID, "1")
    TOAST_INVALID_ID = (AppiumBy.XPATH, "//android.widget.Toast[contains(@text,'رقم الهوية غير صحيح')]")



    def __init__(self, driver):
        self.driver = driver


    def click_SETTING_BUTTON(self):
        setting_button = wait_for_element_visibility(self.driver, self.SETTING_BUTTON, 20)
        if setting_button:
            setting_button.click()
        else:
            print("SETTING BUTTON not found.")

    def click_ACCOUNT_BUTTON(self):
        account_button = wait_for_element_visibility(self.driver, self.ACCOUNT_BUTTON, 20)
        if account_button:
            account_button.click()
        else:
            print("ACCOUNT BUTTON not found.")

    def click_ABOUT_NUMBER(self):
        about_number = wait_for_element_visibility(self.driver, self.ABOUT_NUMBER, 20)
        if about_number:
            about_number.click()
        else:
            print("ABOUT NUMBER not found.")


    def click_CHANGE_PHONE_NO_INPUT_FIELD(self):
        change_phone_number_input = wait_for_element_visibility(self.driver, self.CHANGE_PHONE_NO_INPUT_FIELD, 20)
        if change_phone_number_input:
            change_phone_number_input.click()
        else:
            print("CHANGE PHONE NO INPUT FIELD not found.")

    def enter_new_phone_number(self, phone_number=None):
        try:
            # If no phone number provided, generate one
            if phone_number is None:
                phone_number = RandomDataGenerator.generate_valid_saudi_number()

            phone_input = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.CHANGE_PHONE_NO_INPUT_FIELD)
            )

            phone_input.click()
            time.sleep(0.5)
            phone_input.clear()
            time.sleep(0.5)

            # re-locate to avoid stale element
            phone_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CHANGE_PHONE_NO_INPUT_FIELD)
            )
            phone_input.send_keys(phone_number)
            self.driver.hide_keyboard()  # optional

            print(f" New phone number entered: {phone_number}")

            return phone_number  # optional, if you want to use it later

        except Exception as e:
            print(f" Phone input field error: {e}")
            self.driver.save_screenshot("phone_input_error.png")
            raise



    def click_continue_button(self):
        continue_button = wait_for_element_visibility(self.driver, self.CONTINUE_BUTTON, 20)
        if continue_button:
            continue_button.click()
        else:
            print("continue button not found.")

    def enter_otp_code(self):
        """Enters OTP code if OTP screen is displayed, otherwise skips."""
        try:
            # Step 1: Check if OTP element is visible (with soft fail)
            otp_element = wait_for_element_visibility(self.driver, self.OTP, 20, soft_fail=True)
            if not otp_element:
                print("OTP screen not displayed, skipping OTP entry.")
                return
            # Step 2: Extract OTP digits from content-desc
            otp_code = otp_element.get_attribute("content-desc")
            print(f"Detected OTP: {otp_code}")

            # Step 3: Wait for the EditText input field to be ready
            otp_input = wait_for_element_visibility(self.driver, self.OTP_INPUT, 20, soft_fail=True)
            if not otp_input:
                print("OTP input field not found, skipping OTP entry.")
                return

            # Step 4: Enter the OTP code as a whole into the field
            otp_input.click()
            otp_input.send_keys(otp_code)
            print("OTP entered successfully.")
            time.sleep(1)  # Optional pause for UI to transition

        except Exception as e:
            print(f"Error entering OTP: {str(e)}")
            print("Continuing without OTP entry...")


    def enter_Nid_number(self, id_number: str):
        """
        Clicks the ID card input field, clears existing text, enters a new ID number,
        and hides the keyboard if possible.
        """
        for attempt in range(3):  # try up to 3 times
            try:
                # Locate the element fresh each attempt
                id_input = wait_for_element_visibility(self.driver, self.IDCARD_INPUT_FIELD, 20)

                id_input.click()
                time.sleep(0.5)

                id_input.clear()
                print("ID card input field cleared successfully")
                time.sleep(0.5)

                id_input.send_keys(id_number)
                print(f"Entered ID number: {id_number}")
                time.sleep(0.5)

                try:
                    self.driver.hide_keyboard()
                    print("Keyboard hidden successfully")
                except:
                    pass

                break  # success, exit loop

            except StaleElementReferenceException:
                print(f"StaleElementReferenceException, retrying {attempt + 1}/3")
                time.sleep(0.5)
        else:
            # After 3 attempts, fail test
            pytest.fail(f"Failed to enter ID card number: Element kept going stale")

    def click_dob_field(self):
        dob_field = wait_for_element_visibility(self.driver, self.BIRTHDAY_SELECT_FIELD, 20)
        if dob_field :
            dob_field.click()
        else:
            print("DOB Field not found.")

    def click_miladi_tab(self):
        tab = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.MILADI_TAB)
        )

        loc = tab.location
        size = tab.size
        x = loc["x"] + int(size["width"] * 0.75)
        y = loc["y"] + size["height"] // 2

        # W3C Touch Actions
        finger = PointerInput("touch", "finger")
        actions = ActionBuilder(self.driver, mouse=finger)

        # Add pointer actions
        actions.pointer_action.move_to_location(x, y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pointer_up()

        # Perform the actions
        actions.perform()

    def scroll_and_select_by_content_desc(self, scroller_element, target_desc, max_swipes=400):
        """
        Scroll a circular bottom-sheet picker sequentially DOWN (finger swipes UP)
        to select the exact target value.
        Works for years, months, and days.
        Always scrolls like a user swiping UP.
        """

        swipe_count = 0

        while swipe_count < max_swipes:
            children = scroller_element.find_elements(AppiumBy.XPATH, ".//*")
            visible_descs = [c.get_attribute("content-desc") for c in children if c.get_attribute("content-desc")]

            if not visible_descs:
                raise Exception("No visible items in scroller")

            # Click if target is visible
            for c in children:
                if c.get_attribute("content-desc") == target_desc:
                    c.click()
                    print(f"Selected {target_desc}")
                    return

            # Swipe UP (finger moves UP → scroller moves DOWN)
            x = scroller_element.location['x'] + scroller_element.size['width'] // 2
            start_y = scroller_element.location['y'] + scroller_element.size['height'] * 0.55  # lower point
            end_y = scroller_element.location['y'] + scroller_element.size['height'] * 0.45  # higher point

            self.driver.swipe(int(x), int(start_y), int(x), int(end_y), 400)
            time.sleep(0.1)

            swipe_count += 1

        raise Exception(f"Could not find {target_desc} after {max_swipes} swipes")

    def select_dob(self, year: str, month: str, day: str):
        """
        Select DOB from separate bottom-sheet scrollers (year, month, day).
        Always scrolls sequentially like user swiping finger UP.
        """

        wait = WebDriverWait(self.driver, 15)

        # --- YEAR SCROLLER ---
        year_scroller = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "1997")))
        year_scroller.click()
        self.scroll_and_select_by_content_desc(year_scroller, year)

        # --- MONTH SCROLLER ---
        month_scroller = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "يناير")))
        month_scroller.click()
        self.scroll_and_select_by_content_desc(month_scroller, month)

        # --- DAY SCROLLER ---
        day_scroller = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "1")))
        day_scroller.click()
        self.scroll_and_select_by_content_desc(day_scroller, day)

    def click_confirm_dob_from_bottom_sheet(self):
        """Click on confirm date button"""
        self.driver.find_element(*self.CONFIRM_DOB).click()
        time.sleep(1)


    def click_continue_button_after_dob_selection(self):
            """Click on continue button AFTER date of birth selection from bottom sheet"""
            continue_button = wait_for_element_visibility(self.driver, self.CONTINUE_BUTTON_AFTER_DOB_SELECTION, 20)
            if continue_button:
                continue_button.click()
            else:
                print("continue button not found.")

    def enter_Absher_otp_code(self):
        """
        Detects and enters ONLY a 4-digit numeric OTP from content-desc.
        Safely ignores non-OTP screens.
        """
        try:
            # Small wait for OTP to appear
            time.sleep(2)

            otp_code = None

            #  Scan ALL views on screen
            views = self.driver.find_elements(
                AppiumBy.CLASS_NAME, "android.view.View"
            )

            for view in views:
                desc = view.get_attribute("content-desc")

                #  STRICT OTP RULE
                if desc and desc.isdigit() and len(desc) == 4:
                    otp_code = desc
                    break

            if not otp_code:
                print("No OTP detected on this screen, skipping OTP entry.")
                return

            print(f"Detected OTP: {otp_code}")

            # Wait for OTP input field
            otp_input = wait_for_element_visibility(
                self.driver, self.ABSHER_OTP_INPUT, 10, soft_fail=True
            )

            if not otp_input:
                print("OTP input field not found, skipping OTP entry.")
                return

            otp_input.click()
            otp_input.send_keys(otp_code)
            print("OTP entered successfully.")

        except Exception as e:
            print(f"OTP handling failed: {e}")

    def click_Home_button(self):
            home_button = wait_for_element_visibility(self.driver, self.HOME_BUTTON, 20)
            if home_button:
                home_button.click()
            else:
                print(" HOME BUTTON not found.")

    def enter_invalid_password(self):
        wait_for_element_visibility(self.driver, self.PASSWORD_SCREEN_HEADER, 20)
        zero_button = wait_for_element_visibility(self.driver, self.PASSWORD_SCREEN_KEY_1, 10)
        if zero_button:
            for _ in range(6):
                zero_button.click()
                time.sleep(0.3)
        else:
            print("Key '1' not found on password screen.")


    def assert_wrong_id_error_is_shown(self):
        expected_text = "الهوية الوطنية غير مرتبطة برقم الجوال"

        end_time = time.time() + 6  # wait max 6 seconds

        while time.time() < end_time:
            page_source = self.driver.page_source
            if expected_text in page_source:
                print(" NID and Phone mismatch error appeared – TEST PASSED")
                return True
            time.sleep(0.2)

        raise AssertionError(
            f" Expected error '{expected_text}' did NOT appear in UI source"
        )

    # Error message for phone number already registered

    def verify_phone_number_already_exists_error_is_shown(self):
        error_text = "رقم الهاتف المحمول موجود بالفعل"
        locator = (AppiumBy.ACCESSIBILITY_ID, error_text)

        try:
            # Wait for the error to be visible
            wait_for_element_visibility(self.driver, locator, timeout=5, soft_fail=False)
            print(" Phone number already exists error appeared – test PASSED")
            return True
        except Exception:
            # If element not found or timeout occurs
            print(" Phone number already exists error did NOT appear – test FAILED")
            return False



