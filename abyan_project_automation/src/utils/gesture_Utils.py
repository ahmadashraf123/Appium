from selenium.common import NoSuchElementException


def scroll_to_element_and_click(driver, locator_or_element, max_scrolls=5):
    """
    Scrolls until the element is visible and clicks.
    Can accept either a locator tuple (By, value) or a WebElement.
    """
    for _ in range(max_scrolls):
        try:
            # If WebElement is passed, just use it
            if hasattr(locator_or_element, "click"):  
                locator_or_element.click()
                return

            # Otherwise treat it as locator tuple
            element = driver.find_element(*locator_or_element)
            element.click()
            return
        except NoSuchElementException:
            driver.execute_script("mobile: swipe", {"direction": "up", "percent": 0.8})

    raise Exception(f"Element {locator_or_element} not found after {max_scrolls} scrolls")