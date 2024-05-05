import allure
from jsonschema import validate
from diploma.utils.request_helper import api_get
from schemas.schema_get_product import get_product


@allure.parent_suite('API')
@allure.suite('Product')
@allure.title(f'Сhecking product')
@allure.severity('Major')
def test_get_cities():
    url = "/v2/product/1102727"
    id = 1102727
    title = 'Щетка-массажер силиконовый для кожи головы, для мытья волос , антистресс "Кактус"'
    code = 200

    with allure.step('Получаем информацию о товаре'):
        result = api_get(url)

    with allure.step('Проверяем Статус код'):
        assert result.status_code == code
    with allure.step('Проверяем что id товара правильное'):
        assert result.json()['payload']['data']['id'] == id
    with allure.step('Проверяем что название товара правильное'):
        assert result.json()['payload']['data']['title'] == title
    with allure.step('Проверяем схему JSON'):
        validate(result.json(), schema=get_product)
