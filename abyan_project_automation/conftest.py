import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

def pytest_addoption(parser):
    parser.addoption(
        "--apk",
        action="store",
        default="app-staging-debug.apk",
        help="APK file name inside resources folder (e.g., app-staging-debug.apk)"
    )
    parser.addoption(
        "--keep-app-open",
        action="store_true",
        help="If set, the app will stay open after the test for Appium Inspector"
    )

@pytest.fixture(scope="function")
def driver(request):
    apk_name = request.config.getoption("--apk")
    keep_open = request.config.getoption("--keep-app-open")

    project_root = os.path.dirname(os.path.abspath(__file__))
    apk_path = os.path.join(project_root, "resources", apk_name)
    if not os.path.exists(apk_path):
        raise FileNotFoundError(f"APK not found at: {apk_path}")

    # Capabilities
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app = apk_path
    options.app_package = "com.abyanflutter.qa"
    options.app_activity = "com.abyanflutter.abyan_flutter.MainActivity"
    options.no_reset = False
    options.full_reset = True
    options.auto_grant_permissions = True
    options.ensure_webviews_have_pages = True
    options.native_web_screenshot = True
    options.new_command_timeout = 600
    options.connect_hardware_keyboard = True

    # Start driver
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)

    yield driver

    if not keep_open:
        # Quit driver only if user did not request to keep app open
        try:
            driver.quit()
        except Exception as e:
            print(f"Warning: driver.quit() failed: {e}")
