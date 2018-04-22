# -*- coding: utf-8 -*-
from page_objects.IndexPage import IndexPage


class IndexPageHelper:

    def __init__(self):
        pass

    @staticmethod
    def click_search_button():
        IndexPage.header_menu.search_button.link_click(20)
