# -*- coding: utf-8 -*-
from robot.libraries.BuiltIn import BuiltIn


class BaseElement(object):

    _locator = ''
    _timeout = 0

    def __init__(self, locator, timeout=None):
        self._locator = locator
        self._timeout = timeout

    def _seleniumlib():
        return BuiltIn().get_library_instance("Selenium2Library")

    def wait_element_is_enable(self, timeout=_timeout):
        self._seleniumlib().wait_until_element_is_enable(self._locator, timeout)

    def wait_element_is_visible(self, timeout=_timeout):
        self._seleniumlib().wait_until_element_is_visible(self._locator, timeout)
