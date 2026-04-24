import requests

APIKEY = "Введите свои данные"
URL = "https://ru.yougile.com"


def test_create_positive():
    """Тест проверяет создание проекта"""
    myheaders = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {APIKEY}",
    }
    body = {"title": "ГосУслуги"}
    respons = requests.post(
        url=URL + "/api-v2/projects", headers=myheaders, json=body
    )

    assert respons.status_code == 201


def test_create_negative():
    """Тест проверяет не создание проекта"""
    myheaders = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {APIKEY}",
    }
    body = {"title": ""}
    respons = requests.post(
        url=URL + "/api-v2/projects", headers=myheaders, json=body
    )

    assert respons.status_code == 400


def test_updatecreate_positive():
    """Изменяем название проекта"""
    # Создаем проект
    myheaders = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {APIKEY}",
    }
    body = {"title": "ГосУслуги"}
    respons = requests.post(
        url=URL + "/api-v2/projects", headers=myheaders, json=body
    )

    assert respons.status_code == 201
    respons_body = respons.json()
    id = respons_body["id"]
    # Меняем название проекта
    body = {"title": "МАКС"}
    respons = requests.put(
        url=f"{URL}/api-v2/projects/{id}", headers=myheaders, json=body
    )
    assert respons.status_code == 200
    # Получаем проект по ID
    respons = requests.get(
        url=f"{URL}/api-v2/projects/{id}", headers=myheaders
    )
    respons_body = respons.json()
    title = respons_body["title"]
    assert title == "МАКС"


def test_hegative_updatecreate_positive():
    """Отсутсвует название проекта"""
    # Создаем проект
    myheaders = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {APIKEY}",
    }
    body = {"title": "ГосУслуги"}
    respons = requests.post(
        url=URL + "/api-v2/projects", headers=myheaders, json=body
    )

    assert respons.status_code == 201
    respons_body = respons.json()
    id = respons_body["id"]
    # Меняем название проекта
    body = {"title": ""}
    respons = requests.put(
        url=f"{URL}/api-v2/projects/{id}", headers=myheaders, json=body
    )
    assert respons.status_code == 400
    # Получаем проект по ID
    respons = requests.get(
        url=f"{URL}/api-v2/projects/{id}", headers=myheaders
    )
    respons_body = respons.json()
    title = respons_body["title"]
    assert title == "ГосУслуги"


def test_getid_positive():
    """Поулчение ID проекта"""
    # Создаем проект
    myheaders = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {APIKEY}",
    }
    body = {"title": "ГосУслуги"}
    respons = requests.post(
        url=URL + "/api-v2/projects", headers=myheaders, json=body
    )

    assert respons.status_code == 201
    respons_body = respons.json()
    id = respons_body["id"]
    # Получаем проект по ID
    respons = requests.get(
        url=f"{URL}/api-v2/projects/{id}", headers=myheaders
    )
    respons_body = respons.json()
    title = respons_body["title"]
    assert title == "ГосУслуги"


def test_negative_getid_positive():
    """Не получение ID проекта"""
    # Создаем проект
    myheaders = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {APIKEY}",
    }
    body = {"title": "ГосУслуги"}
    respons = requests.post(
        url=URL + "/api-v2/projects", headers=myheaders, json=body
    )

    assert respons.status_code == 201
    respons_body = respons.json()
    id = respons_body[""]
    # Получаем проект по ID
    respons = requests.get(
        url=f"{URL}/api-v2/projects/{id}", headers=myheaders
    )
    respons_body = respons.json()
    title = respons_body["title"]
    assert title == "ГосУслуги"
