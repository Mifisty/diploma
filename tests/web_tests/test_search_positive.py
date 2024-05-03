import allure

from diploma.pages.web.search_page import search_page


@allure.parent_suite('Web')
@allure.suite('Search')
@allure.title(f'Search positive test')
@allure.severity('Major')
def test_search_positive():
    search_page.open()

    search_page.fill_search_field()

    search_page.check_search_result()
