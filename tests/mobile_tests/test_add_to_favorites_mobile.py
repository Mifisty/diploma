import allure
import pytest

from diploma.pages.mobile.mobile_favorites_page import favorites_page
from diploma.pages.mobile.skip_promo_widget_page import skip_widget


@allure.parent_suite('Mobile')
@pytest.mark.mobile
@allure.suite('Favorites')
@allure.title(f'Add to favorites mobile')
@allure.severity('Critical')
def test_add_to_favorites_mobile():
    skip_widget.skip_promo_widget()

    favorites_page.add_item_to_favorites()

    favorites_page.should_item_in_favorites()
