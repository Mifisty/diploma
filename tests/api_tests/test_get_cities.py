import allure
import pytest
from jsonschema import validate
from kazanexpress_project_api_mobile_ui.utils.request_helper import api_get
from schemas.schema_get_cities import get_cities


@allure.parent_suite('API')
@pytest.mark.api
@allure.suite('Cities')
@allure.title(f'Сhecking the number of cities')
@allure.severity('Major')
def test_get_cities():
    url = "main/cities"
    name = 'Агрыз'
    number_of_cities = 122
    code = 200

    with allure.step('Получаем список городов'):
        result = api_get(url)

    with allure.step('Проверяем статус код'):
        assert result.status_code == code
    with allure.step('Проверяем количество городов в списке'):
        assert len(result.json()['payload']) >= number_of_cities
    with allure.step('Проверяем что первый город имеет название Агрыз'):
        assert result.json()['payload'][0]['name'] == name
    with allure.step('Проверяем схему JSON'):
        validate(result.json(), schema=get_cities)
