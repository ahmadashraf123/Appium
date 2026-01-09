import time

from appium.webdriver.common.appiumby import AppiumBy

class CashCategoryToCategoryTransfer:


    def __init__(self, driver):
        self.driver = driver
    time.sleep(3)
    def click_on_transfer_button(self):
        """Clicks on the Transfer button."""
        print("Clicking on Transfer button...")
        transfer_button = (
            AppiumBy.XPATH,
            '//android.view.View[@content-desc="تحويل"]'
        )
        self.driver.find_element(*transfer_button).click()




