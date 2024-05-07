import allure
import pytest

from kazanexpress_project_api_mobile_ui.pages.web.city_page import city_page


@allure.parent_suite('Web')
@pytest.mark.web
@allure.suite('Set city')
@allure.title(f'Set city test')
@allure.severity('Major')
def test_set_city():
    city_page.open()

    city_page.set_city()

    city_page.should_city_changes()
