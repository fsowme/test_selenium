## Тестовое для АО "АльфаСтрахование"
### Запуск
```
git clone git@github.com:fsowme/test_alfa_selenium.git
cd test_alfa_selenium/
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
chmod +x run.sh
wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip
unzip chromedriver_linux64.zip -d venv/bin && rm chromedriver_linux64.zip
```
> Если последняя команда вызвала ошибку, установите ```unzip``` или распакуйте как-то иначе ```сhromedriver``` в папку bin виртуального окружения.

> Так же версия драйвера может отличаться, в зависимости от версии браузера.

Запуск теста в цикле:
```
./run.sh &
```

### Описание
Попытка написать по паттерну **[объекты страниц](https://selenium-python.readthedocs.io/page-objects.html)**.

- [main.py](https://github.com/fsowme/test_alfa_selenium/blob/master/main.py) - основной файл запуска.
    - alfa_test() - имитирует действия пользователя на странице по шагам.
- [locator.py](https://github.com/fsowme/test_alfa_selenium/blob/master/locator.py) - локаторы (карта элементов на странице).
    - class MainPageLocator - локаторы главной страницы.
    - class OsagoCalcLocator - локаторы страницы расчета ОСАГО.
- [base_page.py](https://github.com/fsowme/test_alfa_selenium/blob/master/base_page.py) - базовый класс страниц.
    - class BasePage - базовый класс. Умеет открывать/закрывать страницы и искать на них элементы, и ждать пока загрузится страница после нажатия по ссылке.
- [page.py](https://github.com/fsowme/test_alfa_selenium/blob/master/page.py) - классы страниц.
    - class MainPage(BasePage) - класс управления главной страницы.
        1. Закрывает понель с уведомлением о сборе персональных данных.
        2. Наводит курсор на блок со страховкой на автомобили, автивируя кнопку перехода к калькулятору ОСАГО.
        3. Переходит на страницу ОСАГО
    - class OsagoCalcPage(BasePage) - класс управления страницы калькулятора ОСАГО.
        1. Методы начинающиеся как ```insert_*``` вставляют в поля формы значения.
        2. Методы начинающиеся как ```select_*``` выберают значения из выпадающего списка.
