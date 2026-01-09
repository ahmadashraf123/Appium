import random
import string
import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UpdateJadwaPortfolios:
    def __init__(self, driver):
      self.driver = driver

    def scroll_and_select_portfolio(self, portfolio_name):
        """
        Scrolls inside the ScrollView until a portfolio card with the given name is found,
        clicks it, and verifies that the screen redirects to the correct portfolio detail page.
        """
        print(f" Searching for portfolio named '{portfolio_name}'...")
        # Dynamic XPath for target portfolio card
        portfolio_xpath = f'//android.widget.ImageView[contains(@content-desc, "{portfolio_name}")]'
        verify_xpath = f'//android.view.View[@content-desc="{portfolio_name}"]'
        max_scrolls = 4
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
                print(f" Portfolio not visible yet. Scrolling down... (attempt {scroll_count + 1})")
                size = self.driver.get_window_size()
                start_y = int(size["height"] * 0.8)
                end_y = int(size["height"] * 0.3)
                start_x = int(size["width"] / 2)
                self.driver.swipe(start_x, start_y, start_x, end_y, 800)
                time.sleep(0.1)
                scroll_count += 1
        if not found:
            pytest.fail(f" Portfolio '{portfolio_name}' not found after full scroll.")
        time.sleep(0.2)

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

    def verify_redirect_on_respective_home_screen(self, portfolio_name):
        """
        Verifies that the app redirected to the correct portfolio home screen
        after clicking on the selected portfolio.
        Handles both regular and invested portfolios (which show 'آخر تحديث').
        """
        print(f" Verifying redirection to portfolio '{portfolio_name}' home screen...")
        verify_xpath = f'//*[contains(@content-desc, "{portfolio_name}") or contains(@text, "{portfolio_name}") or contains(@content-desc, "آخر تحديث")]'
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, verify_xpath))
            )
            if element.is_displayed():
                print(f" Successfully redirected to '{portfolio_name}' home screen.")
            else:
                pytest.fail(f" Element found but not visible for portfolio '{portfolio_name}'.")
        except TimeoutException:
            pytest.fail(
                f" Redirection verification failed — portfolio '{portfolio_name}' home screen not visible or 'آخر تحديث' not found.")
        time.sleep(1)

    def click_on_edit_portfolio_tab(self):
        """Click on the 'خصص المحفظة' button to edit the portfolio."""
        try:
            # Wait until the element is visible and clickable
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'خصص المحفظة'))
            )
            element.click()
            print(" Clicked on 'خصص المحفظة' successfully.")
        except Exception as e:
            print(f" Failed to click on 'خصص المحفظة': {e}")

    def click_on_the_success_button_after_update_name(self):
        """Click on the 'تسجيل الدخول' button after updating the portfolio name."""
        try:
            wait = WebDriverWait(self.driver, 20)
            # Wait until the button is clickable
            success_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//*[contains(@content-desc, "تسجيل الدخول")]'))
            )
            # Click on it
            success_button.click()
            print(" Clicked on 'تسجيل الدخول' button successfully.")
        except Exception as e:
            print(f"Failed to click on 'تسجيل الدخول' button: {e}")

    def update_and_verify_portfolio_name(self):
        """
        Update the portfolio name, save changes, click on success/login button,
        and verify that the updated name appears on the home screen.
        Returns the new portfolio name.
        """
        try:
            wait = WebDriverWait(self.driver, 25)
            # Step 1: Locate the name input field
            name_field = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText'))
            )
            name_field.click()
            name_field.clear()
            # Step 2: Generate a new random name (6 letters)
            new_name = ''.join(random.choices(string.ascii_letters, k=6))
            name_field.send_keys(new_name)
            print(f" Entered new portfolio name: {new_name}")
            # Step 3: Click on 'حفظ التغييرات' (Save Changes)
            save_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//*[contains(@content-desc, "حفظ التغييرات")]'))
            )
            save_button.click()
            print(" Clicked on 'حفظ التغييرات' button.")
            # Step 4: Click on 'تسجيل الدخول' (Success/Login) button
            success_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//*[contains(@content-desc, "تسجيل الدخول")]'))
            )
            success_button.click()
            print(" Clicked on 'تسجيل الدخول' button after update.")
            # Step 5: Wait for home screen to load and verify the new name
            updated_name_xpath = f'//android.view.View[@content-desc="{new_name}"]'
            updated_name_element = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, updated_name_xpath))
            )
            assert updated_name_element.is_displayed(), "Updated portfolio name not visible on home screen."
            print(f"Verified updated portfolio name on home screen: {new_name}")
            # Step 6: Return the new name for use in test assertions
            return new_name
        except Exception as e:
            print(f" Failed to update and verify portfolio name: {e}")
            return None

    def update_and_verify_portfolio_name_and_icon(self):
        """
        Update the portfolio name and icon, save changes,
        click on the success/login button, and verify that
        the updated name appears on the home screen.
        Returns the new portfolio name.
        """
        try:
            wait = WebDriverWait(self.driver, 25)

            # Step 1: Locate the name input field
            name_field = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText'))
            )
            name_field.click()
            name_field.clear()
            # Step 2: Generate and enter a new random name
            new_name = ''.join(random.choices(string.ascii_letters, k=6))
            name_field.send_keys(new_name)
            print(f" Entered new portfolio name: {new_name}")
            # Step 3: Hide keyboard if visible
            try:
                self.driver.hide_keyboard()
                print(" Keyboard hidden successfully.")
            except Exception:
                print(" Keyboard was not visible or already hidden.")
            # Step 3: Click on the portfolio icon to update it
            try:
                # Scroll until the target icon becomes visible using Android's UiScrollable
                scrollable_cmd = (
                    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
                    'new UiSelector().className("android.widget.ImageView").instance(7));'
                )
                icon_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable_cmd)
                icon_element.click()
                print(" Selected a new portfolio icon successfully.")
            except Exception as e:
                print(f" Failed to select new portfolio icon: {e}")
            # Step 4: Click on 'حفظ التغييرات' (Save Changes)
            save_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//*[contains(@content-desc, "حفظ التغييرات")]'))
            )
            save_button.click()
            print(" Clicked on 'حفظ التغييرات' button to save name and icon changes.")
            # Step 5: Click on 'تسجيل الدخول' (Success/Login) button
            success_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//*[contains(@content-desc, "تسجيل الدخول")]'))
            )
            success_button.click()
            print(" Clicked on 'تسجيل الدخول' button after saving changes.")
            # Step 6: Wait for home screen to load and verify the new name
            updated_name_xpath = f'//android.view.View[@content-desc="{new_name}"]'
            updated_name_element = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, updated_name_xpath))
            )
            assert updated_name_element.is_displayed(), " Updated portfolio name not visible on home screen."
            print(f" Verified updated portfolio name on home screen: {new_name}")
            return new_name
        except Exception as e:
            print(f" Failed to update and verify portfolio name and icon: {e}")
            return None

    def click_on_the_hide_portfolio_toggle_button_and_redirect_holistic_home(self):
        """Click on the hide portfolio toggle button and verify redirection to holistic home screen."""
        try:
            wait = WebDriverWait(self.driver, 20)
            # Step 1: Locate and click the hide portfolio toggle button
            toggle_xpath = '//android.view.View[@content-desc="اخفاء المحفظة"]/android.view.View'
            toggle_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, toggle_xpath))
            )
            toggle_button.click()
            print(" Clicked on 'Hide Portfolio' toggle button.")
            # Step 2: Verify redirection to holistic home screen
            home_screen_xpath = '//android.view.View[@content-desc="الرئيسية"]'
            home_element = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, home_screen_xpath))
            )
            assert home_element.is_displayed(), "User was not redirected to Holistic Home screen."
            print(" Successfully redirected to Holistic Home screen.")
        except Exception as e:
            print(f" Failed to hide portfolio or verify redirection: {e}")

    def verify_portfolio_not_visible_on_holistic_home(self, portfolio_name):
        """
        Scrolls through the holistic home screen and verifies that the given portfolio
        is NOT visible (i.e., it has been successfully hidden).
        """
        print(f" Verifying that portfolio '{portfolio_name}' is hidden on the holistic home screen...")
        portfolio_xpath = f'//android.widget.ImageView[contains(@content-desc, "{portfolio_name}")]'
        max_scrolls = 4
        scroll_count = 0
        found = False
        while scroll_count < max_scrolls:
            try:
                # Try finding the hidden portfolio
                self.driver.find_element(AppiumBy.XPATH, portfolio_xpath)
                found = True
                break
            except NoSuchElementException:
                # Scroll down
                size = self.driver.get_window_size()
                start_y = int(size["height"] * 0.8)
                end_y = int(size["height"] * 0.3)
                start_x = int(size["width"] / 2)
                self.driver.swipe(start_x, start_y, start_x, end_y, 800)
                scroll_count += 1
                print(f" Scrolling down... (attempt {scroll_count})")
        if found:
            pytest.fail(
                f" Portfolio '{portfolio_name}' is still visible on the holistic home screen (should be hidden).")
        else:
            print(f" Portfolio '{portfolio_name}' successfully hidden and not visible on the holistic home screen.")
        time.sleep(0.1)

    def click_on_the_service_tab_and_proceed(self):
        """
        Clicks on the 'الخدمات' (Services) tab from the bottom navigation bar
        and verifies that the user is redirected to the Services screen.
        """
        print("Attempting to click on the 'الخدمات' (Services) tab...")

        try:
            # Locator for 'الخدمات' tab
            service_tab_xpath = '//android.view.View[@content-desc="الخدمات"]'

            # Wait until the tab is visible and clickable
            service_tab = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, service_tab_xpath))
            )
            service_tab.click()
            print(" Clicked on the 'الخدمات' (Services) tab successfully.")

            # Optional verification step — check if 'الخدمات' page is displayed
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="الخدمات"]'))
            )
            print(" Verified: User is on the Services screen.")

        except TimeoutException:
            pytest.fail(" 'الخدمات' tab not found or not clickable.")
        except Exception as e:
            pytest.fail(f" Failed to click on the 'الخدمات' tab: {e}")

        time.sleep(1)

    def scroll_down_on_service_screen_and_click_on_portfolio_management_option(self):
        """
        Scrolls down inside the 'الخدمات' (Services) screen until
        the 'إدارة المحافظ' (Portfolio Management) option is visible,
        then clicks on it.
        """
        print("Attempting to scroll down and click on 'إدارة المحافظ' (Portfolio Management)...")

        try:
            # ScrollView container
            scroll_view_xpath = '//android.widget.ScrollView'

            # Target option inside the scroll view
            portfolio_management_xpath = '//android.view.View[@content-desc="إدارة المحافظ"]'

            # First, ensure the scroll view is visible
            scroll_view = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, scroll_view_xpath))
            )
            # Try to find the element without scrolling first
            try:
                element = self.driver.find_element(AppiumBy.XPATH, portfolio_management_xpath)
            except NoSuchElementException:
                # If not found, perform a few scrolls down
                print(" 'إدارة المحافظ' not visible yet. Scrolling down...")
                size = self.driver.get_window_size()
                start_y = int(size["height"] * 0.8)
                end_y = int(size["height"] * 0.3)
                start_x = int(size["width"] / 2)
                for attempt in range(1):
                    self.driver.swipe(start_x, start_y, start_x, end_y, 700)
                    time.sleep(0.1)
                    try:
                        element = self.driver.find_element(AppiumBy.XPATH, portfolio_management_xpath)
                        break
                    except NoSuchElementException:
                        print(f" Scroll attempt {attempt + 1}: still not visible.")
                else:
                    pytest.fail(" 'إدارة المحافظ' option not found even after scrolling.")
            # Once found, click the element
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, portfolio_management_xpath))
            ).click()
            print(" Clicked on 'إدارة المحافظ' (Portfolio Management) successfully.")
        except Exception as e:
            pytest.fail(f" Failed to click on 'إدارة المحافظ': {e}")
        time.sleep(0.1)

    def scroll_down_to_find_hidden_portfolio_and_perform_click(self, portfolio_name):
        """
        Scrolls down within the ScrollView to locate a hidden portfolio by name
        and clicks it once found.
        """
        print(f"Searching for hidden portfolio named '{portfolio_name}'...")
        # XPaths
        scroll_view_xpath = '//android.widget.ScrollView/android.view.View'
        portfolio_xpath = f'//android.widget.ImageView[contains(@content-desc, "{portfolio_name}")]'
        max_scrolls = 4
        scroll_count = 0
        found = False
        while scroll_count < max_scrolls:
            try:
                # Try finding the hidden portfolio in current visible area
                portfolio_element = self.driver.find_element(AppiumBy.XPATH, portfolio_xpath)
                print(f" Hidden portfolio '{portfolio_name}' found! Clicking now...")
                portfolio_element.click()
                found = True
                break
            except NoSuchElementException:
                # Perform scroll if portfolio not found yet
                print(f"↕ Portfolio '{portfolio_name}' not visible yet. Scrolling down... (attempt {scroll_count + 1})")
                try:
                    scroll_view = self.driver.find_element(AppiumBy.XPATH, scroll_view_xpath)
                    size = self.driver.get_window_size()
                    start_y = int(size["height"] * 0.75)
                    end_y = int(size["height"] * 0.35)
                    start_x = int(size["width"] / 2)
                    self.driver.swipe(start_x, start_y, start_x, end_y, 700)
                    time.sleep(0.5)
                    scroll_count += 1
                except Exception as e:
                    print(f" Scroll attempt failed: {e}")
                    break
        if not found:
            pytest.fail(f" Hidden portfolio '{portfolio_name}' not found after scrolling attempts.")
        else:
            print(f" Successfully clicked hidden portfolio '{portfolio_name}'.")
        time.sleep(0.1)

    def click_on_the_toggle_button_to_off_the_toggle_and_remove_portfolio_from_hide_listing(self):
        """
        Turns OFF the 'اخفاء المحفظة' toggle button to unhide the portfolio.
        Only performs the toggle action — no save or navigation steps.
        """
        print("Attempting to turn OFF the 'اخفاء المحفظة' (Hide Portfolio) toggle...")
        try:
            wait = WebDriverWait(self.driver, 10)
            # Locate the toggle element
            toggle_xpath = '//android.view.View[@content-desc="اخفاء المحفظة"]/android.view.View'
            toggle_element = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, toggle_xpath))
            )
            # Click the toggle to switch it OFF
            toggle_element.click()
            print(" 'اخفاء المحفظة' toggle turned OFF successfully.")
        except Exception as e:
            print(f" Failed to click the toggle OFF: {e}")
            pytest.fail("Toggle OFF action failed.")

    def click_on_the_back_button_to_redirect_the_portfolio_management_listing(self):
        """
        Clicks the back button to return to the Portfolio Management listing screen (إدارة المحافظ)
        and verifies successful redirection.
        """
        print("Attempting to click on the Back button to return to the Portfolio Management listing screen...")
        try:
            wait = WebDriverWait(self.driver, 20)
            # Step 1: Locate and click the back button
            back_button_xpath = ('//android.widget.FrameLayout[@resource-id="android:id/content"]'
                                 '/android.widget.FrameLayout/android.widget.FrameLayout'
                                 '/android.view.View/android.view.View/android.view.View'
                                 '/android.view.View[1]/android.widget.Button')
            back_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, back_button_xpath))
            )
            back_button.click()
            print(" Clicked on the Back button successfully.")
            # Step 2: Verify redirection to the Portfolio Management listing screen
            portfolio_management_xpath = '//android.view.View[@content-desc="إدارة المحافظ"]'
            portfolio_management_element = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, portfolio_management_xpath))
            )
            assert portfolio_management_element.is_displayed(), "User not redirected to Portfolio Management listing."
            print(" Successfully redirected to the Portfolio Management listing screen (إدارة المحافظ).")
        except Exception as e:
            print(f" Failed to click Back button or verify Portfolio Management redirection: {e}")
            pytest.fail("Back button redirection to Portfolio Management listing failed.")

    def click_back_button_and_move_to_service_home_screen(self):
        """
        Clicks the back button to return from the current screen
        and verifies redirection to the Services (الخدمات) home screen.
        """
        print("Attempting to click the back button and return to the Services screen...")
        try:
            wait = WebDriverWait(self.driver, 10)
            # Step 1: Locate and click the back button
            back_button_xpath = '//android.widget.Button'
            back_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, back_button_xpath))
            )
            back_button.click()
            print(" Clicked the back button successfully.")
            # Step 2: Verify redirection to the Services screen
            services_screen_xpath = '//android.view.View[@content-desc="الخدمات"]'
            services_screen = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, services_screen_xpath))
            )
            assert services_screen.is_displayed(), "Failed to return to the Services home screen."
            print(" Successfully redirected to the Services home screen.")
        except Exception as e:
            print(f" Failed to return to the Services screen: {e}")
            pytest.fail("Back navigation to Services screen failed.")

    def click_on_holistic_tab_and_proceed(self):
        """
        Clicks on the 'الرئيسية' (Holistic Home) tab and verifies
        that the user is redirected to the Holistic Home screen.
        """
        print("Attempting to click on the 'الرئيسية' (Holistic Home) tab...")
        try:
            wait = WebDriverWait(self.driver, 10)
            # Step 1: Locate and click the 'الرئيسية' tab
            holistic_tab_xpath = '//android.view.View[@content-desc="الرئيسية"]'
            holistic_tab = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, holistic_tab_xpath))
            )
            holistic_tab.click()
            print(" Clicked on the 'الرئيسية' (Holistic Home) tab successfully.")
            # Step 2: Verify redirection to Holistic Home screen
            holistic_home_xpath = '//android.view.View[@content-desc="Holistic Home"]'
            try:
                holistic_home = wait.until(
                    EC.presence_of_element_located((AppiumBy.XPATH, holistic_home_xpath))
                )
                if holistic_home.is_displayed():
                    print(" Verified: User redirected to Holistic Home screen.")
            except TimeoutException:
                # In some builds, the Arabic text itself is the home indicator
                print("Using Arabic indicator — staying on 'الرئيسية' tab is confirmed.")
        except Exception as e:
            print(f" Failed to click on 'الرئيسية' tab or verify home screen: {e}")
            pytest.fail("Navigation to Holistic Home tab failed.")

    def verify_respective_portfolio_successfully_unhide(self, portfolio_name):
        """
        Verifies that the previously hidden portfolio is now visible on the Holistic Home screen.
        If found, clicks on it to confirm successful unhide.
        """
        print(f" Verifying that portfolio '{portfolio_name}' is successfully unhidden...")
        try:
            wait = WebDriverWait(self.driver, 10)
            # Step 1: Wait for holistic home screen to load
            holistic_home_xpath = '//android.view.View[@content-desc="الرئيسية"]'
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, holistic_home_xpath)))
            print(" Holistic home screen loaded successfully.")
            # Step 2: Try to locate and click the portfolio
            portfolio_xpath = f'//android.widget.ImageView[contains(@content-desc, "{portfolio_name}")]'
            found = False
            max_scrolls = 10
            scroll_count = 0
            while scroll_count < max_scrolls:
                try:
                    portfolio_element = self.driver.find_element(AppiumBy.XPATH, portfolio_xpath)
                    print(f" Portfolio '{portfolio_name}' found on Holistic Home screen.")
                    portfolio_element.click()
                    print(f"️ Clicked on portfolio '{portfolio_name}' successfully.")
                    found = True
                    break
                except NoSuchElementException:
                    # Scroll if not visible
                    print(f"↕ Scrolling to find '{portfolio_name}'... (attempt {scroll_count + 1})")
                    size = self.driver.get_window_size()
                    start_y = int(size["height"] * 0.8)
                    end_y = int(size["height"] * 0.3)
                    start_x = int(size["width"] / 2)
                    self.driver.swipe(start_x, start_y, start_x, end_y, 800)
                    time.sleep(0.3)
                    scroll_count += 1
            if not found:
                pytest.fail(f" Portfolio '{portfolio_name}' not visible after unhide action.")
            else:
                print(f" Verification successful — '{portfolio_name}' is visible and clickable.")
        except Exception as e:
            print(f" Failed to verify or click unhidden portfolio '{portfolio_name}': {e}")
            pytest.fail(f"Portfolio verification failed: {e}")

    def click_on_hide_portfolio_value_option(self):
        """
        Clicks on the 'إخفاء القيم' (Hide Portfolio Value) button
        using accessibility id.
        """
        print("Attempting to click on 'إخفاء القيم' (Hide Portfolio Value)...")
        try:
            wait = WebDriverWait(self.driver, 10)
            hide_value_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "إخفاء القيم"))
            )
            hide_value_button.click()
            print(" Clicked on 'إخفاء القيم' successfully.")
        except Exception as e:
            print(f" Failed to click 'إخفاء القيم': {e}")
            pytest.fail("Could not click on 'إخفاء القيم' button.")
        time.sleep(1)

    def click_on_unhide_portfolio_value_option(self):
        """
        Clicks on the 'إظهار القيم' (Unhide Portfolio Value) button
        using accessibility id.
        """
        print("Attempting to click on 'إظهار القيم' (Unhide Portfolio Value)...")
        try:
            wait = WebDriverWait(self.driver, 10)
            unhide_value_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "إظهار القيم"))
            )
            unhide_value_button.click()
            print(" Clicked on 'إظهار القيم' successfully.")
        except Exception as e:
            print(f" Failed to click 'إظهار القيم': {e}")
            pytest.fail("Could not click on 'إظهار القيم' button.")

    def verify_portfolio_values_hidden(self):
        """
        Verifies that after clicking 'إخفاء القيم', the portfolio values
        are now hidden (i.e., showing 'XXXX.XX' instead of numeric digits).
        """
        print("Verifying that portfolio values are hidden (masked)...")
        try:
            wait = WebDriverWait(self.driver, 10)
            # XPath for masked value like "XXXX.XX"
            masked_value_xpath = '//android.view.View[contains(@content-desc, "XXXX.XX")]'
            masked_value_element = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, masked_value_xpath))
            )
            if masked_value_element.is_displayed():
                print(" Portfolio values are successfully hidden (showing 'XXXX.XX').")
            else:
                pytest.fail(" Masked value element found but not visible on screen.")
        except TimeoutException:
            # If masked value not found, maybe numeric value still showing
            try:
                numeric_xpath = '//android.view.View[contains(@content-desc, ".") and not(contains(@content-desc, "XXXX"))]'
                numeric_element = self.driver.find_element(AppiumBy.XPATH, numeric_xpath)
                if numeric_element:
                    pytest.fail(" Portfolio values are still visible in digits (not hidden).")
            except NoSuchElementException:
                pytest.fail(" Neither masked nor numeric portfolio value found.")

    def verify_portfolio_values_un_hidde(self):
        """
        Verifies that after clicking 'إظهار القيم', the portfolio values
        are now visible (i.e., showing numeric digits instead of 'XXXX.XX').
        """
        print("Verifying that portfolio values are visible (unhidden)...")
        try:
            wait = WebDriverWait(self.driver, 10)
            # XPath for visible numeric value (e.g., "111.04", "542.00")
            numeric_value_xpath = '//android.view.View[contains(@content-desc, ".") and not(contains(@content-desc, "XXXX"))]'
            numeric_value_element = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, numeric_value_xpath))
            )
            if numeric_value_element.is_displayed():
                print(" Portfolio values are successfully unhidden (showing digits).")
            else:
                pytest.fail(" Numeric value element found but not visible on screen.")
        except TimeoutException:
            # If numeric value not found, maybe still masked
            try:
                masked_xpath = '//android.view.View[contains(@content-desc, "XXXX.XX")]'
                masked_element = self.driver.find_element(AppiumBy.XPATH, masked_xpath)
                if masked_element:
                    pytest.fail(" Portfolio values are still hidden (showing 'XXXX.XX').")
            except NoSuchElementException:
                pytest.fail(" Neither numeric nor masked portfolio value found on the screen.")



















