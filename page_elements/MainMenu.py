# -*- coding: utf-8 -*-
from Button import Button


class MainMenu(object):
    locator = "xpath=//ul[@class='nav-menu']"

    home_button = Button(locator + "//a[text()='Главная']")
    blog_button = Button(locator + "//a[text()='Блог']")
    java_button = Button(locator + "//a[text()='Java\C# & WebDriver']")
    literature = Button(locator + "//a[text()='Литература']")
    site_map_button = Button(locator + "//a[text()='Карта сайта']")  # //ul[@class='nav-menu']//a[text()='Карта сайта']
