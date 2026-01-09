import string
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import random
import time
from faker import Faker

from abyan_project_automation.src.constants.wait_contants import LITTLE_WAIT
from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility, hard_wait

fake = Faker()
class CreateCashPortfolios:
    OTP = (AppiumBy.XPATH, '//android.view.View[@content-desc="ادخل رمز التحقق"]/preceding-sibling::android.view.View[1]')
    OTP_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    popup_1 = "تم تغيير اسامي المحافظ"
    popup_2 = "كيف كانت تجربتك مع مدير علاقتك؟"
    premium_popup_3 = "مرحبًا هزيم"
    SCROLL_BUTTON_TEXT = "إنشاء محفظة"
    CREATE_PORTFOLIO_SCREEN = "إختر نوع المحفظة"
    CREATE_PORTFOLIO_HOME = "تفاصيل المحفظة"
    PORTFOLIO_TARGET = "هدف المحفظة"
    ENTER_PORTFOLIO_NAME = "خصص المحفظة"
    CLICK_BUTTON = "التالي"
    PASSWORD_SCREEN_KEY_0 = (AppiumBy.ACCESSIBILITY_ID, "0")
    SUCCESS = "تم إنشاء المحفظة  "
    CLICK_PLAN_TILE = "انشأ خطة مالية\nحقق أهدافك واحصل على مكافآت !"
    CLICK_NEXT = "خطة مالية لأهدافك"
    PLAN_SCREEN = "مجموع الإيداعات"
    MONTHLY_AMOUNT = "عدد السنوات المتوقعة"
    NUMBER_OF_YEARS = "الدفعات الشهرية"
    ENABLE_NOTIFICATION_HEADER = (AppiumBy.ACCESSIBILITY_ID, "تفعيل الإشعارات")
    ENABLE_NOTIFICATION_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="السماح"]')
    PORTFOLIO_UPDATE_POPUP = (AppiumBy.XPATH, '//android.view.View[@content-desc="المحفظة الآمنة ''المتنوعة (آمنة)\n''المحفظة المتوازنة\n''المتنوعة (متوازنة)\n''محفظة النمو\n''المتنوعة (نمو)"]/android.view.View/android.view.View[2]')
    CONSERVATIVE_PORTFOLIO = (AppiumBy.ACCESSIBILITY_ID, 'المتنوعة\nلتنويع الأصول والمخاطر\nأسهم أمريكية\nأسهم سعودية\nعقارات\nصكوك')
    BACK_TO_HOLISTIC_BTN = 'new UiSelector().className("android.widget.Button").instance(0)'
    CASH_TAB = (AppiumBy.ACCESSIBILITY_ID, 'مدخراتك\n0.00\n' )
    START_SAVING_BTN = (AppiumBy.ACCESSIBILITY_ID, 'ابدأ بالادخار')
    CREATE_PORTFOLIO_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="انشئ فئات ادخاريةافرز ونظّم أموالك في مدخراتك"]')
    SELECTED_PORTFOLIO = (AppiumBy.ACCESSIBILITY_ID, 'فئة مخصصة')
    PRE_DEFINE_PORTFOLIO = (AppiumBy.ACCESSIBILITY_ID, 'إدخار عام')
    PORTFOLIO_NAME_FIELD =(AppiumBy.XPATH, '//android.widget.EditText')
    NEXT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'التالي')
    HOME_SCREEN = (AppiumBy.XPATH, '//android.view.View[@content-desc="الرئيسية"]')


    def __init__(self, driver):
        self.driver = driver

    def click_on_updated_portfolio_popup(self):
        try:
            # Wait up to 5 seconds for popup; adjust if needed
            popup_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((
                    AppiumBy.XPATH,
                    '//android.view.View[@content-desc="المحفظة الآمنة\nالمتنوعة (آمنة)\nالمحفظة المتوازنة\nالمتنوعة (متوازنة)\nمحفظة النمو\nالمتنوعة (نمو)"]/android.view.View/android.view.View[2]'
                ))
            )
            popup_button.click()
            print(" Clicked on the updated portfolio popup button.")
        except TimeoutException:
            print("Popup not visible, skipping.")
        except Exception as e:
            print(f"Error while clicking the popup: {e}")

    def click_on_feedback_popup(self):
        try:
            print("Checking for 'كيف كانت تجربتك مع مدير علاقتك؟' popup...")
            # Wait max 5 seconds to see if popup appears
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="كيف كانت تجربتك مع مدير علاقتك؟"]')))
            print("Popup found! Attempting to click the option...")
            # Click on the desired child view
            option_button = self.driver.find_element(
                AppiumBy.XPATH,'//android.view.View[@content-desc="كيف كانت تجربتك مع مدير علاقتك؟"]/android.view.View[1]/android.view.View[2]')
            option_button.click()
            print("Clicked on feedback option.")
        except TimeoutException:
            print("Popup not displayed — skipping to next test.")
        except Exception as e:
            print(f"Error while handling feedback popup: {e}")
            self.driver.save_screenshot("error_feedback_popup.png")

    def handle_premium_popup(self):
        try:
            print("Checking for premium popup...")

            # Try to find and click the premium button if it appears
            button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.Button[@content-desc="صفحة أبيان الخاصة"]')
                )
            )
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '//android.widget.Button[@content-desc="صفحة أبيان الخاصة"]')
                )
            ).click()
            print("Premium popup found and clicked.")
        except TimeoutException:
            print("Premium popup not displayed — skipping.")
        except Exception as e:
            print(f"Unexpected error while handling premium popup: {e}")

    def handle_enable_notifications_if_displays(self):
        """Tap on 'السماح' by coordinates if the notification screen appears."""
        try:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(
                self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
            )
            actions.w3c_actions.pointer_action.move_to_location(543, 1627)  # adjust coords if needed
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("Tapped on coordinates (543, 1627) for 'السماح'")
        except Exception as e:
            print(f"Failed to tap on coordinates. Reason: {e}")

    def scroll_and_click_create_portfolio_button(self):
        while True:
            try:
                element = self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiScrollable(new UiSelector().scrollable(true))'
                    f'.scrollIntoView(new UiSelector().description("{self.SCROLL_BUTTON_TEXT}"))'
                )
                element.click()
                print("Clicked on 'إنشاء محفظة' button.")
                break
            except NoSuchElementException:
                size = self.driver.get_window_size()
                start_y = int(size["height"] * 0.8)
                end_y = int(size["height"] * 0.2)
                start_x = int(size["width"] / 2)
                self.driver.swipe(start_x, start_y, start_x, end_y, 500)
            except Exception as e:
                print("Failed to click 'إنشاء محفظة' button:", str(e))
                raise

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

    def enter_otp(self):
        try:
            # Step 1: Detect OTP (Assuming OTP is available as content-desc)
            otp_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((AppiumBy.XPATH,
                                                '//android.view.View[@content-desc="ادخل رمز التحقق"]/preceding-sibling::android.view.View[1]'))
            )

            otp_code = otp_element.get_attribute("content-desc")
            if otp_code is None or otp_code == "":
                raise ValueError("OTP code is empty or not detected")
            print(f"Detected OTP: {otp_code}")
            # Step 2: Enter OTP dynamically
            otp_input = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText"))
            )
            otp_input.clear()  # Clear any pre-filled values before entering the OTP
            otp_input.click()
            # Handle OTP entry: Support for dynamic OTP lengths or format
            otp_input.send_keys(otp_code)
            print("OTP entered successfully.")
            # Optional: Wait for confirmation that OTP was accepted or process completed
            time.sleep(2)
        except ValueError as ve:
            print(f"OTP Value Error: {ve}")
        except Exception as e:
            print(f"Error during OTP entry: {e}")
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
                    (AppiumBy.XPATH, '//android.widget.Button[@content-desc="انتقل للمحفظة"]')
                )
            )
            button.click()
            print("Successfully clicked on 'انتقل للمحفظة' button.")
        except TimeoutException:
            self.driver.save_screenshot("error_go_to_portfolio_timeout.png")
            print("Could not find the 'انتقل للمحفظة' button. Screenshot saved.")
            raise AssertionError(" 'انتقل للمحفظة' button was not clickable within the timeout.")

    def scroll_and_click_random_before_create_portfolio(self):
        try:
            print("Scrolling to find 'إنشاء محفظة' button...")
            create_button_xpath = '//android.widget.Button[@content-desc="إنشاء محفظة"]'
            # Scroll manually till the button appears
            max_scrolls = 5
            for i in range(max_scrolls):
                try:
                    create_button = self.driver.find_element(AppiumBy.XPATH, create_button_xpath)
                    if create_button.is_displayed():
                        print(" 'إنشاء محفظة' button found!")
                        break
                except:
                    self.driver.swipe(500, 1500, 500, 500, 800)  # swipe up
                    time.sleep(1)
            else:
                raise TimeoutException("Button not found after scrolling.")
            # Get the button's Y location
            create_button = self.driver.find_element(AppiumBy.XPATH, create_button_xpath)
            create_button_location = create_button.location['y']
            # Get all visible elements above the button
            all_elements = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View | //android.widget.ImageView')
            clickable_above_elements = []
            for el in all_elements:
                try:
                    el_y = el.location['y']
                    is_clickable = el.get_attribute('clickable') == 'true'
                    if el_y < create_button_location and el.is_enabled() and is_clickable:
                        clickable_above_elements.append(el)
                except:
                    continue

            if not clickable_above_elements:
                print(" No clickable elements found above the button.")
                return
            # Click randomly
            random_element = random.choice(clickable_above_elements)
            desc = random_element.get_attribute('content-desc') or "no content-desc"
            print(f" Clicking on element above 'إنشاء محفظة' with content-desc: {desc}")
            random_element.click()
        except TimeoutException:
            print(" 'إنشاء محفظة' button not found even after scrolling.")
        except Exception as e:
            print(f"Error in scroll_and_click_random_before_create_portfolio: {e}")
            self.driver.save_screenshot("error_click_before_create_button.png")

    def click_create_financial_plan(self):
        try:
            print(" Trying to locate 'انشأ خطة مالية' banner...")
            # Use contains() to avoid exact newline and spacing issues
            xpath = '//android.widget.ImageView[contains(@content-desc, "انشأ خطة مالية")]'
            # Optionally scroll to it first (if it's not in view)
            self.driver.execute_script('mobile: scroll', {
                'strategy': AppiumBy.ANDROID_UIAUTOMATOR,
                'selector': 'new UiSelector().descriptionContains("انشأ خطة مالية")'
            })
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
            )
            self.driver.save_screenshot("before_click_create_plan.png")  # For debugging
            element.click()
            print("Clicked on the 'انشأ خطة مالية' banner successfully.")
        except TimeoutException:
            print("Timeout: 'انشأ خطة مالية' banner not clickable.")
            self.driver.save_screenshot("error_create_financial_plan_timeout.png")
            raise
        except Exception as e:
            print(f" Failed to click on the banner: {e}")
            self.driver.save_screenshot("error_create_financial_plan_generic.png")
            raise

    def click_continue_button(self):
        try:
            accessibility_id = "استمرار"
            print("Trying to scroll to the 'استمرار' button...")
            # Scroll until the element with text 'استمرار' is visible
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().description("{}").instance(0));'.format(accessibility_id)
            )
            print("Waiting for the 'استمرار' button to be clickable...")
            element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, accessibility_id))
            )
            element.click()
            print(" Clicked on the 'استمرار' button successfully.")
        except Exception as e:
            print(f" Failed to click on the 'استمرار' button: {e}")
            timestamp = int(time.time())
            self.driver.save_screenshot(f"error_continue_button_{timestamp}.png")
            raise

    def set_seekbar_value(self, seekbar_index, target_value, max_value):
        """
        Sets a specific value on a seekbar based on index.
        """
        try:
            time.sleep(2)
            seekbar_xpath = f"//android.widget.ScrollView/android.widget.SeekBar[{seekbar_index + 1}]"
            seek_bar = self.driver.find_element(AppiumBy.XPATH, seekbar_xpath)

            start_x = seek_bar.location['x']
            start_y = seek_bar.location['y']
            width = seek_bar.size['width']
            height = seek_bar.size['height']
            center_y = start_y + height // 2

            fraction = target_value / max_value
            target_x = start_x + int(width * fraction)

            #  W3C TOUCH ACTION (Appium v2)
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(
                self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
            )
            actions.w3c_actions.pointer_action.move_to_location(start_x, center_y)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.move_to_location(target_x, center_y)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

            print(f"SeekBar[{seekbar_index}] set to value '{target_value}' out of '{max_value}'")
            time.sleep(1)

        except Exception as e:
            print(f"Failed to set SeekBar[{seekbar_index}]: {e}")
            self.driver.save_screenshot(f"seekbar_error_{seekbar_index}.png")
            raise
    def click_on_the_portfolio_name_update_pop_up(self):
        """Handle the Portfolio update pop-up by tapping coordinates if it appears, otherwise skip."""
        try:
            # Try tapping on the pop-up coordinates
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(
                self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
            )
            actions.w3c_actions.pointer_action.move_to_location(93, 1254)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

            print(" Tapped at coordinates (93, 1254) for Portfolio name update pop-up.")
            hard_wait(2)  # wait briefly for transition

        except Exception as e:
            print(f" Skipping Portfolio update pop-up — not displayed or not clickable. Reason: {e}")

    def select_conservative_portfolio_type_and_proceed(self, timeout=10):
        """
        Selects the conservative portfolio option and clicks on the Proceed button.
        """
        try:
            # Click conservative portfolio
            portfolio_option = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.CONSERVATIVE_PORTFOLIO)
            )
            portfolio_option.click()
            print(" Conservative portfolio selected.")
        except TimeoutException:
            print(" Could not select conservative portfolio button not found.")

    def back_to_holistic_screen(self):
        """Click on back button to navigate to Holistic screen"""
        try:
            element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.BACK_TO_HOLISTIC_BTN)
            if element.is_displayed():
                element.click()
                print("Navigated back to Holistic screen successfully.")
            else:
                print("Back button not visible, skipping...")
        except NoSuchElementException:
            print("Back button not found, skipping...")

    def click_home(self):
        home_button = wait_for_element_visibility(
            self.driver,
            (AppiumBy.ACCESSIBILITY_ID, "الرئيسية"),
            20
        )

    def click_on_cash_tab_and_proceed_next_screen(self):
        print("🔍 Looking for Cash button (مدخراتك)...")

        try:
            cash_button = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().descriptionContains("مدخراتك")'
            )
            print(" Cash button found")

            cash_button.click()
            print("🖱 Cash button clicked")

        except Exception:
            print(" Cash button not found")
            return


        if wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, "مدخراتك"),
                timeout=10
        ):
            print(" User is on Cash screen")
        else:
            print(" User is NOT redirected Cash screen")

    def click_on_savings_tile(self):
        """
        Clicks on the 'مدخراتك' tile regardless of amount variation.
        """

        savings_locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().descriptionContains("مدخراتك")'
        )

        savings_tile = wait_for_element_visibility(
            self.driver,
            savings_locator,
            timeout=15
        )

        if not savings_tile:
            pytest.fail(" 'مدخراتك' tile not found")

        savings_tile.click()
        print(" Clicked on 'مدخراتك' tile")

    def click_on_start_saving_button_and_proceed(self):
        """Click on 'ابدأ بالادخار' button and proceed to next screen"""
        try:
            element = wait_for_element_visibility(self.driver,self.START_SAVING_BTN, 20)
            if element.is_displayed():
                element.click()
                print(" Clicked on 'ابدأ بالادخار' button. Proceeding to next screen...")
            else:
                print(" 'ابدأ بالادخار' button found but not visible. Skipping...")
        except NoSuchElementException:
            print(" 'ابدأ بالادخار' button not found. Skipping...")

    def click_on_categories_section(self):
        """Click on Categories section (الفئات الادخارية)."""

        hard_wait(5)
        print(" Clicking on Categories section...")

        categories_btn = wait_for_element_visibility(
            self.driver,
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().descriptionContains("الفئات الادخارية")'
            ),
            timeout=20
        )

        categories_btn.click()
        print("🖱 Categories section clicked")

        hard_wait(LITTLE_WAIT)

    def click_on_create_category_button(self):
        btn = wait_for_element_visibility(
            self.driver,
            (AppiumBy.ACCESSIBILITY_ID, "إنشاء فئة"),
            timeout=3,
            soft_fail=True
        )

        if not btn:
            btn = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().description("إنشاء فئة"))'
            )

        btn.click()
        hard_wait(LITTLE_WAIT)

    def click_on_Custom_Category_portfolio_and_proceed(self):
        """Click on selected portfolio (فئة مخصصة) and proceed to next screen"""
        try:
            element = wait_for_element_visibility(self.driver,self.SELECTED_PORTFOLIO, 15)
            if element.is_displayed():
                element.click()
                print(" Clicked on 'فئة مخصصة' portfolio. Proceeding to next screen...")
            else:
                print(" 'فئة مخصصة' found but not visible. Skipping...")
        except NoSuchElementException:
            print(" 'فئة مخصصة' portfolio not found. Skipping...")
        hard_wait(LITTLE_WAIT)


    def click_on_pre_define_portfolio_and_proceed(self):
        """Click on selected portfolio (إدخار عام) and proceed to next screen"""
        try:
            element = wait_for_element_visibility(self.driver,self.PRE_DEFINE_PORTFOLIO, 15)
            if element.is_displayed():
                element.click()
                print(" Clicked on 'إدخار عام' portfolio. Proceeding to next screen...")
            else:
                print(" 'إدخار عام' found but not visible. Skipping...")
        except NoSuchElementException:
            print(" 'إدخار عام' portfolio not found. Skipping...")
        hard_wait(LITTLE_WAIT)

    def select_field_and_input_portfolio_name_and_proceed(self):
        """Click field, enter random name (with space, no symbols), click التالي, and proceed"""
        try:
            # Step 1: Click field
            field = wait_for_element_visibility(self.driver, self.PORTFOLIO_NAME_FIELD, 15)
            if field and field.is_displayed():
                field.click()
                # Step 2: Generate random name with space (no symbols)
                portfolio_name = "Portfolio " + ''.join(random.choices(string.ascii_letters + string.digits, k=5))
                field.send_keys(portfolio_name)
                print(f" Entered portfolio name: {portfolio_name}")
                # Step 3: Click 'التالي' button
                next_btn = wait_for_element_visibility(self.driver, self.NEXT_BUTTON, 15)
                if next_btn and next_btn.is_displayed():
                    next_btn.click()
                    print(" Clicked on 'التالي' button. Proceeding to next screen...")
                else:
                    print(" 'التالي' button not visible.")
                # Step 4: Hide keyboard (if still open)
                try:
                    self.driver.hide_keyboard()
                except Exception:
                    pass  # ignore if already closed
                return portfolio_name
            else:
                print(" Portfolio name field not visible. Skipping...")
        except NoSuchElementException:
            print(" Portfolio name field or 'التالي' button not found. Skipping...")

    def input_amount_for_category_and_proceed(self):
        """Input random 2-digit amount, close keyboard, and click 'إنشاء الفئة' button"""
        try:
            # Step 1: Locate the EditText field
            amount_field = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            if amount_field.is_displayed():
                # Step 2: Generate random 2-digit number
                random_amount = str(random.randint(10, 99))
                # Step 3: Input into field
                amount_field.click()
                amount_field.clear()
                amount_field.send_keys(random_amount)
                print(f" Entered amount: {random_amount}")
                # Step 4: Hide keyboard (Appium driver method)
                try:
                    self.driver.hide_keyboard()
                    print(" Keyboard closed successfully.")
                except:
                    print(" Keyboard not present or could not be closed.")

            else:
                print(" Amount input field is not visible.")
        except Exception as e:
            print(f" Failed in input_amount_for_category_and_proceed: {e}")
            time.sleep(2)



    def click_to_create_saving_category(self):
        """Click on the 'الفئات الادخارية' (Saving Categories) section."""
        try:
            print(" Waiting for 'الفئات الادخارية' section to become visible...")
            # Step 1: Wait until element is visible using a partial match (safer for dynamic text)
            saving_categories = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "الفئات الادخارية")]'),
                timeout=25
            )
            # Step 2: Click if found
            if saving_categories:
                saving_categories.click()
                print(" Clicked on 'الفئات الادخارية' section successfully.")
            else:
                print(" 'الفئات الادخارية' section not found even after waiting.")
        except Exception as e:
            print(f" Exception while clicking on 'الفئات الادخارية' section: {e}")
        hard_wait(LITTLE_WAIT)

    def click_create_category_button_and_proceed(self):
        """Click on 'إنشاء فئة' (Create Category) button from the custom cash category home screen."""
        try:
            print(" Waiting for 'Create Category' button to appear...")
            # Flexible and more reliable locator (partial match)
            create_category_btn = wait_for_element_visibility(
                self.driver,
                (AppiumBy.ACCESSIBILITY_ID, 'إنشاء الفئة'),
                timeout=25
            )
            if create_category_btn:
                print(" 'Create Category' button found. Clicking now...")
                create_category_btn.click()
                print(" Clicked on ' إنشاء الفئة' button successfully.")
            else:
                print(" 'Create Category' button not found even after waiting.")
                return False
        except Exception as e:
            print(f" Exception while clicking on 'Create Category' button: {e}")
            return False
        hard_wait(LITTLE_WAIT)
        return True

    def click_on_create_category_button_and_proceed(self):
        """Click on the 'إنشاء فئة' (Create Category) button."""
        create_category_btn = wait_for_element_visibility(
            self.driver,
            (AppiumBy.XPATH, '//android.widget.Button[@content-desc="إنشاء فئة"]'),
            timeout=20
        )
        create_category_btn.click()
        print(" Clicked on 'إنشاء فئة' (Create Category) button successfully.")

    def click_button_to_create_custom_category_and_proceed(self):
        saving_categories_section = wait_for_element_visibility(
            self.driver,
            (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "الفئات الادخارية")]'),
            timeout=25
        )
        if saving_categories_section:
            saving_categories_section.click()
            print(" Clicked on 'الفئات الادخارية' section successfully.")
        else:
            print(" 'الفئات الادخارية' section not found.")

    def click_cash_portfolio_and_proceed(self):
        """Reliably click on the Cash Portfolio (مدخراتك) and proceed to the next screen."""
        try:
            print("Waiting for Cash Portfolio (مدخراتك) to appear...")
            # Step 1: Wait for the element to appear
            cash_portfolio = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "مدخراتك")]'),
                timeout=25
            )
            if cash_portfolio:
                print("Cash Portfolio found. Performing W3C action tap...")
                # Using W3C TouchAction for reliable tap
                actions = ActionChains(self.driver)
                actions.w3c_actions = ActionBuilder(
                    self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
                )
                # Get center coordinates of the element
                location = cash_portfolio.location
                size = cash_portfolio.size
                center_x = location['x'] + size['width'] // 2
                center_y = location['y'] + size['height'] // 2
                actions.w3c_actions.pointer_action.move_to_location(center_x, center_y)
                actions.w3c_actions.pointer_action.pointer_down()
                actions.w3c_actions.pointer_action.pause(0.1)
                actions.w3c_actions.pointer_action.release()
                actions.perform()
                print("Tap action performed on 'مدخراتك' (Cash Portfolio).")
                hard_wait(5)

                # Step 2: Verify navigation to “الفئات الادخارية” screen
                next_screen = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "الفئات الادخارية")]'),
                    timeout=10,
                    soft_fail=True
                )
                if next_screen:
                    print("Navigation to 'الفئات الادخارية' screen successful.")
                else:
                    print("Tap executed but navigation not detected. Retrying tap once...")
                    hard_wait(3)
                    # Retry tap
                    actions.w3c_actions.pointer_action.move_to_location(center_x, center_y)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.pause(0.1)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                    hard_wait(5)
                    # Verify again
                    next_screen_retry = wait_for_element_visibility(
                        self.driver,
                        (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "الفئات الادخارية")]'),
                        timeout=10,
                        soft_fail=True
                    )
                    if next_screen_retry:
                        print("Navigation successful after retry.")
                    else:
                        print("Still not navigated after retry.")
                        pytest.fail("Navigation to 'الفئات الادخارية' screen failed after tapping Cash Portfolio.")
            else:
                print("Cash Portfolio not found within timeout.")
                pytest.fail("Failed to locate Cash Portfolio (مدخراتك).")
        except Exception as e:
            print(f"Exception while clicking Cash Portfolio: {e}")
            pytest.fail(f"Failed to click on Cash Portfolio: {e}")

    def click_Skip_button_and_proceed(self):
        """Click on the 'تخطي' (Skip/Create) button to proceed."""
        try:
            print(" Waiting for the 'تخطي' (Skip) button to appear...")
            # Step 1: Wait for the 'تخطي' button
            skip_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.widget.Button[@content-desc="تخطي"]'),
                timeout=20
            )
            # Step 2: Click the button if found
            if skip_button:
                print(" 'تخطي' button found. Clicking now...")
                skip_button.click()
                hard_wait(3)
                print(" Clicked on 'تخطي' button successfully.")
            else:
                print("️ 'تخطي' button not found within timeout.")
                pytest.fail("Failed to find 'تخطي' button on screen.")
        except Exception as e:
            print(f"Exception while clicking 'تخطي' button: {e}")
            pytest.fail(f"Failed to click on 'تخطي' button: {e}")

    def tap_back_button(self):
        """Tap Android system back (icon-only back button)."""

        print("Clicked back button successfully. Navigated to Holistic Home screen.")
        self.driver.back()
        hard_wait(LITTLE_WAIT)


    def verify_cash_portfolio_home_screen(self):
        """Click on the Cash Portfolio (مدخراتك) and verify navigation to Cash Home Screen."""
        try:
            print(" Waiting for Cash Portfolio (مدخراتك) to appear...")

            # Wait for the element
            cash_portfolio = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "مدخراتك")]'),
                timeout=25
            )

            if not cash_portfolio:
                print(" Cash Portfolio not found within timeout.")
                pytest.fail("Failed to locate Cash Portfolio (مدخراتك).")

            print("Cash Portfolio found. Clicking on it...")
            cash_portfolio.click()
            hard_wait(5)

            # Verify navigation to Savings Categories screen
            categories_screen = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "الفئات الادخارية")]'),
                timeout=10,
                soft_fail=True
            )

            if not categories_screen:
                print(" Navigation not detected. Retrying click...")
                cash_portfolio.click()
                hard_wait(3)
                categories_screen = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "الفئات الادخارية")]'),
                    timeout=10,
                    soft_fail=True
                )
                if not categories_screen:
                    pytest.fail("Navigation to 'الفئات الادخارية' screen failed even after retry.")
                else:
                    print(" Navigation successful after retry click.")

            print(" User successfully navigated to 'الفئات الادخارية' screen.")

            # Verify redirection to Cash Home screen
            hard_wait(3)
            cash_home_screen = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.view.View[@content-desc="مدخراتك"]'),
                timeout=15,
                soft_fail=True
            )

            if cash_home_screen:
                print(" User successfully reached the Cash Home Screen ('مدخراتك').")
            else:
                print(" User not redirected to 'مدخراتك' screen as expected.")
                pytest.fail("Failed to verify Cash Home Screen after clicking Cash Portfolio.")

        except Exception as e:
            print(f" Exception while clicking Cash Portfolio: {e}")
            pytest.fail(f"Failed to click on Cash Portfolio: {e}")

    def redirect_holistic_screen_and_verify_user_is_on_holistic_screen(self):
        """
        Click on the 'Continue' (android.widget.Button) from the holistic screen
        and verify that the user is redirected to the Home screen (الرئيسية).
        """
        try:
            print(" Waiting for 'Continue' (android.widget.Button) to appear...")
            # Step 1: Wait for button visibility
            continue_button = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, '//android.widget.Button'),
                timeout=25
            )
            if continue_button:
                print(" 'Continue' button found. Clicking now...")
                continue_button.click()
                hard_wait(5)
                print("Clicked successfully. Waiting for Home screen...")
                # Step 2: Verify navigation to Home screen (الرئيسية)
                home_screen = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.XPATH, '//android.view.View[@content-desc="الرئيسية"]'),
                    timeout=15,
                    soft_fail=True
                )
                if home_screen:
                    print(" Successfully redirected to the Home screen (الرئيسية).")
                else:
                    print(" Button clicked but Home screen not detected. Retrying once...")
                    hard_wait(5)
                    continue_button.click()
                    hard_wait(5)
                    # Retry verification
                    home_screen_retry = wait_for_element_visibility(
                        self.driver,
                        (AppiumBy.XPATH, '//android.view.View[@content-desc="الرئيسية"]'),
                        timeout=10,
                        soft_fail=True
                    )
                    if home_screen_retry:
                        print(" Navigation successful after retry — user is on Home screen (الرئيسية).")
                    else:
                        print(" Still not navigated after retry.")
                        pytest.fail("Navigation to Home screen (الرئيسية) failed.")
            else:
                print(" 'Continue' button not found within timeout.")
                pytest.fail("Failed to locate 'Continue' button on holistic screen.")
        except Exception as e:
            print(f" Exception while clicking 'Continue' button: {e}")
            pytest.fail(f"Failed to click 'Continue' or navigate to Home screen: {e}")

    def click_on_pre_define_category_and_verify_home_screen(self, category_name):
        """
        Scroll and click on a predefined category by its name (content-desc).
        Example category_name: "Portfolio oHErd"
        """
        print(f" Looking for category: {category_name}")

        selector = (
            'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().descriptionContains("{category_name}"))'
        )

        category_element = wait_for_element_visibility(
            self.driver,
            (AppiumBy.ANDROID_UIAUTOMATOR, selector),
            timeout=15,
            soft_fail=False
        )

        print(f" Category '{category_name}' found. Clicking...")
        category_element.click()
        print("🖱 Category clicked successfully")

        hard_wait(LITTLE_WAIT)

    def verify_pre_define_category_home_screen(self, category_name):
        """
        Verify that the user is redirected to the correct pre-defined category home screen
        based on the portfolio name.
        Example: 'Portfolio oHErd'
        """
        try:
            print(f" Verifying user is on '{category_name}' home screen...")
            # Step 1: Wait for the home screen element matching portfolio name
            home_screen_element = wait_for_element_visibility(
                self.driver,
                (AppiumBy.XPATH, f'//android.view.View[@content-desc="{category_name}"]'),
                timeout=10,
                soft_fail=True
            )
            # Step 2: Verification result
            if home_screen_element:
                print(f" User successfully redirected to '{category_name}' home screen.")
            else:
                print(f" '{category_name}' home screen not found. Retrying check...")
                hard_wait(3)
                # Retry once
                home_screen_retry = wait_for_element_visibility(
                    self.driver,
                    (AppiumBy.XPATH, f'//android.view.View[@content-desc="{category_name}"]'),
                    timeout=5,
                    soft_fail=True
                )
                if home_screen_retry:
                    print(f" Verified after retry: '{category_name}' home screen displayed successfully.")
                else:
                    pytest.fail(f" Verification failed — '{category_name}' home screen not displayed.")
        except Exception as e:
            print(f" Exception during home screen verification for '{category_name}': {e}")
            pytest.fail(f"Failed to verify '{category_name}' home screen: {e}")




