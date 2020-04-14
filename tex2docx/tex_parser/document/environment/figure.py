# coding: utf-8

from ..converter import convert_environment, convert_structure
from ..command import Command, IncludeGraphics, Caption, Label
from .environment import Environment


class Figure(Environment):
    command = 'figure'

    def __init__(self, body):
        super().__init__(self.command, body)
        self.make_constructure()
        self.__has_graphics = None

    @property
    def has_graphics(self) -> bool:
        if self.__has_graphics is None:
            self.__has_graphics = any(
                isinstance(child, IncludeGraphics) for child in self.children)
        return self.__has_graphics

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

    def make_constructure(self):
        self.children.extend(convert_environment(self.body))
        convert_structure(self.children)

    @classmethod
    def generate_figure(cls, text: str):
        return [cls(f) for f in cls.get_figure(text)]

    @classmethod
    def get_figure(cls, text: str):
        return cls.get_env(text, cls.command)
