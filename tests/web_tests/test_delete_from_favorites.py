import allure

from diploma.pages.favorites_page import favorites_page


@allure.parent_suite('Web')
@allure.suite('Favorites')
@allure.title(f'Delete from favorites')
@allure.severity('Major')
def test_delete_from_favorites():
    favorites_page.open()

    favorites_page.add_item_to_favorites()
    favorites_page.delete_item_from_favorites()

    favorites_page.should_favorites_empty()
