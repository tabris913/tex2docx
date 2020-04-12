# coding: utf-8

from ..const import ElementType


class TexElement(object):
    def __init__(self, element_type: ElementType):
        self.children = None
        self.__element_type = element_type

    @property
    def ELEMENT_TYPE(self):
        return self.__element_type

    def make_constructure(self):
        self.children = []
