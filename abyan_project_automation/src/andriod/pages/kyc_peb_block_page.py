import pytest
from appium.webdriver.common.appiumby import AppiumBy
import random, string, time

from appium.webdriver.common.touch_action import TouchAction

from faker.typing import Country
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import Interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from abyan_project_automation.src.constants.wait_contants import MID_WAIT, LITTLE_WAIT, LONG_WAIT
from abyan_project_automation.src.utils.wait_utils import wait_for_element_visibility, \
    wait_for_all_elements_to_be_visibility


class KycPebBlock:
    def __init__(self, driver):  # constructor
        self.driver = driver
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
    NEXT_BTN = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="التالي"]')
    USER_IMAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')
    PHONE_INPUT = (AppiumBy.CLASS_NAME, 'android.widget.ImageView')
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "إستمر")
    CLICK_CONTINUE = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="إستمر"]')
    PASSWORD_SCREEN_HEADER = (AppiumBy.ACCESSIBILITY_ID, "أدخل رمز المرور")
    PASSWORD_SCREEN_KEY_0 = (AppiumBy.ACCESSIBILITY_ID, "0")
    OTP = (AppiumBy.XPATH, '//android.view.View[@content-desc="ادخل رمز التحقق"]/preceding-sibling::android.view.View[1]')
    OTP_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    KYC_HEADER = (AppiumBy.ACCESSIBILITY_ID, "إنشاء حساب")
    OTP_ERROR_MESSAGE = (AppiumBy.XPATH, "//android.view.View[@content-desc='رمز التحقق غير صحيح']")
    IDCARD_INPUT_FIELD = (AppiumBy.XPATH, "//android.widget.EditText")
    BIRTHDAY_SELECT_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(11)')
    # DOB_FIELD = (AppiumBy.XPATH, "//android.widget.ImageView")
    DOB_FIELD =  (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(11)')
    CONFIRM_BTN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='تأكيد التاريخ']")
    YEAR_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.SeekBar").index(2)')
    MONTH_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.SeekBar").index(4)')
    DAY_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.SeekBar").index(3)')
    BIRTHDAY_POPUP_CLOSE = (AppiumBy.ACCESSIBILITY_ID, 'تأكيد التاريخ')
    LOADER = (AppiumBy.ID, 'إستمر')
    CLICK_NEXT = (AppiumBy.ACCESSIBILITY_ID, 'إستمر')
    WELCOME_TEXT = (AppiumBy.CLASS_NAME, 'android.widget.ImageView')
    ADDRESS_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'العنوان')
    # Locators for Address Selection Screen
    CITY_FIELD = (AppiumBy.XPATH, '//android.view.View[@content-desc="العنوان"]/android.view.View[1]')
    CITY_DROPDOWN_ITEMS = (AppiumBy.XPATH, '//android.widget.EditText/android.view.View[2]//android.view.View[@content-desc]')
    SELECTED_ITEM = (AppiumBy.XPATH, '//android.view.View[@content-desc="العنوان"]//android.view.View[@text]')
    ADDRESS_FIELD = (AppiumBy.XPATH, '//android.view.View[@content-desc="العنوان"]/android.view.View[2]')
    ADDRESS_DROPDOWN_ITEMS = (AppiumBy.XPATH, '//android.view.View[@content-desc and not(@content-desc="")]')
    ADDRESS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("حي المرقب Al Marqab Dist.")')
    # Locators for InvestmentKnowledge Screen
    INVESTMENT_HEADER_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'المعرفة الاستثمارية')
    KNOWLEDGE_SCREEN_HEADER = (AppiumBy.ACCESSIBILITY_ID, 'المعرفة الاستثمارية')
    KNOWLEDGE_LOW = (
    AppiumBy.ACCESSIBILITY_ID, "مبتدئ في الاستثمار\nأنا جديد في مجال الاستثمار، ليس لدي أي  معرفة بالاستثمار")
    KNOWLEDGE_MEDIUM = (AppiumBy.ACCESSIBILITY_ID, 'أدرك أساسيات الاستثمار\nأدرك أساسيات الاستثمار والأسواق المالية')
    KNOWLEDGE_HIGH = (
    AppiumBy.ACCESSIBILITY_ID, "لدي بعض الخبرة\n لدي خبرات استثمارية سابقة، أدرك مفاهيم الاستثمار الأساسية.")
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
    SOCIAL_STATUS_DIVORCED = (AppiumBy.ACCESSIBILITY_ID, 'مطلق')
    SOCIAL_STATUS_WIDOW = (AppiumBy.ACCESSIBILITY_ID, 'أرمل')
    # Locators for AnnualIncome Screen
    ANNUAL_INCOME_OPTION1 = (AppiumBy.ACCESSIBILITY_ID, 'أقل من 8 ألف')
    ANNUAL_INCOME_OPTION2 = (AppiumBy.ACCESSIBILITY_ID, 'من 8 ألف الى 25 ألف')
    ANNUAL_INCOME_OPTION3 = (AppiumBy.ACCESSIBILITY_ID, 'من 25 ألف الى 50 ألف')
    ANNUAL_INCOME_OPTION4 = (AppiumBy.ACCESSIBILITY_ID, 'من 50 ألف الى 125 ألف')
    ANNUAL_INCOME_OPTION5 = (AppiumBy.ACCESSIBILITY_ID, 'من 125 ألف الى 415 ألف')
    ANNUAL_INCOME_OPTION6 = (AppiumBy.ACCESSIBILITY_ID, 'من 415 ألف الى 830 ألف')
    ANNUAL_INCOME_OPTION7 = (AppiumBy.ACCESSIBILITY_ID, 'من 830 ألف الى 4 مليون')
    ANNUAL_INCOME_OPTION8 = (AppiumBy.ACCESSIBILITY_ID, '4 مليون وأكثر')
    # Locators for NetWorth Screen
    NET_WORTH_OPTION1 = (AppiumBy.ACCESSIBILITY_ID, 'أقل من 100 ألف')
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
    PEB_YES = (AppiumBy.XPATH, '//android.view.View[@content-desc="نعم (بعض الخيارات تنطبق عليّ)"]')
    BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="استمر"]')
    #PEB Block
    HAS_WORK_ON_FINANCIAL = (AppiumBy.XPATH,'//android.view.View[@content-desc="هل سبق للعميل العمل في القطاع المالي خلال السنوات الخمس السابقة؟"]')
    RELATED_EXPERIENCE =(AppiumBy.XPATH, '//android.view.View[@content-desc="هل للعميل أي خبرات عملية أخرى ذات صلة بالقطاع المالي؟"]')
    MEMBERSHIP_RELEVANT = (AppiumBy.XPATH, '//android.view.View[@content-desc="هل العميل عضو مجلس إدارة أو لجنة مراجعة أو أحد كبار التنفيذيين في شركة مدرجة؟"]')
    MEMBERSHIP_RELEVANT_INPUT = (AppiumBy.XPATH, '//android.view.View[@content-desc="هل العميل عضو مجلس إدارة أو لجنة مراجعة أو أحد كبار التنفيذيين في شركة مدرجة؟"]/android.widget.EditText[1]')
    MEMBERSHIP_RELEVANT_INPUT_TWO = (AppiumBy.XPATH,'//android.view.View[@content-desc="هل العميل عضو مجلس إدارة أو لجنة مراجعة أو أحد كبار التنفيذيين في شركة مدرجة؟"]/android.widget.EditText[2]')
    PEB_GOVERNMENT_EMPLOYEE_QUESTION = (AppiumBy.XPATH, '//android.view.View[@content-desc="هل العميل مكلف بمهمات عليا في المملكة أو في دولة أجنبية أو مناصب إدارة عليا أو وظيفة في إحدى المنظمات الدولية؟"]')
    PEB_RELATIVE_GOVERNMENT_EMPLOYEE = (AppiumBy.XPATH,'//android.view.View[@content-desc="هل للعميل صلة قرابة برابطة الدم أو الزواج وصولا إلى الدرجة الثانية، أو يعد مقرباً من شخص مكلف بمهمات عليا في المملكة أو في دولة أجنبية أو مناصب إدارة عليا أو وظيفة في إحدى المنظمات الدولية؟"]')
    PEB_RELATIVE_GOVERNMENT_EMPLOYEE_INPUT1 = (AppiumBy.XPATH,'//android.view.View[@content-desc="هل للعميل صلة قرابة برابطة الدم أو الزواج وصولا إلى الدرجة الثانية، أو يعد مقرباً من شخص مكلف بمهمات عليا في المملكة أو في دولة أجنبية أو مناصب إدارة عليا أو وظيفة في إحدى المنظمات الدولية؟"]/android.widget.EditText[1]')
    PEB_RELATIVE_GOVERNMENT_EMPLOYEE_INPUT2 = (AppiumBy.XPATH,'//android.view.View[@content-desc="هل للعميل صلة قرابة برابطة الدم أو الزواج وصولا إلى الدرجة الثانية، أو يعد مقرباً من شخص مكلف بمهمات عليا في المملكة أو في دولة أجنبية أو مناصب إدارة عليا أو وظيفة في إحدى المنظمات الدولية؟"]/android.widget.EditText[2]')

    # Locators for TaxResidentModel Screen
    TAX_RESIDENT_NO = (AppiumBy.XPATH, '//android.view.View[@content-desc="لا"]')
    INHERITANCE_NO_BUTTON = (AppiumBy.XPATH, '//android.view.View[@content-desc="لا"]')
    GRANTS_NO_BUTTON = (AppiumBy.XPATH, '//android.view.View[@content-desc="لا"]')
    INVESTING_OUTSIDE_ABYAN_OPTION = (AppiumBy.XPATH, '//android.view.View[@content-desc="أسهم"]')
    INVESTING_SEEKBAR = (AppiumBy.XPATH, '//android.widget.SeekBar[@content-desc]')
    INVESTING_SEEKBAR_ONE = (AppiumBy.XPATH, '//android.widget.SeekBar[@content-desc="50%"]')
    INVESTING_SEEKBAR_TWO = (AppiumBy.XPATH, '//android.widget.SeekBar[@content-desc="25%"]')
    INVESTING_SEEKBAR_THREE = (AppiumBy.XPATH, '//android.widget.SeekBar[@content-desc="25%"]')
    INVESTING_OPTION_SHARES = (AppiumBy.ACCESSIBILITY_ID, "أسهم")
    INVESTING_OPTION_PROPERTIES = (AppiumBy.ACCESSIBILITY_ID, "عقارات")
    INVESTING_OPTION_DEPOSITS = (AppiumBy.ACCESSIBILITY_ID, "ودائع ومرابحات")
    INVESTING_OPTION_DEBT =(AppiumBy.ACCESSIBILITY_ID, "أدوات دين")
    COUNTRY_ITEMS = (AppiumBy.XPATH, '//android.widget.EditText/android.view.View[2]/android.view.View')
    COUNTRY_ITEM = (AppiumBy.ACCESSIBILITY_ID, 'ليبيريا\nLiberia')

    INVESTING_SEEKBAR_50 = (AppiumBy.XPATH, '//android.widget.SeekBar[@content-desc="50%"]')
    INVESTING_SEEKBAR_25_FIRST = (AppiumBy.XPATH, '//android.widget.SeekBar[@content-desc="25%"]')
    INVESTING_SEEKBAR_25_SECOND = (AppiumBy.XPATH, '(//android.widget.SeekBar[@content-desc="25%"])[2]')

    FINANCIAL_INSTITUTION_INPUT = (AppiumBy.XPATH, '//android.widget.EditText')
    ADD_INSTITUTION_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="إضافة مؤسسة"]')
    FINANCIAL_INSTITUTION_INPUT_TWO = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout'
        '/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View'
        '/android.view.View[2]/android.view.View/android.view.View/android.view.View'
        '/android.view.View[2]/android.view.View/android.widget.EditText[2]')
    FINANCIAL_INSTITUTION_INPUT_THREE = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout'
        '/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View'
        '/android.view.View[2]/android.view.View/android.view.View/android.view.View'
        '/android.view.View[2]/android.view.View/android.widget.EditText[3]')
    FINANCIAL_INSTITUTION_INPUT_FOUR = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[2]/android.view.View/android.widget.EditText[4]')
    CURRENT_INVESTMENT_VALUE_INPUT = (AppiumBy.XPATH, '//android.widget.EditText')
    EXPECTED_INVESTMENT_ANNUAL_INPUT = (AppiumBy.XPATH, '//android.widget.EditText')
    TAX_RESIDENT_YES = (AppiumBy.ACCESSIBILITY_ID, 'نعم')
    STATE_FIELD = (AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]')
    STATE_OPTIONS = (AppiumBy.XPATH, '//android.widget.EditText/android.view.View/android.view.View//android.view.View[@content-desc]')
    CON_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="التالي"]')
    INHERITANCE_YES_BUTTON = (AppiumBy.XPATH, '//android.view.View[@content-desc="نعم"]')
    # --- Inheritance Year ---
    INHERITANCE_YEAR_FIELD = (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[3]")
    INHERITANCE_SEEKBARS = (AppiumBy.XPATH, "//android.widget.SeekBar[@content-desc]")
    INHERITANCE_YEAR_CONFIRM_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="تأكيد السنة"]')
    COUNTRY_DROPDOWN_CONTAINER = (AppiumBy.XPATH,'//android.widget.EditText/android.view.View[2]')

    INVESTMENT_VALUE_INPUT = (AppiumBy.XPATH, '//android.widget.EditText')
    INHERITANCE_FIELD_INPUT = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[4]')
    INHERITANCE_TYPE_PROPERTIES = (AppiumBy.ACCESSIBILITY_ID, "عقارات")
    INHERITANCE_TYPE_MOVABLE = (AppiumBy.ACCESSIBILITY_ID, "أموال منقولة")
    INHERITANCE_TYPE_SHARES = (AppiumBy.ACCESSIBILITY_ID, "أسهم")
    INHERITANCE_TYPE_OTHER = (AppiumBy.ACCESSIBILITY_ID, "أخرى")
    INHERITANCE_CONFIRM_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="تأكيد الإختيار"]')
    INHERITANCE_COUNTRY_FRAME = (AppiumBy.XPATH,'//android.view.View/android.view.View[5]')
    INHERITANCE_COUNTRY_OPTIONS = (AppiumBy.XPATH, '//android.view.View[@content-desc]')
    GRANTS_YES_BUTTON = (AppiumBy.XPATH, '//android.view.View[@content-desc="نعم"]')
    GRANT_YEAR_FRAME = (AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View[3]')
    GRANT_YEAR_SEEKBARS = (AppiumBy.XPATH, '//android.widget.SeekBar[@content-desc]')
    GRANT_YEAR_CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'تأكيد السنة')
    GRANT_VALUE_INPUT = (AppiumBy.XPATH, '//android.widget.EditText')
    GRANT_TYPE_FRAME = (AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View[4]')
    GRANT_TYPE_PROPERTIES = (AppiumBy.ACCESSIBILITY_ID, "عقارات")
    GRANT_TYPE_MOVABLE = (AppiumBy.ACCESSIBILITY_ID, "أموال منقولة")
    GRANT_TYPE_SHARES = (AppiumBy.ACCESSIBILITY_ID, "أسهم")
    GRANT_TYPE_CONFIRM_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="تأكيد الإختيار"]')
    GRANT_COUNTRY_FRAME = (AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View[5]')
    GRANT_COUNTRY_OPTIONS = (AppiumBy.XPATH, '//android.view.View[@content-desc]')  # all country options
    GRANT_COUNTRY_CONFIRM_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="تأكيد الإختيار"]')
    TIN_NO_OPTION = (AppiumBy.XPATH, '//android.view.View[@content-desc="لا"]')
    OTHER_OPTION = (AppiumBy.XPATH, '//android.view.View[@content-desc="آخر"]')
    OTHER_TEXT_FIELD = (AppiumBy.XPATH, '//android.widget.EditText')
    BUTTON_CONTINUE = (AppiumBy.ACCESSIBILITY_ID, 'إنشاء حساب')
    EMAIL_SCREEN = (AppiumBy.ACCESSIBILITY_ID, 'البريد الإلكتروني')
    EMAIL_INPUT = (AppiumBy.CLASS_NAME, 'android.widget.EditText')
    DOMAINS = ["@gmail.com", "@hotmail.com"]
    CREATE_SUCCESS_SCREEN = (AppiumBy.ACCESSIBILITY_ID, ' "في طور اقتراح المحفظة الاستثمارية الأنسب لك"')
    CREATE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'إنشاء المحفظة')
    OTP_CREATE_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="create_otp_input"]')
    OTP_CODE = (AppiumBy.XPATH, '//android.view.View[@content-desc and string-length(@content-desc)=4]')
    OTP_INPUT_FIELD = (AppiumBy.CLASS_NAME, 'android.widget.EditText')
    HOME_SCREEN = (AppiumBy.XPATH, '//android.view.View[@content-desc="الرئيسية"]')
    PORTFOLIO_TYPE = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc,"محفظة")]')
    UNDER_REVIEW_SCREEN = (AppiumBy.ACCESSIBILITY_ID, 'حسابك تحت المراجعة')
    REFRESH_PAGE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'تحديث الصفحة')
    FIELD =(AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[5]')
    CONTINUE_EDIT = (AppiumBy.ACCESSIBILITY_ID, 'استمر للنموذج')

    EDIT_SUCCESS = (AppiumBy.ACCESSIBILITY_ID, 'الصفحة الرئيسية')
    REMOVE_THREE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(12)')
    REMOVE_TWO = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(11)')
    REMOVE_ONE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(10)')

    def click_welcomescreen_next_buttons(self, times=3):
        user_present = wait_for_element_visibility(self.driver, self.USER_IMAGE, LITTLE_WAIT,soft_fail=True)
        if user_present:
            print("User selection screen detected — skipping 'next' button clicks.")
            return
        else:
            for _ in range(times):
                next_button = wait_for_element_visibility(self.driver, self.NEXT_BUTTON, 10, soft_fail=True)
                if next_button:
                    time.sleep(2)
                    next_button.click()
                else:
                    print("Next button not found — skipping remaining clicks.")
                    break

    def select_user(self):
        user_element = wait_for_element_visibility(self.driver, self.USER_IMAGE, 10, soft_fail=True)
        if user_element:
            user_element.click()
            print("User selected successfully.")
        else:
            print("User image not visible — skipping user selection step.")

    def enter_phone_number(self, phone_number):
        phone_input = wait_for_element_visibility(self.driver, self.PHONE_INPUT, 20)
        if phone_input:
            phone_input.click()
            time.sleep(2)
            phone_input = wait_for_element_visibility(self.driver, self.PHONE_INPUT, 10)
            phone_input.send_keys(phone_number)
        else:
            print("Phone input field not found.")

    def click_continue_next(self):
        continue_button = wait_for_element_visibility(self.driver, self.CONTINUE_BUTTON, 20)
        if continue_button:
            continue_button.click()
        else:
            print("Continue button not found.")
    def click_btn(self):
        continue_button = wait_for_element_visibility(self.driver, self.BUTTON, 20)
        if continue_button:
            continue_button.click()
        else:
            print("Continue button not found.")

    def click_continue(self):
        continue_button = wait_for_element_visibility(self.driver, self.CLICK_CONTINUE, 20)
        if continue_button:
            continue_button.click()
        else:
            print("Continue button not found.")

    def enter_password(self):
        zero_button = wait_for_element_visibility(self.driver, self.PASSWORD_SCREEN_KEY_0, 10, MID_WAIT)
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
            otp_input = wait_for_element_visibility(self.driver, self.OTP_INPUT, 20)
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
        time.sleep(5)

    def close_popup(self):
        continue_button = wait_for_element_visibility(self.driver, self.BIRTHDAY_POPUP_CLOSE, 10)
        if continue_button:
            continue_button.click()
            print("Clicked Confirm Date button, waiting for loader to disappear...")
            from selenium.common import TimeoutException
            try:
                # Wait for loader to disappear (invisible or not present)
                from selenium.webdriver.support.wait import WebDriverWait
                WebDriverWait(self.driver, 5).until(
                    EC.invisibility_of_element_located(self.LOADER)
                )
                print("Loader disappeared.")
            except TimeoutException:
                print("Loader did not disappear within timeout.")
        else:
            print("Confirm Date button not found.")

    def click_next(self):
        next_button = wait_for_element_visibility(self.driver, self.CLICK_NEXT, 20)
        if next_button:
            next_button.click()
            print("Clicked Confirm Date button, waiting for loader to disappear...")
    def click_dob_field(self):
        """Click DOB field to open date picker"""
        self.driver.find_element(*self.DOB_FIELD).click()
        time.sleep(1)

    def select_random_dob(self):
        """Swipe pickers randomly to select Year / Month / Day"""
        action = TouchAction(self.driver)

        # Random swipe movements for year/month/day

        year_swipes = random.randint(1, 5)
        month_swipes = random.randint(1, 12)
        day_swipes = random.randint(1, 28)

        for _ in range(year_swipes):
            action.press(x=300, y=1500).wait(500).move_to(x=300, y=1000).release().perform()
            time.sleep(0.5)

        for _ in range(month_swipes):
            action.press(x=600, y=1500).wait(500).move_to(x=600, y=1000).release().perform()
            time.sleep(0.5)

        for _ in range(day_swipes):
            action.press(x=800, y=1500).wait(500).move_to(x=800, y=1000).release().perform()
            time.sleep(0.5)

    def confirm_date(self):
        """Click on confirm date button"""
        self.driver.find_element(*self.CONFIRM_BTN).click()
        time.sleep(1)

    def verify_user_is_on_welcome_screen(self):
        try:
            element = wait_for_element_visibility(self.driver, self.WELCOME_TEXT, 20)
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
        # dropdown_items = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(self.CITY_DROPDOWN_ITEMS))
        dropdown_items = wait_for_all_elements_to_be_visibility(self.driver, self.CITY_DROPDOWN_ITEMS, MID_WAIT)
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

    def select_random_district_and_proceed(self):

        address_label = wait_for_element_visibility(self.driver, self.ADDRESS_FIELD, 30)
        address_label.click()
        time.sleep(5)

        dropdown_items = wait_for_all_elements_to_be_visibility(self.driver, self.ADDRESS_DROPDOWN_ITEMS, 30)

        if not dropdown_items:
            raise Exception(" No district options found in dropdown!")
        # Select random district
        random_item = random.choice(dropdown_items)
        selected_text = random_item.get_attribute("content-desc") or random_item.text or "Unknown"
        random_item.click()
        print(f"Selected district: {selected_text}")
        # Wait until dropdown closes
        wait_for_element_visibility(self.driver, self.ADDRESS_FIELD, 20)
        print("Dropdown closed successfully")
        continue_btn = wait_for_element_visibility(self.driver, self.CONTINUE_BUTTON, 20)
        continue_btn.click()
        print("Clicked Continue after selecting district")
        time.sleep(3)

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
        self.click_continue()

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

        # Methods for EmployementStatus Screen

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
        unemployed_option = wait_for_element_visibility(self.driver, self.EMPLOYMENT_UNEMPLOYED, 10)
        unemployed_option.click()
        print("Selected employment status: Unemployed")

    # Methods for IncomeSource Screen
    def select_income_job_and_proceed(self):
        """Selects 'Job' income source and proceeds to next question."""
        job_option = wait_for_element_visibility(self.driver, self.INCOME_JOB, 10)
        job_option.click()
        print("Selected income source: Job")
        time.sleep(1)  # Wait for UI update
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
        inheritance_option = wait_for_element_visibility(self.driver, self.INCOME_INHERITANCE, 10)
        inheritance_option.click()
        print("Selected income source: Inheritance")

    def select_income_savings_and_proceed(self):
        """Selects 'Savings' income source and proceeds to next question."""
        savings_option = wait_for_element_visibility(self.driver, self.INCOME_SAVINGS, 10)
        savings_option.click()
        print("Selected income source: Savings")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    # def select_income_family_and_proceed(self):
    #     """Selects 'Family' income source and proceeds to next question."""
    #     family_option = wait_for_element_visibility(self.driver, self.INCOME_FAMILY, 10)
    #     family_option.click()
    #     print("Selected income source: Family")
    def select_income_family_and_proceed(self):
        """Scrolls until 'Family' income option is visible, selects it, and proceeds."""
        max_swipes = 7
        for _ in range(max_swipes):
            try:
                family_option = wait_for_element_visibility(self.driver, self.INCOME_FAMILY, 3)
                if family_option.is_displayed():
                    family_option.click()
                    print("Selected income source: Family")
                    return
            except Exception:
                # perform scroll/swipe if not visible yet
                size = self.driver.get_window_size()
                start_x = size['width'] / 2
                start_y = size['height'] * 0.8
                end_y = size['height'] * 0.3
                self.driver.swipe(start_x, start_y, start_x, end_y, 600)

        raise Exception(" Could not find 'Family' income option after scrolling")

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
        single_option = wait_for_element_visibility(self.driver, self.SOCIAL_STATUS_SINGLE, 10)
        single_option.click()
        print("Selected social status: Single")

    def select_social_status_married_and_proceed(self):
        """Selects 'Married' social status and proceeds to next question."""
        married_option = wait_for_element_visibility(self.driver, self.SOCIAL_STATUS_MARRIED, 10)
        married_option.click()
        print("Selected social status: Married")
        time.sleep(1)  # Wait for UI update
        self.click_continue()

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
        option1 = wait_for_element_visibility(self.driver, self.ANNUAL_INCOME_OPTION1, 10)
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
        self.click_continue()

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
        self.click_continue()

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
        self.click_continue()

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

    # Method for RiskAbility Screen
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
        self.click_continue()

    def select_risk_ability_high_and_proceed(self):
        """Selects 'High' risk ability and proceeds to next question."""
        high_option = wait_for_element_visibility(self.driver, self.RISK_ABILITY_HIGH, 10)
        high_option.click()
        print("Selected risk ability: High (مخاطر عالية)")
        time.sleep(1)  # Wait for UI update
        self.click_continue()


    def select_risk_ability_very_high_and_proceed(self):
        """Scrolls until 'Very High' risk ability option is visible, selects it, and proceeds."""
        max_swipes = 7
        for _ in range(max_swipes):
            try:
                very_high_option = wait_for_element_visibility(self.driver, self.RISK_ABILITY_VERY_HIGH, 3)
                if very_high_option.is_displayed():
                    very_high_option.click()
                    print(" Selected risk ability: Very High (مخاطر عالية جدًا)")
                    return
            except Exception:
                # Perform scroll if not visible
                size = self.driver.get_window_size()
                start_x = size['width'] / 2
                start_y = size['height'] * 0.8
                end_y = size['height'] * 0.3
                self.driver.swipe(start_x, start_y, start_x, end_y, 600)

        raise Exception(" Could not find 'Very High' risk ability option after scrolling")

    # Mthod for InvestmentTimePeriod Screen
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
        time.sleep(1)  # Wait for UI update
        self.click_continue()

    # Method for InvestmentGoals Screen
    def select_investment_goals_capital_growth_and_proceed(self):
        """Selects 'Capital Growth' investment goal and proceeds to next question."""
        capital_growth_option = wait_for_element_visibility(self.driver, self.INVESTMENT_GOALS_CAPITAL_GROWTH, 10)
        capital_growth_option.click()
        print("Selected investment goal: Capital Growth (نمو رأس المال)")

    def select_investment_goals_protecting_capital_and_proceed(self):
        """Selects 'Protecting Capital' investment goal and proceeds to next question."""
        protecting_capital_option = wait_for_element_visibility(self.driver, self.INVESTMENT_GOALS_PROTECTING_CAPITAL,
                                                                10)
        protecting_capital_option.click()
        print("Selected investment goal: Protecting Capital (المحافظة على رأس المال)")
        time.sleep(1)  # Wait for UI update
        self.click_continue()
    def select_yes_for_PEB(self, next_screen_locator=None):
        button = wait_for_element_visibility(self.driver, self.PEB_YES, 20)
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
    def select_state_and_proceed(self):
        """Selects a random state from the list and clicks Continue."""

        # --- Click state field ---
        field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.STATE_FIELD)
        )
        field.click()

        # --- Wait and fetch all options ---
        options = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(self.STATE_OPTIONS)
        )
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
        text_field.clear()
        text_field.send_keys(random_text)
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass
        next_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CON_BUTTON)
        )
        next_btn.click()
        return random_text

    def select_inheritance_yes(self):

        yes_button = wait_for_element_visibility(self.driver, self.INHERITANCE_YES_BUTTON, 20)
        if yes_button:
            yes_button.click()

    def select_inheritance_year(self):

        # Step 1: Open year selector
        year_field = wait_for_element_visibility(self.driver,self.INHERITANCE_YEAR_FIELD, 20)
        if year_field:
            year_field.click()
        # Step 2: Wait for and pick random SeekBar
        seekbars = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(self.INHERITANCE_SEEKBARS))
        if seekbars:
            random.choice(seekbars).click()
        # Step 3: Confirm year
        confirm_btn = wait_for_element_visibility(
            self.driver,
            self.INHERITANCE_YEAR_CONFIRM_BUTTON,
            20
        )
        if confirm_btn:
            confirm_btn.click()

    def input_investment_value(self, value=None):

        field = wait_for_element_visibility(self.driver, self.INVESTMENT_VALUE_INPUT, 15)
        if field:
            field.click()
            if value is None:
                value = str(random.randint(100000, 999999))
            field.send_keys(value)
            # Close the keyboard
            try:
                self.driver.hide_keyboard()
                print("Keyboard hidden successfully after entering investment value.")
            except Exception:
                print("Keyboard was not open, skipping hide_keyboard.")
            return value

    def select_inheritance_types_and_proceed(self):
        frame = wait_for_element_visibility(self.driver, self.INHERITANCE_FIELD_INPUT, 20)
        if frame:
            frame.click()
        for option in [
            self.INHERITANCE_TYPE_PROPERTIES,
            self.INHERITANCE_TYPE_MOVABLE,
            self.INHERITANCE_TYPE_SHARES
        ]:
            element = wait_for_element_visibility(self.driver, option, 20)
            if element:
                element.click()
                print(f"Selected: {option}")
        # Step 3: Scroll down for 'Other'
        self.driver.swipe(500, 1500, 500, 800, 600)
        other_option = wait_for_element_visibility(self.driver, self.INHERITANCE_TYPE_OTHER, 20)
        if other_option:
            other_option.click()
            print("Selected: Other (أخرى)")
        # Step 4: Scroll to find Confirm button
        confirm_btn = None
        for i in range(5):
            confirm_btn = wait_for_element_visibility(
                self.driver, self.INHERITANCE_CONFIRM_BUTTON, timeout=5, soft_fail=True)
            if confirm_btn:
                break
            else:
                self.driver.swipe(500, 1500, 500, 800, 600)
                print(f"Scrolling to find confirm button... attempt {i + 1}")
        # Step 5: Click Confirm button
        if confirm_btn:
            confirm_btn.click()
            print("Inheritance type selection confirmed.")
        else:
            pytest.fail("Confirm button not found after scrolling.")

    def click_country_field(self):
        field =wait_for_element_visibility(self.driver,self.FIELD, 20)
        field.click()

    def select_random_inheritance_country(self):

        dropdown_items = wait_for_element_visibility(self.driver, self.COUNTRY_ITEM, LITTLE_WAIT)
        dropdown_items.click()
        time.sleep(2)

    def select_grants_yes(self):

        yes_button = wait_for_element_visibility(self.driver, self.GRANTS_YES_BUTTON, 15)
        if yes_button:
            yes_button.click()

    def select_year_of_grant(self):

        # Step 1: Click the grant year frame
        frame = wait_for_element_visibility(self.driver, self.GRANT_YEAR_FRAME, 20)
        if frame:
            frame.click()

        # Step 2: Scroll down & select a random SeekBar with year 2025
        seekbars = self.driver.find_elements(*self.GRANT_YEAR_SEEKBARS)
        if seekbars:
            random.choice(seekbars).click()

        # Step 3: Click confirm button
        confirm_btn = wait_for_element_visibility(self.driver, self.GRANT_YEAR_CONFIRM_BUTTON, 15)
        if confirm_btn:
            confirm_btn.click()

    def input_value_of_grant(self, value=None):
        """
        Clicks the grant value EditText and enters a 6-digit value.
        If no value is provided, generates a random 6-digit number.
        Closes the keyboard after entry.
        """
        field = wait_for_element_visibility(self.driver, self.GRANT_VALUE_INPUT, 15)
        if field:
            field.click()
            if value is None:
                value = str(random.randint(100000, 999999))
            field.send_keys(value)

            # Close keyboard
            try:
                self.driver.hide_keyboard()
            except:
                # Keyboard may already be hidden
                pass

            return value  # return for verification in tests

    def type_of_grant(self):
        """
        Opens grant type frame, selects عقارات, أموال منقولة, أسهم,
        and confirms the selection.
        """
        # Step 1: Open grant type selection frame
        frame = wait_for_element_visibility(self.driver, self.GRANT_TYPE_FRAME, 20)
        if frame:
            frame.click()

        # Step 2: Select each grant type option
        for option in [
            self.GRANT_TYPE_PROPERTIES,
            self.GRANT_TYPE_MOVABLE,
            self.GRANT_TYPE_SHARES
        ]:
            element = wait_for_element_visibility(self.driver, option, 20)
            if element:
                element.click()

        # Step 3: Confirm selection
        confirm_btn = wait_for_element_visibility(self.driver, self.GRANT_TYPE_CONFIRM_BUTTON, 20)
        if confirm_btn:
            confirm_btn.click()

    def country_of_grant(self):

        # Step 1: Open country selection frame
        frame = wait_for_element_visibility(self.driver, self.GRANT_COUNTRY_FRAME, 20)
        if frame:
            frame.click()
            # Optional: hide keyboard if it blocks the dropdown
            try:
                self.driver.hide_keyboard()
            except:
                pass

        # Step 2: Select a random country from dropdown
        dropdown_items = wait_for_all_elements_to_be_visibility(self.driver, self.COUNTRY_ITEM, LITTLE_WAIT)
        if dropdown_items:
            random.choice(dropdown_items).click()
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

    def select_inheritance_no(self):
        """
        Selects 'لا' option in inheritance section.
        """
        no_button = wait_for_element_visibility(self.driver, self.INHERITANCE_NO_BUTTON, 15)
        if no_button:
            no_button.click()

    def select_grants_no(self):
        """
        Selects 'لا' option in grants section.
        """
        no_button = wait_for_element_visibility(self.driver, self.GRANTS_NO_BUTTON, 15)
        if no_button:
            no_button.click()

    def select_investing_outside_abyan(self):
        """
        Selects 'أسهم' option and moves SeekBar to 100%.
        """
        # Step 1: Click on 'أسهم'
        option = wait_for_element_visibility(self.driver, self.INVESTING_OUTSIDE_ABYAN_OPTION, 15)
        if option:
            option.click()
        # Step 2: Move SeekBar to 100%
        seekbar = wait_for_element_visibility(self.driver, self.INVESTING_SEEKBAR, 15)
        if seekbar:
            # get SeekBar dimensions
            start_x = seekbar.location['x']
            start_y = seekbar.location['y']
            width = seekbar.size['width']
            height = seekbar.size['height']
            # move to 100% (end of SeekBar)
            end_x = start_x + width
            end_y = start_y + (height // 2)
            action = TouchAction(self.driver)
            action.press(x=start_x, y=end_y).move_to(x=end_x, y=end_y).release().perform()

    def scroll_up_in_scrollview(self):
        """Scroll up inside //android.widget.ScrollView"""
        scrollview = self.driver.find_element("xpath", "//android.widget.ScrollView")
        # Get element location and size
        loc = scrollview.location
        size = scrollview.size
        # Calculate scroll coordinates (inside the element)
        start_x = loc["x"] + size["width"] // 2
        start_y = loc["y"] + int(size["height"] * 0.8)  # near bottom
        end_x = start_x
        end_y = loc["y"] + int(size["height"] * 0.2)  # near top
        # Perform scroll up
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    # def move_seekbar_to_percentage(self, start_x=961, end_x=352, y=1027, percentage=0.5):
    #     """
    #     Move seekbar to a specific percentage (0.0 - 1.0).
    #     Example: 0.5 = 50%
    #     """
    #     # total width
    #     width = start_x - end_x
    #     # calculate target x
    #     target_x = int(end_x + (width * percentage))
    #
    #     actions = ActionChains(self.driver)
    #     actions.w3c_actions = ActionBuilder(
    #         self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
    #     )
    #     actions.w3c_actions.pointer_action.move_to_location(start_x, y)
    #     actions.w3c_actions.pointer_action.pointer_down()
    #     actions.w3c_actions.pointer_action.move_to_location(target_x, y)
    #     actions.w3c_actions.pointer_action.release()
    #     actions.perform()
    def move_seekbar_to_percentage(self, element, percentage=0.5):
        """
        Move seekbar thumb to a specific percentage of the width.
        element: seekbar WebElement
        percentage: float between 0.0 - 1.0
        """
        # get element size and location
        location = element.location
        size = element.size

        start_x = location["x"]
        end_x = start_x + size["width"]
        y = location["y"] + size["height"] // 2

        # calculate target
        target_x = int(start_x + (size["width"] * percentage))

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.w3c_actions.pointer_action.move_to_location(start_x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(target_x, y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def select_first_investing_outside(self):
        """Select 'أسهم' first and move SeekBar to 50%."""
        field = wait_for_element_visibility(self.driver, self.INVESTING_OPTION_SHARES, 15)
        field.click()
        seekbar = wait_for_element_visibility(self.driver, self.INVESTING_SEEKBAR, 15)
        self.move_seekbar_to_percentage(seekbar, percentage=0.5)

    def select_second_investing_outside(self):
        """Select 'أدوات دين' and move SeekBar to 30%."""
        field = wait_for_element_visibility(self.driver, self.INVESTING_OPTION_PROPERTIES, 15)
        field.click()
        seekbar = wait_for_element_visibility(self.driver, self.INVESTING_SEEKBAR, 15)
        self.move_seekbar_to_percentage(seekbar, percentage=0.3)

    def select_third_investing_outside(self):
        """Select 'عقارات' and move SeekBar to 20%."""
        field = wait_for_element_visibility(self.driver, self.INVESTING_OPTION_DEPOSITS, 15)
        field.click()
        seekbar = wait_for_element_visibility(self.driver, self.INVESTING_SEEKBAR, 15)
        self.move_seekbar_to_percentage(seekbar, percentage=0.2)

    def select_fourth_investing_outside(self):
        """Select 'أموال منقولة' and move SeekBar to 10%."""
        field = wait_for_element_visibility(self.driver, self.INVESTING_OPTION_DEBT, 15)
        field.click()
        seekbar = wait_for_element_visibility(self.driver, self.INVESTING_SEEKBAR, 15)
        self.move_seekbar_to_percentage(seekbar, percentage=0.1)

    def input_financial_institution(self):
        """
        Clicks on financial institution input field and enters random text.
        Either 10 random letters OR 3 random words.
        """
        field = wait_for_element_visibility(self.driver, self.FINANCIAL_INSTITUTION_INPUT, 15)
        if field:
            field.click()

            # --- Random choice: letters or words ---
            if random.choice([True, False]):
                # 10 random letters
                text = ''.join(random.choices(string.ascii_letters, k=10))
            else:
                # 3 random words
                words = [
                    ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))
                    for _ in range(3)
                ]
                text = " ".join(words)

            field.send_keys(text)

    def click_add_institution(self):
        """
        Clicks on 'إضافة مؤسسة' button.
        """
        button = wait_for_element_visibility(self.driver, self.ADD_INSTITUTION_BUTTON, 15)
        if button:
            button.click()

    def input_financial_institution_two(self):
        """
        Clicks on the 2nd financial institution input field and enters 3 random words.
        """
        field = wait_for_element_visibility(self.driver, self.FINANCIAL_INSTITUTION_INPUT_TWO, 15)
        if field:
            field.click()

            # Generate 3 random words (each 3–6 letters)
            words = [
                ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))
                for _ in range(3)
            ]
            text = " ".join(words)

            field.send_keys(text)

    def input_financial_institution_three(self):
        """
        Clicks on the 3rd financial institution input field and enters 3 random words.
        """
        field = wait_for_element_visibility(self.driver, self.FINANCIAL_INSTITUTION_INPUT_THREE, 15)
        if field:
            field.click()

            # Generate 3 random words (each 3–6 letters)
            words = [
                ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))
                for _ in range(3)
            ]
            text = " ".join(words)

            field.send_keys(text)

    def input_financial_institution_four(self):
        """
        Clicks on the 4th financial institution input field and enters 3 random words.
        """
        field = wait_for_element_visibility(self.driver, self.FINANCIAL_INSTITUTION_INPUT_FOUR, 20)
        if field:
            field.click()

            # Generate 3 random words (each 3–6 letters)
            words = [
                ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))
                for _ in range(3)
            ]
            text = " ".join(words)

            field.send_keys(text)

    def select_next(self):
        """
        Clicks on 'التالي' (Next) button.
        """
        button = wait_for_element_visibility(self.driver, self.NEXT_BUTTON, 20)
        if button:
            button.click()
    def select_next_btn(self):
        """
        Clicks on 'التالي' (Next) button.
        """
        button = wait_for_element_visibility(self.driver, self.NEXT_BTN, 20)
        if button:
            button.click()

    def input_current_investment_value(self):
        """
        Clicks on 'Current Investment Value' field and enters a random 6-digit amount.
        """
        field = wait_for_element_visibility(self.driver, self.CURRENT_INVESTMENT_VALUE_INPUT, 15)
        if field:
            field.click()
            value = str(random.randint(100000, 999999))  # always 6 digits
            field.send_keys(value)

    def input_expected_investment_annual(self):
        """
        Clicks on 'Expected Investment Annual' field and enters a random 6-digit amount.
        """
        field = wait_for_element_visibility(self.driver, self.EXPECTED_INVESTMENT_ANNUAL_INPUT, 15)
        if field:
            field.click()
            amount = str(random.randint(100000, 999999))  # ensures 6 digits
            field.send_keys(amount)


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
        email = f"{random_str}@test.com"
        email_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_field.click()
        time.sleep(2)
        email_field.clear()
        email_field.send_keys(email)
        print(f"Entered random email: {email}")
        return email

    def button_continue(self):
        continue_button = wait_for_element_visibility(self.driver, self.BUTTON_CONTINUE, 20)
        if continue_button:
            continue_button.click()
            time.sleep(2)
        else:
            print("Continue button not found.")

    def verify_user_is_on_create_success_screen(self):
        try:
            element = wait_for_element_visibility(self.driver, self.CREATE_SUCCESS_SCREEN, 20)
            print(" User is on the create success screen.")
            return True
        except TimeoutException:
            print("create success screen not found.")
            return False

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
#PEB Screen five questions
    def select_has_work_on_Financial(self):
        """Click on 'هل سبق للعميل العمل في القطاع المالي خلال السنوات الخمس السابقة؟' field."""
        element = wait_for_element_visibility(self.driver, KycPebBlock.HAS_WORK_ON_FINANCIAL, 20)
        element.click()
    def select_related_experience(self):
        """Click on 'هل سبق للعميل العمل في القطاع المالي خلال السنوات الخمس السابقة؟' field."""
        element = wait_for_element_visibility(self.driver, KycPebBlock.RELATED_EXPERIENCE, 20)
        element.click()


    def select_peb_question_for_membership_relevant(self, max_scrolls=5):
        """
        Always scroll first, then check if 'Board Member / Executive' question is visible.
        Once visible: click it, then input 9 random letters into its EditText.
        """
        for i in range(max_scrolls):
            try:
                # Step 1: Scroll first (force scroll every iteration)
                print(f"Scrolling... attempt {i + 1}")
                self.driver.swipe(
                    start_x=500, start_y=1200,
                    end_x=500, end_y=600,
                    duration=600
                )

                # Step 2: Check if the question is visible after scroll
                element = wait_for_element_visibility(
                    self.driver,
                    self.MEMBERSHIP_RELEVANT,
                    timeout=5,
                    soft_fail=True
                )
                if element:
                    element.click()
                    print(" Clicked on 'Board Member / Executive' question.")

                    # Step 3: Input field interaction
                    input_field = self.driver.find_element(*self.MEMBERSHIP_RELEVANT_INPUT)
                    input_field.click()

                    random_text = ''.join(random.choices(string.ascii_letters, k=9))
                    input_field.clear()
                    input_field.send_keys(random_text)
                    print(f" Entered random text: {random_text}")
                    return random_text
            except Exception as e:
                print(f" Attempt {i + 1} failed with error: {e}")

        print(" Could not find 'Board Member / Executive' question after scrolling.")
        return None

    def select_peb_question_for_government_employee(self, max_scrolls=5):
        """
        Always scroll first, then check if 'Government Employee' PEB question is visible.
        Once visible: click it.
        """
        for i in range(max_scrolls):
            try:
                # Step 1: Scroll first (force scroll every iteration)
                print(f" Scrolling... attempt {i + 1}")
                self.driver.swipe(
                    start_x=500, start_y=1200,
                    end_x=500, end_y=600,
                    duration=600
                )

                # Step 2: Check if the question is visible after scroll
                element = wait_for_element_visibility(
                    self.driver,
                    self.PEB_GOVERNMENT_EMPLOYEE_QUESTION,
                    timeout=5,
                    soft_fail=True
                )
                if element:
                    element.click()

                    print(" Clicked on 'Government Employee' question.")
                    return
            except Exception as e:
                print(f" Attempt {i + 1} failed: {e}")

        # If loop ends without finding element
        raise Exception(" Could not find 'Government Employee' question after scrolling.")

    def input_random_text_in_field_second(self):
        """
        Clicks on the first Membership/Executive input field and enters 9 random letters.
        """
        element = wait_for_element_visibility(self.driver, self.MEMBERSHIP_RELEVANT_INPUT_TWO, timeout=20)
        element.click()
        self.driver.hide_keyboard()
        print(" Clicked on Membership input field")

        # Generate exactly 9 random letters
        random_text = ''.join(random.choices(string.ascii_letters, k=9))

        # Clear field first then input
        element.clear()
        element.send_keys(random_text)
        print(f" Entered random text: {random_text}")
        return random_text

    def select_peb_question_for_relative_government_employee(self, max_scrolls=5):
        """
        Scroll and select 'Relative Government Employee' PEB question.
        Then input random text into its two EditText fields.
        """
        for i in range(max_scrolls):
            try:
                # Step 1: Scroll first
                print(f" Scrolling... attempt {i + 1}")
                self.driver.swipe(
                    start_x=500, start_y=1200,
                    end_x=500, end_y=600,
                    duration=600
                )

                # Step 2: Check if question is visible
                element = wait_for_element_visibility(
                    self.driver,
                    self.PEB_RELATIVE_GOVERNMENT_EMPLOYEE,
                    timeout=5,
                    soft_fail=True
                )
                if element:
                    element.click()
                    print("Clicked on 'Relative Government Employee' question.")

                    # Step 3: Input field 1
                    input1 = self.driver.find_element(*self.PEB_RELATIVE_GOVERNMENT_EMPLOYEE_INPUT1)
                    input1.click()
                    random_text1 = ''.join(random.choices(string.ascii_letters, k=9))
                    input1.clear()
                    input1.send_keys(random_text1)
                    print(f"️ Entered random text in field 1: {random_text1}")

                    # Step 4: Input field 2
                    input2 = self.driver.find_element(*self.PEB_RELATIVE_GOVERNMENT_EMPLOYEE_INPUT2)
                    input2.click()
                    random_text2 = ''.join(random.choices(string.ascii_letters, k=9))
                    input2.clear()
                    input2.send_keys(random_text2)
                    self.driver.hide_keyboard()
                    print(f" Entered random text in field 2: {random_text2}")

                    return random_text1, random_text2


            except Exception as e:
                print(f" Attempt {i + 1} failed with error: {e}")

        print(" Could not find 'Relative Government Employee' question after scrolling.")
        return None

    def verify_under_review_screen(self):
        """
        Verify that user is on 'Account Under Review' screen.
        """
        element = wait_for_element_visibility(self.driver, self.UNDER_REVIEW_SCREEN, timeout=20, soft_fail=False)
        assert element is not None, " User is not on 'Account Under Review' screen."
        print(" User is on 'Account Under Review' screen.")
        time.sleep(LONG_WAIT)


    def click_refresh_page(self):

        button = wait_for_element_visibility(self.driver, self.REFRESH_PAGE_BUTTON, timeout=20)
        if button:
            button.click()
        time.sleep(LITTLE_WAIT)

    def continue_to_edit(self):
        button = wait_for_element_visibility(self.driver, self.CONTINUE_EDIT, 10)
        button.click()

    def adjust_distribution_ratio(self, x=549, y=1767):
        """
        Tap on the given coordinates (default: 549, 1767).
        """
        action = TouchAction(self.driver)
        action.tap(x=x, y=y).perform()
        time.sleep(1)

    def select_invest_outside(self,x=678, y=851):
        action = TouchAction(self.driver)
        action.tap(x=x, y=y).perform()
        time.sleep(1)

    def click_success_edit_due_diligence(self):
        button =wait_for_element_visibility(self.driver,self.EDIT_SUCCESS, 15)
        button.click()

    def remove_financial_institution_three(self):
        button =wait_for_element_visibility(self.driver,self.REMOVE_THREE, 15)
        button.click()
    def remove_financial_institution_two(self):
        button =wait_for_element_visibility(self.driver,self.REMOVE_TWO, 15)
        button.click()
    def remove_financial_institution_one(self):
        button =wait_for_element_visibility(self.driver,self.REMOVE_ONE, 15)
        button.click()

    def remove_and_input_current_investment_value(self):
        """
        Clicks on 'Current Investment Value' field, clears existing text,
        and enters a random 6-digit amount.
        """
        field = wait_for_element_visibility(self.driver, self.CURRENT_INVESTMENT_VALUE_INPUT, 15)
        if field:
            field.click()
            field.clear()  #  remove existing text first
            value = str(random.randint(100000, 999999))  # always 6 digits
            field.send_keys(value)
            return value
    def remove_and_input_expected_investment_annual(self):
        """
        Clicks on 'Expected Investment Annual' field and enters a random 6-digit amount.
        """
        field = wait_for_element_visibility(self.driver, self.EXPECTED_INVESTMENT_ANNUAL_INPUT, 15)
        if field:
            field.click()
            field.clear()
            amount = str(random.randint(100000, 999999))  # ensures 6 digits
            field.send_keys(amount)
            return amount








