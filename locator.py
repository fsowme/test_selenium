from selenium.webdriver.common.by import By


class MainPageLocator:
    CALC_POSITION = 2
    COOKIES = (By.CSS_SELECTOR, "span.cookie-info__close")
    CAR_BUTTON = (By.CSS_SELECTOR, "div.calc__item")
    CALC_OSAGO = (
        By.CSS_SELECTOR,
        f"div.calc__list div.calc-popup__list "
        f"div.calc-popup__item:nth-of-type({CALC_POSITION}) "
        f"a.calc-popup__link",
    )


class OsagoCalcLocator:
    CAR_FORM = (By.CSS_SELECTOR, "form__group")
    LICENSE_NUMBER = (By.NAME, "AUTO_NUMBER")
    LICENSE_REGION = (By.NAME, "AUTO_REGION")
    VIN = (By.NAME, "CarIdVIN")
    CATEGORY_SELECTOR = (By.NAME, "category")
    CAR_BRAND = (By.NAME, "brand_name")
    CAR_MODEL = (By.NAME, "model_name")
    YEAR = (By.NAME, "year")
    NEXT_BUTTON = (By.CLASS_NAME, "btn.js-submit-osago-step-1")
