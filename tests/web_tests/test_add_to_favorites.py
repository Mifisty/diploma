import allure
import pytest

from kazanexpress_project_api_mobile_ui.pages.web.favorites_page import favorites_page


@allure.parent_suite('Web')
@pytest.mark.web
@allure.suite('Favorites')
@allure.title(f'Add to favorites')
@allure.severity('Major')
def test_add_favorites():
    favorites_page.open()

    favorites_page.add_item_to_favorites()

    favorites_page.should_item_in_favorites()
