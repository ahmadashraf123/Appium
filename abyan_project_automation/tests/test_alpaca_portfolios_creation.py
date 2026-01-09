from abyan_project_automation.src.andriod.pages.alpaca_portfolios_creation_page import CreateAlPacaPortfolios
from abyan_project_automation.src.andriod.pages.login_page import LoginPage
from abyan_project_automation.src.utils.driver_factory import create_driver


def test_alpaca_growth_portfolio_creation():
    """ alpaca growth portfolio creation invest for goal"""
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("536982214")
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    holistic_page = CreateAlPacaPortfolios(driver)
    holistic_page.scroll_and_click_create_portfolio_button()
    holistic_page.click_on_alpaca_portfolio()
    holistic_page.select_growth_portfolio_to_create_and_proceed()
    holistic_page.click_create_portfolio_button()
    holistic_page.click_on_portfolio_goal_target()
    holistic_page.select_goal_icon_proceed()
    holistic_page.enter_portfolio_goal_name_and_press_next()
    login_page.enter_otp_code()
    holistic_page.click_portfolio_success_button()

def test_alpaca_moderate_portfolio_creation():
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("536982214")
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    holistic_page = CreateAlPacaPortfolios(driver)
    holistic_page.scroll_and_click_create_portfolio_button()
    holistic_page.click_on_alpaca_portfolio()
    holistic_page.select_moderate_portfolio()
    holistic_page.click_create_portfolio_button()
    holistic_page.click_on_portfolio_goal_target()
    holistic_page.select_goal_icon_proceed()
    holistic_page.enter_portfolio_goal_name_and_press_next()
    login_page.enter_otp_code()
    # holistic_page.click_portfolio_success_button()

def test_alpaca_conservative_portfolio_creation():
    """ alpaca conservative آمنة portfolio creation invest for goal"""
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("536982214")
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    holistic_page = CreateAlPacaPortfolios(driver)
    holistic_page.scroll_and_click_create_portfolio_button()
    holistic_page.click_on_alpaca_portfolio()
    holistic_page.select_conservative_portfolio()
    holistic_page.click_create_portfolio_button()
    holistic_page.click_on_portfolio_goal_target()
    holistic_page.select_goal_icon_proceed()
    holistic_page.enter_portfolio_goal_name_and_press_next()
    login_page.enter_otp_code()
    # holistic_page.click_portfolio_success_button()
    # holistic_page.holistic_screen_scroll_until_end()

def test_alpaca_growth_portfolio_creation_invest_for_children():
    """ alpaca growth portfolio creation invest for children"""
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("536982214")
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    holistic_page = CreateAlPacaPortfolios(driver)
    holistic_page.scroll_and_click_create_portfolio_button()
    holistic_page.click_on_alpaca_portfolio()
    holistic_page.select_growth_portfolio_to_create_and_proceed()
    holistic_page.click_create_portfolio_button()
    holistic_page.click_on_portfolio_children_target()
    holistic_page.select_children_icon_proceed()
    holistic_page.enter_portfolio_goal_name_and_press_next()
    login_page.enter_otp_code()
    # holistic_page.click_portfolio_success_button()

def test_alpaca_moderate_portfolio_creation_invest_for_children():
    """ alpaca moderate portfolio creation invest for children"""
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("536982214")
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    holistic_page = CreateAlPacaPortfolios(driver)
    holistic_page.scroll_and_click_create_portfolio_button()
    holistic_page.click_on_alpaca_portfolio()
    holistic_page.select_moderate_portfolio()
    holistic_page.click_create_portfolio_button()
    holistic_page.click_on_portfolio_children_target()
    holistic_page.select_children_icon_proceed()
    holistic_page.enter_portfolio_goal_name_and_press_next()
    login_page.enter_otp_code()
    # holistic_page.click_portfolio_success_button()










