from abyan_project_automation.src.andriod.pages.alpaca_and_jadwa_portfolio_to_portfolio_transfer_page import \
    WithdrawalPortfolioToPortfolio
from abyan_project_automation.src.andriod.pages.cash_category_to_category_transfer_page import \
    CashCategoryToCategoryTransfer
from abyan_project_automation.src.andriod.pages.deposit_cases_investment_portfolios_page import \
    DepositInvestmentPortfolio
from abyan_project_automation.src.andriod.pages.investment_portfolio_withdrawal_to_bank_page import \
    WithdrawalInvestmentPortfolios
from abyan_project_automation.src.andriod.pages.login_page import LoginPage
from abyan_project_automation.src.constants.credentials import password


def test_cash_category_to_category_transfer(driver):
    """All Cases of Cash and Categories transfer"""
    # Initialize page objects
    login_page = LoginPage(driver)
    cash_category_to_category_transfer = CashCategoryToCategoryTransfer(driver)
    withdrawal_page = WithdrawalPortfolioToPortfolio(driver)
    settings_page = WithdrawalInvestmentPortfolios(driver)
    investment_deposit = DepositInvestmentPortfolio(driver)
    investment_portfolio_withdrawal = WithdrawalInvestmentPortfolios(driver)
    # Step 1: Login
    login_page.click_welcomescreen_next_buttons()
    login_page.select_user()
    login_page.enter_phone_number("587423695")
    login_page.click_continue()
    login_page.enter_password(password)
    # OTP entry - will skip if OTP screen not displayed (some sessions don't require OTP)
    login_page.enter_otp_code()
    login_page.verify_holistic_home_screen()
    investment_deposit.click_on_respective_single_portfolio_and_verify_home_screen("مدخراتك")
    cash_category_to_category_transfer.click_on_transfer_button()
    investment_deposit.click_on_respective_single_portfolio_and_verify_home_screen("travel")
    investment_deposit.verify_category_clicked("travel")
    investment_deposit.click_on_respective_single_portfolio_and_verify_home_screen("مدخراتك")
    investment_deposit.verify_category_clicked("مدخراتك")
    # Step 3: Enter withdrawal amount
    withdrawal_page.click_on_input_field()
    withdrawal_page.input_hundred()
    # Step 4: Continue to confirmation
    withdrawal_page.confirm_transaction()
    # Step 5: Confirm transaction
    withdrawal_page.complete_transaction()
    settings_page.click_on_home_button()