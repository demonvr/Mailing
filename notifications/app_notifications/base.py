# coding=utf-8
from abc import abstractmethod


class SenderBase():
    """Абстрактный класс для создания отправителей сообщений"""

    @staticmethod
    @abstractmethod
    def send(messages):
        """Отправка сообщения"""
        pass
