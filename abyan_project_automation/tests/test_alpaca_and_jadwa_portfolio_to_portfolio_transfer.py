from abyan_project_automation.src.andriod.pages.alpaca_and_jadwa_portfolio_to_portfolio_transfer_page import \
    WithdrawalPortfolioToPortfolio
from abyan_project_automation.src.andriod.pages.deposit_cases_investment_portfolios_page import \
    DepositInvestmentPortfolio
from abyan_project_automation.src.andriod.pages.investment_portfolio_withdrawal_to_bank_page import \
    WithdrawalInvestmentPortfolios
from abyan_project_automation.src.andriod.pages.login_page import LoginPage


def test_transfer_portfolio_to_portfolio(driver):

    """All Cases of jadwa and investment portfolio to portfolio transfer"""
    # Initialize page objects
    login_page = LoginPage(driver)
    withdrawal_page = WithdrawalPortfolioToPortfolio(driver)
    settings_page = WithdrawalInvestmentPortfolios(driver)
    investment_deposit = DepositInvestmentPortfolio(driver)
    investment_portfolio_withdrawal = WithdrawalInvestmentPortfolios(driver)
    # Step 1: Login
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("587423695")
    login_page.click_continue()
    login_page.enter_password()
    # OTP entry - will skip if OTP screen not displayed (some sessions don't require OTP)
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    # Step 2: Navigate to wallet transfer
    settings_page.click_on_settings_button()
    settings_page.click_on_orders_tab()
    withdrawal_page.click_on_wallet_transfer_option()
    investment_deposit.click_on_respective_portfolio_and_verify_home_screen("growth")
    investment_deposit.click_on_respective_portfolio_and_verify_home_screen("moderate")
    # # Step 3: Enter withdrawal amount
    withdrawal_page.click_on_input_field()
    withdrawal_page.input_hundred()
    # Step 4: Continue to confirmation
    withdrawal_page.confirm_transaction()
    # Step 5: Confirm transaction
    withdrawal_page.complete_transaction()
    from abyan_project_automation.src.constants.credentials import PIN
    withdrawal_page.enter_transaction_pin(PIN)
    login_page.enter_otp_code()
    settings_page.click_on_home_button()
#   Cancel transfer request
    investment_portfolio_withdrawal.click_on_settings_button()
    investment_portfolio_withdrawal.click_on_orders_tab()
    investment_portfolio_withdrawal.click_on_cancel_existing_transaction()
    investment_portfolio_withdrawal.click_on_continue_button()
    investment_portfolio_withdrawal.click_on_delivery_between_guards()
    investment_portfolio_withdrawal.click_on_cancel_withdrawal_button()
    login_page.enter_password()
    login_page.enter_otp_code()
    investment_portfolio_withdrawal.click_on_home_button()







