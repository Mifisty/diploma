import allure
import pytest

from kazanexpress_project_api_mobile_ui.pages.mobile.mobile_basket_page import basket_page
from kazanexpress_project_api_mobile_ui.pages.mobile.skip_promo_widget_page import skip_widget


@allure.parent_suite('Mobile')
@pytest.mark.mobile
@allure.suite('Basket')
@allure.title(f'Add to basket mobile')
@allure.severity('Blocker')
def test_add_to_basket_mobile():
    skip_widget.skip_promo_widget()

    basket_page.add_item_to_basket()

    basket_page.should_item_in_basket()
