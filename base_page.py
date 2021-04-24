from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.action = ActionChains(self.driver)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message="Can't find element",
        )

    def open_page(self):
        self.driver.get(self.url)

    def wait_page_load(self, old_url, time=10):
        WebDriverWait(self.driver, time).until(EC.url_changes(old_url))
