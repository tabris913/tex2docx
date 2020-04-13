# coding: utf-8

from __future__ import annotations

from typing import List, Optional

from .utils import Children
from ..const import ElementType


class TexElement(object):
    def __init__(self, element_type: ElementType):
        self.children: Optional[List[TexElement]] = None
        self.__element_type = element_type

    @property
    def ELEMENT_TYPE(self):
        return self.__element_type

    def set_children(self):
        self.children = Children()
