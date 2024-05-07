import allure
import pytest

from kazanexpress_project_api_mobile_ui.pages.web.basket_page import basket_page


@allure.parent_suite('Web')
@pytest.mark.web
@allure.suite('Basket')
@allure.title(f'Delete from basket')
@allure.severity('Critical')
def test_delete_from_basket():
    basket_page.open()

    basket_page.add_item_to_basket()
    basket_page.delete_item_from_basket()

    basket_page.should_basket_empty()
