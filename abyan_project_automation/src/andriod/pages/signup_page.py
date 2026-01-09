import time
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.common import TimeoutException
# from src.utils.password_utils import Passwordutils
from appium.webdriver.common.appiumby import AppiumBy

from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility


class SignUpPage:
    # -------------------
    # Locators (class level)
    # -------------------
    NEXT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "التالي")
    USER_IMAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')
    PHONE_INPUT = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "إستمر")
    PASSWORD_SCREEN_HEADER = (AppiumBy.ACCESSIBILITY_ID, "إنشاء كلمة مرور")
    PASSWORD_SCREEN_KEY_0 = (AppiumBy.ACCESSIBILITY_ID, "0")
    OTP = (AppiumBy.XPATH,'//android.view.View[@content-desc="ادخل رمز التحقق"]/preceding-sibling::android.view.View[1]')
    OTP_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    KYC_HEADER = (AppiumBy.ACCESSIBILITY_ID, "إنشاء حساب")
    OTP_ERROR_MESSAGE = (AppiumBy.XPATH, "//android.view.View[@content-desc='رمز التحقق غير صحيح']")

    def __init__(self, driver):
        self.driver = driver

    # -------------------
    # Actions (methods)
    # -------------------
    def click_welcomescreen_next_buttons(self, times=3):
        # Check if user image exists (OPTIONAL)
        user_present = wait_for_element_visibility(self.driver,self.USER_IMAGE,timeout=5,soft_fail=True)

        if user_present:
            print("User selection screen detected — skipping welcome screen.")
            return

        # Otherwise click Next buttons
        for i in range(times):
            next_button = wait_for_element_visibility(self.driver,self.NEXT_BUTTON,timeout=10,soft_fail=True)

            if next_button:
                time.sleep(2)
                next_button.click()
                print(f"Clicked Next button {i + 1}")
            else:
                print("Next button not found — stopping clicks.")
                break

    def select_user(self):
        user_element = wait_for_element_visibility(self.driver, self.USER_IMAGE, 10)
        if user_element:
            user_element.click()
            print("User selected successfully.")
        else:
            print("User image not visible — skipping user selection step.")
            time.sleep(1)

    def enter_phone_number(self, phone_number):
        phone_input = wait_for_element_visibility(self.driver, self.PHONE_INPUT, 30)
        if phone_input:
            phone_input.click()
            time.sleep(2)
            phone_input = wait_for_element_visibility(self.driver, self.PHONE_INPUT, 10)
            phone_input.send_keys(phone_number)
        else:
            print("Phone input field not found.")

    def click_continue(self):
        continue_button = wait_for_element_visibility(self.driver, self.CONTINUE_BUTTON, 20)
        if continue_button:
            continue_button.click()
        else:
            print("Continue button not found.")

    def enter_password(self):
        wait_for_element_visibility(self.driver, self.PASSWORD_SCREEN_HEADER, 20)
        zero_button = wait_for_element_visibility(self.driver, self.PASSWORD_SCREEN_KEY_0, 10)
        if zero_button:
            for _ in range(6):
                zero_button.click()
                time.sleep(0.3)
        else:
            print("Key '0' not found on password screen.")

    def enter_otp_code(self):
        try:
            # Step 1: Locate the OTP element just above the "ادخل رمز التحقق" label
            otp_element = wait_for_element_visibility(self.driver, self.OTP, 10)
            # Step 2: Extract OTP digits from content-desc
            otp_code = otp_element.get_attribute("content-desc")
            print(f"Detected OTP: {otp_code}")
            # Step 3: Wait for the EditText input field to be ready
            otp_input = wait_for_element_visibility(self.driver,self.OTP_INPUT, 10)
            # Step 4: Enter the OTP code as a whole into the field
            otp_input.click()
            otp_input.send_keys(otp_code)
            print("OTP entered successfully.")
            time.sleep(3)  # Optional pause for UI to transition
        except Exception as e:
            print(f"Error entering OTP: {str(e)}")

    def verify_redirection_to_KYC(self):
        try:
            wait_for_element_visibility(self.driver, self.KYC_HEADER, 20)
            print(" Signup screen is displayed.")
            return True
        except:
            print(" Signup screen is NOT displayed.")
            return False

    def input_invalid_otp(self, otp_value="1234"):
        """
        Enter an invalid OTP.
        Prevent keyboard from reappearing after hiding.
        """
        otp_field = wait_for_element_visibility(self.driver, self.OTP_INPUT, 20)
        assert otp_field is not None, "OTP input field not found"

        otp_field.send_keys(otp_value)  # invalid OTP

        # Handle keyboard
        try:
            self.driver.hide_keyboard()
            print("Keyboard hidden successfully.")
            self.driver.press_keycode(AndroidKey.ENTER)
            print("ENTER key pressed to prevent keyboard reopening.")
        except Exception as e:
            print(f"Keyboard handling skipped: {e}")

    def verify_otp_error_massage(self):
        """
        Verify error message after entering invalid OTP.
        """
        error_el = wait_for_element_visibility(self.driver, self.OTP_ERROR_MESSAGE, 25)
        assert error_el is not None, "OTP error message element not found"

        # Check both possible attributes (text or content-desc)
        error_text = (
                error_el.get_attribute("text")
                or error_el.get_attribute("content-desc")
                or ""
        )
        print(f"OTP error message verified: {error_text}")
        assert "رمز التحقق غير صحيح" in error_text, f"Unexpected error text: {error_text}"

    def verify_password_screen(self):
        wait_for_element_visibility(self.driver, self.PASSWORD_SCREEN_HEADER, 20)

    def request_new_otp(self):
        pass

