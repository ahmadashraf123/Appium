import time

from abyan_project_automation.src.andriod.pages.change_phone_number_page import ChangePhoneNumber
from abyan_project_automation.src.andriod.pages.login_page import LoginPage
from abyan_project_automation.src.constants.credentials import id_number, wrong_N_ID_number


def test_successful_change_phone_number(driver):
    """Verify that the user can successfully change the phone number using valid credentials and OTPs."""
    change_phone_number_page = ChangePhoneNumber(driver)
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    old_number = "533193463"  # Step 2: Enter old number for login and make sure user already completed KYC
    login_page.enter_phone_number(old_number)
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_redirect_to_home_screen()
    change_phone_number_page.click_SETTING_BUTTON()
    change_phone_number_page.click_ACCOUNT_BUTTON()
    change_phone_number_page.click_ABOUT_NUMBER()
    change_phone_number_page.click_CHANGE_PHONE_NO_INPUT_FIELD()
    change_phone_number_page.click_CHANGE_PHONE_NO_INPUT_FIELD()
    change_phone_number_page.enter_new_phone_number()
    change_phone_number_page.click_continue_button()
    change_phone_number_page.enter_otp_code()
    change_phone_number_page.enter_Nid_number(id_number)
    change_phone_number_page.click_dob_field()
    change_phone_number_page.click_miladi_tab()
    change_phone_number_page.select_dob("2006", "مارس", "10")
    change_phone_number_page.click_confirm_dob_from_bottom_sheet()
    change_phone_number_page.click_continue_button_after_dob_selection()
    change_phone_number_page.enter_Absher_otp_code()
    change_phone_number_page.click_Home_button()



def test_change_phone_number_invalid_nid(driver):
    """Verify that the user cannot change the phone number using a valid phone number, valid password, valid OTP, and invalid NID."""
    change_phone_number_page = ChangePhoneNumber(driver)
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    old_number = "533193463"  # Step 2: Enter old number for login and make sure user already completed KYC
    login_page.enter_phone_number(old_number)
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_redirect_to_home_screen()
    change_phone_number_page.click_SETTING_BUTTON()
    change_phone_number_page.click_ACCOUNT_BUTTON()
    change_phone_number_page.click_ABOUT_NUMBER()
    change_phone_number_page.click_CHANGE_PHONE_NO_INPUT_FIELD()
    change_phone_number_page.click_CHANGE_PHONE_NO_INPUT_FIELD()
    change_phone_number_page.enter_new_phone_number()
    change_phone_number_page.click_continue_button()
    change_phone_number_page.enter_otp_code()
    change_phone_number_page.enter_Nid_number(wrong_N_ID_number)
    change_phone_number_page.click_dob_field()
    change_phone_number_page.click_miladi_tab()
    change_phone_number_page.select_dob("2006", "مارس", "10")
    change_phone_number_page.click_confirm_dob_from_bottom_sheet()
    change_phone_number_page.click_continue_button_after_dob_selection()
    assert change_phone_number_page.assert_wrong_id_error_is_shown()


def test_change_phone_number_already_registered(driver):
    """
    Verify that the user cannot change the phone number to a phone number that is already registered.
    """
    change_phone_number_page = ChangePhoneNumber(driver)
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    old_number = "533193463"  # Step 2: Enter old number for login and make sure user already completed KYC
    login_page.enter_phone_number(old_number)
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_redirect_to_home_screen()
    change_phone_number_page.click_SETTING_BUTTON()
    change_phone_number_page.click_ACCOUNT_BUTTON()
    change_phone_number_page.click_ABOUT_NUMBER()
    change_phone_number_page.click_CHANGE_PHONE_NO_INPUT_FIELD()
    change_phone_number_page.click_CHANGE_PHONE_NO_INPUT_FIELD()
    registered_phone_no ="531451377"
    change_phone_number_page.enter_new_phone_number(registered_phone_no)
    change_phone_number_page.click_continue_button()
    change_phone_number_page.enter_otp_code()
    change_phone_number_page.enter_Nid_number(id_number)
    change_phone_number_page.click_dob_field()
    change_phone_number_page.click_miladi_tab()
    change_phone_number_page.select_dob("2006", "مارس", "10")
    change_phone_number_page.click_confirm_dob_from_bottom_sheet()
    change_phone_number_page.click_continue_button_after_dob_selection()
    change_phone_number_page.enter_Absher_otp_code()
    assert change_phone_number_page.verify_phone_number_already_exists_error_is_shown()



