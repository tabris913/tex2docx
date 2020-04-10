# coding: utf-8

import functools
import os

from .const import TRANSMAP
from .parser import Parser


class TexParser(object):
    def __init__(self, filename: str):
        self.__filename = filename
        self.__doc = Parser()

        self.__parse()

    @property
    def parser(self):
        return self.__doc

    def __check_file(self):
        return os.path.exists(self.__filename)

    def __parse(self):
        if self.__check_file():
            with open(self.__filename, encoding='utf8') as tex:
                replaced = functools.reduce(
                    lambda x, y: x.replace(*y), TRANSMAP.items(), tex.read())
                self.__doc.add_text(replaced)
        else:
            raise FileNotFoundError(f'"{self.__filename}" was not found')
