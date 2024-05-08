import time

import allure
from selene import have, browser, be


class BasketPage:

    @allure.step('Открываем браузер на странице https://kazanexpress.ru/')
    def open(self):
        browser.open('/')

    @allure.step('Находим и добавляем товар в корзину')
    def add_item_to_basket(self):
        browser.element('[data-test-id=input__search]').type('Кастрюля из нержавеющей стали').press_enter()
        browser.all('[data-test-id=item__product-card]').element_by(
            have.text('Кастрюля из нержавеющей стали со стеклянной крышкой')).click()
        try:
            browser.all('.radio-text-wrapper').element_by(have.text('2 литра')).click()
            browser.element('[data-test-id=button__add-to-cart]').click()
            browser.element('[data-test-id=button__to-cart]').click()
        except:
            browser.all('[data-test-id=item__sku]').element_by(have.text('2 литра')).click()
            browser.element('[data-test-id=button__add-cart]').click()
            browser.element('[data-test-id=button__cart]').click()

    @allure.step('Проверяем то что в корзине находится 1 товар добавленный нами')
    def should_item_in_basket(self):
        browser.element('[data-test-id=text__item-quantity]').should(have.text('1 товар'))

    @allure.step('Удаляем товар из корзины')
    def delete_item_from_basket(self):
        browser.element('[data-test-id="list__products"] .list-complete-item').should(be.visible)
        browser.element('[data-test-id=button__delete-from-cart]').click()

    @allure.step('Проверяем то что в корзине нет товаров')
    def should_basket_empty(self):
        browser.element('[data-test-id=text__empty-favorite-title]').should(have.text('В корзине пока нет товаров'))


basket_page = BasketPage()
