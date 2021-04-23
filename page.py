from selenium.webdriver.support.ui import Select

from base_page import BasePage
from locator import MainPageLocator, OsagoCalcLocator


class MainPage(BasePage):
    def close_cookies(self):
        self.find_element(MainPageLocator.COOKIES).click()

    def activate_car_block(self):
        self.action.move_to_element(
            self.find_element(MainPageLocator.CAR_BUTTON)
        ).perform()

    def goto_osago_calc(self):
        self.find_element(MainPageLocator.CALC_OSAGO).click()


class OsagoCalcPage(BasePage):
    def insert_license_plate(self, number, region):
        self.find_element(OsagoCalcLocator.LICENSE_NUMBER).send_keys(number)
        self.find_element(OsagoCalcLocator.LICENSE_REGION).send_keys(region)

    def insert_vin(self, vin):
        self.find_element(OsagoCalcLocator.VIN).send_keys(vin)

    def select_category(self, category):
        element = self.find_element(OsagoCalcLocator.CATEGORY_SELECTOR)
        Select(element).select_by_value(category)

    def insert_car_brand(self, brand):
        self.find_element(OsagoCalcLocator.CAR_BRAND).send_keys(brand)

    def insert_car_model(self, model):
        self.find_element(OsagoCalcLocator.CAR_MODEL).send_keys(model)

    def insert_year(self, year):
        self.find_element(OsagoCalcLocator.YEAR).send_keys(year, "\ue004")

    def click_next(self):
        self.action.move_to_element(
            self.find_element(OsagoCalcLocator.NEXT_BUTTON)
        ).perform()
        self.action.send_keys("\ue015")
        self.action.send_keys("\ue015")
        self.action.pause(1).perform()
        element = self.find_element(OsagoCalcLocator.NEXT_BUTTON)
        element.click()
