import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.driver_finder import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility, hard_wait


class ChangeInvestmentPortfoliosType:
    def __init__(self, driver):
      self.driver = driver

    def click_on_alpaca_moderate_portfolio_and_verify_moderate_home_screen(self, alpaca_moderate_portfolio_name):
        """
        Scrolls down (if needed) and clicks on the Alpaca Moderate portfolio card by its name.
        Example portfolio name: 'Kevin'
        """
        try:
            print(f" Searching for portfolio '{alpaca_moderate_portfolio_name}' ...")
            # Primary XPath for the given portfolio name
            dynamic_xpath = f'//android.widget.ImageView[@content-desc="‪{alpaca_moderate_portfolio_name}‬‬"]'
            # Try finding it without scroll first
            element = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, dynamic_xpath),
                timeout=2,
                soft_fail=True
            )
            # If not found, scroll and search again
            if not element:
                print(" Portfolio not visible — scrolling down to find it...")
                window_size = self.driver.get_window_size()
                start_y = window_size['height'] * 0.8
                end_y = window_size['height'] * 0.3
                x = window_size['width'] / 2
                for i in range(3):  # Try up to 5 scrolls
                    self.driver.swipe(x, start_y, x, end_y, 800)
                    hard_wait(1)
                    element = wait_for_element_visibility(
                        self.driver,
                        (AppiumBy.XPATH, dynamic_xpath),
                        timeout=2,
                        soft_fail=True
                    )
                    if element:
                        print(f" Found '{alpaca_moderate_portfolio_name}' after {i + 1} scroll(s).")
                        break
            # Fallback: Try contains() in case content-desc differs slightly (e.g., formatting)
            if not element:
                print("Trying fallback locator with contains() for flexibility...")
                fallback_xpath = f'//android.widget.ImageView[contains(@content-desc, "{alpaca_moderate_portfolio_name}")]'
                element = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.XPATH, fallback_xpath),
                    timeout=2,
                    soft_fail=True
                )
            # Final check and click
            if element:
                print(f" Clicking on '{alpaca_moderate_portfolio_name}' portfolio card...")
                element.click()
                print(" Click successful. Navigating to its home screen...")
            else:
                pytest.fail(f"Portfolio '{alpaca_moderate_portfolio_name}' not found even after scrolling.")
        except Exception as e:
            print(f" Exception while clicking on portfolio '{alpaca_moderate_portfolio_name}': {e}")
            pytest.fail(f"Failed to click on portfolio '{alpaca_moderate_portfolio_name}': {e}")

    def click_on_alpaca_growth_portfolio_and_verify_growth_home_screen(self, alpaca_growth_portfolio_name):
        """
        Scrolls down (if needed) and clicks on the Alpaca growth portfolio card by its name.
        Example portfolio name: 'Sarah'
        """
        try:
            print(f" Searching for portfolio '{alpaca_growth_portfolio_name}' ...")
            # Primary XPath for the given portfolio name
            dynamic_xpath = f'//android.widget.ImageView[@content-desc="‪{alpaca_growth_portfolio_name}‬‬"]'
            # Try finding it without scroll first
            element = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, dynamic_xpath),
                timeout=2,
                soft_fail=True
            )
            # If not found, scroll and search again
            if not element:
                print(" Portfolio not visible — scrolling down to find it...")
                window_size = self.driver.get_window_size()
                start_y = window_size['height'] * 0.8
                end_y = window_size['height'] * 0.3
                x = window_size['width'] / 2
                for i in range(3):  # Try up to 5 scrolls
                    self.driver.swipe(x, start_y, x, end_y, 800)
                    hard_wait(1)
                    element = wait_for_element_visibility(
                        self.driver,
                        (AppiumBy.XPATH, dynamic_xpath),
                        timeout=2,
                        soft_fail=True
                    )
                    if element:
                        print(f" Found '{alpaca_growth_portfolio_name}' after {i + 1} scroll(s).")
                        break
            # Fallback: Try contains() in case content-desc differs slightly (e.g., formatting)
            if not element:
                print("Trying fallback locator with contains() for flexibility...")
                fallback_xpath = f'//android.widget.ImageView[contains(@content-desc, "{alpaca_growth_portfolio_name}")]'
                element = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.XPATH, fallback_xpath),
                    timeout=0.2,
                    soft_fail=True
                )
            # Final check and click
            if element:
                print(f" Clicking on '{alpaca_growth_portfolio_name}' portfolio card...")
                element.click()
                print(" Click successful. Navigating to its home screen...")
            else:
                pytest.fail(f"Portfolio '{alpaca_growth_portfolio_name}' not found even after scrolling.")
        except Exception as e:
            print(f" Exception while clicking on portfolio '{alpaca_growth_portfolio_name}': {e}")
            pytest.fail(f"Failed to click on portfolio '{alpaca_growth_portfolio_name}': {e}")

    def click_on_alpaca_conservative_portfolio_and_verify_conservative_home_screen(self, alpaca_conservative_portfolio_name):
        """
        Scrolls down (if needed) and clicks on the Alpaca conservative portfolio card by its name.
        Example portfolio name: 'Sarah'
        """
        try:
            print(f" Searching for portfolio '{alpaca_conservative_portfolio_name}' ...")
            # Primary XPath for the given portfolio name
            dynamic_xpath = f'//android.widget.ImageView[@content-desc="‪{alpaca_conservative_portfolio_name}‬‬"]'
            # Try finding it without scroll first
            element = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, dynamic_xpath),
                timeout=1,
                soft_fail=True
            )
            # If not found, scroll and search again
            if not element:
                print(" Portfolio not visible — scrolling down to find it...")
                window_size = self.driver.get_window_size()
                start_y = window_size['height'] * 0.8
                end_y = window_size['height'] * 0.3
                x = window_size['width'] / 2
                for i in range(3):  # Try up to 5 scrolls
                    self.driver.swipe(x, start_y, x, end_y, 800)
                    hard_wait(1)
                    element = wait_for_element_visibility(
                        self.driver,
                        (AppiumBy.XPATH, dynamic_xpath),
                        timeout=0.4,
                        soft_fail=True
                    )
                    if element:
                        print(f" Found '{alpaca_conservative_portfolio_name}' after {i + 1} scroll(s).")
                        break
            # Fallback: Try contains() in case content-desc differs slightly (e.g., formatting)
            if not element:
                print("Trying fallback locator with contains() for flexibility...")
                fallback_xpath = f'//android.widget.ImageView[contains(@content-desc, "{alpaca_conservative_portfolio_name}")]'
                element = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.XPATH, fallback_xpath),
                    timeout=0.1,
                    soft_fail=True
                )
            # Final check and click
            if element:
                print(f" Clicking on '{alpaca_conservative_portfolio_name}' portfolio card...")
                element.click()
                print(" Click successful. Navigating to its home screen...")
            else:
                pytest.fail(f"Portfolio '{alpaca_conservative_portfolio_name}' not found even after scrolling.")
        except Exception as e:
            print(f" Exception while clicking on portfolio '{alpaca_conservative_portfolio_name}': {e}")
            pytest.fail(f"Failed to click on portfolio '{alpaca_conservative_portfolio_name}': {e}")

    def verify_alpaca_moderate_portfolio_home_screen(self, alpaca_moderate_portfolio_name):
        """
        Verify that the user is successfully redirected to the Alpaca Moderate
        home screen after clicking the specific portfolio.
        """
        try:
            print(f" Verifying redirection to Alpaca Moderate home screen: '{alpaca_moderate_portfolio_name}' ...")
            # Step 1: Build the primary XPath (exact match)
            alpaca_moderate_xpath = (
                f'//android.view.View[@content-desc="{alpaca_moderate_portfolio_name}"]'
            )
            # Step 2: Try finding element with exact match first
            category_screen = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, alpaca_moderate_xpath),
                timeout=5,
                soft_fail=True
            )
            # Step 3: If not found, try contains() version (fallback)
            if not category_screen:
                print(" Exact match not found — trying flexible match...")
                fallback_xpath = (
                    f'//android.view.View[contains(@content-desc, "{alpaca_moderate_portfolio_name}")]'
                )
                category_screen = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.XPATH, fallback_xpath),
                    timeout=5,
                    soft_fail=True
                )
            # Step 4: Validation
            if category_screen:
                print(
                    f" User successfully redirected to '{alpaca_moderate_portfolio_name}' Alpaca Moderate home screen.")
            else:
                pytest.fail(
                    f" User was NOT redirected to '{alpaca_moderate_portfolio_name}' Alpaca Moderate home screen.")
        except Exception as e:
            print(f" Exception while verifying Alpaca Moderate home screen: {e}")
            pytest.fail(f"Failed to verify redirection for Alpaca Moderate '{alpaca_moderate_portfolio_name}': {e}")
        hard_wait(0.2)

    def verify_alpaca_growth_portfolio_home_screen(self, alpaca_growth_portfolio_name):
        """
        Verify that the user is successfully redirected to the Alpaca growth
        home screen after clicking the specific portfolio.
        """
        try:
            print(f" Verifying redirection to Alpaca growth home screen: '{alpaca_growth_portfolio_name}' ...")
            # Step 1: Build the primary XPath (exact match)
            alpaca_growth_xpath = (
                f'//android.view.View[@content-desc="{alpaca_growth_portfolio_name}"]'
            )
            # Step 2: Try finding element with exact match first
            category_screen = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, alpaca_growth_xpath),
                timeout=2,
                soft_fail=True
            )
            # Step 3: If not found, try contains() version (fallback)
            if not category_screen:
                print(" Exact match not found — trying flexible match...")
                fallback_xpath = (
                    f'//android.view.View[contains(@content-desc, "{alpaca_growth_portfolio_name}")]'
                )
                category_screen = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.XPATH, fallback_xpath),
                    timeout=2,
                    soft_fail=True
                )
            # Step 4: Validation
            if category_screen:
                print(
                    f" User successfully redirected to '{alpaca_growth_portfolio_name}' Alpaca Moderate home screen.")
            else:
                pytest.fail(
                    f" User was NOT redirected to '{alpaca_growth_portfolio_name}' Alpaca Moderate home screen.")
        except Exception as e:
            print(f" Exception while verifying Alpaca Moderate home screen: {e}")
            pytest.fail(f"Failed to verify redirection for Alpaca Moderate '{alpaca_growth_portfolio_name}': {e}")

    def verify_alpaca_conservative_portfolio_home_screen(self, alpaca_conservative_portfolio_name):
        """
        Verify that the user is successfully redirected to the Alpaca conservative
        home screen after clicking the specific portfolio.
        """
        try:
            print(f" Verifying redirection to Alpaca growth home screen: '{alpaca_conservative_portfolio_name}' ...")
            # Step 1: Build the primary XPath (exact match)
            alpaca_growth_xpath = (
                f'//android.view.View[@content-desc="{alpaca_conservative_portfolio_name}"]'
            )
            # Step 2: Try finding element with exact match first
            category_screen = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, alpaca_growth_xpath),
                timeout=1,
                soft_fail=True
            )
            # Step 3: If not found, try contains() version (fallback)
            if not category_screen:
                print(" Exact match not found — trying flexible match...")
                fallback_xpath = (
                    f'//android.view.View[contains(@content-desc, "{alpaca_conservative_portfolio_name}")]'
                )
                category_screen = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.XPATH, fallback_xpath),
                    timeout=1,
                    soft_fail=True
                )
            # Step 4: Validation
            if category_screen:
                print(
                    f" User successfully redirected to '{alpaca_conservative_portfolio_name}' Alpaca Moderate home screen.")
            else:
                pytest.fail(
                    f" User was NOT redirected to '{alpaca_conservative_portfolio_name}' Alpaca Moderate home screen.")
        except Exception as e:
            print(f" Exception while verifying Alpaca Moderate home screen: {e}")
            pytest.fail(f"Failed to verify redirection for Alpaca Moderate '{alpaca_conservative_portfolio_name}': {e}")
        hard_wait(0.1)

    def click_on_update_button(self):
        """
        Clicks on the 'Update' button on the Alpaca portfolio screen.
        """
        try:
            print(" Attempting to click on the 'Update' button...")
            update_button_xpath = (
                '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/'
                'android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/'
                'android.view.View[1]/android.view.View/android.view.View/android.widget.Button[2]'
            )
            # Wait for the Update button to become visible
            update_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, update_button_xpath),
                timeout=10,
                soft_fail=True
            )
            if update_button:
                print(" 'Update' button found. Clicking now...")
                update_button.click()
                print(" 'Update' button clicked successfully.")
            else:
                pytest.fail(" 'Update' button not found on the screen. Cannot perform click.")
        except Exception as e:
            print(f" Exception while clicking on the 'Update' button: {e}")

            pytest.fail(f"Failed to click on the 'Update' button: {e}")
        hard_wait(0.2)

    def select_update_button_and_proceed(self):
        """
        Clicks on the 'إدارة المحفظة' (Manage Portfolio) button using Accessibility ID.
        """
        try:
            print(" Attempting to click on the 'إدارة المحفظة' (Manage Portfolio) button...")
            # Locate the button by accessibility id
            update_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "إدارة المحفظة"),
                timeout=0.5,
                soft_fail=True
            )
            if update_button:
                print(" 'إدارة المحفظة' button found. Clicking now...")
                update_button.click()
                print(" 'إدارة المحفظة' button clicked successfully — proceeding to next screen.")
            else:
                pytest.fail(" 'إدارة المحفظة' button not found on the screen. Cannot proceed.")
        except Exception as e:
            print(f" Exception while clicking 'إدارة المحفظة' button: {e}")
            pytest.fail(f"Failed to click 'إدارة المحفظة' button: {e}")
        hard_wait(0.2)

    def select_wallet_type_option_and_proceed(self):
        """
        Selects the wallet type option dynamically.
        Tries in this order:
          1. نوع المحفظة المتنوعة (نمو)
          2. نوع المحفظة المتنوعة (متوازنة)
          3. نوع المحفظة المتنوعة (آمنة)
        Does NOT perform any scrolling for speed.
        """
        try:
            print(" Attempting to select a wallet type option (نمو / متوازنة / آمنة)...")
            # All possible wallet type locators
            wallet_type_xpaths = [
                '//android.widget.Button[@content-desc="نوع المحفظة\nالمتنوعة (نمو)"]',
                '//android.widget.Button[@content-desc="نوع المحفظة\nالمتنوعة (متوازنة)"]',
                '//android.widget.Button[@content-desc="نوع المحفظة\nالمتنوعة (آمنة)"]'
            ]
            wallet_type_button = None
            # Try each XPath until one matches
            for wallet_xpath in wallet_type_xpaths:
                print(f"️ Checking for wallet type using XPath: {wallet_xpath}")
                wallet_type_button = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.XPATH, wallet_xpath),
                    timeout=8,
                    soft_fail=True
                )
                if wallet_type_button:
                    print(f" Found wallet type button using: {wallet_xpath}")
                    break
            # Click if found
            if wallet_type_button:
                print(" Clicking on the wallet type option...")
                wallet_type_button.click()
                print(" Wallet type option selected successfully.")
            else:
                pytest.fail(" None of the wallet type options (نمو / متوازنة / آمنة) found on screen. Cannot proceed.")
        except Exception as e:
            print(f" Exception while selecting wallet type option: {e}")
            pytest.fail(f"Failed to select wallet type option: {e}")

    def select_continue_for_changing_wallet_type_and_proceed(self):
        """
        Clicks on the 'استمر' (Continue) button to proceed with changing the wallet type.
        """
        try:
            print(" Attempting to click on the 'استمر' (Continue) button...")
            # Locate the Continue button using accessibility id
            continue_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "استمر"),
                timeout=15,
                soft_fail=True
            )
            if continue_button:
                print("️ 'استمر' button found. Clicking now...")
                continue_button.click()
                print(" 'استمر' button clicked successfully — proceeding to the next step.")
            else:
                pytest.fail(" 'استمر' button not found on the screen. Cannot proceed.")
        except Exception as e:
            print(f" Exception while clicking on 'استمر' button: {e}")
            pytest.fail(f"Failed to click on 'استمر' button: {e}")

    def select_conservative_portfolio_type_to_update_conservative_portfolio_type(self):
        """
        Selects the 'آمنة' (Conservative) portfolio type option to update the portfolio type to Moderate.
        """
        try:
            print(" Attempting to select the 'آمنة' (Conservative) portfolio type...")
            # Locate the 'آمنة' portfolio type button using Accessibility ID
            growth_portfolio_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "آمنة"),
                timeout=5,
                soft_fail=True
            )
            if growth_portfolio_button:
                print("️ 'آمنة' (Growth) portfolio type found. Clicking now...")
                growth_portfolio_button.click()
                print(" 'آمنة' portfolio type selected successfully.")
            else:
                pytest.fail(" 'آمنة' portfolio type not found on the screen. Cannot proceed.")
        except Exception as e:
            print(f" Exception while selecting 'آمنة' portfolio type: {e}")
            pytest.fail(f"Failed to select 'آمنة' portfolio type: {e}")

    def select_growth_portfolio_type_to_update_growth_portfolio_type(self):
        """
        Selects the 'نمو' (Growth) portfolio type option to update the portfolio type to Moderate.
        """
        try:
            print(" Attempting to select the 'نمو' (Growth) portfolio type...")
            # Locate the 'نمو' portfolio type button using Accessibility ID
            growth_portfolio_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "نمو"),
                timeout=10,
                soft_fail=True
            )
            if growth_portfolio_button:
                print("️ 'نمو' (Growth) portfolio type found. Clicking now...")
                growth_portfolio_button.click()
                print(" 'نمو' portfolio type selected successfully.")
            else:
                pytest.fail(" 'نمو' portfolio type not found on the screen. Cannot proceed.")
        except Exception as e:
            print(f" Exception while selecting 'نمو' portfolio type: {e}")
            pytest.fail(f"Failed to select 'نمو' portfolio type: {e}")

    def select_moderate_portfolio_type_to_update_moderate_portfolio_type(self):
        """
        Selects the 'متوازنة' (Growth) portfolio type option to update the portfolio type to Moderate.
        """
        try:
            print(" Attempting to select the 'متوازنة' (Growth) portfolio type...")
            # Locate the 'نمو' portfolio type button using Accessibility ID
            growth_portfolio_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "متوازنة"),
                timeout=10,
                soft_fail=True
            )
            if growth_portfolio_button:
                print("️ 'متوازنة' (Growth) portfolio type found. Clicking now...")
                growth_portfolio_button.click()
                print(" 'متوازنة' portfolio type selected successfully.")
            else:
                pytest.fail(" 'متوازنة' portfolio type not found on the screen. Cannot proceed.")
        except Exception as e:
            print(f" Exception while selecting 'متوازنة' portfolio type: {e}")
            pytest.fail(f"Failed to select 'متوازنة' portfolio type: {e}")

    def click_on_create_portfolio_button_and_proceed(self):
        """
        Clicks on the 'إنشاء المحفظة' (Create Portfolio) button to proceed with portfolio creation.
        """
        try:
            print(" Attempting to click on the 'إنشاء المحفظة' (Create Portfolio) button...")
            # Locate the 'إنشاء المحفظة' button using Accessibility ID
            create_portfolio_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "إنشاء المحفظة"),
                timeout=10,
                soft_fail=True
            )
            if create_portfolio_button:
                print("️ 'إنشاء المحفظة' button found. Clicking now...")
                create_portfolio_button.click()
                print(" Successfully clicked on the 'إنشاء المحفظة' (Create Portfolio) button.")
            else:
                pytest.fail(" 'إنشاء المحفظة' button not found on the screen. Cannot proceed.")
        except Exception as e:
            print(f" Exception while clicking 'إنشاء المحفظة' button: {e}")
            pytest.fail(f"Failed to click 'إنشاء المحفظة' button: {e}")

    def click_on_wallet_management_button_on_success_screen(self):
        """
        Clicks on the 'إدارة المحافظ' (Wallet Management) button on the success screen.
        """
        try:
            print("Attempting to click on the 'إدارة المحافظ' (Wallet Management) button on success screen...")
            # Locate the 'إدارة المحافظ' button using Accessibility ID
            wallet_management_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "إدارة المحافظ"),
                timeout=5,
                soft_fail=True
            )
            if wallet_management_button:
                print(" 'إدارة المحافظ' button found. Clicking now...")
                wallet_management_button.click()
                print(" Successfully clicked on the 'إدارة المحافظ' (Wallet Management) button.")
            else:
                pytest.fail(" 'إدارة المحافظ' button not found on the success screen. Cannot proceed.")
        except Exception as e:
            print(f" Exception while clicking 'إدارة المحافظ' button: {e}")
            pytest.fail(f"Failed to click 'إدارة المحافظ' button: {e}")

    def scroll_until_other_details_button_and_click(self):
        """
        Scrolls down once, then clicks the 'تفاصيل اخرى' (Other Details) button.
        """
        try:
            print(" Scrolling down to reveal 'تفاصيل اخرى' button...")
            scroll_view_xpath = '//android.widget.ScrollView'
            other_details_id = "تفاصيل اخرى"
            # Perform a single scroll first
            scroll_area = self.driver.find_element(AppiumBy.XPATH, scroll_view_xpath)
            self.driver.swipe(500, 1800, 500, 800, 800)
            hard_wait(0.1)
            # Now check for the button
            print("Searching for 'تفاصيل اخرى' button after scroll...")
            button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, other_details_id),
                timeout=0.2,
                soft_fail=False
            )
            if button:
                print(" 'تفاصيل اخرى' button found. Clicking now...")
                button.click()
                print("️ 'تفاصيل اخرى' button clicked successfully.")
            else:
                pytest.fail(" 'تفاصيل اخرى' button not found on screen after scrolling.")
        except Exception as e:
            print(f" Exception while scrolling/clicking 'تفاصيل اخرى': {e}")
            pytest.fail(f"Failed to click 'تفاصيل اخرى' button: {e}")

    def scroll_until_transactions_listing_and_click(self):
        logger.info("Scrolling down to reveal 'العمليات' button if not visible...")
        max_scrolls = 3
        for attempt in range(max_scrolls):
            try:
                button = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.ACCESSIBILITY_ID, "العمليات"),
                    timeout=0.5,
                    soft_fail=True
                )
                if button:
                    logger.info(" 'العمليات' button found. Clicking now...")
                    button.click()
                    logger.info(" 'العمليات' button clicked successfully.")
                    return
                else:
                    logger.info(
                        f" 'العمليات' button not found yet (attempt {attempt + 1}/{max_scrolls}). Scrolling down...")
                    self.scroll_down()
                    time.sleep(0.2)
            except Exception as e:
                logger.warning(f"Scroll attempt {attempt + 1} failed due to: {e}")
        pytest.fail(" 'العمليات' button not found after multiple scroll attempts.")

    def click_on_conservative_change_portfolio_type_tab(self):
        """
        Clicks on the 'تغيير نوع المحفظة' entry from operations history
        that includes 'المتنوعة (آمنة)' and confirms the operation was successful.
        Uses a generic XPath ignoring date/time.
        """
        try:
            print(" Searching for 'تغيير نوع المحفظة' entry with 'المتنوعة (آمنة)'...")
            entry_xpath = (
                '//android.widget.Button['
                'contains(@content-desc, "تغيير نوع المحفظة") '
                'and contains(@content-desc, "المتنوعة (آمنة)") '
                'and contains(@content-desc, "تمت العملية بنجاح")]'
            )
            entry = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, entry_xpath),
                timeout=0.5,
                soft_fail=False
            )
            if entry:
                print(" Found 'تغيير نوع المحفظة' entry. Clicking now...")
                entry.click()
                print(" Clicked on 'تغيير نوع المحفظة' entry successfully.")
            else:
                pytest.fail(" Could not find 'تغيير نوع المحفظة' entry on screen.")
        except Exception as e:
            print(f" Exception while clicking on 'تغيير نوع المحفظة': {e}")
            pytest.fail(f"Failed to click 'تغيير نوع المحفظة' entry: {e}")

    def click_on_moderate_change_portfolio_type_tab(self):
        """
        Clicks on the 'تغيير نوع المحفظة' entry from operations history
        that includes 'المتنوعة  (متوازنة)' and confirms the operation was successful.
        Uses a generic XPath ignoring date/time.
        """
        try:
            print(" Searching for 'تغيير نوع المحفظة' entry with 'المتنوعة (متوازنة)'...")
            entry_xpath = (
                '//android.widget.Button['
                'contains(@content-desc, "تغيير نوع المحفظة") '
                'and contains(@content-desc, "المتنوعة (متوازنة)") '
                'and contains(@content-desc, "تمت العملية بنجاح")]'
            )
            entry = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, entry_xpath),
                timeout=0.5,
                soft_fail=False
            )
            if entry:
                print(" Found 'تغيير نوع المحفظة' entry. Clicking now...")
                entry.click()
                print(" Clicked on 'تغيير نوع المحفظة' entry successfully.")
            else:
                pytest.fail(" Could not find 'تغيير نوع المحفظة' entry on screen.")
        except Exception as e:
            print(f" Exception while clicking on 'تغيير نوع المحفظة': {e}")
            pytest.fail(f"Failed to click 'تغيير نوع المحفظة' entry: {e}")

    def click_on_growth_change_portfolio_type_tab(self):
        """
        Clicks on the 'تغيير نوع المحفظة' entry from operations history
        that includes 'المتنوعة (نمو)' and confirms the operation was successful.
        Uses a generic XPath ignoring date/time.
        """
        try:
            print(" Searching for 'تغيير نوع المحفظة' entry with 'المتنوعة (نمو)'...")
            entry_xpath = (
                '//android.widget.Button['
                'contains(@content-desc, "تغيير نوع المحفظة") '
                'and contains(@content-desc, "المتنوعة (نمو)") '
                'and contains(@content-desc, "تمت العملية بنجاح")]'
            )
            entry = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, entry_xpath),
                timeout=0.5,
                soft_fail=False
            )
            if entry:
                print(" Found 'تغيير نوع المحفظة' entry. Clicking now...")
                entry.click()
                print(" Clicked on 'تغيير نوع المحفظة' entry successfully.")
            else:
                pytest.fail(" Could not find 'تغيير نوع المحفظة' entry on screen.")
        except Exception as e:
            print(f" Exception while clicking on 'تغيير نوع المحفظة': {e}")
            pytest.fail(f"Failed to click 'تغيير نوع المحفظة' entry: {e}")

    def verify_user_on_change_portfolio_screen(self):
        """
        Verifies that the user is on the 'Change Portfolio Type' screen by:
        1. Checking for the screen title/identifier using partial text match in XPath.
        2. Ensuring 'من' (From) and 'الى' (To) fields are visible.
        """
        try:
            print(" Verifying user is on the 'Change Portfolio Type' screen...")

            # Step 1: Verify screen title or unique section identifier
            change_portfolio_xpath = '//android.view.View[contains(@content-desc, "تغيير نوع المحفظة")]'
            change_portfolio_element = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, change_portfolio_xpath),
                timeout=3,
                soft_fail=True
            )
            # Step 2: Verify 'from' and 'to' fields (من / الى)
            from_id = "من"
            to_id = "الى"
            from_element = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, from_id),
                timeout=4,
                soft_fail=True
            )
            to_element = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, to_id),
                timeout=3,
                soft_fail=True
            )
            if change_portfolio_element and from_element and to_element:
                print(" User is on the 'Change Portfolio Type' screen successfully.")
            else:
                pytest.fail(" User not redirected to the 'Change Portfolio Type' screen.")
        except Exception as e:
            print(f"️ Exception during screen verification: {e}")
            pytest.fail(f"Failed to verify 'Change Portfolio Type' screen: {e}")

    def verify_portfolio_type_changed_successfully(self):
        """
        Verifies that the portfolio type was changed from 'المتنوعة (متوازنة)' to 'المتنوعة (آمنة)'.
        """
        try:
            print(" Verifying portfolio type change (متوازنة ➜ آمنة)...")
            from_type_id = "المتنوعة (متوازنة)"
            to_type_id = "المتنوعة (آمنة)"
            from_type = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, from_type_id),
                timeout=2,
                soft_fail=True
            )
            to_type = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, to_type_id),
                timeout=2,
                soft_fail=True
            )
            if from_type and to_type:
                print(" Portfolio type successfully updated from 'متوازنة' to 'آمنة'.")
            else:
                pytest.fail(" Portfolio type verification failed — types not found.")
        except Exception as e:
            print(f" Exception while verifying portfolio type change: {e}")
            pytest.fail(f"Failed to verify portfolio type change: {e}")

















