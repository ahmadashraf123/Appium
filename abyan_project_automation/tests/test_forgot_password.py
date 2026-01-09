import time


import utils # For password generation and storage

from abyan_project_automation.src.andriod.pages.forgot_password_page import ForgotPassword
from abyan_project_automation.src.andriod.pages.login_page import LoginPage
from abyan_project_automation.src.utils.password_utils import get_last_saved_password, save_credentials_to_csv


 # Case 1: Successful reset with valid OTP
def test_forgot_password_with_valid_phone_number_and_otp(driver):
    forgot_page = ForgotPassword(driver)
    forgot_page.click_welcomescreen_next_buttons()
    forgot_page.select_user()
    forgot_page.enter_phone_number(584292929)
    forgot_page.click_continue()
    forgot_page.click_CANT_LOGIN_BUTTON()
    forgot_page.click_on_forgot_link()
    forgot_page.enter_otp_code()
    forgot_page.enter_password()
    forgot_page.click_on_success_button()

 # Case 2: OTP expired scenario
def test_forgot_password_with_expired_otp(driver):
    forgot_page = ForgotPassword(driver)
    forgot_page.click_welcomescreen_next_buttons()
    forgot_page.select_user()
    forgot_page.enter_phone_number(584292929)
    forgot_page.click_continue()
    forgot_page.click_CANT_LOGIN_BUTTON()
    forgot_page.click_on_forgot_link()
    time.sleep(65)  # Wait for OTP expiry
    forgot_page.input_expired_otp()
    forgot_page.verify_otp_expired_message()

 # Case 3: Request new OTP after expiry and reset password
def test_forgot_password_request_new_otp_after_expiry(driver):
    forgot_page = ForgotPassword(driver)
    forgot_page.click_welcomescreen_next_buttons()
    forgot_page.select_user()
    forgot_page.enter_phone_number(584292929)
    forgot_page.click_continue()
    forgot_page.click_CANT_LOGIN_BUTTON()

    forgot_page.click_on_forgot_link()
    time.sleep(65)
    forgot_page.click_resend_otp_button()
    forgot_page.enter_otp_code()  # Enter new OTP
    forgot_page.enter_password()
    forgot_page.click_on_success_button()

 # Case 4: Invalid OTP scenario
def test_forgot_password_with_invalid_otp(driver):
    forgot_page = ForgotPassword(driver)
    forgot_page.click_welcomescreen_next_buttons()
    forgot_page.select_user()
    forgot_page.enter_phone_number(584292929)
    forgot_page.click_continue()
    forgot_page.click_CANT_LOGIN_BUTTON()
    forgot_page.click_on_forgot_link()
    forgot_page.enter_incorrect_otp()
    forgot_page.verify_incorrect_otp_error()

 # Case 5: Login successfully with new password after forgot flow
def test_login_success_with_new_password_after_forgot(driver):
    forgot_page = ForgotPassword(driver)
    forgot_page.click_welcomescreen_next_buttons()
    forgot_page.select_user()
    forgot_page.enter_phone_number(584292929)
    forgot_page.click_continue()
    forgot_page.click_CANT_LOGIN_BUTTON()
    forgot_page.click_on_forgot_link()
    forgot_page.enter_otp_code()
    forgot_page.enter_password()
    forgot_page.click_on_success_button()
    login_page = LoginPage(driver)
    login_page.enter_phone_number(584292929)
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.is_login_successful()
