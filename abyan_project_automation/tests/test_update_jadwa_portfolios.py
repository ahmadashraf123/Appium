from abyan_project_automation.src.andriod.pages.login_page import LoginPage
from abyan_project_automation.src.andriod.pages.update_jadwa_portfolios_page import UpdateJadwaPortfolios
from abyan_project_automation.src.constants.credentials import password
from abyan_project_automation.src.utils.driver_factory import create_driver


class UpdateAlPacaPortfolios:
    pass


def test_update_jadwa_portfolio_name():
    """Verify successfully update the jadwa portfolio name and display the new name on the Portfolio Home Screen."""
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("535553454")
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    update_jadwa_page = UpdateJadwaPortfolios(driver)
    update_jadwa_page.scroll_and_select_portfolio("beenish")
    update_jadwa_page.verify_correctly_redirect_on_respective_home_screen("beenish")
    update_alpaca_page = UpdateAlPacaPortfolios(driver)
    update_alpaca_page.click_on_update_button()
    update_alpaca_page.select_update_button_and_proceed()
    update_jadwa_page.click_on_edit_portfolio_tab()
    update_jadwa_page.update_and_verify_portfolio_name()

# def test_update_jadwa_portfolio_icon():
#     """Verify successfully update the jadwa portfolio Goal icon and display new goal icon on the Portfolio Home Screen."""
#     driver = create_driver()
#     login_page = LoginPage(driver)
#     login_page.click_welcomescreen_next_buttons()
#     login_page.select_user()
#     login_page.enter_phone_number("535553454")
#     login_page.click_continue()
#     login_page.enter_password(password)
#     # login_page.enter_otp_code()
#     login_page.verify_holistic_home_screen()
#     update_jadwa_page = UpdateJadwaPortfolios(driver)
#     update_jadwa_page.scroll_and_select_portfolio("beenish")
#     update_jadwa_page.verify_correctly_redirect_on_respective_home_screen("beenish")
#     update_alpaca_page = UpdateAlPacaPortfolios(driver)
#     update_alpaca_page.click_on_update_button()
#     update_alpaca_page.select_update_button_and_proceed()
#     update_jadwa_page.click_on_edit_portfolio_tab()
#     update_jadwa_page.update_and_verify_portfolio_name_and_icon()

def test_update_jadwa_portfolio_():
    """Verify successfully hide the jadwa portfolio and ensure it is not visible on the Holistic Home Screen."""
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("535553454")
    login_page.click_continue()
    login_page.enter_password(password)
    # login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    update_jadwa_page = UpdateJadwaPortfolios(driver)
    update_jadwa_page.scroll_and_select_portfolio("beenish")
    update_jadwa_page.verify_correctly_redirect_on_respective_home_screen("beenish")
    update_alpaca_page = ChangeInvestmentPortfoliosType(driver)
    update_alpaca_page.click_on_update_button()
    update_alpaca_page.select_update_button_and_proceed()
    update_jadwa_page.click_on_the_hide_portfolio_toggle_button_and_redirect_holistic_home()
    update_jadwa_page.verify_portfolio_not_visible_on_holistic_home("beenish")

# def test_update_jadwa_portfolio_():
#     """Verify successfully remove the jadwa portfolio from the hidden listing and display it again on the Holistic Home Screen."""
#     driver = create_driver()
#     login_page = LoginPage(driver)
#     login_page.click_welcomescreen_next_buttons()
#     login_page.select_user()
#     login_page.enter_phone_number("535553454")
#     login_page.click_continue()
#     login_page.enter_password(password)
#     # login_page.enter_otp_code()
#     login_page.verify_holistic_home_screen()
#     update_jadwa_page = UpdateJadwaPortfolios(driver)
#     update_jadwa_page.scroll_and_select_portfolio("beenish")
#     update_jadwa_page.verify_correctly_redirect_on_respective_home_screen("beenish")
#     update_alpaca_page = UpdateAlPacaPortfolios(driver)
#     update_alpaca_page.click_on_update_button()
#     update_alpaca_page.select_update_button_and_proceed()
#     update_jadwa_page.click_on_the_hide_portfolio_toggle_button_and_redirect_holistic_home()
#     update_jadwa_page.verify_portfolio_not_visible_on_holistic_home("beenish")
#     update_jadwa_page.click_on_the_service_tab_and_proceed()
#     update_jadwa_page.scroll_down_on_service_screen_and_click_on_portfolio_management_option()
#     update_jadwa_page.scroll_down_to_find_hidden_portfolio_and_perform_click("beenish")
#     update_jadwa_page.click_on_the_toggle_button_to_off_the_toggle_and_remove_portfolio_from_hide_listing()
#     update_jadwa_page.click_on_the_back_button_to_redirect_the_portfolio_management_listing()
#     update_jadwa_page.click_back_button_and_move_to_service_home_screen()
#     update_jadwa_page.click_on_holistic_tab_and_proceed()
#     update_jadwa_page.verify_respective_portfolio_successfully_unhide("beenish")

def test_update_jadwa_portfolio_():
    """Verify successfully hide the jadwa portfolio value on the Portfolio Home Screen"""
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("584243165")
    login_page.click_continue()
    login_page.enter_password(password)
    # login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    update_jadwa_page = UpdateJadwaPortfolios(driver)
    update_jadwa_page.scroll_and_select_portfolio("beenish")
    update_jadwa_page.verify_redirect_on_respective_home_screen("beenish")
    update_alpaca_page = ChangeInvestmentPortfoliosType(driver)
    update_alpaca_page.click_on_update_button()
    update_jadwa_page.click_on_hide_portfolio_value_option()
    update_jadwa_page.verify_portfolio_values_hidden()

def test_update_jadwa_portfolio_():
    """Verify successfully unhide the jadwa portfolio value and ensure the value in digits is displayed correctly on the Portfolio Home Screen."""
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("584243165")
    login_page.click_continue()
    login_page.enter_password(password)
    # login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    update_jadwa_page = UpdateJadwaPortfolios(driver)
    update_jadwa_page.scroll_and_select_portfolio("beenish")
    update_jadwa_page.verify_redirect_on_respective_home_screen("beenish")
    update_alpaca_page = ChangeInvestmentPortfoliosType(driver)
    update_alpaca_page.click_on_update_button()
    update_jadwa_page.click_on_hide_portfolio_value_option()
    update_jadwa_page.verify_portfolio_values_hidden()
    update_alpaca_page.click_on_update_button()
    update_jadwa_page.click_on_unhide_portfolio_value_option()
    update_jadwa_page.verify_portfolio_values_un_hidde()


















