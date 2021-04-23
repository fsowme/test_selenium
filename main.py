import json
import timeit

import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from page import MainPage, OsagoCalcPage

URL = "https://www.alfastrah.ru/"
REPORT_URL = "https://b2b-test.alfastrah.ru/amis-api/test/write/"

options = Options()
options.add_argument("--disable-notifications")


def alfa_test(url=URL):
    start_time = timeit.default_timer()
    with Chrome(options=options) as driver:
        alfa_mainpage = MainPage(driver, url)
        alfa_mainpage.open_page()
        alfa_mainpage.close_cookies()
        alfa_mainpage.activate_car_block()
        alfa_mainpage.goto_osago_calc()
        alfa_osago_page = OsagoCalcPage(driver, driver.current_url)
        alfa_osago_page.insert_license_plate("В 223 ВС", "777")
        alfa_osago_page.insert_vin("SDVFBN38NV38FNK3U")
        alfa_osago_page.select_category("B - легковые")
        alfa_osago_page.insert_car_brand("ASTON MARTIN")
        alfa_osago_page.insert_car_model("DB11")
        alfa_osago_page.insert_year("2021")
        alfa_osago_page.click_next()
    return timeit.default_timer() - start_time


def send_result(url=REPORT_URL):
    time = alfa_test()
    data = json.dumps(
        {
            "it_service": "site_test",
            "measurements": {"calc_eosago": time},
            "source": "selenium",
        }
    )
    headers = {"Content-Type": "application/json"}
    requests.post(url, data=data, headers=headers)


if __name__ == "__main__":

    send_result()
