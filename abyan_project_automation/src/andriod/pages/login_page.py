import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.common import TimeoutException

from abyan_project_automation.src.utils.password_utils import PasswordUtils
from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility, hard_wait


class LoginPage:
    # -------------------
    # Locators (class level)
    # -------------------
    NEXT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "التالي")
    USER_IMAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')
    PHONE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView")')
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "إستمر")
    PASSWORD_SCREEN_HEADER = (AppiumBy.ACCESSIBILITY_ID, "أدخل رمز المرور")
    PASSWORD_SCREEN_KEY_0 = (AppiumBy.ACCESSIBILITY_ID, "0")
    OTP = (AppiumBy.XPATH,'//android.view.View[@content-desc="ادخل رمز التحقق"]/preceding-sibling::android.view.View[1]')
    OTP_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    HOME_SCREEN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("الرئيسية")')
    ENABLE_NOTIFICATION_HEADER = (AppiumBy.ACCESSIBILITY_ID, "تفعيل الإشعارات")
    NOT_NOW_ENABLE_NOTIFICATION_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "ربما لاحقًا")
    KYC_HEADER = (AppiumBy.ACCESSIBILITY_ID, "إنشاء حساب")
    PASSWORD_KEY_1 = (AppiumBy.ACCESSIBILITY_ID, "1")
    ERROR_MESSAGE_INCORRECT_CREDENTIALS = (AppiumBy.ACCESSIBILITY_ID, "رقم الجوال او كلمة المرور غير صحيحة")
    PREMIUM_POP_UP = (AppiumBy.ACCESSIBILITY_ID, "تم تغيير اسامي المحافظ")
    CLICK_PREMIUM_POP_UP = (AppiumBy.ACCESSIBILITY_ID, "صفحة الخدمات")
    OTP_ERROR_MESSAGE = (AppiumBy.XPATH,"//android.view.View[@content-desc='رمز التحقق غير صحيح']")
    HOLISTIC_WELCOME = (AppiumBy.XPATH,'//android.view.View[contains(@content-desc, "مرحبًا")]')
    INCORRECT_OTP_MESSAGE = "رمز التحقق غير صحيح"
    SUCCESS_INDICATOR = (AppiumBy.XPATH, "//android.view.View[@content-desc='الرئيسية']")
    ERROR_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "رقم الجوال او كلمة المرور غير صحيحة")

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

    def enter_phone_number(self, phone_number):
        phone_input = wait_for_element_visibility(self.driver, self.PHONE_INPUT, 20)
        if phone_input:
            phone_input.click()
            time.sleep(2)
            phone_input.send_keys(phone_number)
        else:
            print("Phone input field not found.")

    def click_continue(self):
        continue_button = wait_for_element_visibility(self.driver, self.CONTINUE_BUTTON, 20)
        if continue_button:
            continue_button.click()
        else:
            pytest.fail("Continue button not found.")

    def enter_password(self):
        wait_for_element_visibility(self.driver, self.PASSWORD_SCREEN_HEADER, 20)
        zero_button = wait_for_element_visibility(self.driver, self.PASSWORD_SCREEN_KEY_0, 10)
        if zero_button:
            for _ in range(6):
                zero_button.click()
                time.sleep(0.3)
        else:
            print("Key '0' not found on password screen.")



    # def enter_otp_code(self):
    #     try:
    #         otp_element = wait_for_element_visibility(
    #             self.driver, self.OTP, 15, soft_fail=True
    #         )
    #         if not otp_element:
    #             print("OTP screen not displayed")
    #             return
    #
    #         otp_code = otp_element.get_attribute("content-desc")
    #         print(f"Detected OTP: {otp_code}")
    #
    #         otp_input = wait_for_element_visibility(
    #             self.driver, self.OTP_INPUT, 15
    #         )
    #
    #         otp_input.click()
    #         time.sleep(1)
    #
    #         #  SAFE OTP ENTRY
    #         self.driver.execute_script(
    #             "mobile: shell",
    #             {"command": "input", "args": ["text", otp_code]}
    #         )
    #
    #         print("OTP entered")
    #
    #     except Exception as e:
    #         print(f"OTP error: {e}")

    def enter_otp_code(self):
        try:
            # Try to detect OTP bubble (do NOT fail if not found)
            otp_element = wait_for_element_visibility(
                self.driver, self.OTP, timeout=5, soft_fail=True
            )

            if not otp_element:
                print("OTP not found.")
                return

            otp_code = otp_element.get_attribute("content-desc")
            print(f"Detected OTP: {otp_code}")

            # Find OTP input field
            otp_input = wait_for_element_visibility(
                self.driver, self.OTP_INPUT, timeout=5, soft_fail=True
            )

            if not otp_input:
                print("OTP input field not found.")
                return

            otp_input.click()
            otp_input.send_keys(otp_code)
            print("OTP entered successfully.")

            time.sleep(2)  # allow UI transition

        except Exception as e:
            print(f"Error entering OTP: {e}")

    def verify_holistic_home_screen(self):
        try:
            home_element = wait_for_element_visibility(self.driver, self.HOME_SCREEN, 20)
            if home_element and home_element.is_displayed():
                # confirm by attribute
                screen_text = home_element.get_attribute("content-desc")
                if screen_text == "الرئيسية":
                    print(" Confirmed: User is on Home Screen")
                    hard_wait(15)
                    return True
                else:
                    print(f" Element found but text mismatch: {screen_text}")
                    hard_wait(15)
                    return False
            else:
                print(" Home Screen element not visible")
                hard_wait(5)
                return False

        except Exception as e:
            print(f"Error verifying Home Screen: {str(e)}")
            hard_wait(5)
            return False

    def handle_enable_notifications_if_displays(self):
        try:
            element = wait_for_element_visibility(self.driver, self.ENABLE_NOTIFICATION_HEADER, 20, soft_fail=True)
            not_now_button = wait_for_element_visibility(self.driver, self.NOT_NOW_ENABLE_NOTIFICATION_BUTTON, 10, soft_fail=True)
            if element and not_now_button:
                print("Enable notification screen verified successfully.")
                not_now_button.click()
                print("Clicked on 'Not Now' button successfully.")
            else:
                print("Enable notification screen not displayed, skipping verification.")

        except Exception as e:
            print(f"Failed to verify or click 'Not Now' button: {e}")
            print("Skipping as this screen may not appear every time.")

    def handle_premium_pop_up_if_displays(self):
        try:
            element = wait_for_element_visibility(self.driver, self.PREMIUM_POP_UP, 15, soft_fail=True)
            if element is None:
                print("Premium Home Screen not displayed, skipping verification.")
                return  # Skip further checks if screen not present
            print("Premium Home Screen verified successfully.")
        except Exception as e:
            print("Failed to verify Premium Home Screen:", str(e))
            print("Skipping Premium Home Screen verification as it may not appear every time.")
            return  # Skip if any unexpected error occurs
        try:
            button = wait_for_element_visibility(self.driver, self.CLICK_PREMIUM_POP_UP, timeout=10, soft_fail=True)
            if button:
                button.click()
                print("Clicked on Premium Wallet button successfully.")
            else:
                print("Premium Wallet button not found, skipping.")
        except Exception as e:
            print("Failed to click on Premium Wallet button:", str(e))
            # Don't raise exception, just log and continue
    def verify_redirect_to_home_screen(self):
        try:
            home_element = wait_for_element_visibility(self.driver, self.HOME_SCREEN, 15)
            if home_element and home_element.is_displayed():
                # confirm by attribute
                screen_text = home_element.get_attribute("content-desc")
                if screen_text == "الرئيسية":
                    print(" Confirmed: User is on Home Screen")
                    return True
                else:
                    print(f" Element found but text mismatch: {screen_text}")
                    return False
            else:
                print(" Home Screen element not visible")
                return False
        except Exception as e:
            print(f"Error verifying Home Screen: {str(e)}")
            return False

    def verify_welcome_message_for_non_premium(self):
        """
        Verify welcome message 'مرحبًا' is displayed on HomeScreen for non-premium users.
        """
        try:
            homescreen = wait_for_element_visibility(self.driver, self.HOLISTIC_WELCOME, 30)
            assert homescreen is not None, "HomeScreen with greeting 'مرحبًا' not found"
            print("Welcome message for non-premium user verified successfully.")
        except AssertionError as e:
            print(str(e))
            raise
        except Exception as e:
            print(f"Failed to verify welcome message for non-premium user: {e}")
            raise

    def test_create_password_and_save(self, setup_driver):
        driver = setup_driver
        phone_number = "1234567890"
        password = PasswordUtils.generate_numeric_password()
        password_field_xpath = (
            "//android.widget.FrameLayout[@resource-id='android:id/content']"
            "/android.widget.FrameLayout/android.widget.FrameLayout"
            "/android.view.View/android.view.View/android.view.View"
            "/android.view.View[2]/android.view.View[2]"
        )
        driver.find_element(AppiumBy.XPATH, password_field_xpath).click()
        time.sleep(0.1)
        for digit in password:
            digit_xpath = f"//android.view.View[@content-desc='{digit}']"
            driver.find_element(AppiumBy.XPATH, digit_xpath).click()
            time.sleep(0.3)
        PasswordUtils.save_credentials_to_csv(phone_number, password)
        print(f"Password '{password}' saved for phone number {phone_number}")

    def verify_redirect_to_signup_screen(self):
        try:
            wait_for_element_visibility(self.driver, self.KYC_HEADER, 20)
            print(" Signup screen is displayed.")
            return True
        except:
            print(" Signup screen is NOT displayed.")
            return False

    def enter_incorrect_password(self):
        """Press '1' six times to enter 111111 as password."""
        # Wait until password screen is visible
        wait_for_element_visibility(self.driver, self.PASSWORD_SCREEN_HEADER, 10)
        # Find key '1'
        key_1 = wait_for_element_visibility(self.driver, self.PASSWORD_KEY_1)
        # Tap '1' six times
        for _ in range(6):
            wait_for_element_visibility(self.driver, self.PASSWORD_KEY_1, 5).click()

    def verify_error_incorrect_password(self):
        """
        Verify error message appears for incorrect password.
        """
        error_el = wait_for_element_visibility(self.driver, self.ERROR_MESSAGE_INCORRECT_CREDENTIALS, 10)
        assert error_el is not None, "Password error message element not found"

        # Extract actual text from element
        actual_text = error_el.get_attribute("content-desc") or error_el.text
        expected_text = "رقم الجوال او كلمة المرور غير صحيحة"

        assert actual_text.strip() == expected_text, \
            f"Expected '{expected_text}' but got '{actual_text}'"
        print("Incorrect password error verified successfully:", actual_text)
        return actual_text

    def enter_invalid_otp(self, otp_value="1234"):
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

    def verify_error_invalid_otp(self):
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

    def is_login_successful(self, timeout=20):
        try:
            element = wait_for_element_visibility(self.driver, self.SUCCESS_INDICATOR)
            return element.is_displayed()
        except:
            return False

    def click_login_button(self):
        pass

    def is_login_failed(self):
        """
        Check if login failed by verifying the presence of error message element.
        """
        try:
            error_element = wait_for_element_visibility(self.driver, self.ERROR_MESSAGE, 10)
            return error_element is not None
        except Exception:
            return False

    def request_new_otp(self):
        pass

    def verify_error_otp_expired(self):
        pass








