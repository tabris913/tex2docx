# coding: utf-8

from .element import TexElement
from ..const import ElementType


class Text(TexElement):
    def __init__(self, text: str):
        super().__init__(ElementType.TEXT)
        self.__text = text

    def __str__(self):
        return f'[T] {self.__text}'

    @property
    def text(self):
        return self.__text
