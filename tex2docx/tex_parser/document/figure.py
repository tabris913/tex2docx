# coding: utf-8

from .command import Command
from .environment import Environment


class Figure(Environment):
    def __init__(self, body):
        super().__init__('figure', body)


class IncludeGraphics(Command):
    def __init__(self):
        super().__init__('\\includegraphics')
