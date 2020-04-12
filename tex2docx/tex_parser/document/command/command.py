# coding: utf-8

from ..element import TexElement
from ...const import ElementType


class Command(TexElement):
    def __init__(self, command: str):
        super().__init__(ElementType.COMMAND)
        self.__raw_command = command

    @property
    def raw_command(self):
        return self.__raw_command

    def __parameter(self):
        ...

    def __option(self):
        ...

    def __command_name(self):
        ...
