# coding: utf-8

from typing import Tuple

from ...command import Caption, Label
from ...converter import convert_environment, convert_structure
from ..environment import Environment
from .tabular import Tabular


class Table(Environment):
    command = 'table'

    def __init__(self, body: str):
        super().__init__(self.command, body)
        self.make_constructure()
        self.__has_tabular = None

    @property
    def has_tabular(self) -> bool:
        if self.__has_tabular is None:
            self.__has_tabular = any(isinstance(child, Tabular)
                                     for child in self.children)
        return self.__has_tabular

    @property
    def caption(self) -> Caption:
        for child in self.children:
            if isinstance(child, Caption):
                return child
        raise Exception('table has no caption')

    @property
    def label(self) -> Label:
        for child in self.children:
            if isinstance(child, Label):
                return child
        raise Exception('table has no label')

    @property
    def shape(self) -> Tuple[int]:
        if self.has_tabular:
            for child in self.children:
                if isinstance(child, Tabular):
                    return child.shape
        raise Exception('table has no tabular environment')

    def make_constructure(self):
        self.children.extend(convert_environment(self.body))
        convert_structure(self.children)

    @classmethod
    def generate_table(cls, text: str):
        return [cls(t) for t in cls.get_table(text)]

    @classmethod
    def get_table(cls, text: str):
        return cls.get_env(text, cls.command)
