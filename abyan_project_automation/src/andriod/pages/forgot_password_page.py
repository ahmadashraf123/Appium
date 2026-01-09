import time
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.webdriver.common.appiumby import AppiumBy

from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility


class ForgotPassword:
    # -------------------
    # Locators
    # -------------------
    NEXT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "التالي")
    USER_IMAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')
    PHONE_INPUT = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "إستمر")
    CANT_LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "لا تستطيع تسجيل الدخول؟")
    FORGOT_LINK = (AppiumBy.ACCESSIBILITY_ID, "نسيت رمز المرور")
    # FORGOT_POPUP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "إعادة تعيين")
    FORGET_PASSWORD_SCREEN_HEADER = (AppiumBy.ACCESSIBILITY_ID, "أدخل رمز المرور الجديد")
    FORGET_PASSWORD_SCREEN_KEY_0 = (AppiumBy.ACCESSIBILITY_ID, "0")
    FORGET_PASSWORD_SCREEN_KEY_1 = (AppiumBy.ACCESSIBILITY_ID, "1")
    OTP = (AppiumBy.XPATH,'//android.view.View[@content-desc="ادخل رمز التحقق"]/preceding-sibling::android.view.View[1]')
    OTP_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    KYC_HEADER = (AppiumBy.ACCESSIBILITY_ID, "إنشاء حساب")
    OTP_ERROR_MESSAGE = (AppiumBy.XPATH, "//android.view.View[@content-desc='رمز التحقق غير صحيح']")
    RESEND_OTP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "إعادة ارسال الرمز")
    SUCCESS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "تسجيل الدخول")

    def __init__(self, driver):
        self.driver = driver

    # -------------------
    # Actions
    # -------------------
    def click_welcomescreen_next_buttons(self, times=3):
        user_present = wait_for_element_visibility(self.driver,self.USER_IMAGE,timeout=5,soft_fail=True)
        if user_present:
            return
        for i in range(times):
            next_button = wait_for_element_visibility(self.driver,self.NEXT_BUTTON,timeout=10,soft_fail=True)
            if next_button:
                time.sleep(2)
                next_button.click()

    def select_user(self):
        user_element = wait_for_element_visibility(self.driver, self.USER_IMAGE, 10)
        if user_element:
            user_element.click()

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

    def click_CANT_LOGIN_BUTTON(self):
        continue_button = wait_for_element_visibility(self.driver, self.CANT_LOGIN_BUTTON, 20)
        if continue_button:
            continue_button.click()

    def click_on_forgot_link(self):
        forgot_link = wait_for_element_visibility(self.driver, self.FORGOT_LINK, 10)
        if forgot_link:
            forgot_link.click()

    # def click_forgot_password_popup_button(self):
    #     popup_btn = wait_for_element_visibility(self.driver, self.FORGOT_POPUP_BUTTON, 10)
    #     if popup_btn:
    #         popup_btn.click()

    def enter_otp_code(self):
        otp_element = wait_for_element_visibility(self.driver, self.OTP, 10)
        if otp_element:
            otp_code = otp_element.get_attribute("content-desc")
            otp_input = wait_for_element_visibility(self.driver,self.OTP_INPUT, 10)
            otp_input.click()
            otp_input.send_keys(otp_code)
            time.sleep(1)

    def enter_password(self):
        wait_for_element_visibility(self.driver, self.FORGET_PASSWORD_SCREEN_HEADER , 20)
        zero_button = wait_for_element_visibility(self.driver, self.FORGET_PASSWORD_SCREEN_KEY_0, 10)
        if zero_button:
            for _ in range(6):
                zero_button.click()
                time.sleep(0.3)
        else:
            print("Key '0' not found on password screen.")

    # def enter_password(self, key_locator):
    #     """Enter 6-digit password by clicking same key"""
    #
    #     wait_for_element_visibility(self.driver, self.FORGET_PASSWORD_SCREEN_HEADER, 20)
    #
    #     key_button = wait_for_element_visibility(self.driver, key_locator, 10)
    #
    #     if key_button:
    #         for _ in range(6):
    #             key_button.click()
    #             time.sleep(0.3)
    #         print(" Password entered")
    #     else:
    #         print(" Password key not found")

    def input_expired_otp(self, otp_value="1234"):
        otp_input = wait_for_element_visibility(self.driver, self.OTP_INPUT, 10)
        otp_input.send_keys(otp_value)
        try:
            self.driver.hide_keyboard()
            self.driver.press_keycode(AndroidKey.ENTER)
        except:
            pass

    def click_resend_otp_button(self):
        resend_btn = wait_for_element_visibility(self.driver, self.RESEND_OTP_BUTTON, 10)
        if resend_btn:
            resend_btn.click()

    def enter_incorrect_otp(self, otp_value="1111"):
        otp_input = wait_for_element_visibility(self.driver, self.OTP_INPUT, 10)
        otp_input.send_keys(otp_value)
        try:
            self.driver.hide_keyboard()
            self.driver.press_keycode(AndroidKey.ENTER)
        except:
            pass

    def verify_otp_expired_message(self):
        error_el = wait_for_element_visibility(self.driver, self.OTP_ERROR_MESSAGE, 10)
        assert error_el is not None, "OTP expired message not found"

    def verify_incorrect_otp_error(self):
        error_el = wait_for_element_visibility(self.driver, self.OTP_ERROR_MESSAGE, 10)
        assert error_el is not None, "Incorrect OTP error not found"

    def click_on_success_button(self):
        success_btn = wait_for_element_visibility(self.driver, self.SUCCESS_BUTTON, 10)
        if success_btn:
            success_btn.click()
