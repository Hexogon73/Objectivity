# -*- coding: utf-8 -*-
from robot.libraries.BuiltIn import BuiltIn


class BaseElement(object):
    """
    Инкапсулирует в себе общие методы работы с элементами страницы
    """

    _locator = ''
    _timeout = 0

    def __init__(self, locator, timeout=None):
        self._locator = locator
        self._timeout = timeout

    @staticmethod
    def _seleniumlib():
        return BuiltIn().get_library_instance("Selenium2Library")

    def wait_element_is_enable(self, timeout=_timeout):
        BaseElement._seleniumlib().wait_until_element_is_enabled(self._locator, timeout)

    def wait_element_is_visible(self, timeout=_timeout):
        BaseElement._seleniumlib().wait_until_element_is_visible(self._locator, timeout)
