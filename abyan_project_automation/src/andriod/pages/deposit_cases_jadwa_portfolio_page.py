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


class DepositJadwaPortfolio:

    def __init__(self, driver):
      self.driver = driver

    def click_on_the_deposit_button(self):
        """
        Waits for and clicks on the 'إيداع' (Deposit) button.
        Verifies that the click action is successful.
        """
        try:
            print("Waiting for the 'إيداع' (Deposit) button to appear...")
            deposit_button_xpath = '//android.widget.Button[@content-desc="إيداع" or @text="إيداع"]'
            # Wait for button visibility
            deposit_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, deposit_button_xpath),
                timeout=15
            )
            if deposit_button:
                print(" 'إيداع' (Deposit) button found. Clicking now...")
                deposit_button.click()
                print("Click on 'إيداع' (Deposit) successful. Proceeding to the next step.")
                hard_wait(3)
            else:
                pytest.fail(" 'إيداع' (Deposit) button not found on the screen.")
        except Exception as e:
            print(f" Exception while clicking on 'إيداع' (Deposit) button: {e}")
            pytest.fail(f"Failed to click on 'إيداع' (Deposit) button: {e}")

    def click_on_payment_by_card_option(self):
        """
        Waits for and clicks on the 'بطاقة دفع' (Payment by Card) option using accessibility id.
        """
        try:
            print("Waiting for the 'بطاقة دفع' (Payment by Card) option to appear...")
            card_option = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "بطاقة دفع"),
                timeout=15
            )
            if card_option:
                print(" 'بطاقة دفع' option found. Clicking now...")
                card_option.click()
                print("Click on 'بطاقة دفع' successful. Proceeding to next step.")
                hard_wait(2)
            else:
                pytest.fail(" 'بطاقة دفع' option not found on screen.")
        except Exception as e:
            print(f" Exception while clicking on 'بطاقة دفع': {e}")
            pytest.fail(f"Failed to click on 'بطاقة دفع' option: {e}")

    def click_on_input_field_to_enter_amount_and_proceed(self):
        """
        Clicks on the amount input field (//android.widget.EditText)
        """
        try:
            print("Waiting for the amount input field to appear...")
            amount_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, "//android.widget.EditText"),
                timeout=15
            )
            if amount_field:
                print("Amount input field found. Clicking now...")
                amount_field.click()
                print("Click on amount input field successful.")
            else:
                pytest.fail("Amount input field not found on screen.")
        except Exception as e:
            print(f"Exception while clicking on amount input field: {e}")
            pytest.fail(f"Failed to click on amount input field: {e}")

    def input_deposit_amount(self, amount="1000"):
        """
        Inputs the given deposit amount (default: 1000) into the EditText field.
        """
        try:
            print(f"Waiting for the deposit amount input field to appear...")
            amount_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, "//android.widget.EditText"),
                timeout=15
            )
            if amount_field:
                print(f"Deposit amount field found. Entering amount: {amount}")
                amount_field.click()
                amount_field.clear()
                amount_field.send_keys(str(amount))
                print(f"Successfully entered deposit amount: {amount}")
            else:
                pytest.fail("Deposit amount input field not found on screen.")
        except Exception as e:
            print(f"Exception while entering deposit amount: {e}")
            pytest.fail(f"Failed to enter deposit amount: {e}")

    def click_on_the_view_to_close_the_keyboard(self):
        """
        Performs a tap on a specific screen coordinate to close the keyboard.
        Useful when the keyboard hides elements and cannot be closed normally.
        """
        try:
            print("Attempting to close the keyboard by tapping on the view...")
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(484, 451)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("Tap action performed successfully — keyboard should now be closed.")
        except Exception as e:
            print(f"Exception while trying to close keyboard: {e}")
            pytest.fail(f"Failed to close keyboard using view tap: {e}")

    def click_deposit_button(self):
        """
        Waits for and clicks on the 'إيداع مبلغ 1000.00 ' (Deposit) button.
        """
        try:
            print("Waiting for the 'إيداع مبلغ 1000.00 ' (Deposit) button to appear...")
            deposit_button_xpath = '//android.widget.Button[@content-desc="ايداع مبلغ 1000.00 "]'
            deposit_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, deposit_button_xpath),
                timeout=15
            )
            if deposit_button:
                print("Deposit button found. Clicking now...")
                deposit_button.click()
                print("Click on deposit button successful.")
            else:
                pytest.fail("Deposit button not found on screen.")
        except Exception as e:
            print(f"Exception while clicking on deposit button: {e}")
            pytest.fail(f"Failed to click on deposit button: {e}")
        hard_wait(5)

    def click_on_payment_method_mada(self):
        """
        Clicks on the 'بطاقة مدى' (Mada Card) payment method using accessibility id.
        """
        try:
            print("Waiting for the 'بطاقة مدى' (Mada Card) payment method to appear...")
            mada_option = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "بطاقة مدى"),
                timeout=15
            )
            if mada_option:
                print(" 'بطاقة مدى' option found. Clicking now...")
                mada_option.click()
                print("Click on 'بطاقة مدى' payment method successful.")
            else:
                pytest.fail(" 'بطاقة مدى' payment option not found on screen.")
        except Exception as e:
            print(f"Exception while clicking on 'بطاقة مدى' payment method: {e}")
            pytest.fail(f"Failed to click on 'بطاقة مدى' payment method: {e}")
        hard_wait(4)

    def click_on_input_name_field_and_input_name(self):
        """
        Clicks on the card_holder name field and enters a random name.
        Handles StaleElementReferenceException gracefully.
        """
        name_field_xpath = '//android.widget.EditText[@resource-id="card_holder_name"]'
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
                        time.sleep(1)  # Allow for keyboard/UI refresh
                        # Re-fetch after click in case DOM updated
                        name_field = self.driver.find_element(AppiumBy.XPATH, name_field_xpath)
                        name_field.clear()
                        random_name = "User" + ''.join(random.choices(string.ascii_uppercase, k=3))
                        print(f"Typing random card holder name: {random_name}")
                        name_field.send_keys(random_name)
                        print("Random name entered successfully.")
                        self.latest_card_holder_name = random_name
                        return random_name
                    else:
                        pytest.fail("Card Holder Name input field not found on screen.")
                except StaleElementReferenceException:
                    print(f" Stale element detected on attempt {attempt + 1}. Retrying...")
                    if attempt == retries - 1:
                        raise
                    time.sleep(1)
        except Exception as e:
            print(f"Exception while entering random name: {e}")
            pytest.fail(f"Failed to input card holder name: {e}")

    def click_on_input_name_field_and_input_name_for_tap(self):
        """
        Clicks on the Cardholder Name field and enters a random name.
        Handles StaleElementReferenceException gracefully.
        Updated XPath: //android.widget.EditText[@resource-id="card-holder"]
        """
        name_field_xpath = '//android.widget.EditText[@resource-id="card-holder"]'
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
                        time.sleep(1)  # Allow for keyboard/UI refresh
                        # Re-fetch after click in case DOM updated
                        name_field = self.driver.find_element(AppiumBy.XPATH, name_field_xpath)
                        name_field.clear()
                        random_name = "User" + ''.join(random.choices(string.ascii_uppercase, k=3))
                        print(f"Typing random card holder name: {random_name}")
                        name_field.send_keys(random_name)
                        print("Random name entered successfully.")
                        self.latest_card_holder_name = random_name
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

    def click_on_field_and_input_mada_card_number(self):
        """
        Clicks on the card number field and enters a fixed testing card number.
        Card Number: 4201320111111010
        """
        try:
            print("Waiting for the 'Card Number' input field to appear...")
            card_number_xpath = '//android.widget.EditText[@resource-id="card_number"]'
            card_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, card_number_xpath),
                timeout=15
            )
            if card_field:
                print("Card number field found. Clicking now...")
                card_field.click()
                card_field.clear()
                test_card_number = "4201320111111010"
                print(f"Entering test card number: {test_card_number}")
                card_field.send_keys(test_card_number)
                print("Card number entered successfully.")
            else:
                pytest.fail("Card number input field not found on screen.")
        except Exception as e:
            print(f"Exception while entering card number: {e}")
            pytest.fail(f"Failed to input card number: {e}")

    def click_on_field_and_input_visa_master_card_number_for_tap(self):
        print("Waiting for Card Number field...")
        card_field = wait_for_element_visibility(
            self.driver,
            (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="card-number"]'),
            timeout=20
        )
        card_field.click()
        card_field.send_keys("4508750015741019")  # Example Visa card
        print("Card number entered successfully.")

    def click_on_field_and_input_visa_master_card_number(self):
        """
        Clicks on the card number field and enters a fixed testing card number.
        Card Number:  4111114005765430
        """
        try:
            print("Waiting for the 'Card Number' input field to appear...")
            card_number_xpath = '//android.widget.EditText[@resource-id="card_number"]'
            card_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, card_number_xpath),
                timeout=15
            )
            if card_field:
                print("Card number field found. Clicking now...")
                card_field.click()
                card_field.clear()
                test_card_number = "4111114005765430"
                print(f"Entering test card number: {test_card_number}")
                card_field.send_keys(test_card_number)
                print("Card number entered successfully.")
            else:
                pytest.fail("Card number input field not found on screen.")
        except Exception as e:
            print(f"Exception while entering card number: {e}")
            pytest.fail(f"Failed to input card number: {e}")

    def click_on_field_and_input_visa_card_number(self):
        """
        Clicks on the card number field and enters a fixed testing card number.
        Card Number: 4508750015741019
        """
        try:
            print("Waiting for the 'Card Number' input field to appear...")
            card_number_xpath = '//android.widget.EditText[@resource-id="card_number"]'
            card_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, card_number_xpath),
                timeout=15
            )
            if card_field:
                print("Card number field found. Clicking now...")
                card_field.click()
                card_field.clear()
                test_card_number = "4508750015741019"
                print(f"Entering test card number: {test_card_number}")
                card_field.send_keys(test_card_number)
                print("Card number entered successfully.")
            else:
                pytest.fail("Card number input field not found on screen.")
        except Exception as e:
            print(f"Exception while entering card number: {e}")
            pytest.fail(f"Failed to input card number: {e}")

    def click_on_screen_view_and_close_the_keyboard(self):
        """
        Clicks on a specific screen view element to close the keyboard.
        XPath used: (//android.view.View[@resource-id="preact_root"])[2]
        """
        try:
            print("Attempting to click on screen view to close the keyboard...")
            screen_view_xpath = '(//android.view.View[@resource-id="preact_root"])[2]'
            screen_view = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, screen_view_xpath),
                timeout=10
            )
            if screen_view:
                screen_view.click()
                print("Clicked on screen view successfully. Keyboard closed.")
            else:
                pytest.fail("Screen view element not found to close the keyboard.")
        except Exception as e:
            print(f"Exception while clicking on screen view: {e}")
            pytest.fail(f"Failed to close keyboard by clicking on screen view: {e}")

    def click_on_screen_view_and_close_the_keyboard_for_tap(self):
        """
        Clicks on an outer container view to close the keyboard.
        Updated XPath: //android.view.View[@resource-id="form-container"]
        """
        try:
            print("Attempting to click on screen view to close the keyboard...")
            screen_view_xpath = '//android.view.View[@resource-id="form-container"]'
            screen_view = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, screen_view_xpath),
                timeout=15
            )
            if screen_view:
                screen_view.click()
                print("Clicked on screen view successfully. Keyboard closed.")
            else:
                pytest.fail("Screen view element not found to close the keyboard.")
        except Exception as e:
            print(f"Exception while clicking on screen view: {e}")
            pytest.fail(f"Failed to close keyboard by clicking on screen view: {e}")

    def click_field_and_input_expiry_month_info(self):
        """
        Clicks on the expiry month field and inputs a fixed month '12'.
        Adds wait, retry, and scroll handling for stability.
        """
        expiry_month_xpath = '//android.widget.EditText[@resource-id="expiry_month"]'
        try:
            print("Locating the expiry month field to input data...")
            retries = 2
            for attempt in range(retries):
                try:
                    # Try to find element
                    expiry_month_field = wait_for_element_visibility(
                        self.driver,
                        (AppiumBy.XPATH, expiry_month_xpath),
                        timeout=10
                    )
                    if expiry_month_field:
                        print(f"Attempt {attempt + 1}: Expiry month field found. Clicking now...")
                        expiry_month_field.click()
                        time.sleep(1)
                        expiry_month_field.clear()
                        expiry_month_field.send_keys("12")
                        print("Entered fixed expiry month: 12")
                        return
                    else:
                        print("Expiry month field not found, trying to scroll...")
                        self.driver.swipe(500, 1500, 500, 800, 800)
                except StaleElementReferenceException:
                    print(f" Stale element on attempt {attempt + 1}. Retrying...")
                    time.sleep(1)
            pytest.fail("Failed to locate and input expiry month field after retries.")
        except Exception as e:
            print(f"Exception while entering expiry month: {e}")
            pytest.fail(f"Failed to input expiry month: {e}")

    def click_on_field_and_input_expiry_date_for_tap(self):
        """
        Clicks on the expiry date field and enters a combined value '01/39'.
        New XPath: //android.widget.EditText[@resource-id="expiration-date"]
        """
        expiry_xpath = '//android.widget.EditText[@resource-id="expiration-date"]'
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
                expiry_field.clear()
                expiry_field.send_keys("01/39")  # example expiry date value
                print("Successfully entered expiry date: 01/39")
            else:
                pytest.fail("Expiry date field not found on screen.")

        except Exception as e:
            print(f"Exception while entering expiry date: {e}")
            pytest.fail(f"Failed to input expiry date: {e}")

    def click_field_and_input_expiry_month_info_for_visa_card(self):
        """
        Clicks on the expiry month field and inputs a fixed month ' 01'.
        Adds wait, retry, and scroll handling for stability.
        """
        expiry_month_xpath = '//android.widget.EditText[@resource-id="expiry_month"]'
        try:
            print("Locating the expiry month field to input data...")
            retries = 2
            for attempt in range(retries):
                try:
                    # Try to find element
                    expiry_month_field = wait_for_element_visibility(
                        self.driver,
                        (AppiumBy.XPATH, expiry_month_xpath),
                        timeout=10
                    )
                    if expiry_month_field:
                        print(f"Attempt {attempt + 1}: Expiry month field found. Clicking now...")
                        expiry_month_field.click()
                        time.sleep(1)
                        expiry_month_field.clear()
                        expiry_month_field.send_keys("01")
                        print("Entered fixed expiry month: 01")
                        return
                    else:
                        print("Expiry month field not found, trying to scroll...")
                        self.driver.swipe(500, 1500, 500, 800, 800)
                except StaleElementReferenceException:
                    print(f" Stale element on attempt {attempt + 1}. Retrying...")
                    time.sleep(1)
            pytest.fail("Failed to locate and input expiry month field after retries.")
        except Exception as e:
            print(f"Exception while entering expiry month: {e}")
            pytest.fail(f"Failed to input expiry month: {e}")

    def click_field_and_input_expiry_month_info_for_visa(self):
        """
        Clicks on the expiry month field and inputs a fixed month '01'.
        Adds wait, retry, and scroll handling for stability.
        """
        expiry_month_xpath = '//android.widget.EditText[@resource-id="expiry_month"]'
        try:
            print("Locating the expiry month field to input data...")
            retries = 2
            for attempt in range(retries):
                try:
                    # Try to find the element
                    expiry_month_field = wait_for_element_visibility(
                        self.driver,
                        (AppiumBy.XPATH, expiry_month_xpath),
                        timeout=10
                    )
                    if expiry_month_field:
                        print(f"Attempt {attempt + 1}: Expiry month field found. Clicking now...")
                        expiry_month_field.click()
                        time.sleep(1)
                        expiry_month_field.clear()
                        expiry_month_field.send_keys("01")
                        print("Entered fixed expiry month: 01")
                        return
                    else:
                        print("Expiry month field not found, trying to scroll...")
                        self.driver.swipe(500, 1500, 500, 800, 800)
                except StaleElementReferenceException:
                    print(f" Stale element on attempt {attempt + 1}. Retrying...")
                    time.sleep(1)
            pytest.fail("Failed to locate and input expiry month field after retries.")
        except Exception as e:
            print(f"Exception while entering expiry month: {e}")
            pytest.fail(f"Failed to input expiry month: {e}")

    def click_on_field_and_input_expiry_year_info(self):
        """
        Clicks on the expiry year field and enters a fixed value '25'.
        XPath: //android.widget.EditText[@resource-id="expiry_year"]
        """
        try:
            print("Locating the expiry year field to input data...")
            expiry_year_xpath = '//android.widget.EditText[@resource-id="expiry_year"]'
            expiry_year_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, expiry_year_xpath),
                timeout=10
            )
            if expiry_year_field:
                expiry_year_field.click()
                expiry_year_field.send_keys("25")
                print("Entered expiry year: 25")
            else:
                pytest.fail("Expiry year field not found on the screen.")
        except Exception as e:
            print(f"Exception while entering expiry year: {e}")
            pytest.fail(f"Failed to input expiry year: {e}")

    def click_on_field_and_input_expiry_year_info_for_visa_master(self):
        """
        Clicks on the expiry year field and enters a fixed value '25'.
        XPath: //android.widget.EditText[@resource-id="expiry_year"]
        """
        try:
            print("Locating the expiry year field to input data...")
            expiry_year_xpath = '//android.widget.EditText[@resource-id="expiry_year"]'
            expiry_year_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, expiry_year_xpath),
                timeout=10
            )
            if expiry_year_field:
                expiry_year_field.click()
                expiry_year_field.send_keys("39")
                print("Entered expiry year: 39")
            else:
                pytest.fail("Expiry year field not found on the screen.")
        except Exception as e:
            print(f"Exception while entering expiry year: {e}")
            pytest.fail(f"Failed to input expiry year: {e}")

    def click_on_field_and_input_expiry_year_info_for_visa(self):
        """
        Clicks on the expiry year field and enters a fixed value '39'.
        XPath: //android.widget.EditText[@resource-id="expiry_year"]
        """
        try:
            print("Locating the expiry year field to input data...")
            expiry_year_xpath = '//android.widget.EditText[@resource-id="expiry_year"]'
            expiry_year_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, expiry_year_xpath),
                timeout=10
            )
            if expiry_year_field:
                print("Expiry year field found. Clicking now...")
                expiry_year_field.click()
                time.sleep(1)
                expiry_year_field.clear()
                expiry_year_field.send_keys("39")
                print("Entered fixed expiry year: 39")
            else:
                pytest.fail("Expiry year field not found on the screen.")
        except Exception as e:
            print(f"Exception while entering expiry year: {e}")
            pytest.fail(f"Failed to input expiry year: {e}")

    # def click_on_cvv_and_input_number(self):
    #     """
    #     Clicks on the CVV field and enters a random 3- or 4-digit number.
    #     XPath: //android.widget.EditText[@resource-id="cvv"]
    #     """
    #     try:
    #         print("Locating the CVV field to input data...")
    #         cvv_xpath = '//android.widget.EditText[@resource-id="cvv"]'
    #         cvv_field = wait_for_element_visibility(
    #             self.driver,
    #             (AppiumBy.XPATH, cvv_xpath),
    #             timeout=10
    #         )
    #         if cvv_field:
    #             cvv_field.click()
    #             random_cvv = str(random.randint(100, 9999))
    #             cvv_field.send_keys(random_cvv)
    #             print(f"Entered CVV number: {random_cvv}")
    #         else:
    #             pytest.fail("CVV field not found on the screen.")
    #     except Exception as e:
    #         print(f"Exception while entering CVV number: {e}")
    #         pytest.fail(f"Failed to input CVV number: {e}")
    def click_on_cvv_and_input_number(self):
        """
        Clicks on the CVV field, enters a random 3- or 4-digit number,
        and closes the keyboard.
        XPath: //android.widget.EditText[@resource-id="cvv"]
        """
        try:
            print("Locating the CVV field to input data...")
            cvv_xpath = '//android.widget.EditText[@resource-id="cvv"]'
            cvv_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, cvv_xpath),
                timeout=10
            )

            if cvv_field:
                cvv_field.click()

                # Enter random CVV (3–4 digits)
                random_cvv = str(random.randint(100, 9999))
                cvv_field.send_keys(random_cvv)
                print(f"Entered CVV number: {random_cvv}")

                # ---------- CLOSE KEYBOARD ----------
                try:
                    self.driver.hide_keyboard()
                    print("Keyboard closed using hide_keyboard().")
                except:
                    # Backup: press Back key to close keyboard
                    try:
                        self.driver.press_keycode(4)
                        print("Keyboard closed using press_keycode(4).")
                    except:
                        print("Failed to close keyboard.")
                # -------------------------------------

            else:
                pytest.fail("CVV field not found on the screen.")

        except Exception as e:
            print(f"Exception while entering CVV number: {e}")
            pytest.fail(f"Failed to input CVV number: {e}")

    def click_on_cvv_and_input_number_for_visa_master_for_tap(self):
        """
        Clicks on the CVV field and enters the fixed CVV '100'.
        Updated XPath: //android.widget.EditText[@resource-id="cvv"]
        """
        try:
            print("Locating the CVV field to input data...")
            cvv_xpath = '//android.widget.EditText[@resource-id="cvv"]'

            cvv_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, cvv_xpath),
                timeout=15
            )

            if cvv_field:
                cvv_field.click()
                cvv_field.clear()
                fixed_cvv = "100"
                cvv_field.send_keys(fixed_cvv)
                print(f"Entered CVV number: {fixed_cvv}")
            else:
                pytest.fail("CVV field not found on the screen.")

        except Exception as e:
            print(f"Exception while entering CVV number: {e}")
            pytest.fail(f"Failed to input CVV number: {e}")

    def click_on_cvv_and_input_number_for_visa_master(self):
        """
        Clicks on the CVV field and enters the fixed CVV '100'.
        XPath: //android.widget.EditText[@resource-id="cvv"]
        """
        try:
            print("Locating the CVV field to input data...")
            cvv_xpath = '//android.widget.EditText[@resource-id="cvv"]'
            cvv_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, cvv_xpath),
                timeout=10
            )
            if cvv_field:
                cvv_field.click()
                cvv_field.clear()
                fixed_cvv = "100"
                cvv_field.send_keys(fixed_cvv)
                print(f"Entered CVV number: {fixed_cvv}")
            else:
                pytest.fail("CVV field not found on the screen.")
        except Exception as e:
            print(f"Exception while entering CVV number: {e}")
            pytest.fail(f"Failed to input CVV number: {e}")

    def click_on_cvv_and_input_number_for_visa(self):
        """
        Clicks on the CVV field and enters a fixed value '100'.
        XPath: //android.widget.EditText[@resource-id="cvv"]
        """
        try:
            print("Locating the CVV field to input data...")
            cvv_xpath = '//android.widget.EditText[@resource-id="cvv"]'
            cvv_field = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, cvv_xpath),
                timeout=10
            )
            if cvv_field:
                print("CVV field found. Clicking now...")
                cvv_field.click()
                time.sleep(1)
                cvv_field.clear()
                cvv_field.send_keys("100")
                print("Entered fixed CVV number: 100")
            else:
                pytest.fail("CVV field not found on the screen.")

        except Exception as e:
            print(f"Exception while entering CVV number: {e}")
            pytest.fail(f"Failed to input CVV number: {e}")

    def click_on_pay_button_for_tap_and_money_hash(self):
        """
        Clicks on the Pay button (Tap) using updated resource-id 'tap-btn'.
        """
        print("Waiting for the 'ادفع' (Pay) button to appear...")

        try:
            pay_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.widget.Button[@resource-id="tap-btn"]'),
                timeout=15
            )

            if pay_button:
                pay_button.click()
                hard_wait(30)  # Wait for payment processing
                print("Click on 'ادفع' (Pay) button successful.")
            else:
                pytest.fail("'ادفع' (Pay) button not found on the screen.")

        except Exception as e:
            print(f"Failed to click on 'ادفع' (Pay) button: {e}")
            pytest.fail(f"Exception while clicking on Pay button: {e}")

    def click_on_pay_button(self):
        """
        Clicks on the Pay button regardless of the amount (e.g., 'ادفع 1000.00SAR').
        """
        print("Waiting for the 'ادفع' (Pay) button to appear...")
        try:
            pay_button = wait_for_element_visibility(
                self.driver,
                (
                    AppiumBy.XPATH,
                    "//android.widget.Button[contains(@text,'ادفع') and contains(@text,'SAR')]"
                ),
                timeout=10
            )
            pay_button.click()
            hard_wait(15)
            print("Click on 'ادفع' (Pay) button successful.")
        except Exception as e:
            print(f" Failed to click on 'ادفع' (Pay) button: {e}")
            raise














