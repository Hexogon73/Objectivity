# -*- coding: utf-8 -*-
from page_elements.Link import Link
from BasePage import BasePage


class SubscriptionPopup(BasePage):
    """
    Модель всплывающего окна с предложением подписаться
    """

    close_button = Link("xpath=//div[contains(@class,'popup')]//a[contains(@class,'close')]")

    @staticmethod
    def close_subscription_popup():
        SubscriptionPopup.close_button.link_click(20)
