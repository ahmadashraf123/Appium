import random
import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from appium.webdriver.webdriver import WebDriver

from abyan_project_automation.src.andriod.pages.cash_portfolios_creation_page import fake
from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility


class CreateJadwaPortfolios:
    SCROLL_BUTTON_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'إنشاء محفظة')
    OTP = (AppiumBy.XPATH, '//android.view.View[@content-desc="ادخل رمز التحقق"]/preceding-sibling::android.view.View[1]')
    OTP_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")

    def __init__(self, driver):
      self.driver = driver

    def scroll_and_click_create_portfolio_button(self):
        """
        Continuously scrolls down until the 'إنشاء محفظة' button appears,
        then clicks it immediately.
        """
        print(" Starting to scroll down to find the 'إنشاء محفظة' button...")
        button_locator = (AppiumBy.ACCESSIBILITY_ID, 'إنشاء محفظة')
        max_scrolls = 10  # safety limit
        scroll_count = 0
        while scroll_count < max_scrolls:
            try:
                # Try finding the button
                button = self.driver.find_element(*button_locator)
                print(" 'إنشاء محفظة' button is now visible. Clicking it...")
                button.click()
                print(" Successfully clicked on 'إنشاء محفظة' button.")
                return  # Stop once clicked

            except NoSuchElementException:
                # Scroll down if button not visible
                size = self.driver.get_window_size()
                start_y = int(size["height"] * 0.8)
                end_y = int(size["height"] * 0.3)
                start_x = int(size["width"] / 2)
                self.driver.swipe(start_x, start_y, start_x, end_y, 800)
                scroll_count += 1
                print(f"↕ Scrolling down... attempt {scroll_count}")
                time.sleep(1)
        # If reached here, button was not found
        pytest.fail(" 'إنشاء محفظة' button not found even after scrolling the full page.")

    def holictic_screen_scroll_until_end(self):
        """
        Continuously scrolls down until the bottom of the page is reached
        or until the max scroll limit is hit.
        """
        print(" Starting to scroll down...")

        max_scrolls = 10  # safety limit to prevent infinite scroll
        scroll_count = 0
        last_page_source = ""
        while scroll_count < max_scrolls:
            current_page_source = self.driver.page_source
            # Check if we've reached the end (no new content)
            if current_page_source == last_page_source:
                print(" Reached the end of the scrollable content.")
                break
            # Perform scroll
            size = self.driver.get_window_size()
            start_y = int(size["height"] * 0.8)
            end_y = int(size["height"] * 0.3)
            start_x = int(size["width"] / 2)
            self.driver.swipe(start_x, start_y, start_x, end_y, 800)
            scroll_count += 1
            print(f"Scrolling down... attempt {scroll_count}")
            last_page_source = current_page_source
            time.sleep(1)
        print(" Finished scrolling.")

    def create_jadwa_portfolio(self, timeout=15):
        """
        Clicks on the 'السوق السعودي' card using the specified XPath.
        """
        xpath = '//android.widget.ImageView[@content-desc="السوق السعودي\nلعوائد مرتفعة في صندوق سعودي مضاربي\nأسهم سعودية (جدوى)"]'
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.XPATH, xpath))
            )
            element.click()
            print("Clicked on 'السوق السعودي' card successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            print("Failed to click 'السوق السعودي' card:", str(e))
            raise
    def click_create_jadwa_portfolio_button(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.Button[@content-desc="إنشاء المحفظة"]')
                )
            )
            element.click()
            print("Clicked 'إنشاء المحفظة' button successfully.")
        except TimeoutException:
            print("Failed to find 'إنشاء المحفظة' button within the timeout.")

    def click_on_portfolio_target(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="استثمر لأبنائك"]')))
            element.click()
            print("Clicked on 'استثمر لأبنائك' successfully.")
        except TimeoutException:
            print("Element with content-desc 'استثمر لأبنائك' not found within the timeout.")
        except Exception as e:
            print("Error while clicking on 'استثمر لأبنائك':", str(e))

    def click_on_portfolio_goal_target(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="استثمر لهدفك"]')))
            element.click()
            print("Clicked on 'استثمر لهدفك ' successfully.")
        except TimeoutException:
            print("Element with content-desc 'استثمر لهدفك' not found within the timeout.")
        except Exception as e:
            print("Error while clicking on 'استثمر لهدفك':", str(e))

    def select_goal_icon_proceed(self):
        """
        Selects the 7th goal icon (based on ImageView index) and proceeds.
        Handles visibility, scrolling, and stale element exceptions.
        """
        goal_icon_xpath = ('//android.view.View[@content-desc="رفض"]/android.view.View/android.view.View'
                           '/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.ImageView[7]')
        print("Attempting to select goal icon...")
        try:
            # Try to find and click the goal icon (retry once if stale)
            for attempt in range(2):
                try:
                    goal_icon = WebDriverWait(self.driver, 15).until(
                        EC.element_to_be_clickable((AppiumBy.XPATH, goal_icon_xpath))
                    )
                    goal_icon.click()
                    print(" Goal icon selected successfully.")
                    break
                except StaleElementReferenceException:
                    print(f" Goal icon went stale (attempt {attempt + 1}). Retrying...")
                    time.sleep(1)
            # Optional: click 'Next' or 'Continue' if that follows
            try:
                next_button = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "التالي"))
                )
                next_button.click()
                print(" Clicked 'التالي' (Next) after selecting goal icon.")
            except TimeoutException:
                print(" 'التالي' button not found after selecting goal icon — maybe not required here.")
        except TimeoutException:
            print(" Timeout: Goal icon not found or not clickable.")
        except Exception as e:
            print(f" Unexpected error during goal icon selection: {e}")

    def enter_portfolio_name_and_press_next(self, name=None):
        try:
            if not name:
                name = fake.first_name()
            # Step 1: Focus the input field
            focus_xpath = '//android.view.View[@content-desc="رفض"]/android.view.View/android.view.View'
            focus_element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, focus_xpath))
            )
            focus_element.click()
            print("Focused input field and opened keyboard")
            time.sleep(1.5)
            # Step 2: Enter text into the EditText field
            input_xpath = '//android.widget.EditText'
            input_element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, input_xpath))
            )
            input_element.click()
            time.sleep(0.5)
            try:
                input_element.clear()
            except Exception:
                print("Clear not supported on this field, continuing anyway.")
            input_element.send_keys(name)
            print(f"Entered text: {name}")
            # Step 3: Hide keyboard to ensure the "Next" button is clickable
            try:
                self.driver.hide_keyboard()
                print(" Keyboard hidden successfully.")
            except Exception:
                print("Could not hide keyboard (might not be open).")
            # Step 4: Click the "Next" button
            next_button_xpath = '//android.widget.Button[@content-desc="التالي"]'
            next_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, next_button_xpath))
            )
            next_button.click()
            print("Pressed 'التالي' (Next) button")
            time.sleep(3)
            print("Waited 3 seconds after pressing the button.")
        except TimeoutException:
            print("Timeout: Could not find or click one of the required elements.")

    def enter_portfolio_goal_name_and_press_next(self, name=None):
        """
        Clicks on EditText field, enters portfolio name, and presses 'التالي' (Next).
        Handles stale element and visibility issues safely.
        """
        try:
            if not name:
                name = fake.first_name()
            input_xpath = '//android.widget.EditText'
            next_button_xpath = '//android.widget.Button[@content-desc="التالي"]'
            print(" Waiting for portfolio name input field...")
            input_element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, input_xpath))
            )
            # Try interacting, retry if stale
            for attempt in range(2):
                try:
                    input_element.click()
                    print(" Clicked on input field.")
                    time.sleep(0.5)
                    try:
                        input_element.clear()
                        print(" Cleared previous text.")
                    except Exception:
                        print(" Clear not supported, continuing anyway.")
                    input_element.send_keys(name)
                    print(f" Entered portfolio name: {name}")
                    # Hide keyboard if open
                    try:
                        self.driver.hide_keyboard()
                        print(" Keyboard hidden successfully.")
                    except Exception:
                        print(" Keyboard not open, skipping hide.")
                    # Wait for and click 'Next' button
                    next_button = WebDriverWait(self.driver, 15).until(
                        EC.element_to_be_clickable((AppiumBy.XPATH, next_button_xpath))
                    )
                    next_button.click()
                    print(" Pressed 'التالي' (Next) button.")
                    time.sleep(2)
                    print(" Portfolio name step completed.")
                    return
                except StaleElementReferenceException:
                    print(f" Stale element detected (attempt {attempt + 1}). Retrying...")
                    time.sleep(1)
                    input_element = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((AppiumBy.XPATH, input_xpath))
                    )
            # If all attempts failed
            raise Exception(" Unable to enter name due to repeated stale element errors.")
        except TimeoutException:
            print(" Timeout: Could not find the EditText or Next button.")
        except Exception as e:
            print(f" Unexpected error while entering portfolio name: {e}")
    def enter_otp_code(self):
        try:
            # Step 1: Locate the OTP element just above the "ادخل رمز التحقق" label
            otp_element = wait_for_element_visibility(self.driver, self.OTP, 20)
            # Step 2: Extract OTP digits from content-desc
            otp_code = otp_element.get_attribute("content-desc")
            print(f"Detected OTP: {otp_code}")
            # Step 3: Wait for the EditText input field to be ready
            otp_input = wait_for_element_visibility(self.driver,self.OTP_INPUT, 20)
            # Step 4: Enter the OTP code as a whole into the field
            otp_input.click()
            otp_input.send_keys(otp_code)
            print("OTP entered successfully.")
            time.sleep(3)  # Optional pause for UI to transition
        except Exception as e:
            pytest.fail(f"Error entering OTP: {str(e)}")

    def click_portfolio_success_button(self):
        """
        Waits for and clicks the 'انتقل للمحفظة' (Go to Portfolio) button.
        """
        try:
            print("Waiting for 'انتقل للمحفظة' button to become clickable...")
            time.sleep(2)  # Give time for transition animation if needed
            button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '//android.widget.Button[@content-desc="انتقل للمحفظة"]')
                )
            )
            button.click()
            print("Successfully clicked on 'انتقل للمحفظة' button.")
        except TimeoutException:
            self.driver.save_screenshot("error_go_to_portfolio_timeout.png")
            print("Could not find the 'انتقل للمحفظة' button. Screenshot saved.")
            raise AssertionError(" 'انتقل للمحفظة' button was not clickable within the timeout.")

    def scroll_and_select_portfolio(self, portfolio_name):
        """
        Scrolls inside the ScrollView until a portfolio card with the given name is found,
        clicks it, and verifies that the screen redirects to the correct portfolio detail page.
        """
        print(f" Searching for portfolio named '{portfolio_name}'...")
        # Dynamic XPath for target portfolio card
        portfolio_xpath = f'//android.widget.ImageView[contains(@content-desc, "{portfolio_name}")]'
        verify_xpath = f'//android.view.View[@content-desc="{portfolio_name}"]'
        max_scrolls = 10
        scroll_count = 0
        found = False
        while scroll_count < max_scrolls:
            try:
                # Try finding the portfolio card
                portfolio_element = self.driver.find_element(AppiumBy.XPATH, portfolio_xpath)
                print(f" Found portfolio card '{portfolio_name}'! Clicking...")
                portfolio_element.click()
                found = True
                break
            except NoSuchElementException:
                # Perform scroll
                print(f"↕ Portfolio not visible yet. Scrolling down... (attempt {scroll_count + 1})")
                size = self.driver.get_window_size()
                start_y = int(size["height"] * 0.8)
                end_y = int(size["height"] * 0.3)
                start_x = int(size["width"] / 2)
                self.driver.swipe(start_x, start_y, start_x, end_y, 800)
                time.sleep(1)
                scroll_count += 1
        if not found:
            pytest.fail(f" Portfolio '{portfolio_name}' not found after full scroll.")
        time.sleep(2)
    def verify_correctly_redirect_on_respective_home_screen(self, portfolio_name):
        """
        Verifies that the app redirected to the correct portfolio home screen
        after clicking on the selected portfolio.
        """
        print(f" Verifying redirection to portfolio '{portfolio_name}' home screen...")
        # Locator for verifying portfolio detail screen
        verify_xpath = f'//android.view.View[@content-desc="{portfolio_name}"]'
        try:
            # Wait for the element to appear on the new screen
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, verify_xpath))
            )
            if element.is_displayed():
                print(f" Successfully redirected to '{portfolio_name}' home screen.")
            else:
                pytest.fail(f" Element found but not visible for portfolio '{portfolio_name}'.")
        except TimeoutException:
            pytest.fail(f" Redirection verification failed — portfolio '{portfolio_name}' home screen not visible.")
        time.sleep(5)

    def verify_correctly_redirect_on_parent_portfolio_home_screen(self, portfolio_name):
        print(f" Verifying redirection to portfolio '{portfolio_name}' home screen...")

        try:
            WebDriverWait(self.driver, 25).until(
                EC.visibility_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID, portfolio_name.strip())
                )
            )
            print(f" Successfully redirected to '{portfolio_name}' home screen.")
        except TimeoutException:
            pytest.fail(
                f"Redirection verification failed — portfolio '{portfolio_name}' home screen not visible."
            )

    def redirect_back_holistic_screen(self):
        """
        Clicks on the Back button to return to the Holistic screen,
        then verifies successful redirection.
        """
        print(" Attempting to navigate back to the Holistic screen...")
        # Step 1: Back button locator
        back_button_xpath = (
            '//android.widget.FrameLayout[@resource-id="android:id/content"]'
            '/android.widget.FrameLayout/android.widget.FrameLayout'
            '/android.view.View/android.view.View/android.view.View'
            '/android.view.View[1]/android.view.View/android.view.View[1]'
            '/android.widget.Button[1]'
        )
        try:
            # Wait for the back button to be clickable and click it
            back_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, back_button_xpath))
            )
            back_button.click()
            print(" Back button clicked successfully.")
            time.sleep(2)
            # Step 2: Verify redirected to the Holistic (الرئيسية) screen
            home_xpath = '//android.view.View[@content-desc="الرئيسية"]'
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((AppiumBy.XPATH, home_xpath))
            )
            print(" Successfully redirected to the Holistic (الرئيسية) screen.")
        except TimeoutException:
            print(" Timeout: Could not verify redirection to the Holistic (الرئيسية) screen.")
            pytest.fail("Holistic (الرئيسية) screen was not displayed after clicking back.")
        except Exception as e:
            print(f" Unexpected error during redirection verification: {e}")
            pytest.fail(f"Unexpected error while redirecting: {e}")




