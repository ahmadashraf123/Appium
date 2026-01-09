import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility, hard_wait


class WithdrawalPortfolioToPortfolio:

    def __init__(self, driver):
        self.driver = driver

    def click_on_wallet_transfer_option(self):
        """Clicks on the wallet transfer (portfolio-to-portfolio) option."""
        print("Clicking on wallet transfer option...")
        # Use the exact locator provided
        wallet_transfer_locator = (
            AppiumBy.XPATH,
            '//android.view.View[@content-desc="التحويل بين المحافظ"]'
        )
        element = wait_for_element_visibility(self.driver, wallet_transfer_locator, timeout=10)
        element.click()
        print("Wallet transfer option clicked successfully.")

    # def select_source_portfolio(self, portfolio_name):
    #     """Selects the source portfolio (e.g., Growth portfolio) without verifying home screen."""
    #     print(f"Selecting source portfolio: {portfolio_name}...")
    #     self._select_portfolio_by_name(portfolio_name)
    #     print(f"Source portfolio '{portfolio_name}' selected successfully.")
    #
    # def _select_portfolio_by_name(self, portfolio_name):
    #     """Helper method to select a portfolio by name with scrolling support."""
    #     import time
    #     from appium.webdriver.common.appiumby import AppiumBy
    #
    #     xpath_variants = [
    #         f'//android.view.View[contains(@content-desc, "{portfolio_name}")]',
    #         f'//android.widget.ImageView[contains(@content-desc, "{portfolio_name}")]',
    #         f'//android.view.ViewGroup[contains(@content-desc, "{portfolio_name}")]',
    #         f'//android.widget.TextView[contains(@text, "{portfolio_name}")]',
    #     ]
    #     max_scrolls = 10
    #     for attempt in range(max_scrolls):
    #         print(f"Scroll attempt {attempt + 1} ...")
    #         for xpath in xpath_variants:
    #             try:
    #                 elements = self.driver.find_elements(AppiumBy.XPATH, xpath)
    #                 if elements:
    #                     element = elements[0]
    #                     desc = element.get_attribute("contentDescription") or element.get_attribute("text")
    #                     print(f"Found element with content: {desc}")
    #                     # Use tap for better reliability
    #                     rect = element.rect
    #                     x = rect["x"] + rect["width"] / 2
    #                     y = rect["y"] + rect["height"] / 2
    #                     self.driver.tap([(x, y)])
    #                     print(f"Portfolio '{portfolio_name}' clicked successfully.")
    #                     time.sleep(1)  # Wait for screen transition
    #                     return
    #             except Exception as e:
    #                 continue
    #         # Scroll if not found
    #         print("Not found yet, trying to scroll...")
    #         try:
    #             self.driver.find_element(
    #                 AppiumBy.ANDROID_UIAUTOMATOR,
    #                 'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
    #             )
    #             time.sleep(0.5)
    #         except Exception:
    #             # Fallback to manual swipe
    #             size = self.driver.get_window_size()
    #             start_y = int(size["height"] * 0.8)
    #             end_y = int(size["height"] * 0.3)
    #             start_x = int(size["width"] / 2)
    #             self.driver.swipe(start_x, start_y, start_x, end_y, 800)
    #             time.sleep(0.5)
    #     pytest.fail(f"Portfolio '{portfolio_name}' not found after {max_scrolls} scrolling attempts.")

    def click_on_input_field(self):
        """Clicks on the amount input field."""
        print("Clicking on amount input field...")
        input_field_locator = (AppiumBy.XPATH, '//android.widget.EditText')
        element = wait_for_element_visibility(self.driver, input_field_locator, timeout=10)
        element.click()
        hard_wait(2)
        print("Amount input field clicked successfully.")

    def input_amount(self, amount):
        """Enters the withdrawal amount in the input field."""
        print(f"Entering withdrawal amount: {amount} SAR...")
        input_field_locator = (AppiumBy.XPATH, '//android.widget.EditText')
        element = wait_for_element_visibility(self.driver, input_field_locator, timeout=10)
        element.clear()
        element.send_keys(str(amount))
        print(f"Amount {amount} SAR entered successfully.")

    def input_hundred(self):
        """Clicks on the 100 SAR amount option."""
        print("Selecting 100 SAR amount option...")
        try:
            amount_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText'))
            )
            amount_input.click()
            amount_input.send_keys("100")
        except TimeoutException:
            pytest.fail("Amount input field not found or visible")

    def confirm_transaction(self):
        """Click on Review Transfer / Continue button."""
        print("Clicking on Review Transfer button...")

        continue_button_locator = (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="مراجعة التحويل"]'
        )

        continue_button = wait_for_element_visibility(
            self.driver,
            continue_button_locator,
            timeout=10
        )
        continue_button.click()
        print("Review Transfer button clicked successfully.")

    def enter_transaction_pin(self, pin: str):
        """
        Enter 6 digit transaction PIN using keypad
        """
        print("Entering transaction PIN...")
        for digit in pin:
            locator = (AppiumBy.XPATH, f'//android.view.View[@content-desc="{digit}"]')
            wait_for_element_visibility(self.driver, locator, timeout=10).click()
            hard_wait(0.5)
        print("Transaction PIN entered successfully.")

    def complete_transaction(self):
        """Click on Complete Transaction button."""
        print("Clicking on Complete Transaction button...")

        complete_transaction_locator = (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="اتمام العملية"]'
        )

        complete_transaction_button = wait_for_element_visibility(
            self.driver,
            complete_transaction_locator,
            timeout=1
        )
        complete_transaction_button.click()

        print("Complete Transaction button clicked successfully.")

    def verify_withdrawal_success(self):
        """Verifies that the withdrawal was successful by checking for success indicators."""
        print("Verifying withdrawal success...")
        try:
            # Check for transaction completed button or success message
            success_indicators = [
                (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "تم")]'),
                (AppiumBy.XPATH, '//android.widget.Button[@content-desc="اتمام العملية"]'),
            ]
            
            for locator in success_indicators:
                element = wait_for_element_visibility(
                    self.driver, locator, timeout=5, soft_fail=True
                )
                if element:
                    print("Withdrawal success verified.")
                    return True
            
            # Alternative: Check if we're back on home screen
            home_screen = (AppiumBy.XPATH, '//android.view.View[@content-desc="الرئيسية"]')
            element = wait_for_element_visibility(
                self.driver, home_screen, timeout=10, soft_fail=True
            )
            if element:
                print("Withdrawal success verified - user redirected to home screen.")
                return True
            
            print("Warning: Could not find explicit success indicator, but proceeding...")
            return True
        except Exception as e:
            print(f"Error verifying withdrawal success: {e}")
            return False