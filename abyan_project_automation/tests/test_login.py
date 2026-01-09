
import time

from abyan_project_automation.src.andriod.pages.login_page import LoginPage
from abyan_project_automation.src.constants.credentials import NON_PREMIUM_PHONE, password, SIGNUP_FLOW_PHONE, \
    INCORRECT_PASSWORD_PHONE, PREMIUM_PHONE


def test_login_with_valid_phone_password_otp(driver):
    """Verify that the user can successfully log in using a valid phone number, password, and OTP, and is redirected to the home screen."""
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number(567876544)
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_redirect_to_home_screen()
    login_page.handle_enable_notifications_if_displays()
    login_page.handle_premium_pop_up_if_displays()


def test_login_with_valid_number_invalid_password(driver):
    """Verify that the user cannot log in with a valid phone number and invalid password, and receives an error message indicating incorrect password."""
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number(567876544)
    login_page.click_continue()
    login_page.enter_incorrect_password()
    login_page.verify_error_incorrect_password()

def test_login_with_valid_number_password_and_invalid_otp(driver):
    """Verify that the user cannot log in with a valid phone number, password, and invalid OTP, and receives an error message indicating invalid OTP."""
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number(567876544)
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_invalid_otp()
    login_page.verify_error_invalid_otp()

def test_login_with_expired_otp(driver):
    """Verify that the user cannot log in using a valid phone number and password if the OTP is retried after 1 minute, and receives an OTP expired message."""
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number(PREMIUM_PHONE)
    login_page.click_continue()
    login_page.enter_password()
    time.sleep(70)  # wait 1 minute to simulate OTP expiration
    login_page.enter_otp_code()
    login_page.verify_error_otp_expired()


def test_login_request_new_otp_after_expiration(driver):
    """Verify that the user can request a new OTP after the previous OTP has expired, and can log in successfully using the new OTP."""
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number(NON_PREMIUM_PHONE)
    login_page.click_continue()
    login_page.enter_password()
    time.sleep(60)  # previous OTP expired
    login_page.request_new_otp()
    login_page.enter_otp_code()  # enter new valid OTP
    login_page.verify_redirect_to_home_screen()


