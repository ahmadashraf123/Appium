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

from abyan_project_automation.src.andriod.pages.cash_portfolios_creation_page import fake


class CreateAlPacaPortfolios:
    def __init__(self, driver):
      self.driver = driver

    def scroll_and_click_create_portfolio_button(self):
        """
        Scrolls using UiScrollable until 'إنشاء محفظة' is visible, then clicks it.
        This avoids swipe crashes and socket hang up errors.
        """
        print("Searching for 'إنشاء محفظة' button using UiScrollable...")

        try:
            create_portfolio_button = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                (
                    'new UiScrollable(new UiSelector().scrollable(true))'
                    '.scrollIntoView(new UiSelector().description("إنشاء محفظة"))'
                )
            )

            create_portfolio_button.click()
            print("Clicked 'إنشاء محفظة' button successfully.")

        except Exception as e:
            pytest.fail(f"Failed to find or click 'إنشاء محفظة' button: {e}")


    def click_on_alpaca_portfolio(self):
        """Simply clicks on the 'المتنوعة' portfolio card."""
        try:
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "المتنوعة\nلتنويع الأصول والمخاطر\nأسهم أمريكية\nأسهم سعودية\nعقارات\nصكوك")
            element.click()
            print(" Clicked on 'المتنوعة' portfolio successfully.")
        except Exception as e:
            print(f" Failed to click on 'المتنوعة' portfolio: {e}")
            if hasattr(self, "take_screenshot"):
                self.take_screenshot("click_alpaca_portfolio_failure")
            raise


    def select_growth_portfolio_to_create_and_proceed(self):
        """Simply clicks on the 'نمو' portfolio card."""
        try:
            element = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='نمو']")
            element.click()
            print(" Clicked on 'نمو' portfolio successfully.")
        except Exception as e:
            print(f" Failed to click on 'نمو' portfolio: {e}")
            if hasattr(self, "take_screenshot"):
                self.take_screenshot("click_growth_portfolio_failure")
            raise

    def click_create_portfolio_button(self):
        """Clicks on the 'إنشاء المحفظة' (Create Portfolio) button."""
        try:
            element = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='إنشاء المحفظة']")
            element.click()
            print(" Clicked on 'إنشاء المحفظة' button successfully.")
        except Exception as e:
            print(f" Failed to click on 'إنشاء المحفظة' button: {e}")
            if hasattr(self, "take_screenshot"):
                self.take_screenshot("click_create_portfolio_failure")
            raise

    def click_portfolio_success_button(self):
        """
        Waits for and clicks the 'انتقل للمحفظة' (Go to Portfolio) button.
        """
        try:
            print("Waiting for 'انتقل للمحفظة' button to become clickable...")
            time.sleep(2)  # Give time for transition animation if needed

            button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, 'انتقل للمحفظة')
                )
            )
            button.click()
            print("Successfully clicked on 'انتقل للمحفظة' button.")
        except TimeoutException:
            self.driver.save_screenshot("error_go_to_portfolio_timeout.png")
            print("Could not find the 'انتقل للمحفظة' button. Screenshot saved.")
            raise AssertionError(" 'انتقل للمحفظة' button was not clickable within the timeout.")

    # def holistic_screen_scroll_until_end(self):
    #     """
    #     Continuously scrolls down until the bottom of the page is reached
    #     or until the max scroll limit is hit.
    #     """
    #     print(" Starting to scroll down...")
    #     max_scrolls = 10  # safety limit to prevent infinite scroll
    #     scroll_count = 0
    #     last_page_source = ""
    #     while scroll_count < max_scrolls:
    #         current_page_source = self.driver.page_source
    #         # Check if we've reached the end (no new content)
    #         if current_page_source == last_page_source:
    #             print(" Reached the end of the scrollable content.")
    #             break
    #         # Perform scroll
    #         size = self.driver.get_window_size()
    #         start_y = int(size["height"] * 0.8)
    #         end_y = int(size["height"] * 0.3)
    #         start_x = int(size["width"] / 2)
    #         self.driver.swipe(start_x, start_y, start_x, end_y, 800)
    #         scroll_count += 1
    #         print(f"↕ Scrolling down... attempt {scroll_count}")
    #
    #         last_page_source = current_page_source
    #         time.sleep(1)
    #     print(" Finished scrolling.")

    def select_moderate_portfolio(self):
        """Selects the 'متوازنة' (Balanced) portfolio option."""
        try:
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "متوازنة")
            element.click()
            print("Clicked on 'متوازنة' portfolio successfully.")
        except Exception as e:
            print(f" Failed to click on 'متوازنة' portfolio: {e}")
            if hasattr(self, "take_screenshot"):
                self.take_screenshot("click_balanced_portfolio_failure")
            raise
    def select_conservative_portfolio(self):
        """Selects the 'آمنة' (conservative) portfolio option."""
        try:
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "آمنة")
            element.click()
            print("Clicked on 'آمنة' portfolio successfully.")
        except Exception as e:
            print(f" Failed to click on 'آمنة' portfolio: {e}")
            if hasattr(self, "take_screenshot"):
                self.take_screenshot("click_conservative_portfolio_failure")
            raise
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
        Selects the 7th goal icon (based on ImageView index).
        """
        goal_icon_xpath = (
            '//android.view.View[@content-desc="رفض"]/android.view.View/android.view.View'
            '/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.ImageView[7]'
        )

        goal_icon = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, goal_icon_xpath))
        )
        goal_icon.click()
        print("Goal icon selected successfully.")

    def click_on_edit_text_field(self):
        """Clicks on the EditText field."""
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.EditText"))
            )
            element.click()
            print("Clicked on EditText successfully.")
        except Exception as e:
            print(f" Failed to click on EditText: {e}")
            if hasattr(self, "take_screenshot"):
                self.take_screenshot("click_edittext_failure")
            raise
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
    def click_on_portfolio_children_target(self):
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

    def select_children_icon_proceed(self):
        """
        Selects the 4th goal icon (children) and proceeds.
        """
        children_icon_xpath = (
            '//android.view.View[@content-desc="رفض"]/android.view.View/android.view.View'
            '/android.view.View[2]/android.widget.ImageView[4]'
        )

        children_icon = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, children_icon_xpath))
        )
        children_icon.click()
        print("Children goal icon selected successfully.")





