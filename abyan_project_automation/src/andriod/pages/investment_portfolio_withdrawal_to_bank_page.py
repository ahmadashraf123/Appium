import random
import string
import time
import pytest
import re
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility


class WithdrawalInvestmentPortfolios:

    def __init__(self, driver):
      self.driver = driver

    def click_on_settings_button(self):
        print("Clicking on Settings button…")
        settings_btn = (AppiumBy.ACCESSIBILITY_ID, "الإعدادات")
        element = wait_for_element_visibility(self.driver, settings_btn, timeout=10)
        element.click()

    def click_on_orders_tab(self):
        print("Clicking on Orders tab…")
        orders_tab_locator = (
            AppiumBy.XPATH,
            '//android.widget.Button[contains(@content-desc, "الأوامر")]'
        )
        element = wait_for_element_visibility(self.driver, orders_tab_locator, timeout=10)
        element.click()

    def click_on_cancel_existing_transaction(self):
        print("Trying to click on 'Cancel Existing Transaction' button...")
        cancel_transaction_locator = (
            AppiumBy.XPATH,
            '//android.view.View[@content-desc="إلغاء عملية قائمة" or @text="إلغاء عملية قائمة" or @content-desc="Cancel Existing Transaction" or @text="Cancel Existing Transaction"]'
        )
        element = wait_for_element_visibility(
            self.driver,
            cancel_transaction_locator,
            timeout=6,
            soft_fail=False
        )
        element.click()
        print("Clicked on 'Cancel Existing Transaction' button.")
    def click_on_withdrawal_funds_option(self):
        print("Clicking on Withdrawal Funds option…")
        withdrawal_option = (
            AppiumBy.ACCESSIBILITY_ID,
            "سحب الأموال")
        element = wait_for_element_visibility(self.driver, withdrawal_option, timeout=10)
        element.click()

    def click_on_continue_withdrawal_button(self):
        print("Clicking on Continue Withdrawal button…")
        continue_btn = (
            AppiumBy.ACCESSIBILITY_ID,
            "إستمر"
        )
        element = wait_for_element_visibility(self.driver, continue_btn, timeout=10)
        element.click()

    def select_portfolio_performance_option(self):

        print("Selecting Portfolio Performance option…")
        portfolio_performance = (
            AppiumBy.ACCESSIBILITY_ID,
            "اداء المحفظة"
        )
        element = wait_for_element_visibility(self.driver, portfolio_performance, timeout=10)
        element.click()

    def click_on_continue_button(self):
        print("Clicking on Continue button…")
        continue_btn = (
            AppiumBy.ACCESSIBILITY_ID,
            "إستمر"
        )
        element = wait_for_element_visibility(self.driver, continue_btn, timeout=10)
        element.click()
    def click_on_two_thousand_option(self):
        """
        Clicks specifically on the 2,000 amount option.
        """
        print("Trying to click on 2,000 amount option...")

        amount_locator = (
            AppiumBy.XPATH,
            '//android.view.View[contains(@content-desc, "2,000")]'
        )

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(amount_locator)
            )
            element.click()
            print("Clicked on 2,000 amount option successfully!")
        except:
            pytest.fail("2,000 amount option not clickable or not found.")

    def click_on_five_thousand_option(self):
        """
        Clicks specifically on the 5,000 amount option.
        """
        print("Trying to click on 5,000 amount option...")

        amount_locator = (
            AppiumBy.XPATH,
            '//android.view.View[contains(@content-desc, "5,000")]'
        )

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(amount_locator)
            )
            element.click()
            print("Clicked on 5,000 amount option successfully!")
        except:
            pytest.fail("5,000 amount option not clickable or not found.")

    def click_on_full_amount_option(self):
        locator = (
            AppiumBy.XPATH,
            '//android.view.View[contains(@content-desc, "اخر")]'
        )
        element = wait_for_element_visibility(self.driver, locator)
        element.click()

    # def enter_full_portfolio_amount(self, portfolio_name):
    #     print(f"Extracting amount from portfolio: {portfolio_name}")
    #
    #     # Dynamic locator
    #     portfolio_locator = (
    #         AppiumBy.XPATH,
    #         f'//android.widget.ImageView[contains(@content-desc, "{portfolio_name}")]'
    #     )
    #
    #     element = wait_for_element_visibility(self.driver, portfolio_locator, timeout=12)
    #     content_desc = element.get_attribute("contentDescription")
    #     print("Portfolio content-desc => ", content_desc)
    #
    #     import re
    #     match = re.search(r'([\d,]+\.\d+)', content_desc)
    #     if not match:
    #         pytest.fail("Amount not found in portfolio card")
    #
    #     amount = match.group(1)
    #     print("Extracted amount => ", amount)
    #
    #     # Input field
    #     amount_input_locator = (AppiumBy.XPATH, '//android.widget.EditText')
    #     input_field = wait_for_element_visibility(self.driver, amount_input_locator, timeout=10)
    #
    #     # Tap on the input field to make it editable
    #     rect = input_field.rect
    #     x = rect["x"] + rect["width"] / 2
    #     y = rect["y"] + rect["height"] / 2
    #     self.driver.tap([(x, y)])
    #
    #     # Clear and enter amount
    #     input_field.clear()
    #     input_field.send_keys(amount)
    #
    #     print("Full amount entered successfully!")
    import re
    import pytest
    from appium.webdriver.common.appiumby import AppiumBy

    import re
    import pytest
    from appium.webdriver.common.appiumby import AppiumBy
    from appium.webdriver.common.touch_action import TouchAction

    import re
    import pytest
    from appium.webdriver.common.appiumby import AppiumBy
    from appium.webdriver.common.touch_action import TouchAction

    import re
    import pytest
    from appium.webdriver.common.appiumby import AppiumBy
    from appium.webdriver.common.touch_action import TouchAction

    def enter_full_portfolio_amount(self, portfolio_name):
        print(f"Extracting amount from portfolio: {portfolio_name}")

        # Dynamic locator for portfolio card
        portfolio_locator = (
            AppiumBy.XPATH,
            f'//android.widget.ImageView[contains(@content-desc, "{portfolio_name}")]'
        )

        element = wait_for_element_visibility(self.driver, portfolio_locator, timeout=12)
        content_desc = element.get_attribute("contentDescription")
        print("Portfolio content-desc =>", content_desc)

        # Remove commas and extract integer part before decimal
        cleaned_content = content_desc.replace(',', '')
        match = re.search(r'(\d+)(?:[\.,]\d+)?', cleaned_content)
        if not match:
            pytest.fail(f"Integer part not found in portfolio: {content_desc}")

        amount_before_decimal = match.group(1)
        print("Amount before decimal (integer only) =>", amount_before_decimal)

        # Input field
        amount_input_locator = (AppiumBy.XPATH, '//android.widget.EditText')
        input_field = wait_for_element_visibility(self.driver, amount_input_locator, timeout=10)

        # Scroll input field into view (if needed)
        try:
            self.driver.execute_script("mobile: scroll", {"elementId": input_field.id, "toVisible": True})
        except:
            pass

        # Tap using TouchAction to focus
        action = TouchAction(self.driver)
        action.tap(element=input_field).perform()

        # Clear existing text and enter integer
        input_field.clear()
        input_field.send_keys(amount_before_decimal)

        print("Integer amount entered successfully!")

    def click_on_delivery_between_guards(self):

        print("Trying to click on 'Delivery Between Guards' button...")
        delivery_locator = (
            AppiumBy.XPATH,
            '//android.widget.ImageView[contains(@content-desc, "تحويل بين محافظ")]'
        )
        element = wait_for_element_visibility(
            self.driver,
            delivery_locator,
            timeout=6,
            soft_fail=False
        )
        element.click()
        print("Clicked on 'Delivery Between Guards'.")

    def click_on_cancel_withdrawal_button(self):
        print("Trying to click on 'Cancel Withdrawal' button...")
        cancel_withdrawal_locator = (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="إلغاء السحب" or @text="إلغاء السحب" or @content-desc="Cancel Withdrawal" or @text="Cancel Withdrawal"]'
        )
        element = wait_for_element_visibility(
            self.driver,
            cancel_withdrawal_locator,
            timeout=6,
            soft_fail=False
        )
        element.click()
        print("Clicked on 'Cancel Withdrawal' button.")
    def click_on_conservative_portfolio(self):
        print("Clicking on Conservative Portfolio…")
        conservative_portfolio_locator = (
            AppiumBy.XPATH,
            '//android.widget.ImageView[contains(@content-desc, "conservative")]'
        )
        element = wait_for_element_visibility(self.driver, conservative_portfolio_locator, timeout=10)
        element.click()

    def click_on_hundred_option(self):
        print("Clicking on 100 amount option…")
        hundred_option_locator = (
            AppiumBy.XPATH,
            '//android.view.View[contains(@content-desc, "100")]'
        )
        element = wait_for_element_visibility(self.driver, hundred_option_locator, timeout=10)
        element.click()

    def click_on_conservative_portfolio_and_verify_home_screen(self, category_name):
        xpath_variants = [
            f'//android.view.View[contains(@content-desc, "{category_name}")]',
            f'//android.widget.ImageView[contains(@content-desc, "{category_name}")]',
            f'//android.view.ViewGroup[contains(@content-desc, "{category_name}")]'
        ]
        self.driver.implicitly_wait(0.2)
        for attempt in range(4):
            print(f"Scroll attempt {attempt + 1} ...")
            for xpath in xpath_variants:
                elements = self.driver.find_elements(AppiumBy.XPATH, xpath)
                if elements:
                    element = elements[0]
                    desc = element.get_attribute("contentDescription")
                    print(f" Found element:\n{desc}")
                    rect = element.rect
                    x = rect["x"] + rect["width"] / 2
                    y = rect["y"] + rect["height"] / 2
                    self.driver.tap([(x, y)])
                    print(" Category clicked successfully.")
                    self.driver.implicitly_wait(5)
                    return
            print(" Not found yet, trying to scroll fast...")
            size = self.driver.get_window_size()
            self.driver.swipe(size['width'] / 2, size['height'] * 0.8, size['width'] / 2, size['height'] * 0.3, 200)
            time.sleep(0.1)
        self.driver.implicitly_wait(5)
        pytest.fail(f"Category '{category_name}' not found after scrolling attempts.")

    def click_on_transfer_your_savings_button(self):
        print("Trying to click on 'Transfer to your savings' button...")
        transfer_button_locator = (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="حول إلى مدخراتك" or @text="حول إلى مدخراتك" or @content-desc="Transfer to your savings" or @text="Transfer to your savings"]'
        )
        element = wait_for_element_visibility(
            self.driver,
            transfer_button_locator,
            timeout=6,
            soft_fail=False
        )
        element.click()
        print("Clicked on 'Transfer to your savings' button.")

    def click_on_transaction_completed_button(self):
        print("Trying to click on 'Transaction Completed' button...")
        transaction_completed_locator = (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="اتمام العملية" or @text="اتمام العملية" or @content-desc="Transaction Completed" or @text="Transaction Completed"]'
        )
        element = wait_for_element_visibility(
            self.driver,
            transaction_completed_locator,
            timeout=6,
            soft_fail=False
        )
        element.click()
        print("Clicked on 'Transaction Completed' button.")

    def click_on_home_button(self):
        print("Trying to click on 'Home' button...")

        home_button_locator = (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="الصفحة الرئيسية"]'
        )

        element = wait_for_element_visibility(
            self.driver,
            home_button_locator,
            timeout=20,  # OTP ke baad screen transition slow hoti hai
            soft_fail=True  # agar na ho to test fail na ho
        )

        if element:
            element.click()
            print("Clicked on 'Home' button.")
        else:
            print("Home button not displayed — already on Home or flow auto-redirected.")

    def click_on_keep_withdrawal_option(self):

        print("Clicking on Keep Withdrawal option…")
        keep_withdrawal_locator = (
            AppiumBy.ACCESSIBILITY_ID,
            "إستمر في السحب"
        )
        element = wait_for_element_visibility(self.driver, keep_withdrawal_locator, timeout=10)
        element.click()












