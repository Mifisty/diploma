import allure
from jsonschema import validate
from diploma.utils.request_helper import api_get
from schemas.schema_get_cities import get_cities


@allure.parent_suite('API')
@allure.suite('Cities')
@allure.title(f'Сhecking the number of cities')
@allure.severity('Major')
def test_get_cities():
    url = "main/cities"
    name = 'Агрыз'
    number_of_cities = 122
    code = 200

    with allure.step('Получаем список городов'):
        response = api_get(url)

    with allure.step('Проверяем статус код'):
        assert response.status_code == code

    with allure.step('Проверяем количество городов в списке'):
        assert len(response.json()['payload']) >= number_of_cities

    with allure.step('Проверяем что первый город имеет название Агрыз'):
        assert response.json()['payload'][0]['name'] == name

    with allure.step('Проверяем схему JSON'):
        validate(response.json(), schema=get_cities)
