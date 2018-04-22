# -*- coding: utf-8 -*-
from page_elements.MainMenu import MainMenu
from BasePage import BasePage


class IndexPage(BasePage):
    """
    Модель главной страницы сайта
    """

    header_menu = MainMenu()

    @staticmethod
    def click_search_button():
        IndexPage.header_menu.search_button.link_click(20)
