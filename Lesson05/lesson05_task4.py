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
        driver.get("http://the-internet.herokuapp.com/login")
        print("Страница загружена.")

        # Ожидание загрузки страницы
        time.sleep(2)

        # Ввод логина в поле username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")
        print("Введён логин: tomsmith")

        # Ввод пароля в поле password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        print("Введён пароль: SuperSecretPassword!")

        # Нажатие на кнопку Login
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        print("Нажата кнопка Login")

        # Ожидание появления сообщения (зелёной плашки)
        time.sleep(3)

        # Поиск текста с зелёной плашки (успешное сообщение)
        success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
        message_text = success_message.text.strip()

        # Вывод текста сообщения в консоль
        print("Текст с зелёной плашки:")
        print(message_text)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        # Закрытие браузера
        driver.quit()
        print("Браузер закрыт.")

if __name__ == "__main__":
    main()