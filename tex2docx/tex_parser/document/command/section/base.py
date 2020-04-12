# coding: utf-8

import re

from ..command import Command
from .....error import InvalidCommandName

REG_GET_TAG = re.compile(r'\\\w+?\*?\{(.+?)\}', re.DOTALL)


class SectionBase(Command):
    def __init__(self, command: str, body: str):
        super().__init__(command)
        self.__set_name()
        self.__body = body
        self.constructure = None

    @property
    def name(self) -> str:
        return self.__name

    @property
    def body(self) -> str:
        return self.__body

    def __set_name(self):
        tags = REG_GET_TAG.findall(self.raw_command)
        if len(tags) == 1:
            self.__name = tags[0]
        else:
            raise InvalidCommandName()

    def make_constructure(self):
        self.constructure = []
