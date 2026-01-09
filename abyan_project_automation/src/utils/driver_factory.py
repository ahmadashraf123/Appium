import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_driver(install_app=True):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"

    apk_path = apk_path =  r"D:\\AbyanApplication\\abyan_project_automation\\resources\\app-staging-debug.apk"

    if install_app and os.path.exists(apk_path):
        # Install app if file exists and install_app is True
        options.app = apk_path
        options.no_reset = False
        options.full_reset = True
    else:
        # Do not reinstall app
        options.app_package = "com.abyanflutter.qa"
        options.app_activity = "com.abyanflutter.abyan_flutter.MainActivity"
        options.no_reset = True  # Important! Keeps app installed and logged in
        options.full_reset = False

    options.ensure_webviews_have_pages = True
    options.native_web_screenshot = True
    options.new_command_timeout = 3600
    options.connect_hardware_keyboard = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    return driver

