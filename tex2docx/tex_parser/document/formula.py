# coding: utf-8

import re

from .element import TexElement
from ..const import ElementType

REG_FORMULA = re.compile(r'\$\$(.+?)\$\$', re.DOTALL)
REG_FORMULA_INLINE = re.compile(r'\$(.+?)\$', re.DOTALL)


class Formula(TexElement):
    def __init__(self, formula: str, inline: bool = True):
        super().__init__(ElementType.FORMULA)
        self.__text = formula
        self.__inline = inline
        self.__set_formula()

    def __str__(self):
        return f'[F] {self.__formula}'

    @property
    def text(self):
        return self.__text if self.__inline else self.__text[1:-1]

    @property
    def formula(self):
        return self.__formula

    def __set_formula(self):
        f = (
            REG_FORMULA_INLINE if self.__inline else REG_FORMULA).findall(
            self.__text)

        if len(f) == 1:
            self.__formula = f[0]
