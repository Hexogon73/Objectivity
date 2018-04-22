# -*- coding: utf-8 -*-
from robot.libraries.BuiltIn import BuiltIn


def _seleniumlib():
    return BuiltIn().get_library_instance("Selenium2Library")


class BrowserManager:
    """
    Вспомогательный класс для работы с браузером
    """

    def __init__(self):
        pass

    @staticmethod
    def open_test_browser():
        _seleniumlib().open_browser(url='http://autoqa.org/', browser='chrome')

    @staticmethod
    def close_test_browser():
        _seleniumlib().close_browser()
