# coding: utf-8

from .environment import Environment


class Table(Environment):
    def __init__(self, body):
        super().__init__('table', body)


class Tabular(Environment):
    def __init__(self, body):
        super().__init__('tabular', body)
