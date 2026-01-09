from abyan_project_automation.src.andriod.pages.deposit_cases_jadwa_portfolio_page import DepositJadwaPortfolio
from abyan_project_automation.src.andriod.pages.login_page import LoginPage
from abyan_project_automation.src.andriod.pages.update_jadwa_portfolios_page import UpdateJadwaPortfolios
from abyan_project_automation.src.constants.credentials import password
from abyan_project_automation.src.utils.driver_factory import create_driver


def test_deposit_jadwa_portfolio_with_mada_card_using_money_hash():

    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("518181810")
    login_page.click_continue()
    login_page.enter_password(password)
    # login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    update_jadwa_page = UpdateJadwaPortfolios(driver)
    deposit_in_jadwa = DepositJadwaPortfolio(driver)
    update_jadwa_page.scroll_and_select_portfolio("beenish")
    # update_jadwa_page.verify_correctly_redirect_on_respective_home_screen("beenish")
    deposit_in_jadwa.click_on_the_deposit_button()
    deposit_in_jadwa.click_on_payment_by_card_option()
    deposit_in_jadwa.click_on_input_field_to_enter_amount_and_proceed()
    deposit_in_jadwa.input_deposit_amount(1000)
    # deposit_in_jadwa.click_on_the_view_to_close_the_keyboard()
    deposit_in_jadwa.click_deposit_button()
    deposit_in_jadwa.click_on_payment_method_mada()
    deposit_in_jadwa.click_on_input_name_field_and_input_name()
    deposit_in_jadwa.click_on_screen_view_and_close_the_keyboard()
    deposit_in_jadwa.click_on_field_and_input_mada_card_number()
    deposit_in_jadwa.click_on_screen_view_and_close_the_keyboard()
    deposit_in_jadwa.click_field_and_input_expiry_month_info()
    deposit_in_jadwa.click_on_screen_view_and_close_the_keyboard()
    deposit_in_jadwa.click_on_field_and_input_expiry_year_info()
    deposit_in_jadwa.click_on_screen_view_and_close_the_keyboard()
    deposit_in_jadwa.click_on_cvv_and_input_number()
    deposit_in_jadwa.click_on_screen_view_and_close_the_keyboard()
    deposit_in_jadwa.click_on_pay_button()

# def test_deposit_jadwa_portfolio_with_visa_card_using_money_hash():
#
#     driver = create_driver()
#     login_page = LoginPage(driver)
#     login_page.click_welcomescreen_next_buttons()
#     login_page.select_user()
#     login_page.enter_phone_number("518181810")
#     login_page.click_continue()
#     login_page.enter_password(password)
#     # login_page.enter_otp_code()
#     login_page.verify_holistic_home_screen()
#     update_jadwa_page = UpdateJadwaPortfolios(driver)
#     update_jadwa_page.scroll_and_select_portfolio("beenish")
#     update_jadwa_page.verify_correctly_redirect_on_respective_home_screen("beenish")
#     deposit_in_jadwa = DepositJadwaPortfolio(driver)
#     deposit_in_jadwa.click_on_the_deposit_button()
#     deposit_in_jadwa.click_on_payment_by_card_option()
#     deposit_in_jadwa.click_on_input_field_to_enter_amount_and_proceed()
#     deposit_in_jadwa.input_deposit_amount(1000)
#     # deposit_in_jadwa.click_on_the_view_to_close_the_keyboard()
#     deposit_in_jadwa.click_deposit_button()
#     deposit_in_jadwa.click_on_payment_method_mada()
#     deposit_in_jadwa.click_on_input_name_field_and_input_name()
#     deposit_in_jadwa.click_on_screen_view_and_close_the_keyboard()
#     deposit_in_jadwa.click_on_field_and_input_visa_card_number()
#     deposit_in_jadwa.click_on_screen_view_and_close_the_keyboard()
#     deposit_in_jadwa.click_field_and_input_expiry_month_info_for_visa()
#     deposit_in_jadwa.click_on_screen_view_and_close_the_keyboard()
#     deposit_in_jadwa.click_on_field_and_input_expiry_year_info_for_visa()
#     deposit_in_jadwa.click_on_screen_view_and_close_the_keyboard()
#     deposit_in_jadwa.click_on_cvv_and_input_number_for_visa()
#     deposit_in_jadwa.click_on_screen_view_and_close_the_keyboard()
#     deposit_in_jadwa.click_on_pay_button()
#
#





