# -*- coding: utf-8 -*-
from BaseElement import BaseElement


class Button(BaseElement):

    def __init__(self, locator, timeout=None):
        BaseElement.__init__(locator, timeout)
        self._locator = locator
        self._timeout = timeout

    def wait_button_is_enable(self):
        BaseElement.wait_element_is_enable(self._locator, timeout)

    def button_click(self):
        self.wait_element_is_enable()
        self._seleniumlib().click_button(self._locator)
