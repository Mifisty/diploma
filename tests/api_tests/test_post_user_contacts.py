import json
import os

import allure
import pytest

from diploma.utils.request_helper import api_post
from dotenv import load_dotenv


@allure.parent_suite('API')
@pytest.mark.api
@allure.suite('Profile')
@allure.title(f'Change user contacts')
@allure.severity('Major')
def test_change_user_contacts():
    load_dotenv()
    phone_number = os.getenv('API_PHONE')
    url = '/user/contacts'
    payload = json.dumps({
        "email": "mail@mail.ru",
        "firstname": "Иван",
        "lastname": "Иванов",
        "patronymic": "Иванович",
        "phone": phone_number,
        "sex": "",
        "birthDate": None,
        "accountId": 0
    })
    with allure.step('Выполняем запрос на изменение персоальных данных'):
        response = api_post(url, data=payload)

    with allure.step('Проверяем статус код ответа'):
        assert response.status_code == 200
    with allure.step('Проверяем изменились данные пользователя'):
        assert response.json()['timestamp']
