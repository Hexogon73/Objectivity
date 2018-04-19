# -*- coding: utf-8 -*-
from Button import Button


class MainMenu(object):
    logo_link = "xpath//a[@rel='home']"

    locator_menu = "xpath=//ul[@class='nav-menu']"
    home_button = Button(locator_menu + "//a[text()='Главная']")
    blog_button = Button(locator_menu + "//a[text()='Блог']")
    java_button = Button(locator_menu + "//a[text()='Java\C# & WebDriver']")
    literature = Button(locator_menu + "//a[text()='Литература']")
    site_map_button = Button(locator_menu + "//a[text()='Карта сайта']")
    # //ul[@class='nav-menu']//a[text()='Карта сайта']
    search_button = "xpath=//div[@class='search-toggle']"

    # ---  search form  ---
    search_form = "xpath=//div[@id='search-box']"
    search_input = search_form + "//input[@type='search']"
    submit_button = search_form + "//input[@type='submit']"
