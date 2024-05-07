import json
import allure
import pytest

from kazanexpress_project_api_mobile_ui.utils.request_helper import api_post


@allure.parent_suite('API')
@pytest.mark.api
@allure.suite('Favorites')
@allure.title(f'Delete from favorites')
@allure.severity('Major')
def test_add_favorites():
    url_add = "/favorites/add"
    url_remove = "/favorites/remove"
    payload = json.dumps({
        "productId": 2318024
    })
    code = 200

    with allure.step('Отправляем запрос на добавление товара в избранное'):
        result = api_post(url_add, data=payload)

    with allure.step('Проверяем Статус код'):
        assert result.status_code == code

    with allure.step('Отправляем запрос на удаление товара из избранного'):
        result = api_post(url_remove, data=payload)

    with allure.step('Проверяем Статус код'):
        assert result.status_code == code
    with allure.step('Проверяем что товар удалился из избранного'):
        assert result.json()['timestamp']
