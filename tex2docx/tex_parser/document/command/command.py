# coding: utf-8

import re

from ..element import TexElement
from ...const import ElementType

REG_PARAM = re.compile(r'\{(\w+)\}')
REG_OPTION = re.compile(r'\[(.+)\]')
REG_NAME = re.compile(r'\\(.+?)\*?(?:(?=\[|\{|\Z))')
REG_COMMAND = re.compile(r'(\\.+?)\*?(?:(?=\[|\{|\Z))')


class Command(TexElement):
    def __init__(self, command: str):
        super().__init__(ElementType.COMMAND)
        self.__raw_command = command
        # self.__command_name = None
        # self.__parameter = None
        # self.__option = None
        self.__set_name()
        self.__set_parameter()
        self.__set_option()
        self.__set_command()

    def __str__(self):
        return f'[C] {self.command_name}'

    @property
    def raw_command(self):
        return self.__raw_command

    @property
    def parameter(self):
        return self.__parameter

    @property
    def option(self):
        return self.__option

    @property
    def command_name(self):
        return self.__command_name

    @property
    def cmd(self):
        return self.__command

    def __set_parameter(self):
        param = REG_PARAM.findall(self.__raw_command)
        if len(param) == 0:
            self.__parameter = None
        elif len(param) == 1:
            self.__parameter = param[0]
        else:
            raise

    def __set_option(self):
        option = REG_OPTION.findall(self.__raw_command)
        if len(option) == 0:
            self.__option = None
        elif len(option) == 1:
            self.__option = option[0]
        else:
            raise

    def __set_name(self):
        name = REG_NAME.findall(self.__raw_command)
        if len(name) == 0:
            self.__command_name = None
        elif len(name) == 1:
            self.__command_name = name[0]
        else:
            raise

    def __set_command(self):
        command = REG_COMMAND.findall(self.__raw_command)
        if len(command) == 0:
            self.__command = None
        elif len(command) == 1:
            self.__command = command[0]
        else:
            raise
