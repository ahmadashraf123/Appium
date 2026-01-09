
from appium.webdriver.webdriver import WebDriver

from abyan_project_automation.src.andriod.pages.jadwa_portfolios_creation_page import CreateJadwaPortfolios
from abyan_project_automation.src.andriod.pages.login_page import LoginPage
from abyan_project_automation.src.constants.credentials import parent_jadwa
from abyan_project_automation.src.utils.driver_factory import create_driver


def test_create_jadwa_portfolios_for_invest_for_child():
    """Case 1: Create Jadwa Portfolios for Invest for Children"""
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number(parent_jadwa)
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    jadwa_portfolios_creation_page = CreateJadwaPortfolios(driver)
    jadwa_portfolios_creation_page.scroll_and_click_create_portfolio_button()
    jadwa_portfolios_creation_page.create_jadwa_portfolio()
    jadwa_portfolios_creation_page.click_create_jadwa_portfolio_button()
    jadwa_portfolios_creation_page.click_on_portfolio_target()
    jadwa_portfolios_creation_page.enter_portfolio_name_and_press_next()
    login_page.enter_otp_code()
    jadwa_portfolios_creation_page.click_portfolio_success_button()


def test_create_jadwa_portfolios_for_invest_of_goal():
    """Create Jadwa Portfolios for “Invest for Goal” """
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number(parent_jadwa)
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    jadwa_portfolios_creation_page = CreateJadwaPortfolios(driver)
    jadwa_portfolios_creation_page.scroll_and_click_create_portfolio_button()
    jadwa_portfolios_creation_page.create_jadwa_portfolio()
    jadwa_portfolios_creation_page.click_create_jadwa_portfolio_button()
    jadwa_portfolios_creation_page.click_on_portfolio_goal_target()
    jadwa_portfolios_creation_page.enter_portfolio_goal_name_and_press_next()
    login_page.enter_otp_code()
    jadwa_portfolios_creation_page.click_portfolio_success_button()


def test_verify_portfolios_home_redirection():
    """Verify that the user is redirected successfully to the Jadwa Portfolio Home Screen when clicking a Jadwa portfolio from the Holistic Home Screen."""
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number(parent_jadwa)
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    jadwa_portfolios_creation_page = CreateJadwaPortfolios(driver)
    jadwa_portfolios_creation_page.scroll_and_select_portfolio("Kevin")
    jadwa_portfolios_creation_page.verify_correctly_redirect_on_respective_home_screen("Kevin")
    jadwa_portfolios_creation_page.redirect_back_holistic_screen()
    jadwa_portfolios_creation_page.scroll_and_select_portfolio("Wendy")
    jadwa_portfolios_creation_page.verify_correctly_redirect_on_respective_home_screen("Wendy")
    jadwa_portfolios_creation_page.redirect_back_holistic_screen()
    jadwa_portfolios_creation_page.scroll_and_select_portfolio(" السوق السعودي")
    jadwa_portfolios_creation_page.verify_correctly_redirect_on_parent_portfolio_home_screen(" السوق السعودي")
    jadwa_portfolios_creation_page.redirect_back_holistic_screen()
    jadwa_portfolios_creation_page.holictic_screen_scroll_until_end()



