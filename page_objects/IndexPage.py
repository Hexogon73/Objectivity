# -*- coding: utf-8 -*-
from BasePage import BasePage
from page_elements.MainMenu import MainMenu


class IndexPage(BasePage):
    """
    Модель главной страницы сайта
    """

    header_menu = MainMenu()

    @staticmethod
    def click_search_button():
        IndexPage.header_menu.search_button.link_click(20)

    @staticmethod
    def check_search_form():
        IndexPage.header_menu.search_form.check_open_search_form(20)
