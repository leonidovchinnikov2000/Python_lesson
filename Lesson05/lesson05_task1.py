from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Автоматическая установка и настройка ChromeDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # Опции для более стабильной работы (можно убрать при необходимости)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Инициализация драйвера
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Переход на целевую страницу
        driver.get("http://uitestingplayground.com/classattr")
        print("Страница загружена.")

        # Ожидание загрузки страницы (небольшая задержка для надёжности)
        time.sleep(2)

        # Поиск синей кнопки по классу (класс содержит "btn-primary" или похож)
        # На странице кнопка имеет класс "btn btn-primary"
        button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

        # Клик по кнопке
        button.click()
        print("Клик по синей кнопке выполнен.")

        # Небольшая задержка, чтобы увидеть результат клика (опционально)
        time.sleep(3)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        # Закрытие браузера
        driver.quit()
        print("Браузер закрыт.")

if __name__ == "__main__":
    main()