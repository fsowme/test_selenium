from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.action = ActionChains(self.driver)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message="Can't find element",
        )

    def find_all_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message="Can't find elements",
        )

    def open_page(self):
        self.driver.get(self.url)

    def perform(self):
        self.action.perform()

    def wait_page_load(self, old_url, time=10):
        WebDriverWait(self.driver, time).until(EC.url_changes(old_url))

    def close(self):
        self.driver.close()
