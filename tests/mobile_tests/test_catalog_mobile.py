import allure
import pytest

from kazanexpress_project_api_mobile_ui.pages.mobile.mobile_catalog_page import catalog_page
from kazanexpress_project_api_mobile_ui.pages.mobile.skip_promo_widget_page import skip_widget


@allure.parent_suite('Mobile')
@pytest.mark.mobile
@allure.suite('Catalog')
@allure.title(f'Search item by category catalog mobile')
@allure.severity('Major')
def test_catalog_mobile():
    skip_widget.skip_promo_widget()

    catalog_page.product_search_by_сategory()

    catalog_page.check_search_results()
