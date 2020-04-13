# coding: utf-8

from ..command import Command
from .....error import InvalidCommandName


class SectionBase(Command):
    def __init__(self, command: str, body: str):
        super().__init__(command)
        self.__body = body
        self.set_children()

    def __str__(self):
        to_print = [f'[C] {self.command_name}']
        for child in self.children:
            to_print.append(f'{str(child)}')
        return '\n'.join(to_print)

    @property
    def body(self) -> str:
        return self.__body

    @property
    def name(self) -> str:
        return self.parameter
