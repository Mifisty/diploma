import allure
import pytest

from kazanexpress_project_api_mobile_ui.pages.web.login_page import login_page


@allure.parent_suite('Web')
@pytest.mark.web
@allure.suite('Login button')
@allure.title(f'Login negative test')
@allure.severity('Critical')
def test_login_negative():
    login_page.open()

    login_page.click_login_button()
    login_page.fill_phone_number()

    login_page.should_error_message()
