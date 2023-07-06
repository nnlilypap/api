import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestingOLX():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.passed_tests = 0
        self.failed_tests = 0
        self.test_results = []

    def teardown_method(self, method):
        self.driver.quit()

    def remove_onetrust_consent(self):
        # Wait for the onetrust-consent-sdk element to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'onetrust-consent-sdk'))
        )

        # Execute JavaScript to remove the onetrust-consent-sdk element from the DOM
        self.driver.execute_script('''
            var element = document.getElementById('onetrust-consent-sdk');
            element.parentNode.removeChild(element);
        ''')

    def test_testingOLX(self):
        self.driver.get('https://www.olx.pl/')

        # Remove the onetrust-consent-sdk element from the DOM
        self.remove_onetrust_consent()

        self.driver.set_window_size(1440, 900)

        elements = self.driver.find_elements(By.ID, 'headerSearch')
        if len(elements) > 0:
            self.passed_tests += 1
            self.test_results.append('Test Testing OLX - Element present: PASSED')
        else:
            self.failed_tests += 1
            self.test_results.append('Test Testing OLX - Element present: FAILED')

        assert len(elements) > 0
        self.driver.find_element(By.ID, 'headerSearch').click()
        self.driver.find_element(By.ID, 'headerSearch').send_keys('laptop')
        value = self.driver.find_element(By.ID, 'headerSearch').get_attribute('value')
        assert value == 'laptop'
        elements = self.driver.find_elements(By.ID, 'submit-searchmain')

        assert len(elements) > 0
        self.driver.find_element(By.ID, 'submit-searchmain').click()
        value = self.driver.find_element(By.ID, 'search').get_attribute('value')
        assert value == 'laptop'

        self.driver.close()

    def test_testOLX2(self):
        self.driver.get('https://www.olx.pl/')

        # Remove the onetrust-consent-sdk element from the DOM
        self.remove_onetrust_consent()

        self.driver.set_window_size(1440, 900)

        element = self.driver.find_element(By.CSS_SELECTOR, '.cat-icon-3')
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        element = self.driver.find_element(By.CSS_SELECTOR, 'body')
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        elements = self.driver.find_elements(By.CSS_SELECTOR, '.cat-icon-3')
        assert len(elements) > 0

        self.driver.find_element(By.CSS_SELECTOR, '.cat-icon-3').click()
        self.driver.execute_script('window.scrollTo(0,157)')
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '#bottom3 > .subcategories-title').click()

        elements = self.driver.find_elements(By.CSS_SELECTOR, '.fleft:nth-child(1) > .cat-3 > .link > span')
        assert len(elements) > 0

        self.driver.find_element(By.CSS_SELECTOR, '.fleft:nth-child(1) > .cat-3 > .link > span').click()
        self.driver.find_element(By.CSS_SELECTOR, '.fleft:nth-child(1) > .cat-3 > .link > span').click()
        self.driver.find_element(By.CSS_SELECTOR, '.fleft:nth-child(1) > .cat-3 > .link > span').click()

        time.sleep(2)

        # Check if the current URL matches the expected URL
        expected_url = 'https://www.olx.pl/nieruchomosci/mieszkania/'
        current_url = self.driver.current_url
        if current_url == expected_url:
            self.passed_tests += 1
            self.test_results.append('Test Test OLX2 - URL match: PASSED')
        else:
            self.failed_tests += 1
            self.test_results.append('Test Test OLX2 - URL match: FAILED')

        self.driver.close()

    def test_testOLX3(self):
        self.driver.get('https://www.olx.pl/')

        # Remove the onetrust-consent-sdk element from the DOM
        self.remove_onetrust_consent()

        self.driver.set_window_size(1440, 900)

        elements = self.driver.find_elements(By.CSS_SELECTOR, '.static:nth-child(1) .block:nth-child(2) span')
        assert len(elements) > 0

        self.driver.find_element(By.CSS_SELECTOR, '.static:nth-child(1) .block:nth-child(2) span').click()

        time.sleep(2)

        # Check if the current URL matches the expected URL
        expected_url = 'https://pomoc.olx.pl/olxplhelp/s/'
        current_url = self.driver.current_url
        if current_url == expected_url:
            self.passed_tests += 1
            self.test_results.append('Test Test OLX3 - URL match: PASSED')
        else:
            self.failed_tests += 1
            self.test_results.append('Test Test OLX3 - URL match: FAILED')

        self.driver.close()

    def test_testOLX4(self):
        self.driver.get('https://www.olx.pl/')

        # Remove the onetrust-consent-sdk element from the DOM
        self.remove_onetrust_consent()

        self.driver.set_window_size(1440, 900)

        elements = self.driver.find_elements(By.CSS_SELECTOR, '.static:nth-child(2) .block:nth-child(6) span')
        assert len(elements) > 0

        time.sleep(2)

        link_element = self.driver.find_element(By.CSS_SELECTOR, '.static:nth-child(2) .block:nth-child(6) span')

        # Right-click on the link element
        actions = ActionChains(self.driver)
        actions.context_click(link_element).perform()

        # Select the option to open the link in a new tab from the context menu
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[1])

        time.sleep(2)

        # Check if the current URL matches the expected URL
        expected_url = 'https://careers.olxgroup.com/'
        current_url = self.driver.current_url
        if current_url == expected_url:
            self.passed_tests += 1
            self.test_results.append('Test Test OLX4 - URL match: PASSED')
        else:
            self.failed_tests += 1
            self.test_results.append('Test Test OLX4 - URL match: FAILED')

        # Close the new tab and switch back to the original tab
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Use JavaScript to close the original tab/window
        self.driver.execute_script('window.close();')

        # Quit the driver to ensure all windows/tabs are closed
        self.driver.quit()

    def test_testOLX5(self):
        self.driver.get('https://www.olx.pl/')

        # Remove the onetrust-consent-sdk element from the DOM
        self.remove_onetrust_consent()

        self.driver.set_window_size(1440, 900)
        elements = self.driver.find_elements(By.CSS_SELECTOR, '.nowrap > span')
        assert len(elements) > 0

        if len(elements) > 0:
            self.passed_tests += 1
            self.test_results.append('Test Testing OLX5 - Element present: PASSED')
        else:
            self.failed_tests += 1
            self.test_results.append('Test Testing OLX5 - Element present: FAILED')

        self.driver.find_element(By.CSS_SELECTOR, '.nowrap > span').click()
        # Close the new tab and switch back to the original tab
        self.driver.close()

        # Quit the driver to close all windows/tabs
        self.driver.quit()

    def run_tests(self):
        self.setup_method(None)
        self.test_testingOLX()
        self.teardown_method(None)

        self.setup_method(None)
        self.test_testOLX2()
        self.teardown_method(None)

        self.setup_method(None)
        self.test_testOLX3()
        self.teardown_method(None)

        self.setup_method(None)
        self.test_testOLX4()
        self.teardown_method(None)

        self.setup_method(None)
        self.test_testOLX5()
        self.teardown_method(None)

        self.print_test_results()

    def print_test_results(self):
        total_tests = self.passed_tests + self.failed_tests
        print(f'Total tests: {total_tests}')
        print(f'Passed tests: {self.passed_tests}')
        print(f'Failed tests: {self.failed_tests}')
        print('\n'.join(self.test_results))

        if self.failed_tests == 0:
            print('All tests passed successfully!')
        else:
            print('Some tests failed.')

if __name__ == '__main__':
    p = TestTestingOLX()
    p.run_tests()
