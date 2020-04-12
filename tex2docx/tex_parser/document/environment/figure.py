# coding: utf-8

from ..command import Command
from .environment import Environment


class Figure(Environment):
    command = 'figure'

    def __init__(self, body):
        super().__init__(self.command, body)

    @classmethod
    def generate_figure(cls, text: str):
        return [cls(f) for f in cls.get_figure(text)]

    @classmethod
    def get_figure(cls, text: str):
        return cls.get_env(text, cls.command)


class IncludeGraphics(Command):
    def __init__(self):
        super().__init__('\\includegraphics')
