# -*- coding: utf-8 -*-
from BaseElement import BaseElement


class Button(BaseElement):

    _locator = ''
    _timeout = 0

    def __init__(self, locator, timeout=None):
        BaseElement.__init__(locator, timeout)
        self._locator = locator
        self._timeout = timeout

    def wait_button_is_enable(self, timeout=_timeout):
        BaseElement.wait_element_is_enable(self._locator, timeout)

    def button_click(self, timeout=_timeout):
        self.wait_element_is_enable()
        self._seleniumlib().click_button(self._locator, timeout)
