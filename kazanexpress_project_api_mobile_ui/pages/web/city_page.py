import allure
from selene import browser, have


class CityPage:

    @allure.step('Открываем браузер на странице https://kazanexpress.ru/')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Меняем город нахождения на Воронеж')
    def set_city(self):
        browser.element('[data-test-id=button__select-city]').click()
        browser.all('[data-test-id=list__city]').element_by(have.text('Воронеж')).click()

    @allure.step('Проверяем, что город поменялся на Воронеж')
    def should_city_changes(self):
        browser.element('[data-test-id=button__select-city]').should(have.text('Воронеж'))


city_page = CityPage()
