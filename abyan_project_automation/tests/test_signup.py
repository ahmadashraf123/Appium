# tests/test_signup.py
import time

from abyan_project_automation.src.andriod.pages.signup_page import SignUpPage
from abyan_project_automation.src.utils.randomdatagenerator import RandomDataGenerator


def test_signup_with_valid_phone_otp_and_password(driver):
    """Verify that the user can successfully sign up using a valid phone number, OTP, and password,
    and is redirected to the KYC NID screen."""

    signup_page = SignUpPage(driver)
    signup_page.click_welcomescreen_next_buttons()
    signup_page.select_user()
    signup_page.enter_phone_number(RandomDataGenerator.generate_valid_saudi_number())
    signup_page.click_continue()
    signup_page.enter_otp_code()
    signup_page.enter_password()
    signup_page.verify_redirection_to_KYC()

def test_signup_with_valid_phone_number_invalid_otp(driver):
    """Verify that the user cannot sign up using a valid phone number and invalid OTP,
    and receives an error message indicating invalid OTP."""
    signup_page = SignUpPage(driver)
    signup_page.click_welcomescreen_next_buttons()
    signup_page.select_user()
    signup_page.enter_phone_number(RandomDataGenerator.generate_valid_saudi_number())
    signup_page.click_continue()
    signup_page.input_invalid_otp()
    signup_page.verify_otp_error_massage()

def test_signup_with_expired_otp(driver):
    """Verify that the user cannot sign up using a valid phone number if the OTP is retried after 1 minute,
    and receives an OTP expired message."""
    signup_page = SignUpPage(driver)
    signup_page.click_welcomescreen_next_buttons()
    signup_page.select_user()
    signup_page.enter_phone_number(RandomDataGenerator.generate_valid_saudi_number())
    signup_page.click_continue()
    time.sleep(61)  # simulate OTP expiration
    signup_page.enter_otp_code()
    signup_page.verify_otp_error_massage()  # treat expired OTP as invalid OTP

def test_signup_with_request_new_otp_after_expiration(driver):
    """Verify that the user can request a new OTP after the previous OTP has expired
    and successfully complete sign-up."""
    signup_page = SignUpPage(driver)
    signup_page.click_welcomescreen_next_buttons()
    signup_page.select_user()
    signup_page.enter_phone_number(RandomDataGenerator.generate_valid_saudi_number())
    signup_page.click_continue()
    time.sleep(60)  # simulate OTP expiration
    signup_page.request_new_otp()  # You need to implement this method in SignUpPage
    signup_page.enter_otp_code()
    signup_page.enter_password()
    signup_page.verify_redirection_to_KYC()

def test_signup_with_already_used_number_redirect_to_password_screen(driver):
    """Verify that the user is redirected to the password screen
    when attempting to sign up with a phone number that is already registered."""
    signup_page = SignUpPage(driver)
    signup_page.click_welcomescreen_next_buttons()
    signup_page.select_user()
    signup_page.enter_phone_number(RandomDataGenerator.generate_used_saudi_number())  # implement generator for used number
    signup_page.click_continue()
    signup_page.verify_password_screen()

