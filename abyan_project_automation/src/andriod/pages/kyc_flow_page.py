import pytest
import unicodedata
from appium.webdriver.common.appiumby import AppiumBy
import random, string, time
import unicodedata
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from attr.converters import optional
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.webdriver import WebDriver

from abyan_project_automation.src.constants.wait_contants import LITTLE_WAIT, MID_WAIT
from abyan_project_automation.src.utils.gesture_Utils import scroll_to_element_and_click
from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility, hard_wait, \
    wait_for_all_elements_to_be_visibility


class KYCFlow:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.arabic_months = {
            "يناير": 1,
            "فبراير": 2,
            "مارس": 3,
            "أبريل": 4,
            "مايو": 5,
            "يونيو": 6,
            "يوليو": 7,
            "أغسطس": 8,
            "سبتمبر": 9,
            "أكتوبر": 10,
            "نوفمبر": 11,
            "ديسمبر": 12
        }
        # Arabic month mapping
        self.month_map_ar = {
            1: "يناير",  # January
            2: "فبراير",  # February
            3: "مارس",  # March
            4: "أبريل",  # April
            5: "مايو",  # May
            6: "يونيو",  # June
            7: "يوليو",  # July
            8: "أغسطس",  # August
            9: "سبتمبر",  # September
            10: "أكتوبر",  # October
            11: "نوفمبر",  # November
            12: "ديسمبر"  # December
        }
        # Reverse mapping: int to Arabic name
        self.int_to_arabic_month = {v: k for k, v in self.arabic_months.items()}
        KEYCODE_MAPPING = {
            'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35,
            'h': 36, 'i': 37, 'j': 38, 'k': 39, 'l': 40, 'm': 41, 'n': 42,
            'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48, 'u': 49,
            'v': 50, 'w': 51, 'x': 52, 'y': 53, 'z': 54,
            '0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13,
            '7': 14, '8': 15, '9': 16,
            '@': 77, '.': 56
        }
        # Locators
    NEXT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "التالي")
    USER_IMAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')
    PHONE_INPUT = (AppiumBy.CLASS_NAME, 'android.widget.ImageView')
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "إستمر")
    PASSWORD_SCREEN_HEADER = (AppiumBy.ACCESSIBILITY_ID, "أدخل رمز المرور")
    PASSWORD_SCREEN_KEY_0 = (AppiumBy.ACCESSIBILITY_ID, "0")
    OTP = (AppiumBy.XPATH, '//android.view.View[@content-desc="ادخل رمز التحقق"]/preceding-sibling::android.view.View[1]')
    OTP_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    KYC_HEADER = (AppiumBy.ACCESSIBILITY_ID, "إنشاء حساب")
    OTP_ERROR_MESSAGE = (AppiumBy.XPATH, "//android.view.View[@content-desc='رمز التحقق غير صحيح']")
    IDCARD_INPUT_FIELD = (AppiumBy.XPATH, "//android.widget.EditText")
    DOB_FIELD = (AppiumBy.XPATH, "//android.widget.ImageView")
    CONFIRM_BTN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='تأكيد التاريخ']")
    CLICK_CONTINUE = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="إستمر"]')
    BIRTHDAY_SELECT_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(11)')
    YEAR_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.SeekBar").index(2)')
    MONTH_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.SeekBar").index(4)')
    DAY_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.SeekBar").index(3)')
    MONTH = (AppiumBy.XPATH, '//android.widget.SeekBar[@content-desc="ديسمبر"]')
    # MONTH = (AppiumBy.XPATH, '//android.widget.NumberPicker[1]')
    BIRTHDAY_POPUP_CLOSE = (AppiumBy.ACCESSIBILITY_ID, 'تأكيد التاريخ')
    LOADER = (AppiumBy.ID, 'إستمر')
    CLICK_NEXT = (AppiumBy.ACCESSIBILITY_ID, 'إستمر')
    WELCOME_TEXT = (AppiumBy.CLASS_NAME, 'android.widget.ImageView')
    ADDRESS_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'العنوان')
    # Locators for Address Selection Screen
    CITY_FIELD = (AppiumBy.XPATH, '//android.view.View[@content-desc="العنوان"]/android.view.View[1]')
    CITY_DROPDOWN_ITEMS = (AppiumBy.XPATH, '//android.widget.EditText/android.view.View[2]//android.view.View[@content-desc]')
    SELECTED_ITEM = (AppiumBy.XPATH, '//android.view.View[@content-desc="العنوان"]//android.view.View[@text]')
    CITY_FIELD_SEARCH = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(8)')
    CITY_INPUT = (AppiumBy.XPATH,'//android.widget.EditText')
    CITY_OPTION = (AppiumBy.ACCESSIBILITY_ID, 'الرياض\nRIYADH')
    ADDRESS_FIELD = (AppiumBy.XPATH, '//android.view.View[@content-desc="العنوان"]/android.view.View[2]')
    DIST_OPTION = (AppiumBy.ACCESSIBILITY_ID, 'حي الملك عبدالله\nKing Abdullah Dist.')
    ADDRESS_DROPDOWN_ITEMS = (AppiumBy.XPATH, '//android.view.View[@content-desc and not(@content-desc="")]')
    ADDRESS = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("حي المرقب Al Marqab Dist.")')
    #Locators for InvestmentKnowledge Screen
    INVESTMENT_HEADER_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'المعرفة الاستثمارية')
    KNOWLEDGE_SCREEN_HEADER = (AppiumBy.ACCESSIBILITY_ID, 'المعرفة الاستثمارية')
    # KNOWLEDGE_LOW = (AppiumBy.ACCESSIBILITY_ID, "مبتدئ في الاستثمار\nأنا جديد في مجال الاستثمار، ليس لدي أي  معرفة بالاستثمار")
    KNOWLEDGE_LOW = (AppiumBy.ACCESSIBILITY_ID,'مبتدئ في الاستثمار\nأنا جديد في مجال الاستثمار، ليس لدي أي  معرفة بالاستثمار')
    # Low knowledge screen locators
    SCROLL_VIEW = (AppiumBy.XPATH,'//android.widget.ScrollView')
    # Wrong investment option
    INVESTMENT_WRONG_OPTION = (AppiumBy.XPATH,'//android.view.View[@content-desc="شراء أرض"]')
    # Correct investment option
    INVESTMENT_CORRECT_OPTION = (AppiumBy.XPATH,'//android.view.View[@content-desc="الاستثمار في صندوق مؤشر للعقارات"]')
    NEXT_BTN = (AppiumBy.XPATH,'//android.widget.Button[@content-desc="التالي"]')
    KNOWLEDGE_MEDIUM = (AppiumBy.ACCESSIBILITY_ID, 'أدرك أساسيات الاستثمار\nأدرك أساسيات الاستثمار والأسواق المالية')
    KNOWLEDGE_HIGH = (AppiumBy.ACCESSIBILITY_ID, "لدي بعض الخبرة\n لدي خبرات استثمارية سابقة، أدرك مفاهيم الاستثمار الأساسية.")
    KNOWLEDGE_VERY_HIGH = (AppiumBy.ACCESSIBILITY_ID, "مستثمر خبير\nأدير محفظتي بشكل نشط، أملك خبرة استثمارية عالية.")
    # Locators for EducationLevel Screen
    EDUCATION_PRIMARY = (AppiumBy.ACCESSIBILITY_ID, 'ابتدائي')
    EDUCATION_INTERMEDIATE = (AppiumBy.ACCESSIBILITY_ID, 'متوسط')
    EDUCATION_HIGH = (AppiumBy.ACCESSIBILITY_ID, 'ثانوي')
    EDUCATION_DIPLOMA = (AppiumBy.ACCESSIBILITY_ID, 'دبلوم')
    EDUCATION_BACHELOR = (AppiumBy.ACCESSIBILITY_ID, 'بكالوريوس')
    EDUCATION_HIGHER = (AppiumBy.ACCESSIBILITY_ID, 'دراسات عليا')
    # Locators for EmploymentStatus Screen
    EMPLOYMENT_STUDENT = (AppiumBy.ACCESSIBILITY_ID, 'طالب')
    EMPLOYMENT_FREELANCE = (AppiumBy.ACCESSIBILITY_ID, 'موظف')
    INPUT_RANDOM_FIELD_ONE = (AppiumBy.XPATH,'(//android.widget.ScrollView//android.widget.EditText)[1]')
    SECOND_INPUT_CONTAINER = (AppiumBy.XPATH,'(//android.widget.ScrollView/android.view.View[2]//android.view.View)[1]')
    DROPDOWN_OPTIONS = (AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]//android.view.View[@content-desc]')
    SELECTED_VALUE_FIELD = (AppiumBy.XPATH,'(//android.widget.ScrollView/android.view.View[2]//android.view.View)[1]')
    INPUT_RANDOM_FIELD_THREE = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View/android.widget.EditText[2]')
    INPUT_RANDOM_FIELD_FOUR = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View/android.widget.EditText[3]')
    EMPLOYMENT_EMPLOYED = (AppiumBy.ACCESSIBILITY_ID, 'عمل خاص')
    EMPLOYMENT_RETIRED = (AppiumBy.ACCESSIBILITY_ID, 'متقاعد')
    EMPLOYMENT_UNEMPLOYED = (AppiumBy.ACCESSIBILITY_ID, 'غير موظف')
    # Locators for IncomeSource Screen
    INCOME_JOB = (AppiumBy.ACCESSIBILITY_ID, 'وظيفة')
    INCOME_BUSINESS = (AppiumBy.ACCESSIBILITY_ID, 'عمل تجاري')
    INCOME_INHERITANCE = (AppiumBy.ACCESSIBILITY_ID, 'ميراث')
    INCOME_SAVINGS = (AppiumBy.ACCESSIBILITY_ID, 'ادخار')
    INCOME_FAMILY = (AppiumBy.ACCESSIBILITY_ID, 'أسرة')
    INCOME_INVESTMENT = (AppiumBy.ACCESSIBILITY_ID, 'استثمار')
    # Locators for SocialStatus Screen
    SOCIAL_STATUS_SINGLE = (AppiumBy.ACCESSIBILITY_ID, 'أعزب')
    SOCIAL_STATUS_MARRIED = (AppiumBy.ACCESSIBILITY_ID, 'متزوج')
    DIGIT_FIELD = (AppiumBy.XPATH, "//android.widget.EditText")
    SOCIAL_STATUS_DIVORCED = (AppiumBy.ACCESSIBILITY_ID, 'مطلق')
    SOCIAL_STATUS_WIDOW = (AppiumBy.ACCESSIBILITY_ID, 'أرمل')
    # Locators for AnnualIncome Screen
    ANNUAL_INCOME_OPTION1 = (AppiumBy.XPATH, '//android.view.View[@content-desc="أقل من 8 ألف"]')
    ANNUAL_INCOME_OPTION2 = (AppiumBy.ACCESSIBILITY_ID, 'من 8 ألف الى 25 ألف')
    ANNUAL_INCOME_OPTION3 = (AppiumBy.ACCESSIBILITY_ID, 'من 25 ألف الى 50 ألف')
    ANNUAL_INCOME_OPTION4 = (AppiumBy.ACCESSIBILITY_ID, 'من 50 ألف الى 125 ألف')
    ANNUAL_INCOME_OPTION5 = (AppiumBy.ACCESSIBILITY_ID, 'من 125 ألف الى 415 ألف')
    ANNUAL_INCOME_OPTION6 = (AppiumBy.ACCESSIBILITY_ID, 'من 415 ألف الى 830 ألف')
    ANNUAL_INCOME_OPTION7 = (AppiumBy.ACCESSIBILITY_ID, 'من 830 ألف الى 4 مليون')
    ANNUAL_INCOME_OPTION8 = (AppiumBy.ACCESSIBILITY_ID, '4 مليون وأكثر')
    # Locators for NetWorth Screen
    NET_WORTH_OPTION1 = (AppiumBy.XPATH, '//android.view.View[@content-desc="أقل من 100 ألف"]')
    NET_WORTH_OPTION2 = (AppiumBy.ACCESSIBILITY_ID, 'من 100 ألف الى 300 ألف')
    NET_WORTH_OPTION3 = (AppiumBy.ACCESSIBILITY_ID, 'من 300 ألف الى 600 ألف')
    NET_WORTH_OPTION4 = (AppiumBy.ACCESSIBILITY_ID, '600 ألف الى مليون ونصف')
    NET_WORTH_OPTION5 = (AppiumBy.ACCESSIBILITY_ID, 'مليون ونصف الى 5 مليون')
    NET_WORTH_OPTION6 = (AppiumBy.ACCESSIBILITY_ID, '5 مليون الى 10 مليون')
    NET_WORTH_OPTION7 = (AppiumBy.ACCESSIBILITY_ID, '10 مليون الى 50 مليون')
    NET_WORTH_OPTION8 = (AppiumBy.ACCESSIBILITY_ID, 'أكثر من 50 مليون')
    # Locators for RiskAbility Screen
    RISK_ABILITY_VERY_LOW = (AppiumBy.ACCESSIBILITY_ID, 'مخاطر منخفضة جدًا')
    RISK_ABILITY_LOW = (AppiumBy.ACCESSIBILITY_ID, 'مخاطر منخفضة')
    RISK_ABILITY_MEDIUM = (AppiumBy.ACCESSIBILITY_ID, 'مخاطر متوسطة')
    RISK_ABILITY_HIGH = (AppiumBy.ACCESSIBILITY_ID, 'مخاطر عالية')
    RISK_ABILITY_VERY_HIGH = (AppiumBy.ACCESSIBILITY_ID, 'مخاطر عالية جدًا')
    # Locators for InvestmentTimePeriod Screen
    INVESTMENT_TIME_PERIOD_OPTION1 = (AppiumBy.ACCESSIBILITY_ID, 'أقل من سنة')
    INVESTMENT_TIME_PERIOD_OPTION2 = (AppiumBy.ACCESSIBILITY_ID, 'من سنة إلى 5 سنوات')
    INVESTMENT_TIME_PERIOD_OPTION3 = (AppiumBy.ACCESSIBILITY_ID, 'أكثر من 5 سنوات')
    # Locators for InvestmentGoals Screen
    INVESTMENT_GOALS_CAPITAL_GROWTH = (AppiumBy.ACCESSIBILITY_ID, 'المحافظة على رأس المال')
    INVESTMENT_GOALS_PROTECTING_CAPITAL = (AppiumBy.ACCESSIBILITY_ID, 'نمو رأس المال')
    BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="استمر"]')
    # Locators for TaxResidentModel Screen
    TAX_RESIDENT_NO = (AppiumBy.XPATH, '//android.view.View[@content-desc="لا"]')
    TAX_RESIDENT_YES = (AppiumBy.ACCESSIBILITY_ID, 'نعم')
    STATE_FIELD = (AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]')
    STATE_OPTION =(AppiumBy.ACCESSIBILITY_ID, 'الولايات المتحدة\nUnited States')
    STATE_OPTIONS = (AppiumBy.XPATH,'//android.widget.EditText/android.view.View/android.view.View//android.view.View[@content-desc]')
    CON_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="التالي"]')
    TIN_NO_OPTION = (AppiumBy.XPATH, '//android.view.View[@content-desc="لا"]')
    TIN_YES = (AppiumBy.XPATH, '//android.view.View[@content-desc="نعم"]')
    TIN_INPUT = (AppiumBy.XPATH, '//android.widget.EditText')
    OTHER_OPTION = (AppiumBy.XPATH, '//android.view.View[@content-desc="آخر"]')
    OTHER_TEXT_FIELD = (AppiumBy.XPATH, '//android.widget.EditText')
    BUTTON_CONTINUE = (AppiumBy.ACCESSIBILITY_ID, 'إنشاء حساب')
    EMAIL_SCREEN = (AppiumBy.ACCESSIBILITY_ID,'البريد الإلكتروني')
    EMAIL_INPUT = (AppiumBy.CLASS_NAME, 'android.widget.EditText')
    DOMAINS = ["@gmail.com", "@hotmail.com"]
    CREATE_SUCCESS_SCREEN = (AppiumBy.ACCESSIBILITY_ID, ' "في طور اقتراح المحفظة الاستثمارية الأنسب لك"')
    CREATE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'إنشاء المحفظة')
    OTP_CREATE_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="create_otp_input"]')
    OTP_CODE = (AppiumBy.XPATH, '//android.view.View[@content-desc and string-length(@content-desc)=4]')
    OTP_INPUT_FIELD = (AppiumBy.CLASS_NAME, 'android.widget.EditText')
    HOME_SCREEN = (AppiumBy.XPATH, '//android.view.View[@content-desc="الرئيسية"]')
    PORTFOLIO_TYPE = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc,"محفظة")]')
    CHANGE_PORTFOLIO_TYPE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0))''.scrollIntoView(new UiSelector().className("android.widget.Button").description("تغيير نوع المحفظة"));')
    SELECT_CONSERVATIVE = ( AppiumBy.ACCESSIBILITY_ID,"المتنوعة (آمنة)\nعائد يصل إلى %8+ سنويًا")

    def click_welcomescreen_next_buttons(self, times=3):
        user_present = wait_for_element_visibility(self.driver, self.USER_IMAGE, LITTLE_WAIT,soft_fail=True)
        if user_present:
            print("User selection screen detected — skipping 'next' button clicks.")
            return
        else:
            for _ in range(times):
                next_button = wait_for_element_visibility(self.driver, self.NEXT_BUTTON, 10,soft_fail=True)
                if next_button:
                    time.sleep(2)
                    next_button.click()
                else:
                    print("Next button not found — skipping remaining clicks.")
                    break

    def select_user(self):
        user_element = wait_for_element_visibility(self.driver, self.USER_IMAGE, 10,soft_fail=True)
        if user_element:
            user_element.click()
            print("User selected successfully.")
        else:
            print("User image not visible — skipping user selection step.")

    def enter_phone_number(self, phone_number):
        phone_input = wait_for_element_visibility(self.driver, self.PHONE_INPUT, 20)
        if phone_input:
            phone_input.click()
            time.sleep(5)
            phone_input = wait_for_element_visibility(self.driver, self.PHONE_INPUT, 10)
            phone_input.send_keys(phone_number)
        else:
            print("Phone input field not found.")

    def click_continue(self):
        continue_button = wait_for_element_visibility(self.driver, self.CONTINUE_BUTTON, 20)
        if continue_button:
            continue_button.click()
        else:
            print("Continue button not found.")

    def enter_password(self):
       # wait_for_element_visibility(self.driver, self.PASSWORD_SCREEN_HEADER, LONG_WAIT)
        zero_button = wait_for_element_visibility(self.driver, self.PASSWORD_SCREEN_KEY_0, MID_WAIT)
        if zero_button:
            for _ in range(6):
                zero_button.click()
                time.sleep(0.3)
        else:
            print("Key '0' not found on password screen.")

    def enter_otp_code(self):
        try:
            # Step 1: Locate the OTP element just above the "ادخل رمز التحقق" label
            otp_element = wait_for_element_visibility(self.driver, self.OTP, 20)
            # Step 2: Extract OTP digits from content-desc
            otp_code = otp_element.get_attribute("content-desc")
            print(f"Detected OTP: {otp_code}")
            # Step 3: Wait for the EditText input field to be ready
            otp_input = wait_for_element_visibility(self.driver,self.OTP_INPUT, 10)
            # Step 4: Enter the OTP code as a whole into the field
            otp_input.click()
            otp_input.send_keys(otp_code)
            print("OTP entered successfully.")
            time.sleep(3)  # Optional pause for UI to transition
        except Exception as e:
            print(f"Error entering OTP: {str(e)}")

    def enter_Id_card_number(self, idcardnumber):
        idcard = wait_for_element_visibility(self.driver, self.IDCARD_INPUT_FIELD, 20)
        idcard.click()
        idcard.send_keys(idcardnumber)
        try:
            self.driver.hide_keyboard()
            print("keyboard hidden successfully")
        except Exception as e:
            print("could not hide keyboard", e)

    def enter_invalid_Id_card_number(self, id_number = str):
        idcard = wait_for_element_visibility(self.driver, self.IDCARD_INPUT_FIELD, 20)
        idcard.click()
        idcard.send_keys(id_number)
        try:
            self.driver.hide_keyboard()
            print("keyboard hidden successfully")
        except Exception as e:
            print("could not hide keyboard", e)

    def click_dob_field(self):
        """Click DOB field to open date picker"""
        self.driver.find_element(*self.DOB_FIELD).click()
        time.sleep(1)

    def select_random_dob(self):
        """Swipe pickers randomly to select Year / Month / Day (W3C actions)"""

        finger = PointerInput(PointerInput.TOUCH, "finger")
        actions = ActionBuilder(self.driver, mouse=finger)

        year_swipes = random.randint(1, 5)
        month_swipes = random.randint(1, 12)
        day_swipes = random.randint(1, 28)

        for _ in range(year_swipes):
            actions.pointer_action.move_to_location(300, 1500)
            actions.pointer_action.pointer_down()
            actions.pointer_action.pause(0.5)
            actions.pointer_action.move_to_location(300, 1000)
            actions.pointer_action.pointer_up()
            actions.perform()
            time.sleep(0.5)

        for _ in range(month_swipes):
            actions.pointer_action.move_to_location(600, 1500)
            actions.pointer_action.pointer_down()
            actions.pointer_action.pause(0.5)
            actions.pointer_action.move_to_location(600, 1000)
            actions.pointer_action.pointer_up()
            actions.perform()
            time.sleep(0.5)

        for _ in range(day_swipes):
            actions.pointer_action.move_to_location(800, 1500)
            actions.pointer_action.pointer_down()
            actions.pointer_action.pause(0.5)
            actions.pointer_action.move_to_location(800, 1000)
            actions.pointer_action.pointer_up()
            actions.perform()
            time.sleep(0.5)

    def confirm_date(self):
        """Click on confirm date button"""
        self.driver.find_element(*self.CONFIRM_BTN).click()
        time.sleep(1)

    def check_toast_in_logcat(self, expected_text, timeout=10):
        """Check toast text inside Android logcat."""
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                import subprocess
                logs = subprocess.check_output(
                    ["adb", "logcat", "-d"], stderr=subprocess.STDOUT
                ).decode("utf-8", errors="ignore")
                if expected_text in logs:
                    print(f" Toast found in logcat: {expected_text}")
                    return True
            except subprocess.CalledProcessError as e:
                print("Failed to read logcat:", e)
            time.sleep(1)  # poll every 1 sec
        print(f"Toast not found in logcat within {timeout} sec")
        return False

    def clear_and_enter_text(self, id_number: str):
        """Clears the EditText field inside the main content view and enters the provided text"""
        try:
            # Locate the EditText
            edit_text = wait_for_element_visibility(self.driver,self.IDCARD_INPUT_FIELD, 15)
            # Clear existing text
            edit_text.clear()
            print("EditText field cleared successfully")
            # Enter new text
            edit_text.send_keys(id_number)
            print(f"Entered text: {id_number}")
            time.sleep(1)
            # Optionally hide keyboard
            try:
                self.driver.hide_keyboard()
                time.sleep(1)
                print(" Keyboard hidden successfully")
            except Exception as e:
                print(" Could not hide keyboard:", e)
        except Exception as e:
            pytest.fail(f" Failed to clear and enter text. Error: {e}")

    def get_current_selected_year(self):
        year_field = wait_for_element_visibility(self.driver, self.YEAR_LOCATOR, 20)
        return year_field.get_attribute("content-desc"), year_field

    def get_current_selected_month(self):
        month_feild = wait_for_element_visibility(self.driver, self.MONTH_LOCATOR, 10)
        return month_feild.get_attribute("content-desc"), month_feild

    def get_current_selected_day(self):
        day_feild = wait_for_element_visibility(self.driver, self.DAY_LOCATOR, 10)
        return day_feild.get_attribute("content-desc"), day_feild

    def select_birthday(self, day, month, year):
        birthday_field = wait_for_element_visibility(self.driver, self.BIRTHDAY_SELECT_FIELD, 10)
        time.sleep(2)
        birthday_field.click()
        # Get the input fields
        selected_year_text, year_field = self.get_current_selected_year()
        selected_month_name, month_field = self.get_current_selected_month()
        selected_day_text, day_field = self.get_current_selected_day()
        # Send input
        year_field.send_keys(year)
        month_field.send_keys(self.int_to_arabic_month.get(month))
        day_field.send_keys(day)
        time.sleep(1)
        # Get values again from UI after typing
        selected_year_text, _ = self.get_current_selected_year()
        selected_month_name, _ = self.get_current_selected_month()
        selected_day_text, _ = self.get_current_selected_day()
        # Convert values to correct types
        selected_year = int(selected_year_text)
        selected_day = int(selected_day_text)
        expected_month_name = self.int_to_arabic_month.get(month)
        print(selected_day, selected_month_name, selected_year)
        # Assertions
        assert selected_year == year, f"Year mismatch: expected {year}, got {selected_year}"
        assert selected_month_name == expected_month_name, f"Month mismatch: expected {expected_month_name}, got {selected_month_name}"
        assert selected_day == day, f"Day mismatch: expected {day}, got {selected_day}"
        hard_wait(LITTLE_WAIT)

    def select_non_saudi_birthday(self):
        birthday_field = wait_for_element_visibility(self.driver, self.BIRTHDAY_SELECT_FIELD, 20)
        birthday_field.click()
        print("Birthday picker opened")

    def select_year(self, year: int):
        """Scroll year wheel until given year is found"""
        year_field = wait_for_element_visibility(self.driver, self.YEAR_LOCATOR, 10)
        if not year_field:
            raise Exception("Year field not found")
        self.scroll_to_value(year_field, str(year))
        print(f"  Year selected: {year}")

    def select_day(self, day: int):
        """Scroll day wheel until given day is found"""
        day_field = wait_for_element_visibility(self.driver, self.DAY_LOCATOR, 10)
        if not day_field:
            raise Exception("Day field not found")
        self.scroll_to_value(day_field, str(day))
        print(f"  Day selected: {day}")

    def select_month_arabic(self):
        """
        Month ke liye simple method:
        Bas ek dafa scroll down aur jo Arabic month top par hai, use pick karo
        """
        month_field = wait_for_element_visibility(self.driver, self.MONTH_LOCATOR, 10)
        if not month_field:
            raise Exception("Month field not found")
        # Ek dafa swipe down
        self.driver.execute_script("mobile: swipeGesture", {
            "elementId": month_field.id,
            "direction": "down",
            "percent": 0.5
        })
        time.sleep(1)
        # Jo month currently visible hai usko read karo
        selected_month = month_field.get_attribute("content-desc") or month_field.text
        print(f"  Month selected (Arabic): {selected_month}")
        return selected_month

    # def select_non_saudi_birthday(self, month, day, year):
    #     birthday_field = wait_for_element_visibility(self.driver, self.BIRTHDAY_SELECT_FIELD, 20)
    #     birthday_field.click()
    #     print(" Birthday picker opened.")
    #
    #     # wheels locate karo
    #     year_field = wait_for_element_visibility(self.driver, self.YEAR_LOCATOR, 10)
    #     month_field = wait_for_element_visibility(self.driver, self.MONTH_LOCATOR, 10)
    #     day_field = wait_for_element_visibility(self.driver, self.DAY_LOCATOR, 10)
    #
    #     # year select
    #     self.scroll_to_value(year_field, str(year))
    #
    #     # month select (Arabic month name ka use karo)
    #     month_name = self.month_map_ar[month]  # 12 -> "ديسمبر"
    #     self.scroll_to_value(month_field, month_name)
    #
    #     # day select
    #     self.scroll_to_value(day_field, str(day))
    #
    #     print(f" Birthday selected: {day} {month_name} {year}")

    def scroll_to_value(self, element, expected_value, attrs=("content-desc", "text", "value", "label"), max_swipes=40):
        expected_value = str(expected_value).strip()

        for _ in range(max_swipes):
            current_value = None
            for attr in attrs:
                try:
                    val = element.get_attribute(attr)
                    if val:
                        current_value = val.strip()
                        break
                except:
                    continue
            print(f" Current: {current_value}, Looking for: {expected_value}")
            if current_value == expected_value:
                print(f"  Found value: {current_value}")
                return True
            # For months: always swipe down
            self.driver.execute_script("mobile: swipeGesture", {
                "elementId": element.id,
                "direction": "down",
                "percent": 0.5
            })
            time.sleep(0.5)

        raise Exception(f"  Could not find value: {expected_value}")

    def current_selected_year(self):
        year_field = wait_for_element_visibility(self.driver, self.YEAR_LOCATOR, 10)
        selected_year = year_field.get_attribute("content-desc").strip()
        return selected_year, year_field

    def current_selected_month(self):
        month_field = wait_for_element_visibility(self.driver, self.MONTH, 10)
        selected_month = month_field.get_attribute("content-desc").strip()
        return selected_month, month_field

    def current_selected_day(self):
        day_field = wait_for_element_visibility(self.driver, self.DAY_LOCATOR, 10)
        selected_day = day_field.get_attribute("content-desc").strip()
        return selected_day, day_field

    def confirm_dob(self):
            """DOB popup close kare."""
            continue_button = wait_for_element_visibility(self.driver, self.BIRTHDAY_POPUP_CLOSE, 10)
            if continue_button:
                continue_button.click()
                print(" Clicked Confirm Date button...")
                return True
            else:
                print(" Confirm Date button not found.")
                return False

    def click_birthday_input(self, timeout=10):
        """Click on the birthday input field."""
        elem = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(11)'
            ))
        )
        elem.click()
        print(" Birthday input field clicked.")
        time.sleep(2)  # give popup time to appear
        return True

    def click_miladi_hijri_option(self, timeout=10):
        """Click on 'ميلادي هجري' option (fallback handling for newline)."""
        locators = [
            'new UiSelector().description("ميلادي\\nهجري")',
            'new UiSelector().description("ميلادي هجري")',
            'new UiSelector().descriptionContains("ميلادي")'
        ]
        for locator in locators:
            try:
                elem = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, locator))
                )
                elem.click()
                print(f" Clicked using locator: {locator}")
                return True
            except TimeoutException:
                continue
        print(" Could not find 'ميلادي هجري' option with any locator.")
        return False

    def click_next(self):
        next_button  = wait_for_element_visibility(self.driver, self.CLICK_NEXT, 10)
        if next_button :
            next_button.click()
            print("Clicked Confirm Date button, waiting for loader to disappear...")

    def verify_user_is_on_welcome_screen(self):
        try:
            element = wait_for_element_visibility(self.driver, self.WELCOME_TEXT, 10)
            print(" User is on the welcome screen.")
            return True
        except TimeoutException:
            print("Welcome screen text not found.")
            return False

    def verify_user_is_on_address_screen(self):
        try:
            element = wait_for_element_visibility(self.driver, self.ADDRESS_TEXT, 10)
            print(" User is on the Address screen.")
            return True
        except TimeoutException:
            print("Address screen text not found.")
            return False

    def select_random_city_and_proceed(self):
        # Step 1: Wait for city field and click
        city_field = wait_for_element_visibility(self.driver, self.CITY_FIELD, 20)
        city_field.click()
        print(" City dropdown opened.")
        # Step 2: Wait until multiple dropdown items appear
        #dropdown_items = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(self.CITY_DROPDOWN_ITEMS))
        dropdown_items = wait_for_all_elements_to_be_visibility(self.driver,self.CITY_DROPDOWN_ITEMS,MID_WAIT)
        # Step 4: Pick one random city
        random_item = random.choice(dropdown_items)
        random_item.click()
        selected_element = wait_for_element_visibility(self.driver, self.SELECTED_ITEM, 10)
        selected_text = selected_element.text or selected_element.get_attribute("content-desc")
        print(f"Selected random city: {selected_text}")
        # Wait until dropdown closes
        wait_for_element_visibility(self.driver, self.ADDRESS_FIELD, 20)
        print("Dropdown closed successfully")
        # Step 1: Click city field

    def click_by_coordinates(self):
        x, y = 836, 481
        self.driver.execute_script("mobile: doubleClickGesture", {"x": x, "y": y})
        time.sleep(5)

    def click_city_field(self):
        city_field = wait_for_element_visibility(self.driver, self.CITY_FIELD_SEARCH, 20)
        city_field.click()
        time.sleep(5)
        print("Clicked on city field")

    def type_in_city_search_bar(self, city_name="RIYADH"):
        try:
            self.click_by_coordinates()
            city_input_text = city_name
            self.driver.switch_to.active_element.send_keys(city_name)
            print(f"Entered city name: {city_input_text}")
            try:
                self.driver.hide_keyboard()
            except:
                pass
            time.sleep(10)
        except Exception as e:
            pytest.fail(f"Failed to type city name using coordinates: {e}")

    def click_district_field(self):
        address_label = wait_for_element_visibility(self.driver, self.ADDRESS_FIELD, 10)
        address_label.click()
        time.sleep(5)

    def click_by_dist_coordinates(self):
        x, y = 821, 504
        self.driver.execute_script("mobile: doubleClickGesture", {"x": x, "y": y})
        time.sleep(5)

    def type_in_district_search_bar(self, dist_name="King Abdullah Dist"):
        try:
            self.click_by_dist_coordinates()
            city_input_text = dist_name
            self.driver.switch_to.active_element.send_keys(dist_name)
            print(f"Entered dist name: {city_input_text}")
            try:
                self.driver.hide_keyboard()
            except:
                pass
            time.sleep(10)
        except Exception as e:
            pytest.fail(f"Failed to type dist name using coordinates: {e}")

    def search_and_select_dist(self):
         dropdown_item = wait_for_element_visibility(self.driver, self.DIST_OPTION, 20)
         dropdown_item.click()
         time.sleep(5)

    def search_and_select_city(self):
         dropdown_item = wait_for_element_visibility(self.driver, self.CITY_OPTION, 20)
         dropdown_item.click()
         time.sleep(5)

    def select_random_district_and_proceed(self):
        address_label = wait_for_element_visibility(self.driver, self.ADDRESS_FIELD, 30)
        address_label.click()
        time.sleep(5)
        # Get list of all districts
        dropdown_items = wait_for_all_elements_to_be_visibility(self.driver, self.ADDRESS_DROPDOWN_ITEMS,30)
        if not dropdown_items:
            raise Exception(" No district options found in dropdown!")
        # Select random district
        random_item  = random.choice(dropdown_items)
        selected_text = random_item.get_attribute("content-desc") or random_item.text or "Unknown"
        random_item.click()
        print(f"Selected district: {selected_text}")
        # Wait until dropdown closes
        wait_for_element_visibility(self.driver, self.ADDRESS_FIELD, 20)
        print("Dropdown closed successfully")
        #  Now press Continue
        continue_btn = wait_for_element_visibility(self.driver, self.CONTINUE_BUTTON, 20)
        continue_btn.click()
        print("Clicked Continue after selecting district")
        time.sleep(3)
        #  Verify if user is on Investment screen
        try:
            element = wait_for_element_visibility(self.driver, self.INVESTMENT_HEADER_TEXT, 20)
            print("User is on the Investment screen.")
            return True
        except TimeoutException:
            print("Investment screen text not found after Continue!")
            return False

    # Methods for InvestmentKnowledge Screen
    def verify_user_is_on_investment_screen(self):
        try:
            element = wait_for_element_visibility(self.driver, self.INVESTMENT_HEADER_TEXT, 20)
            print(" User is on the Investment screen.")
            return True
        except TimeoutException:
            print("Investment screen text not found.")
            return False
    def select_knowledge_low_and_proceed(self):
            """Selects 'Low' investment knowledge and proceeds to next question."""
            low_option = wait_for_element_visibility(self.driver, self.KNOWLEDGE_LOW, 10)
            low_option.click()
            print("Selected investment knowledge: Low")

    def _scroll_screen(self):
        """
        Scroll inside ScrollView once (W3C actions).
        """
        scroll_container = wait_for_element_visibility(
            self.driver, KYCFlow.SCROLL_VIEW, 10
        )

        rect = scroll_container.rect
        start_x = rect["x"] + rect["width"] // 2
        start_y = rect["y"] + int(rect["height"] * 0.8)
        end_y = rect["y"] + int(rect["height"] * 0.2)

        finger = PointerInput(PointerInput.TOUCH, "finger")
        actions = ActionBuilder(self.driver, mouse=finger)

        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(0.3)
        actions.pointer_action.move_to_location(start_x, end_y)
        actions.pointer_action.pointer_up()

        actions.perform()
        time.sleep(1)

    def select_investment_wrong_answer(self):
        """
        Scroll screen and click on wrong investment option.
        """
        self._scroll_screen()
        element = wait_for_element_visibility(self.driver, KYCFlow.INVESTMENT_WRONG_OPTION, 10)
        element.click()
        print("Selected wrong investment option: شراء أرض")

    def click_next_btn(self, timeout: int = 10):
        """
        Click on 'التالي' button.
        """
        element = wait_for_element_visibility(self.driver, KYCFlow.NEXT_BTN, timeout)
        element.click()
        print(" Clicked on 'التالي' button")

    def select_investment_correct_answer(self):
        """
        Scroll screen and click on correct investment option.
        """
        self._scroll_screen()
        element = wait_for_element_visibility(self.driver, KYCFlow.INVESTMENT_CORRECT_OPTION, 20)
        element.click()
        print(" Selected correct investment option: الاستثمار في صندوق مؤشر للعقارات")
    def select_knowledge_medium_and_proceed(self):
        medium_option = wait_for_element_visibility(self.driver, self.KNOWLEDGE_MEDIUM, 20)
        if medium_option:
            medium_option.click()
            print("Selected knowledge medium and continued")
        else:
            print("Medium option not found!")
            raise Exception("Medium investment knowledge option not found")

    def select_knowledge_high_and_proceed(self):
            """Selects 'High' investment knowledge and proceeds to next question."""
            high_option = wait_for_element_visibility(self.driver, self.KNOWLEDGE_HIGH, 10)
            high_option.click()
            print("Selected investment knowledge: High")

    def select_knowledge_very_high_and_proceed(self):
            """Selects 'Very High' investment knowledge and proceeds to next question."""
            very_high_option = wait_for_element_visibility(self.driver, self.KNOWLEDGE_VERY_HIGH, 10)
            very_high_option.click()
            print("Selected investment knowledge: Very High")
            time.sleep(1)  # Wait for UI update

    # Methods for EducationLevel Screen
    def select_education_primary_and_proceed(self):
        """Selects 'Primary' education level and proceeds to next question."""
        primary_option = wait_for_element_visibility(self.driver, self.EDUCATION_PRIMARY, 10)
        primary_option.click()
        print("Selected education level: Primary")

    def select_education_intermediate_and_proceed(self):
        """Selects 'Intermediate' education level and proceeds to next question."""
        intermediate_option = wait_for_element_visibility(self.driver, self.EDUCATION_INTERMEDIATE, 10)
        intermediate_option.click()
        print("Selected education level: Intermediate")

    def select_education_high_and_proceed(self):
        """Selects 'High School' education level and proceeds to next question."""
        high_option = wait_for_element_visibility(self.driver, self.EDUCATION_HIGH, 10)
        high_option.click()
        print("Selected education level: High School")

    def select_education_diploma_and_proceed(self):
        """Selects 'Diploma' education level and proceeds to next question."""
        diploma_option = wait_for_element_visibility(self.driver, self.EDUCATION_DIPLOMA, 10)
        diploma_option.click()
        print("Selected education level: Diploma")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    def select_education_bachelor_and_proceed(self):
        """Selects 'Bachelor' education level and proceeds to next question."""
        bachelor_option = wait_for_element_visibility(self.driver, self.EDUCATION_BACHELOR, 10)
        bachelor_option.click()
        print("Selected education level: Bachelor")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    def select_education_higher_and_proceed(self):
        """Selects 'Higher Education' education level and proceeds to next question."""
        higher_option = wait_for_element_visibility(self.driver, self.EDUCATION_HIGHER, 10)
        higher_option.click()
        print("Selected education level: Higher Education")

        # Methods for Employment Status Screen
    def select_employment_student_and_proceed(self):
            """Selects 'Student' employment status and proceeds to next question."""
            student_option = wait_for_element_visibility(self.driver, self.EMPLOYMENT_STUDENT, 10)
            student_option.click()
            print("Selected employment status: Student")
            time.sleep(1)  # Wait for UI update
            self.click_continue()

    def select_employment_freelance_and_proceed(self):
            """Selects 'Freelance' employment status and proceeds to next question."""
            freelance_option = wait_for_element_visibility(self.driver, self.EMPLOYMENT_FREELANCE, 10)
            freelance_option.click()
            print("Selected employment status: Freelance")
            time.sleep(1)  # Wait for UI update
            self.click_continue()

    def select_all_income_sources_and_proceed(self):
        """Select all income sources (scrolling after Savings) and then continue."""

        #  First batch - visible without scroll
        first_batch = [
            (self.INCOME_JOB, "Job"),
            (self.INCOME_BUSINESS, "Business"),
            (self.INCOME_INHERITANCE, "Inheritance"),
            (self.INCOME_SAVINGS, "Savings"),
        ]
        for locator, label in first_batch:
            option = wait_for_element_visibility(self.driver, locator, timeout=10)
            option.click()
            print(f" Selected income source: {label}")
            time.sleep(0.5)
        #  Scroll after Savings
        print("Scrolling to reveal Family & Investment...")
        size = self.driver.get_window_size()
        start_x = size['width'] / 2
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.3
        self.driver.swipe(start_x, start_y, start_x, end_y, 600)
        time.sleep(1)
        #  Second batch - appears after scroll
        second_batch = [
            (self.INCOME_FAMILY, "Family"),
            (self.INCOME_INVESTMENT, "Investment"),
        ]
        for locator, label in second_batch:
            option = wait_for_element_visibility(self.driver, locator, timeout=10)
            option.click()
            print(f" Selected income source: {label}")

    def input_first_field(self):
        field = wait_for_element_visibility(self.driver, self.INPUT_RANDOM_FIELD_ONE, 10)
        if not field:
            raise Exception("Input field not found")
        # click on field first
        field.click()
        time.sleep(5)
        # random 5 letters generate
        random_text = ''.join(random.choices(string.ascii_letters, k=5))

        field.send_keys(random_text)
        print(f" Entered random letters: {random_text}")
        return random_text

    def select_random_from_second_dropdown(self):
        # Step 1: Click field → open dropdown
        field = wait_for_element_visibility(self.driver, self.SECOND_INPUT_CONTAINER, 10)
        field.click()
        print("Dropdown opened for second field.")
        # Step 2: Wait for options
        options = wait_for_all_elements_to_be_visibility(self.driver, self.DROPDOWN_OPTIONS,30)
        if not options:
            raise Exception(" No dropdown options found for second field.")
        # Step 3: Select random option
        selected_option = random.choice(options)
        selected_text = selected_option.get_attribute("content-desc")
        scroll_to_element_and_click(self.driver,selected_option)
        print(f" Selected option: {selected_text}")
        hard_wait(LITTLE_WAIT)

    def input_third_field(self):
        field = wait_for_element_visibility(self.driver, self.INPUT_RANDOM_FIELD_THREE, 20)
        if not field:
            raise Exception("Input field not found")
        # click on field first
        field.click()
        # generate 2 random digits (00–99)
        random_digits = ''.join(random.choices(string.digits, k=2))
        field.send_keys(random_digits)
        print(f" Entered random digits: {random_digits}")
        return random_digits

    def input_four_field(self):
        # Scroll up to bring the field above the keyboard
        self.scroll_up()
        field = wait_for_element_visibility(self.driver, self.INPUT_RANDOM_FIELD_FOUR, 20)
        if not field:
            raise Exception(" Input field not found")
        # click on field first
        field.click()
        # random 5 letters generate
        random_text = ''.join(random.choices(string.ascii_letters, k=5))
        field.send_keys(random_text)
        print(f" Entered random letters: {random_text}")
        return random_text

    def select_employment_employed_and_proceed(self):
            """Selects 'Employed' employment status and proceeds to next question."""
            employed_option = wait_for_element_visibility(self.driver, self.EMPLOYMENT_EMPLOYED, 10)
            employed_option.click()
            print("Selected employment status: Employed")
            time.sleep(1)  # Wait for UI update
            self.click_continue()

    def select_employment_retired_and_proceed(self):
            """Selects 'Retired' employment status and proceeds to next question."""
            retired_option = wait_for_element_visibility(self.driver, self.EMPLOYMENT_RETIRED, 10)
            retired_option.click()
            print("Selected employment status: Retired")
            time.sleep(1)  # Wait for UI update
            self.click_continue()

    def select_employment_unemployed_and_proceed(self):
            """Selects 'Unemployed' employment status and proceeds to next question."""
            unemployed_option = wait_for_element_visibility(self.driver, self.EMPLOYMENT_UNEMPLOYED, 20)
            unemployed_option.click()
            print("Selected employment status: Unemployed")

# Methods for IncomeSource Screen
    def select_income_job_and_proceed(self):
        """Selects 'Job' income source and proceeds to next question."""
        job_option = wait_for_element_visibility(self.driver, self.INCOME_JOB, 20)
        job_option.click()
        print("Selected income source: Job")
        self.click_continue()

    def select_income_business_and_proceed(self):
        """Selects 'Business' income source and proceeds to next question."""
        business_option = wait_for_element_visibility(self.driver, self.INCOME_BUSINESS, 10)
        business_option.click()
        print("Selected income source: Business")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    def select_income_inheritance_and_proceed(self):
        """Selects 'Inheritance' income source and proceeds to next question."""
        inheritance_option = wait_for_element_visibility(self.driver, self.INCOME_INHERITANCE, 20)
        inheritance_option.click()
        print("Selected income source: Inheritance")
        self.click_continue()

    def select_income_family_and_proceed(self):
        """Scrolls on Income screen until 'Family (أسرة)' option is visible, selects it, and proceeds."""
        max_swipes = 7
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.8)
        end_y = int(size['height'] * 0.3)

        for i in range(max_swipes):
            try:
                # Check if Family option is now visible
                family_option = wait_for_element_visibility(
                    self.driver, self.INCOME_FAMILY, timeout=5, soft_fail=True
                )
                if family_option and family_option.is_displayed():
                    family_option.click()
                    print(" Selected income source: Family (أسرة)")
                    self.click_continue()
                    return
            except Exception as e:
                print(f"Attempt {i + 1}: Family option not found yet ({e})")
            # Always swipe before next attempt
            self.driver.swipe(start_x, start_y, start_x, end_y, 600)
            print(f" Swiped on attempt {i + 1} to search for 'Family (أسرة)' option")
        raise Exception(" Could not find 'Family' income option after maximum scrolling")

    def select_income_investment_and_proceed(self):
        """Selects 'Investment' income source and proceeds to next question."""
        investment_option = wait_for_element_visibility(self.driver, self.INCOME_INVESTMENT, 10)
        investment_option.click()
        print("Selected income source: Investment")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

   # Methods for SocialStatus
    def select_social_status_single_and_proceed(self):
        """Selects 'Single' social status and proceeds to next question."""
        single_option = wait_for_element_visibility(self.driver, self.SOCIAL_STATUS_SINGLE, 20)
        single_option.click()
        print("Selected social status: Single")

    def select_social_status_married_and_proceed(self):
        """Selects 'Married' social status and proceeds to next question."""
        married_option = wait_for_element_visibility(self.driver, self.SOCIAL_STATUS_MARRIED, 10)
        married_option.click()
        print("Selected social status: Married")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    def input_two_random_digits_in_field_and_process(self):
        """
        Input exactly 2 random digits into the EditText field,
        close keyboard, then press Continue.
        """

        # Wait for the field
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DIGIT_FIELD)
        )
        # Generate exactly 2 digits
        value = f"{random.randint(0, 99):02}"  # always two digits like 07, 42, 99
        field.click()
        field.clear()
        field.send_keys(value)
        # Hide keyboard
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass  # in case keyboard isn’t open

        # Click Continue
        continue_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_btn.click()
        return value

    def select_social_status_divorced_and_proceed(self):
        """Selects 'Divorced' social status and proceeds to next question."""
        divorced_option = wait_for_element_visibility(self.driver, self.SOCIAL_STATUS_DIVORCED, 10)
        divorced_option.click()
        print("Selected social status: Divorced")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    def select_social_status_widow_and_proceed(self):
        """Selects 'Widow' social status and proceeds to next question."""
        widow_option = wait_for_element_visibility(self.driver, self.SOCIAL_STATUS_WIDOW, 10)
        widow_option.click()
        print("Selected social status: Widow")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    # Methods for
    def select_annual_income_option1_and_proceed(self):
            """Selects 'Option1' (less than 8k) annual income and proceeds to next question."""
            option1 = wait_for_element_visibility(self.driver, self.ANNUAL_INCOME_OPTION1, 30)
            option1.click()
            print("Selected annual income: Less than 8k")

    def select_annual_income_option2_and_proceed(self):
            """Selects 'Option2' (8k to 25k) annual income and proceeds to next question."""
            option2 = wait_for_element_visibility(self.driver, self.ANNUAL_INCOME_OPTION2, 10)
            option2.click()
            print("Selected annual income: 8k to 25k")

    def select_annual_income_option3_and_proceed(self):
            """Selects 'Option3' (25k to 50k) annual income and proceeds to next question."""
            option3 = wait_for_element_visibility(self.driver, self.ANNUAL_INCOME_OPTION3, 10)
            option3.click()
            print("Selected annual income: 25k to 50k")
            time.sleep(1)  # Wait for UI update
            self.click_continue()

    def select_annual_income_option4_and_proceed(self):
            """Selects 'Option4' (50k to 125k) annual income and proceeds to next question."""
            option4 = wait_for_element_visibility(self.driver, self.ANNUAL_INCOME_OPTION4, 10)
            option4.click()
            print("Selected annual income: 50k to 125k")
            time.sleep(1)  # Wait for UI update

    def select_annual_income_option5_and_proceed(self):
            """Selects 'Option5' (125k to 415k) annual income and proceeds to next question."""
            option5 = wait_for_element_visibility(self.driver, self.ANNUAL_INCOME_OPTION5, 10)
            option5.click()
            print("Selected annual income: 125k to 415k")
            time.sleep(1)  # Wait for UI update
            self.click_continue()

    def select_annual_income_option6_and_proceed(self):
            """Selects 'Option6' (415k to 830k) annual income and proceeds to next question."""
            option6 = wait_for_element_visibility(self.driver, self.ANNUAL_INCOME_OPTION6, 10)
            option6.click()
            print("Selected annual income: 415k to 830k")
            time.sleep(1)  # Wait for UI update


    def select_annual_income_option7_and_proceed(self):
            """Selects 'Option7' (830k to 4m) annual income and proceeds to next question."""
            option7 = wait_for_element_visibility(self.driver, self.ANNUAL_INCOME_OPTION7, 10)
            option7.click()
            print("Selected annual income: 830k to 4m")
            time.sleep(1)  # Wait for UI update
            self.click_continue()

    def select_annual_income_option8_and_proceed(self):
            """Selects 'Option8' (more than 4m) annual income and proceeds to next question."""
            option8 = wait_for_element_visibility(self.driver, self.ANNUAL_INCOME_OPTION8, 10)
            option8.click()
            print("Selected annual income: More than 4m")
            time.sleep(1)  # Wait for UI update
            self.click_continue()

    # Method for NetWorth Screen
    def select_net_worth_option1_and_proceed(self):
        """Selects 'Option1' (less than 100k) net worth and proceeds to next question."""
        option1 = wait_for_element_visibility(self.driver, self.NET_WORTH_OPTION1, 10)
        option1.click()
        print("Selected net worth: Less than 100k")

    def select_net_worth_option2_and_proceed(self):
        """Selects 'Option2' (100k to 300k) net worth and proceeds to next question."""
        option2 = wait_for_element_visibility(self.driver, self.NET_WORTH_OPTION2, 10)
        option2.click()
        print("Selected net worth: 100k to 300k")

    def select_net_worth_option3_and_proceed(self):
        """Selects 'Option3' (300k to 600k) net worth and proceeds to next question."""
        option3 = wait_for_element_visibility(self.driver, self.NET_WORTH_OPTION3, 10)
        option3.click()
        print("Selected net worth: 300k to 600k")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    def select_net_worth_option4_and_proceed(self):
        """Selects 'Option4' (600k to 1.5m) net worth and proceeds to next question."""
        option4 = wait_for_element_visibility(self.driver, self.NET_WORTH_OPTION4, 10)
        option4.click()
        print("Selected net worth: 600k to 1.5m")
        time.sleep(1)  # Wait for UI update


    def select_net_worth_option5_and_proceed(self):
        """Selects 'Option5' (1.5m to 5m) net worth and proceeds to next question."""
        option5 = wait_for_element_visibility(self.driver, self.NET_WORTH_OPTION5, 10)
        option5.click()
        print("Selected net worth: 1.5m to 5m")

    def select_net_worth_option6_and_proceed(self):
        """Selects 'Option6' (5m to 10m) net worth and proceeds to next question."""
        option6 = wait_for_element_visibility(self.driver, self.NET_WORTH_OPTION6, 10)
        option6.click()
        print("Selected net worth: 5m to 10m")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    def select_net_worth_option7_and_proceed(self):
        """Selects 'Option7' (10m to 50m) net worth and proceeds to next question."""
        option7 = wait_for_element_visibility(self.driver, self.NET_WORTH_OPTION7, 10)
        option7.click()
        print("Selected net worth: 10m to 50m")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    def select_net_worth_option8_and_proceed(self):
        """Selects 'Option8' (more than 50m) net worth and proceeds to next question."""
        option8 = wait_for_element_visibility(self.driver, self.NET_WORTH_OPTION8, 10)
        option8.click()
        print("Selected net worth: More than 50m")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    #Method for RiskAbility Screen
    def select_risk_ability_very_low_and_proceed(self):
        """Selects 'Very Low' risk ability and proceeds to next question."""
        very_low_option = wait_for_element_visibility(self.driver, self.RISK_ABILITY_VERY_LOW, 10)
        very_low_option.click()
        print("Selected risk ability: Very Low (مخاطر منخفضة جدًا)")

    def select_risk_ability_low_and_proceed(self):
        """Selects 'Low' risk ability and proceeds to next question."""
        low_option = wait_for_element_visibility(self.driver, self.RISK_ABILITY_LOW, 10)
        low_option.click()
        print("Selected risk ability: Low (مخاطر منخفضة)")

    def select_risk_ability_medium_and_proceed(self):
        """Selects 'Medium' risk ability and proceeds to next question."""
        medium_option = wait_for_element_visibility(self.driver, self.RISK_ABILITY_MEDIUM, 10)
        medium_option.click()
        print("Selected risk ability: Medium (مخاطر متوسطة)")
        time.sleep(1)  # Wait for UI update

    def select_risk_ability_high_and_proceed(self):
        """Selects 'High' risk ability and proceeds to next question."""
        high_option = wait_for_element_visibility(self.driver, self.RISK_ABILITY_HIGH, 10)
        high_option.click()
        print("Selected risk ability: High (مخاطر عالية)")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    def select_risk_ability_very_high(self):
        """Selects 'High' risk ability and proceeds to next question."""
        high_option = wait_for_element_visibility(self.driver, self.RISK_ABILITY_VERY_HIGH, 20)
        high_option.click()
        print("Selected risk ability: High (مخاطر عالية)")
        time.sleep(1)  # Wait for UI update

    def select_risk_ability_very_high_and_proceed(self):
        """Scrolls on Risk Ability screen until 'Very High' option is visible, selects it, and proceeds."""
        max_swipes = 7
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.8)
        end_y = int(size['height'] * 0.3)

        for i in range(max_swipes):
            # Swipe first (since option is usually below screen)
            self.driver.swipe(start_x, start_y, start_x, end_y, 600)
            print(f" Swiped on attempt {i + 1} to search for 'Very High (مخاطر عالية جدًا)' option")

            try:
                very_high_option = wait_for_element_visibility(
                    self.driver, self.RISK_ABILITY_VERY_HIGH, timeout=10, soft_fail=True
                )
                if very_high_option and very_high_option.is_displayed():
                    very_high_option.click()
                    print(" Selected risk ability: Very High (مخاطر عالية جدًا)")
                    return
            except Exception as e:
                print(f" Attempt {i + 1}: 'Very High' option not found yet ({e})")
        raise Exception(" Could not find 'Very High' risk ability option after maximum scrolling")

    #Mthod for InvestmentTimePeriod Screen
    def select_investment_time_period_option1_and_proceed(self):
        """Selects 'Option1' (less than 1 year) investment time period and proceeds to next question."""
        option1 = wait_for_element_visibility(self.driver, self.INVESTMENT_TIME_PERIOD_OPTION1, 10)
        option1.click()
        print("Selected investment time period: Less than 1 year (أقل من سنة)")

    def select_investment_time_period_option2_and_proceed(self):
        """Selects 'Option2' (1 to 5 years) investment time period and proceeds to next question."""
        option2 = wait_for_element_visibility(self.driver, self.INVESTMENT_TIME_PERIOD_OPTION2, 10)
        option2.click()
        print("Selected investment time period: 1 to 5 years (من سنة إلى 5 سنوات)")

    def select_investment_time_period_option3_and_proceed(self):
        """Selects 'Option3' (more than 5 years) investment time period and proceeds to next question."""
        option3 = wait_for_element_visibility(self.driver, self.INVESTMENT_TIME_PERIOD_OPTION3, 10)
        option3.click()
        print("Selected investment time period: More than 5 years (أكثر من 5 سنوات)")
         # Wait for UI update

    # Method for InvestmentGoals Screen
    def select_investment_goals_capital_growth_and_proceed(self):
        """Selects 'Capital Growth' investment goal and proceeds to next question."""
        capital_growth_option = wait_for_element_visibility(self.driver, self.INVESTMENT_GOALS_CAPITAL_GROWTH, 10)
        capital_growth_option.click()
        print("Selected investment goal: Capital Growth (نمو رأس المال)")

    def select_investment_goals_protecting_capital_and_proceed(self):
        """Selects 'Protecting Capital' investment goal and proceeds to next question."""
        protecting_capital_option = wait_for_element_visibility(self.driver, self.INVESTMENT_GOALS_PROTECTING_CAPITAL,                                         10)
        protecting_capital_option.click()
        print("Selected investment goal: Protecting Capital (المحافظة على رأس المال)")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    def click_button(self, next_screen_locator=None):
        button = wait_for_element_visibility(self.driver, self.BUTTON, 20)
        assert button is not None, "Continue button not found on screen"
        button.click()
        print(" Continue button clicked.")
        if next_screen_locator:
            try:
                WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located(next_screen_locator)
                )
                print("Successfully navigated to next screen.")
            except TimeoutException:
                self.driver.save_screenshot("next_screen_fail.png")
                assert False, "Button clicked but next screen did not appear."

    # Method for TaxResidentModel Screen
    def select_tax_resident_yes_and_proceed(self):
        """Selects 'Yes' tax resident option and proceeds to next question."""
        yes_option = wait_for_element_visibility(self.driver, self.TAX_RESIDENT_YES, 10)
        yes_option.click()
        print("Selected tax resident: Yes (نعم)")
        time.sleep(5)

    def click_state_field(self):
        state_field = wait_for_element_visibility(self.driver, self.STATE_FIELD, 20)
        state_field.click()
        time.sleep(5)

    def click_state_by_coordinates(self):
        x, y = 828, 478
        self.driver.execute_script("mobile: doubleClickGesture", {"x": x, "y": y})
        time.sleep(5)

    def type_state_in_search_bar(self, state_name="United States"):
        try:
            self.click_state_by_coordinates()
            city_input_text = state_name
            self.driver.switch_to.active_element.send_keys(state_name)
            print(f"Entered dist name: {city_input_text}")
            try:
                self.driver.hide_keyboard()
            except:
                pass
            time.sleep(10)
        except Exception as e:
            pytest.fail(f"Failed to type dist name using coordinates: {e}")

    def select_state(self):
         dropdown_item = wait_for_element_visibility(self.driver, self.STATE_OPTION, 20)
         dropdown_item.click()
         time.sleep(5)

    def select_state_and_proceed(self):
        field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.STATE_FIELD))
        field.click()
        options = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(self.STATE_OPTIONS))
        if not options:
            raise Exception("No state options found!")
        # --- Randomly select one ---
        choice = random.choice(options)
        selected_state = choice.get_attribute("content-desc")
        choice.click()
        return selected_state

    def select_continue_and_proceed(self):
        # --- Click Continue ---
        continue_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CON_BUTTON)
        )
        continue_btn.click()

    def select_tin_no(self):
        """Selects 'No' for TIN and proceeds by clicking Continue."""

        # --- Click the 'No' option ---
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TIN_NO_OPTION)
        )
        option.click()
    def select_tin_yes(self):
        option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.TIN_YES))
        option.click()

    def enter_random_tin(self, length=7):
        # --- Wait for text field ---
        text_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.TIN_INPUT)
        )
        text_field.click()
        # --- Always generate exactly 7 letters ---
        random_tin = ''.join(random.choices(string.ascii_letters, k=7))
        # --- Enter text ---
        text_field.clear()
        text_field.send_keys(random_tin)
        # --- Close keyboard ---
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass
        # --- Click Next ---
        next_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.CON_BUTTON)
        )
        next_btn.click()
        print(f" Entered random TIN: {random_tin}")
        return random_tin

    def select_other_and_fill_field(self):
        """Selects 'Other', enters random letters (1–5), closes keyboard, and clicks Next."""

        # --- Click "Other" option ---
        other_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.OTHER_OPTION)
        )
        other_option.click()
        # --- Wait for text field ---
        text_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.OTHER_TEXT_FIELD)
        )
        text_field.click()
        # --- Generate random 1–5 letters from abcdef ---
        length = random.randint(1, 5)
        random_text = "".join(random.choice("abcdef") for _ in range(length))
        # --- Enter text ---
        text_field.clear()
        text_field.send_keys(random_text)
        # --- Close keyboard ---
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass
        # --- Click Next ---
        next_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CON_BUTTON)
        )
        next_btn.click()
        return random_text

    def select_tax_resident_no_and_proceed(self):
        """Selects 'No' tax resident option and proceeds to next question."""
        try:
            no_option = wait_for_element_visibility(self.driver, self.TAX_RESIDENT_NO, 20)
            if no_option:
                no_option.click()
                print("Selected tax resident: No (لا)")
            else:
                print("Tax Resident 'No' option not found, might be auto-skipped.")
        except TimeoutException:
            print("Tax Resident 'No' option screen did not appear (auto-redirected).")

    def verify_user_is_on_email_screen(self):
        try:
            element = wait_for_element_visibility(self.driver, self.EMAIL_SCREEN, 20)
            print("User is on the Email screen (البريد الإلكتروني).")
            return True
        except TimeoutException:
            print("Email screen not found")
            return False

    def enter_random_email(self):

        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        email = f"{random_str}@gmail.com"
        email_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_field.click()
        time.sleep(2)
        email_field.clear()
        email_field.send_keys(email)
        print(f"Entered random email: {email}")
        return email

    def enter_gmail_email(self):
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        email = f"{random_str}"
        # Wait for email input field
        email_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_field.click()
        time.sleep(2)
        email_field.clear()
        email_field.send_keys(email)
        print(f" Entered random email: {email}")
        # After typing, click on the Gmail domain option
        gmail_domain = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//android.view.View[@content-desc='@gmail.com']"))
        )
        gmail_domain.click()
        print(" Selected Gmail domain option")
        return email

    def enter_hotmail_email(self):
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        username = f"{random_str}"  # sirf user part
        # Wait for email input field
        email_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_field.click()
        time.sleep(2)
        email_field.clear()
        email_field.send_keys(username)
        print(f" Entered random email username: {username}")
        # After typing, click on the Gmail domain option
        gmail_domain = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//android.view.View[@content-desc='@hotmail.com']"))
        )
        gmail_domain.click()
        print(" Selected Gmail domain option")
        # Return full email (username + @gmail.com)
        return f"{username}@gmail.com"

    def button_continue(self):
        continue_button = wait_for_element_visibility(self.driver, self.BUTTON_CONTINUE, 20)
        if continue_button:
            continue_button.click()
            time.sleep(2)
        else:
            print("Continue button not found.")

    def select_create_button(self):
        try:
            # Wait until button is clickable
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.CREATE_BUTTON)
            )
            button.click()
        except TimeoutException:
            print("Create button")

    def success_otp_code(self):
        try:
            # Step 1: Detect OTP from screen
            otp_element = wait_for_element_visibility(self.driver, self.OTP_CODE, 20)
            otp_code = otp_element.get_attribute("content-desc")
            if not otp_code or not otp_code.isdigit():
                raise ValueError("OTP not detected correctly.")
            print(f"Detected OTP: {otp_code}")
            # Step 2: Locate OTP input field
            otp_input = wait_for_element_visibility(self.driver, self.OTP_INPUT_FIELD, 20)
            otp_input.click()
            otp_input.send_keys(otp_code)
            print("OTP entered successfully.")
            time.sleep(3)
        except Exception as e:
            print(f"Error entering OTP: {str(e)}")

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

    # def handle_enable_notifications_if_displays(self):
    #     """Tap on 'السماح' by coordinates if the notification screen appears."""
    #     try:
    #         actions = ActionChains(self.driver)
    #         actions.w3c_actions = ActionBuilder(
    #             self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
    #         )
    #         actions.w3c_actions.pointer_action.move_to_location(543, 1627)  # adjust coords if needed
    #         actions.w3c_actions.pointer_action.pointer_down()
    #         actions.w3c_actions.pointer_action.pause(0.1)
    #         actions.w3c_actions.pointer_action.release()
    #         actions.perform()
    #         print("Tapped on coordinates (543, 1627) for 'السماح'")
    #     except Exception as e:
    #         print(f"Failed to tap on coordinates. Reason: {e}")

    def handle_enable_notifications_if_displays(self):
        """Tap on 'السماح' button if notification permission screen appears."""
        try:
            allow_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, "السماح")
                )
            )
            allow_button.click()
            print("Clicked on 'السماح' button successfully.")
        except TimeoutException:
            print("'السماح' button not displayed. Skipping notification permission.")
        except Exception as e:
            print(f"Failed to click on 'السماح'. Reason: {e}")

    def verify_holistic_home_screen(self):
        try:
            home_element = wait_for_element_visibility(self.driver, self.HOME_SCREEN, 20)
            if home_element and home_element.is_displayed():
                # confirm by attribute
                screen_text = home_element.get_attribute("content-desc")
                if screen_text == "الرئيسية":
                    print(" Confirmed: User is on Home Screen")
                    return True
                else:
                    print(f" Element found but text mismatch: {screen_text}")
                    return False
            else:
                print(" Home Screen element not visible")
                return False
        except Exception as e:
            print(f"Error verifying Home Screen: {str(e)}")
            return False
        hard_wait(LITTLE_WAIT)

    def verify_holistic_home_screen(self):
        """Verify user is on Holistic Home screen — handles popups, scrolls if needed."""
        try:
            print(" Checking if user reached the Holistic Home screen...")
            # Step 1: Handle optional popups
            self.click_on_the_portfolio_name_update_pop_up()
            self.handle_enable_notifications_if_displays()
            # Step 2: Try finding the home screen element directly
            home_element = wait_for_element_visibility(self.driver, self.HOME_SCREEN, 15, soft_fail=True)
            if not home_element:
                print(" Home screen not immediately visible. Scrolling up once to check...")
                self.scroll_up()
                home_element = wait_for_element_visibility(self.driver, self.HOME_SCREEN, 15, soft_fail=True)
            # Step 3: If still not visible, fail gracefully
            if not home_element:
                print(" Home screen element not found after scroll.")
                self.driver.save_screenshot("home_screen_not_found.png")
                return False
            # Step 4: Validate the content description text
            if home_element.is_displayed():
                screen_text = home_element.get_attribute("content-desc")
                if screen_text == "الرئيسية":
                    print(" Confirmed: User is on the Holistic Home Screen.")
                    return True
                else:
                    print(f" Element found but content-desc mismatch: {screen_text}")
                    return False
            else:
                print(" Home Screen element found but not visible.")
                return False
        except Exception as e:
            print(f" Error verifying Holistic Home Screen: {str(e)}")
            return False

    def get_created_portfolio(self):
        try:
            portfolio_element = wait_for_element_visibility(self.driver, self.PORTFOLIO_TYPE, 20)
            if portfolio_element:
                portfolio_name = portfolio_element.get_attribute("content-desc")
                print(f" Portfolio created: {portfolio_name}")
                return portfolio_name
            else:
                print("Portfolio element not found")
                return None
        except Exception as e:
            print(f"Error detecting portfolio: {str(e)}")
            return None

    def click_change_portfolio_type(self):
        try:
            print("Scrolling and clicking 'Change Portfolio Type' button...")
            change_btn = self.driver.find_element(*self.CHANGE_PORTFOLIO_TYPE_BUTTON)
            change_btn.click()
            print("Clicked on 'Change Portfolio Type' button.")
            return True
        except Exception as e:
            print(f"Error clicking Change Portfolio Type: {str(e)}")
            return False

    def select_conservative_type(self, timeout: int = 15):
        """
        Click on the 'المتنوعة (آمنة)\nعائد يصل إلى %8+ سنويًا' card.
        """
        element = wait_for_element_visibility(self.driver, self.SELECT_CONSERVATIVE, timeout)
        element.click()
    def scroll_up(self):
        pass
    def scroll_to_exact_month(self, expected_month):
        pass

