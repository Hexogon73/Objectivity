# -*- coding: utf-8 -*-
from BaseElement import BaseElement


class Input(BaseElement):
    """
    Инкапсулирует в себе методы работы с ссылкой
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

    def wait_input_is_visible(self, timeout=_timeout):
        # BaseElement.wait_element_is_visible(self._locator, timeout)
        self.wait_element_is_visible(timeout)

    def text_input(self, text, timeout=_timeout):
        self.wait_element_is_enable(timeout)
        self._seleniumlib().input_text(self._locator, text)
