import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def wait_for_element_visibility(driver, locator, timeout=10, soft_fail=False):
    """
    Wait for element visibility.

    :param driver: WebDriver instance
    :param locator: Tuple (By, value)
    :param timeout: Max wait time
    :param soft_fail: If True, do not fail the test when element not found
    """
    try:
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    except (TimeoutException, NoSuchElementException):
        if soft_fail:
            return None   # gracefully return instead of failing test
        else:
            pytest.fail(f"Element {locator} not visible within {timeout} seconds")

def wait_for_element_clickable(driver, locator, timeout=10):
    """
    Waits for an element to be clickable.
    Returns the element if found, else returns None.
    """
    try:
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    except (TimeoutException, NoSuchElementException):
        pytest.fail()

def wait_for_presence_of_element(driver, locator, timeout=10):
    """
    Waits until the element is present in the DOM.
    Useful even if the element is not visible yet.
    Returns the element or None.
    """
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    except (TimeoutException, NoSuchElementException):
        return None

def is_element_present(driver, locator, timeout=10):
    """
    Returns True if the element is present within timeout.
    Otherwise, returns False.
    """
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return True
    except (TimeoutException, NoSuchElementException):
        return False

def hard_wait(seconds):
    """Hardcoded wait - use only when absolutely necessary."""
    time.sleep(seconds)

def wait_for_all_elements_to_be_visibility(driver, locator, timeout=10):

    try:
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
    except (TimeoutException, NoSuchElementException):
        pytest.fail(f"Element {locator} not visible within {timeout} seconds")
