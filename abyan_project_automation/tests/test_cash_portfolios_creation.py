import time

from abyan_project_automation.src.andriod.pages.cash_portfolios_creation_page import CreateCashPortfolios
from abyan_project_automation.src.andriod.pages.kyc_flow_page import KYCFlow
from abyan_project_automation.src.andriod.pages.login_page import LoginPage
from abyan_project_automation.src.constants.credentials import custom_category_name
from abyan_project_automation.src.utils.driver_factory import create_driver
from abyan_project_automation.src.utils.randomdatagenerator import RandomDataGenerator


def test_Create_Custom_Cash_category_with_goal_amount():
    """" verify that user can create custom cash category if he already has custom cash portfolio """
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("567876544")
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    holistic_page = CreateCashPortfolios(driver)
    holistic_page.click_on_cash_tab_and_proceed_next_screen()
    holistic_page.click_on_categories_section()
    holistic_page.click_on_create_category_button()
    holistic_page.click_on_Custom_Category_portfolio_and_proceed()
    holistic_page.select_field_and_input_portfolio_name_and_proceed()
    holistic_page.input_amount_for_category_and_proceed()
    holistic_page.click_create_category_button_and_proceed()
    holistic_page.tap_back_button()



def test_Create_pre_define_Cash_category_with_goal_amount():
    """" verify that user can create predefined cash category portfolio with goal amount """
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("567876544")
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    holistic_page = CreateCashPortfolios(driver)
    holistic_page.click_on_cash_tab_and_proceed_next_screen()
    holistic_page.click_on_categories_section()
    holistic_page.click_on_create_category_button()
    holistic_page.click_on_pre_define_portfolio_and_proceed()
    holistic_page.input_amount_for_category_and_proceed()
    holistic_page.click_create_category_button_and_proceed()
    holistic_page.tap_back_button()



def test_Create_Custom_Cash_category_without_goal_amount():
    """" verify that user can create custom cash category without goal amount """
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("567876544")
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    holistic_page = CreateCashPortfolios(driver)
    holistic_page.click_on_cash_tab_and_proceed_next_screen()
    holistic_page.click_on_categories_section()
    holistic_page.click_on_create_category_button()
    holistic_page.click_on_Custom_Category_portfolio_and_proceed()
    holistic_page.select_field_and_input_portfolio_name_and_proceed()
    holistic_page.click_Skip_button_and_proceed()
    holistic_page.tap_back_button()





def test_verify_pre_defined_category_on_home_screen():

    """verify redirection to cash home screen from holistic home screen
       find predefined cash category on holistic home screen verify redirection to predefined cash category home screen """
    category_name = "زواج"
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("532454578")
    login_page.click_continue()
    login_page.enter_password()
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    holistic_page = CreateCashPortfolios(driver)
    holistic_page.verify_cash_portfolio_home_screen()
    holistic_page.redirect_holistic_screen_and_verify_user_is_on_holistic_screen()
    holistic_page.click_on_pre_define_category_and_verify_home_screen(category_name)
    holistic_page.verify_pre_define_category_home_screen(category_name)






