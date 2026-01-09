import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility, hard_wait


class DepositCashPortfolio:

    def __init__(self, driver):
      self.driver = driver

    def click_on_pre_define_category_and_verify_home_screen(self, category_name):
        try:
            print(f"Searching for category: {category_name} ...")
            for attempt in range(4):
                print(f" Scroll attempt {attempt + 1} ...")
                elements = self.driver.find_elements(
                    AppiumBy.XPATH,
                    f'//android.view.View[contains(@content-desc, "{category_name}")]'
                )
                if elements:
                    element = elements[0]
                    desc = element.get_attribute("contentDescription")
                    print(f" Visible category '{category_name}' found with desc:\n{desc}")
                    # Get element bounds
                    rect = element.rect
                    x = rect["x"] + rect["width"] / 2
                    y = rect["y"] + rect["height"] * 0.25  # tap near top (25% height)
                    # Perform tap at upper clickable region
                    self.driver.tap([(x, y)])
                    print(" Clicked on upper clickable area. Proceeding...")
                    return
                print(f"'{category_name}' not visible yet. Scrolling down...")
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
                )
            pytest.fail(f" Category '{category_name}' not found after scrolling attempts.")
        except Exception as e:
            pytest.fail(f"️ Failed to click on category '{category_name}': {e}")

    def perform_click_action_on_deposit_button_and_navigate_next_screen(self):
        """Click on the 'إيداع' (Deposit) button and navigate to the next screen."""
        try:
            print(" Waiting for 'إيداع' (Deposit) button to appear...")
            locator = (AppiumBy.XPATH, '//android.view.View[@content-desc="إيداع"]')
            deposit_button = wait_for_element_visibility(self.driver, locator, timeout=20)
            print(" Performing tap action on 'إيداع' button...")
            TouchAction(self.driver).tap(deposit_button).perform()
            print(" Tap performed successfully on 'إيداع' (Deposit).")
            hard_wait(5)  # wait for next screen to load
        except Exception as e:
            print(f" Error while clicking 'إيداع' (Deposit) button: {e}")
            raise

    def perform_click_action_on_mada_payment_card(self):
        """Click on the 'بطاقة مدى' (Mada card) button, with swipe only if not visible initially."""
        try:
            print(" Checking for 'بطاقة مدى' (Mada card) button...")
            locator = (AppiumBy.ACCESSIBILITY_ID, "بطاقة مدى")
            mada_card = None
            max_swipes = 2
            # Step 1: Try to find the element without scrolling
            mada_card = wait_for_element_visibility(self.driver, locator, timeout=5, soft_fail=True)
            # Step 2: If not found, perform limited swipes
            if not mada_card:
                print(" 'بطاقة مدى' not visible, starting to swipe...")
                for attempt in range(max_swipes):
                    self.driver.swipe(500, 1600, 500, 1000, 600)
                    mada_card = wait_for_element_visibility(self.driver, locator, timeout=3, soft_fail=True)
                    if mada_card:
                        print(f" Found 'بطاقة مدى' after {attempt + 1} swipe(s).")
                        break
            # Step 3: Tap the element if found
            if mada_card:
                print(" Performing tap action on 'بطاقة مدى'...")
                TouchAction(self.driver).tap(mada_card).perform()
                print(" Tap performed successfully on 'بطاقة مدى'.")
                hard_wait(3)
            else:
                print(" Could not find 'بطاقة مدى' after swiping.")
                raise Exception("Mada payment card not found on screen.")
        except Exception as e:
            print(f" Error while clicking on 'بطاقة مدى': {e}")
            raise

    def perform_click_action_on_amount_input_field(self):
        """Simply click on the amount input field (android.widget.EditText)."""
        try:
            print("Waiting for the Amount Input Field to appear...")
            locator = (AppiumBy.XPATH, '//android.widget.EditText')
            amount_field = wait_for_element_visibility(self.driver, locator, timeout=20)
            print(" Performing tap action on Amount Input Field...")
            TouchAction(self.driver).tap(amount_field).perform()
            print(" Tap performed successfully on Amount Input Field.")
        except Exception as e:
            print(f" Error while clicking on Amount Input Field: {e}")
            time.sleep(2)
            raise

    def input_deposit_amount(self, amount):
        """Enter the deposit amount into the input field (android.widget.EditText)."""
        try:
            print(f" Waiting for the deposit amount input field to appear...")
            locator = (AppiumBy.XPATH, '//android.widget.EditText')
            amount_field = wait_for_element_visibility(self.driver, locator, timeout=20)
            print(f" Entering deposit amount: {amount}")
            amount_field.clear()
            amount_field.send_keys(str(amount))
            print(" Deposit amount entered successfully.")
        except Exception as e:
            print(f" Error while entering deposit amount: {e}")
            raise

    def perform_click_action_on_view_screen(self):
        """Simply click on the view screen (android.widget.ScrollView)."""
        try:
            print(" Waiting for the View Screen (ScrollView) to appear...")
            locator = (AppiumBy.XPATH, '//android.widget.ScrollView')
            view_screen = wait_for_element_visibility(self.driver, locator, timeout=20)
            print(" Performing tap action on the View Screen...")
            TouchAction(self.driver).tap(view_screen).perform()
            print(" Tap performed successfully on the View Screen (ScrollView).")
        except Exception as e:
            print(f" Error while clicking on the View Screen: {e}")
            raise

    def perform_click_on_deposit_button(self):
        """Click on the Deposit button (ايداع مبلغ ...) regardless of the amount."""
        try:
            print(" Waiting for the Deposit button (ايداع مبلغ ...) to appear...")
            # XPath using 'contains' to ignore amount value
            locator = (AppiumBy.XPATH, '//android.widget.Button[contains(@content-desc, "ايداع مبلغ")]')
            deposit_button = wait_for_element_visibility(self.driver, locator, timeout=20)
            print("Performing tap action on the Deposit button...")
            TouchAction(self.driver).tap(deposit_button).perform()
            print(" Tap performed successfully on the Deposit button (ايداع مبلغ ...).")
        except Exception as e:
            print(f" Error while clicking on the Deposit button: {e}")
            time.sleep(2)
            raise

    def enter_cvv_code(self):
        """
        Clicks on the CVV EditText field and inputs '123'.
        """
        from appium.webdriver.common.appiumby import AppiumBy
        from selenium.common.exceptions import TimeoutException
        import pytest
        cvv_locator = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'
        )
        try:
            print(" Waiting for CVV EditText field to be visible...")
            cvv_field = wait_for_element_visibility(self.driver, cvv_locator, timeout=10)
            print(" CVV field found. Clicking on it...")
            cvv_field.click()
            hard_wait(1)  # small pause to allow keyboard focus
            print(" Entering CVV: 123")
            cvv_field.send_keys("123")
            print("Successfully entered CVV: 123")
        except TimeoutException:
            print(" CVV EditText field not found on screen.")
            pytest.fail("CVV input field was not found or not visible.")
        except Exception as e:
            print(f" Error while interacting with CVV field: {e}")
            pytest.fail(f"Failed to enter CVV: {e}")

    def click_on_screen_view_and_close_the_keyboard(self):
        """Tap on screen (ScrollView) to close the keyboard."""
        try:
            print(" Waiting for screen view (ScrollView) to appear...")
            screen_view = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.widget.ScrollView'),
                timeout=15
            )
            print(" Tapping on screen to close keyboard...")
            TouchAction(self.driver).tap(screen_view).perform()
            print(" Keyboard closed successfully.")
        except Exception as e:
            print(f" Error while closing keyboard: {e}")
            raise

    def click_on_add_card_button(self):
        """Click on the 'Add Card' (أضف البطاقة) button."""
        try:
            print(" Waiting for the 'Add Card' (أضف البطاقة) button to appear...")
            add_card_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.widget.Button[@content-desc="أضف البطاقة"]'),
                timeout=20
            )
            print(" Clicking on 'Add Card' button...")
            TouchAction(self.driver).tap(add_card_button).perform()
            print(" Successfully clicked on 'Add Card' (أضف البطاقة) button.")
        except Exception as e:
            print(f" Error while clicking on 'Add Card' button: {e}")
            hard_wait(10)
            raise

    def click_on_screen_to_close_the_keyboard(self):
        """Click on the Submit button on the demo page (XPath first, fallback to coordinate tap)."""
        try:
            print("Trying to click 'Submit' button using XPath...")
            element = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Submit']")
            element.click()
            print(" Submit button clicked successfully using XPath.")
        except Exception as e:
            print(f" XPath click failed: {e}")
            print("Attempting coordinate tap instead...")
            # Fallback: tap on specific coordinates
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput("touch", "touch"))
            actions.w3c_actions.pointer_action.move_to_location(275, 857)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print(" Submit button tapped by coordinates.")

    def click_on_submit_button_on_demo_page(self):
        """Click on the 'Submit' button on the demo page."""
        print("Waiting for the 'Submit' button to appear...")
        locator = (AppiumBy.XPATH, "//android.widget.Button[@text='Submit']")
        try:
            submit_button = wait_for_element_visibility(self.driver, locator, timeout=20)
            print("'Submit' button found. Clicking now...")
            submit_button.click()
            hard_wait(10)
            print("Click on 'Submit' button successful.")
        except Exception as e:
            print(f"Error while clicking 'Submit' button: {e}")
            raise

    def perform_click_action_to_close_the_deposit_screen(self):
        """Click to close the deposit screen."""
        try:
            print(" Waiting for the close area of the deposit screen...")
            close_area = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[2]'),
                timeout=10
            )
            print("Clicking to close the deposit screen...")
            TouchAction(self.driver).tap(close_area).perform()
            print(" Deposit screen closed successfully.")
            time.sleep(2)
        except Exception as e:
            print(f" Error while closing the deposit screen: {e}")
            raise

    def verify_cash_portfolio_home_screen(self):
        """Click on the Cash Portfolio (مدخراتك) and verify navigation to Cash Home Screen."""
        portfolio_locator = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "مدخراتك")]')
        cash_portfolio = wait_for_element_visibility(self.driver, portfolio_locator, timeout=25)
        if not cash_portfolio:
            pytest.fail(" Failed to locate Cash Portfolio (مدخراتك).")
            print("Cash Portfolio found. Preparing to tap...")
            time.sleep(15)

    def perform_scroll_down_and_click_first_transaction(self):
        """
        Scrolls the main ScrollView until the 'العمليات' section is visible,
        then clicks the top-most transaction inside it.
        """
        try:
            print("Scrolling down inside main ScrollView to reach 'العمليات' section...")
            # Scroll inside the main ScrollView
            scroll_view = self.driver.find_element(
                AppiumBy.XPATH, "//android.widget.ScrollView"
            )
            self.driver.execute_script("mobile: scrollGesture", {
                "elementId": scroll_view.id,
                "direction": "down",
                "percent": 0.8
            })
            # Ensure 'العمليات' section is visible
            try:
                self.driver.find_element(
                    AppiumBy.XPATH, "//android.view.View[@content-desc='العمليات']"
                )
                print("Section 'العمليات' is now visible.")
            except:
                print("Section 'العمليات' not visible after scroll.")
                return False
            # Locate the transaction container
            transactions = self.driver.find_elements(
                AppiumBy.XPATH,
                "//android.widget.ScrollView/android.view.View[2]/android.view.View"
            )
            if not transactions:
                print("No transactions found inside the container.")
                return False
            first_transaction = transactions[0]
            print(f"Found {len(transactions)} transactions. Clicking the top-most one...")
            # Perform click
            first_transaction.click()
            print("Successfully clicked on the top-most transaction.")
            return True
        except Exception as e:
            print(f"Error while clicking first transaction: {e}")
            return False

    def click_on_topmost_deposit_transaction(self):
        """
        Scrolls down to find the topmost 'عملية إيداع' (Deposit) transaction
        and clicks it. Works even if date/amount/status text is dynamic.
        """
        try:
            # Find main scroll view
            scroll_view = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView")
            # Try scrolling up to 3 times to locate the transaction
            for _ in range(3):
                deposit_buttons = self.driver.find_elements(
                    AppiumBy.XPATH,
                    "//android.widget.Button[starts-with(@content-desc, 'عملية إيداع')]"
                )
                if deposit_buttons:
                    topmost_button = deposit_buttons[0]
                    # Click using TouchAction (supported in your Appium version)
                    action = TouchAction(self.driver)
                    action.tap(element=topmost_button).perform()
                    return True
                # Scroll down to look for more transactions
                self.driver.execute_script("mobile: scrollGesture", {
                    "elementId": scroll_view.id,
                    "direction": "down",
                    "percent": 0.8
                })
            return False
        except Exception as e:
            print(f"Error while clicking topmost deposit transaction: {str(e)}")
            return False

    def verify_title_of_transection_detail_screen(self):
        """Verify that the transaction detail screen title 'تفاصيل الإيداع' is visible."""
        try:
            print("Verifying the title of the transaction detail screen...")
            title_element = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "تفاصيل الإيداع"),
                timeout=10
            )
            if title_element:
                print(" Transaction detail screen title 'تفاصيل الإيداع' is visible.")
                return True
            else:
                raise Exception(" Title 'تفاصيل الإيداع' not found on the transaction detail screen.")
        except Exception as e:
            print(f" Error while verifying transaction detail screen title: {e}")
            raise

    def click_on_payment_method_visa_master(self):
        """
        Clicks on the Visa/MasterCard payment method icon.
        XPath: //android.widget.ImageView[@content-desc="بطاقة دفع"]
        """
        try:
            print("Locating Visa/MasterCard payment method...")
            visa_master_xpath = '//android.widget.ImageView[@content-desc="بطاقة دفع"]'
            element = self.driver.find_element(By.XPATH, visa_master_xpath)
            element.click()
            print("Clicked on Visa/MasterCard payment method successfully.")
        except Exception as e:
            print(f"Error clicking on Visa/MasterCard payment method: {e}")
            self.driver.save_screenshot("error_click_on_payment_method_visa_master.png")
            raise

    def click_on_success_button(self):
        """
        Clicks on the 'Success' button after completing deposit/payment.
        XPath: //android.widget.Button[@resource-id="acssubmit"]
        """
        print("Waiting for the 'Success' button to appear...")
        try:
            success_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.widget.Button[@resource-id="acssubmit"]'),
                timeout=15
            )
            if success_button:
                success_button.click()
                hard_wait(10)  # Optional wait for UI to process
                print("Clicked on 'Success' button successfully.")
            else:
                pytest.fail("'Success' button not found on the screen.")
        except Exception as e:
            print(f"Failed to click on 'Success' button: {e}")
            pytest.fail(f"Exception while clicking on Success button: {e}")

    def perform_scroll_down_on_screen(self):
        """Perform a scroll down action on the current screen."""
        try:
            print(" Performing scroll down on the screen...")
            scroll_area = self.driver.find_element(
                AppiumBy.XPATH, '//android.widget.ScrollView'
            )
            # Perform scroll gesture
            self.driver.execute_script("mobile: scrollGesture", {
                "elementId": scroll_area.id,
                "direction": "down",
                "percent": 0.8
            })
            print(" Scroll down action performed successfully.")
        except Exception as e:
            print(f"️ Error while performing scroll down on screen: {e}")
            raise

    def click_back_button_to_move_primary_portfolio_home_screen(self):
        """Click the back button to return to the primary portfolio home screen."""
        try:
            print(" Waiting for the back button to appear...")
            back_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.widget.Button'),
                timeout=10
            )
            print(" Clicking the back button to navigate to the portfolio home screen...")
            TouchAction(self.driver).tap(back_button).perform()
            print(" Successfully navigated back to the primary portfolio home screen.")
        except Exception as e:
            print(f" Error while clicking back button: {e}")
            raise

    def click_back_button_to_move_holistic_screen(self):
        """Click the back button to return to the Holistic Home Screen."""
        try:
            print(" Waiting for the back button to appear for Holistic Screen navigation...")
            back_button = wait_for_element_visibility(
                self.driver,
                (
                    AppiumBy.XPATH,
                    '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button'
                ),
                timeout=10
            )
            print(" Clicking the back button to navigate to the Holistic Home Screen...")
            TouchAction(self.driver).tap(back_button).perform()
            hard_wait(2)
            print(" Successfully navigated back to the Holistic Home Screen.")
        except Exception as e:
            print(f" Error while clicking back button to move Holistic Screen: {e}")
            raise

    def perform_pull_down_to_refresh_the_screen(self):
        """Perform a pull-down gesture to refresh the current screen."""
        try:
            print(" Performing pull-down to refresh the screen...")
            scroll_view = self.driver.find_element(
                AppiumBy.XPATH, '//android.widget.ScrollView'
            )
            # Perform pull-down (scroll up) gesture from top to bottom
            self.driver.execute_script("mobile: scrollGesture", {
                "elementId": scroll_view.id,
                "direction": "down",
                "percent": 1.0  # Full pull-down for refresh
            })
            print(" Pull-down refresh action performed successfully.")
            time.sleep(12)
        except Exception as e:
            print(f" Error while performing pull-down refresh: {e}")
            raise


















