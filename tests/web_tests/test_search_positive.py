import allure
import pytest

from kazanexpress_project_api_mobile_ui.pages.web.search_page import search_page


@allure.parent_suite('Web')
@pytest.mark.web
@allure.suite('Search')
@allure.title(f'Search positive test')
@allure.severity('Major')
def test_search_positive():
    search_page.open()

    search_page.fill_search_field()

    search_page.check_search_result()
