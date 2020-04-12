# coding: utf-8

from .environment import Environment


class Table(Environment):
    command = 'table'

    def __init__(self, body):
        super().__init__(self.command, body)

    @classmethod
    def generate_table(cls, text: str):
        return [cls(t) for t in cls.get_table(text)]

    @classmethod
    def get_table(cls, text: str):
        return cls.get_env(text, cls.command)


class Tabular(Environment):
    command = 'tabular'

    def __init__(self, body):
        super().__init__(self.command, body)

    @classmethod
    def generate_tabular(cls, text: str):
        return [cls(t) for t in cls.get_tabular(text)]

    @classmethod
    def get_tabular(cls, text: str):
        return cls.get_env(text, cls.command)
