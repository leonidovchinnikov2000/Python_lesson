from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

def main():
    # Автоматическая установка и настройка GeckoDriver (Firefox)
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        # Переход на целевую страницу
        driver.get("http://the-internet.herokuapp.com/inputs")
        print("Страница загружена.")

        # Ожидание загрузки страницы
        time.sleep(2)

        # Поиск поля ввода
        input_field = driver.find_element(By.TAG_NAME, "input")

        # Ввод текста 12345
        input_field.send_keys("12345")
        print("Введён текст: 12345")

        # Очистка поля
        input_field.clear()
        print("Поле очищено.")

        # Ввод текста 54321
        input_field.send_keys("54321")
        print("Введён текст: 54321")

        # Небольшая задержка, чтобы увидеть результат (опционально)
        time.sleep(3)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        # Закрытие браузера
        driver.quit()
        print("Браузер закрыт.")

if __name__ == "__main__":
    main()