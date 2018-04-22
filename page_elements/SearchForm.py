# -*- coding: utf-8 -*-
from BaseElement import BaseElement
from Input import Input
from Link import Link


class SearchForm(BaseElement):

    _locator = "xpath=//div[@id='search-box']"
    _timeout = 0
    search_input = Input(_locator + "//input[@type='search']")
    submit_button = Link(_locator + "//input[@type='submit']")

    def __init__(self, locator=None, timeout=None):
        BaseElement.__init__(self, locator, timeout)
        self._locator = locator
        self._timeout = timeout

    def check_open_search_form(self, timeout=_timeout):
        self.search_input.wait_element_is_visible(timeout)
        self.submit_button.wait_element_is_enable(timeout)
