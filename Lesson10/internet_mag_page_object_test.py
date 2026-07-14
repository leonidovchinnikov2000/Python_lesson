import allure
from selenium import webdriver

from InternetMagPage import InternetMagPage


@allure.id("Internet_mag")
@allure.epic("Интернет магазин")
@allure.severity("blocker")
@allure.story("Покупка товаров")
@allure.feature("CREATE")
@allure.title("Выбор товара, работа с корзиной и оплата")
@allure.suite("Тесты на работу с интернет-магазином")
def test_form_internet_mag():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome()

    internet_mag_page = InternetMagPage(driver)

    internet_mag_page.authorization("standard_user", "secret_sauce")
    to_be = internet_mag_page.add_products()
    internet_mag_page.go_to_cart()
    internet_mag_page.personal_data("Svetlana", "Voroshilova", "420105")
    as_is = internet_mag_page.total_cost()

    with allure.step("Проверить,что ожидаемая и фактическая стоимость равны"):
        assert as_is == to_be

    internet_mag_page.close()
