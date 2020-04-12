# coding: utf-8

from __future__ import annotations

import re

from ....error import InvalidEnvironment
from ..element import TexElement
from ...parser.utils import is_comment, remove_comment, trim_empty
from ...const import ElementType


class Environment(TexElement):
    def __init__(self, envname: str, body: str):
        super().__init__(ElementType.ENVIRONMENT)
        self.__envname = envname
        self.__body = body
        self.__body_without_comment = None

    @property
    def name(self):
        return self.__envname

    @property
    def body(self):
        return self.__body

    @property
    def body_without_comment(self):
        if self.__body_without_comment is None:
            self.__body_without_comment = self.remove_comment(self.__body)

        return re.sub('\n{2,}', '\n\n', self.__body_without_comment)

    def replace_body(self, old: str, new: str):
        try:
            self.__body = re.sub(old, new, self.__body)
        except re.error:
            replaced = old.replace('\\', '\\\\')
            print(f'replace {old} --> {replaced}')
            self.__body = re.sub(replaced, new, self.__body)
        self.__body_without_comment = self.remove_comment(self.__body)

    def remove_comment(self, lines: str) -> str:
        lines = self.__body.split('\n')
        lines = map(trim_empty, lines)
        lines = filter(lambda line: not is_comment(line), lines)
        lines = map(remove_comment, lines)
        return '\n'.join(lines)

    @classmethod
    def generate_env(cls, body: str, envname: str) -> Environment:
        return cls(envname, cls.get_env(body, envname))

    @classmethod
    def get_env(cls, body: str, envname: str) -> str:
        env = re.findall(
            f'\\\\begin\\{{{envname}\\}}(.+?)\\\\end\\{{{envname}\\}}',
            body,
            re.DOTALL)

        if len(env) == 0:
            raise

        return env
