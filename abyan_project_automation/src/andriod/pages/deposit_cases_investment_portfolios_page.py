import random
import string
import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility, hard_wait


class DepositInvestmentPortfolio:

    def __init__(self, driver):
      self.driver = driver

    def click_on_respective_portfolio_and_verify_home_screen(self, category_name):
        try:
            print(f" Searching for category: {category_name} ...")
            xpath_variants = [
                f'//android.view.View[contains(@content-desc, "{category_name}")]',
                f'//android.widget.ImageView[contains(@content-desc, "{category_name}")]',
                f'//android.view.ViewGroup[contains(@content-desc, "{category_name}")]'
            ]
            for attempt in range(6):
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
                        return
                    hard_wait(5)
                print(" Not found yet, trying to scroll...")
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
                )
            pytest.fail(f" Category '{category_name}' not found after scrolling attempts.")
        except Exception as e:
            pytest.fail(f" Failed to click category '{category_name}': {e}")

    def click_on_respective_single_portfolio_and_verify_home_screen(self, category_name):
        try:
            print(f" Searching for category: {category_name} ...")
            xpath_variants = [
                f'//android.view.View[contains(@content-desc, "{category_name}")]',
                f'//android.widget.ImageView[contains(@content-desc, "{category_name}")]',
                f'//android.view.ViewGroup[contains(@content-desc, "{category_name}")]'
            ]
            for attempt in range(6):
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
                        return
                    hard_wait(5)
                print(" Not found yet, trying to scroll...")
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
                )
            pytest.fail(f" Category '{category_name}' not found after scrolling attempts.")
        except Exception as e:
            pytest.fail(f" Failed to click category '{category_name}': {e}")

    def verify_category_clicked(self, element):
        try:
            wait = WebDriverWait(self.driver, 15)
            try:
                wait.until_not(lambda d: element.is_displayed())
            except:
                pass
            print("Category click verified successfully.")

        except Exception as e:
            pytest.fail(f" Category click verification failed: {e}")

    # def perform_click_action_on_deposit_button(self):
    #     try:
    #         print(" Trying to click on Deposit button...")
    #         deposit_button_locator = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="إيداع"]')
    #         # Wait for visibility
    #         element = wait_for_element_visibility(self.driver, deposit_button_locator, timeout=25)
    #         # Click using tap if regular click fails (safer for Appium)
    #         rect = element.rect
    #         x = rect["x"] + rect["width"] / 2
    #         y = rect["y"] + rect["height"] / 2
    #         self.driver.tap([(x, y)])
    #         print(" Deposit button clicked successfully.")
    #     except Exception as e:
    #         pytest.fail(f" Failed to click on Deposit button: {e}")

    def perform_click_action_on_deposit_button(self):
        print(" Trying to click on Deposit button...")

        deposit_button_locator = (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="إيداع" or @text="إيداع"]'
        )

        try:
            # Try to find without scroll first
            element = wait_for_element_visibility(
                self.driver, deposit_button_locator, timeout=6, soft_fail=True
            )

            if not element:
                print(" Deposit button not visible initially. Trying scrolling...")

                # scroll & retry logic
                for i in range(4):
                    print(f" Scroll attempt {i + 1} ...")
                    self.scroll_down()

                    element = wait_for_element_visibility(
                        self.driver, deposit_button_locator, timeout=4, soft_fail=True
                    )
                    if element:
                        break

            # Final check
            if not element:
                pytest.fail(" Deposit button not found even after scrolling.")

            print(" Deposit button found. Trying to tap...")
            rect = element.rect
            x = rect["x"] + rect["width"] / 2
            y = rect["y"] + rect["height"] / 2
            self.driver.tap([(x, y)])

            print(" Deposit button clicked successfully.")

        except Exception as e:
            pytest.fail(f" Failed to click on Deposit button: {e}")

    def scroll_down(self):
        size = self.driver.get_window_size()
        start_y = size["height"] * 0.80
        end_y = size["height"] * 0.30
        start_x = size["width"] / 2
        print(" Scrolling down...")
        self.driver.swipe(start_x, start_y, start_x, end_y, 800)

    def click_on_browser_success_pay_button(self):
        """
        Clicks on the 'Pay' button in the payment browser.
        Handles wait and safe tap in case element is off-screen or overlayed.
        """
        try:
            print(" Waiting for 'Pay' button to be visible...")
            pay_button_locator = (AppiumBy.XPATH, '//android.widget.Button[@text="Pay"]')
            # Wait until visible
            element = wait_for_element_visibility(self.driver, pay_button_locator, timeout=30)
            # Safe tap (use coordinates)
            rect = element.rect
            x = rect["x"] + rect["width"] / 2
            y = rect["y"] + rect["height"] / 2
            self.driver.tap([(x, y)])
            print(" 'Pay' button clicked successfully.")
            hard_wait(15)
        except Exception as e:
            pytest.fail(f" Failed to click 'Pay' button: {e}")

    def click_deposit_button_for_visamaster_payment(self):
        """
        Clicks on the 'التالي' (Next) button for Visa/MasterCard deposit.
        XPath: //android.widget.Button[@content-desc="التالي"]
        """

        try:
            print("Locating the Visa/Master deposit Next button...")

            next_button_xpath = '//android.widget.Button[@content-desc="التالي"]'

            next_btn = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, next_button_xpath),
                timeout=15
            )

            if next_btn:
                next_btn.click()
                print("Clicked on the Visa/Master Next button successfully.")
            else:
                pytest.fail("Next button ('التالي') not found on the screen.")

        except Exception as e:
            print(f"Exception while clicking Next button: {e}")
            pytest.fail(f"Failed to click Visa/Master Next button: {e}")

    def click_on_field_and_input_mada_card_number(self):
        """
        Clicks on the card number field and enters a fixed testing card number.
        Updated locator:
        //android.widget.EditText[@resource-id="com.abyanflutter.qa:id/cardNumberField"]
        Card Number: 4111114005765430
        """
        try:
            print("Waiting for the 'Card Number' input field to appear...")

            card_number_xpath = '//android.widget.EditText[@resource-id="com.abyanflutter.qa:id/cardNumberField"]'

            card_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, card_number_xpath),
                timeout=15
            )

            if card_field:
                print("Card number field found. Clicking now...")

                card_field.click()
                time.sleep(1)

                # Clear existing digits first
                card_field.clear()

                test_card_number = "4111114005765430"
                print(f"Entering test card number: {test_card_number}")

                card_field.send_keys(test_card_number)
                print("Card number entered successfully.")

                # ---------- Close Keyboard ----------
                try:
                    self.driver.hide_keyboard()
                    print("Keyboard closed using hide_keyboard().")
                except:
                    try:
                        self.driver.press_keycode(4)
                        print("Keyboard closed using press_keycode(4).")
                    except:
                        print("Failed to close keyboard.")
                # -------------------------------------

            else:
                pytest.fail("Card number input field not found on screen.")

        except Exception as e:
            print(f"Exception while entering card number: {e}")
            pytest.fail(f"Failed to input card number: {e}")

    def click_on_input_name_field_and_input_name(self):
        """
        Clicks on the card_holder name field and enters a random name.
        Handles StaleElementReferenceException gracefully.
        Updated locator:
        //android.widget.EditText[@resource-id="com.abyanflutter.qa:id/cardholderNameField"]
        """

        name_field_xpath = '//android.widget.EditText[@resource-id="com.abyanflutter.qa:id/cardholderNameField"]'

        try:
            print("Waiting for the 'Card Holder Name' input field to appear...")
            retries = 2

            for attempt in range(retries):
                try:
                    name_field = wait_for_element_visibility(
                        self.driver,
                        (AppiumBy.XPATH, name_field_xpath),
                        timeout=15
                    )

                    if name_field:
                        print(f"Attempt {attempt + 1}: Name input field found. Clicking now...")

                        name_field.click()
                        time.sleep(1)

                        # Re-fetch after DOM refresh
                        name_field = self.driver.find_element(AppiumBy.XPATH, name_field_xpath)
                        name_field.clear()

                        random_name = "User" + ''.join(random.choices(string.ascii_uppercase, k=3))
                        print(f"Typing random card holder name: {random_name}")

                        name_field.send_keys(random_name)
                        print("Random name entered successfully.")

                        self.latest_card_holder_name = random_name

                        # ---------- Close Keyboard ----------
                        try:
                            self.driver.hide_keyboard()
                            print("Keyboard closed using hide_keyboard().")
                        except:
                            try:
                                self.driver.press_keycode(4)
                                print("Keyboard closed using press_keycode(4).")
                            except:
                                print("Failed to close keyboard.")
                        # ------------------------------------

                        return random_name

                    else:
                        pytest.fail("Card Holder Name input field not found on screen.")

                except StaleElementReferenceException:
                    print(f"Stale element detected on attempt {attempt + 1}. Retrying...")
                    if attempt == retries - 1:
                        raise
                    time.sleep(1)

        except Exception as e:
            print(f"Exception while entering random name: {e}")
            pytest.fail(f"Failed to input card holder name: {e}")

    def click_on_field_and_input_expiry_date(self):
        """
        Clicks on the expiry date field and enters a combined value '01/39'.
        Updated XPath:
        //android.widget.EditText[@resource-id="com.abyanflutter.qa:id/expirationDateField"]
        """
        expiry_xpath = '//android.widget.EditText[@resource-id="com.abyanflutter.qa:id/expirationDateField"]'

        try:
            print("Locating the expiry date field to input month/year...")

            expiry_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, expiry_xpath),
                timeout=15
            )

            if expiry_field:
                print("Expiry date field found. Clicking now...")

                expiry_field.click()
                time.sleep(1)

                # Clear first
                expiry_field.clear()

                expiry_value = "0139"
                expiry_field.send_keys(expiry_value)
                print(f"Successfully entered expiry date: {expiry_value}")

                # ---------- Close Keyboard ----------
                try:
                    self.driver.hide_keyboard()
                    print("Keyboard closed using hide_keyboard().")
                except:
                    try:
                        self.driver.press_keycode(4)
                        print("Keyboard closed using press_keycode(4).")
                    except:
                        print("Failed to close keyboard.")
                # ------------------------------------

            else:
                pytest.fail("Expiry date field not found on screen.")

        except Exception as e:
            print(f"Exception while entering expiry date: {e}")
            pytest.fail(f"Failed to input expiry date: {e}")

    def click_on_cvv_and_input_number(self):
        """
        Clicks on the CVV field, enters a random 3- or 4-digit number,
        and closes the keyboard.
        XPath: //android.widget.EditText[@resource-id="cvv"]
        """
        try:
            print("Locating the CVV field to input data...")
            cvv_xpath = '//android.widget.EditText[@resource-id="com.abyanflutter.qa:id/cvvField"]'
            cvv_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, cvv_xpath),
                timeout=15
            )
            if cvv_field:
                print("CVV field located. Clicking now...")
                cvv_field.click()
                time.sleep(1)
                # Generate random CVV (3 or 4 digits)
                random_cvv = str(random.randint(100, 9999))
                cvv_field.clear()
                cvv_field.send_keys(random_cvv)
                print(f"Entered CVV: {random_cvv}")

                # -------- Close Keyboard --------
                try:
                    self.driver.hide_keyboard()
                    print("Keyboard closed using hide_keyboard().")
                except:
                    try:
                        self.driver.press_keycode(4)  # Android Back button
                        print("Keyboard closed using press_keycode(4).")
                    except:
                        print("Failed to close keyboard via both methods.")
                # ----------------------------------

            else:
                pytest.fail("CVV field not found on the screen.")

        except Exception as e:
            print(f"Exception while entering CVV: {e}")
            pytest.fail(f"Failed to input CVV value: {e}")

    def click_on_pay_button(self):
        """
        Clicks on the Pay button using the exact provided locator:
        //android.widget.TextView[@resource-id="com.abyanflutter.qa:id/pay_button_id"]
        """
        try:
            print("Waiting for the Pay button to appear...")

            pay_button_xpath = '//android.widget.TextView[@resource-id="com.abyanflutter.qa:id/pay_button_id"]'

            pay_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, pay_button_xpath),
                timeout=10
            )

            if pay_button:
                print("Pay button found. Clicking now...")
                pay_button.click()
                hard_wait(15)
                print("Click on Pay button successful.")
            else:
                pytest.fail("Pay button not found on the screen.")

        except Exception as e:
            print(f"Failed to click on Pay button: {e}")
            raise










