import json
import timeit

import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from page import MainPage, OsagoCalcPage

URL = "https://www.alfastrah.ru/"
REPORT_URL = "https://b2b-test.alfastrah.ru/amis-api/test/write/"
VEHICLE_DATA = {
    "license_number": "В 223 ВС",
    "region": "777",
    "vin": "SDVFBN38NV38FNK3U",
    "category": "B - легковые",
    "brand": "ASTON MARTIN",
    "model": "DB11",
    "year": "2021",
}
options = Options()
options.add_argument("--disable-notifications")


def alfa_test(url=URL, vehicle_data=VEHICLE_DATA):
    with Chrome(options=options) as driver:

        # Actions on main page
        alfa_mainpage = MainPage(driver, url)
        alfa_mainpage.open_page()
        alfa_mainpage.close_cookies()
        alfa_mainpage.activate_car_block()
        alfa_mainpage.goto_osago_calc()

        # Actions on calc page
        alfa_osago_page = OsagoCalcPage(driver, driver.current_url)
        alfa_osago_page.insert_license_plate(
            vehicle_data["license_number"], vehicle_data["region"]
        )
        alfa_osago_page.insert_vin(vehicle_data["vin"])
        alfa_osago_page.select_category(vehicle_data["category"])
        alfa_osago_page.insert_brand(vehicle_data["brand"])
        alfa_osago_page.insert_car_model(vehicle_data["model"])
        alfa_osago_page.insert_year(vehicle_data["year"])
        alfa_osago_page.click_next()


def send_result(url=REPORT_URL, func=alfa_test):
    start_time = timeit.default_timer()
    func()
    time = timeit.default_timer() - start_time
    data = json.dumps(
        {
            "it_service": "site_test",
            "measurements": {"calc_eosago": int(time)},
            "source": "selenium",
        }
    )
    headers = {"Content-Type": "application/json"}
    return requests.post(url, data=data, headers=headers)


if __name__ == "__main__":

    send_result()
