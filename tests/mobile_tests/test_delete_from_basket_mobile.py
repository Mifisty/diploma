import allure

from diploma.pages.mobile.mobile_basket_page import basket_page
from diploma.pages.mobile.skip_promo_widget_page import skip_widget


@allure.parent_suite('Mobile')
@allure.suite('Basket')
@allure.title(f'Delete from basket mobile')
@allure.severity('Critical')
def test_delete_from_basket_mobile():
    skip_widget.skip_promo_widget()

    basket_page.add_item_to_basket()
    basket_page.delete_item_from_basket()

    basket_page.should_basket_empty()
