# -*- coding: utf-8 -*-
from BaseElement import BaseElement


class Button(BaseElement):
    """
    Инкапсулирует в себе методы работы с кнопкой
    При создании экземпляра присваивает значения локатора и таймаута переданные в конструктор
    """

    _locator = ''
    _timeout = 0

    def __init__(self, locator, timeout=None):
        BaseElement.__init__(self, locator, timeout)
        self._locator = locator
        self._timeout = timeout

    def get_locator(self):
        return self._locator

    def wait_button_is_enable(self, timeout=_timeout):
        BaseElement.wait_element_is_enable(self._locator, timeout)

    def button_click(self, timeout=_timeout):
        self.wait_element_is_enable(timeout)
        self._seleniumlib().click_button(self._locator)
