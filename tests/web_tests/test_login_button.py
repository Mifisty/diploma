import allure

from diploma.pages.web.login_page import login_page


@allure.parent_suite('Web')
@allure.suite('Login button')
@allure.title(f'Login button test')
@allure.severity('Critical')
def test_login_button():
    login_page.open()

    login_page.click_login_button()

    login_page.should_pop_up_visible()
