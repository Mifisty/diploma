import allure
import pytest

from diploma.pages.web.basket_page import basket_page


@allure.parent_suite('Web')
@pytest.mark.web
@allure.suite('Basket')
@allure.title(f'Add to basket')
@allure.severity('Blocker')
def test_add_to_basket():
    basket_page.open()

    basket_page.add_item_to_basket()

    basket_page.should_item_in_basket()
