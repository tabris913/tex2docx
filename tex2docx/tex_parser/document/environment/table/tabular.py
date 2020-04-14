# coding: utf-8

import re
from typing import Tuple

from ...command import HLine, TopRule, MidRule
from ...converter import convert_environment, convert_structure
from ...text import Text
from ..environment import Environment

REG_SPLIT = re.compile(r'^\{(\w+?)\}(.+)$', re.DOTALL)


class Tabular(Environment):
    command = 'tabular'

    def __init__(self, body: str):
        super().__init__(self.command, body)
        self.__shape = None
        self.__table = None
        self.__convert(body)
        self.children.extend(convert_environment(self.__body))
        convert_structure(self.children)
        self.__make_table()

    @property
    def shape(self) -> Tuple[int]:
        if self.__shape is None:
            self.__shape = (self.__rowsize, self.__colsize)
        return self.__shape

    @property
    def rows(self) -> int:
        return self.shape[0]

    @property
    def cols(self) -> int:
        return self.shape[1]

    @property
    def table(self):
        return self.__table

    def __convert(self, body: str):
        split = REG_SPLIT.findall(body)
        if len(split) == 1 and len(split[0]) == 2:
            self.__align = split[0][0]
            self.__body = split[0][1]
            self.__colsize = len(self.__align)

    def __make_table(self):
        rows = filter(lambda child: isinstance(child, Text), self.children)
        self.__table = [[cell.strip() for cell in row.text.split('&')]
                        for row in rows]
        self.__rowsize = len(self.__table)

    @classmethod
    def generate_tabular(cls, text: str):
        return [cls(t) for t in cls.get_tabular(text)]

    @classmethod
    def get_tabular(cls, text: str):
        return cls.get_env(text, cls.command)
