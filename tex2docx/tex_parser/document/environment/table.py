# coding: utf-8

from ..converter import convert_environment, convert_structure
from .environment import Environment


class Table(Environment):
    command = 'table'

    def __init__(self, body: str):
        super().__init__(self.command, body)
        self.make_constructure()

    @classmethod
    def generate_table(cls, text: str):
        return [cls(t) for t in cls.get_table(text)]

    @classmethod
    def get_table(cls, text: str):
        return cls.get_env(text, cls.command)

    def make_constructure(self):
        self.children.extend(convert_environment(self.body))
        convert_structure(self.children)


class Tabular(Environment):
    command = 'tabular'

    def __init__(self, body: str):
        super().__init__(self.command, body)
        self.children.append(body)

    @classmethod
    def generate_tabular(cls, text: str):
        return [cls(t) for t in cls.get_tabular(text)]

    @classmethod
    def get_tabular(cls, text: str):
        return cls.get_env(text, cls.command)
