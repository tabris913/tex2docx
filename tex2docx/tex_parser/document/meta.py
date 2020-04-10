# coding: utf-8

import datetime
import re


class Meta(object):
    def __init__(self, body: str = ''):
        self._raw = body
        self.set_title()
        self.set_author()
        self.set_date()

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def date(self):
        return self.__date

    def set_title(self):
        title = re.findall(r'\\title\{(.+?)\}', self._raw)
        self.__title = title[-1] if len(title) > 0 else '(Title)'

    def set_author(self):
        author = re.findall(r'\\author\{(.+?)\}', self._raw)
        self.__author = author[-1] if len(author) > 0 else '(Author)'

    def set_date(self):
        date = re.findall(r'\\date\{(.+?)\}', self._raw)
        self.__date = date[-1] if len(
            date) > 0 else f'{str(datetime.date.today())} (auto)'

        if self.__date == '\\YYYYMMDD':
            self.__date = str(datetime.date.today())

    @classmethod
    def generate_meta(cls, body):
        return cls(cls.get_meta(body))

    @classmethod
    def get_meta(cls, body: str) -> str:
        return re.sub(r'\\begin\{document\}.+$', '', body, flags=re.DOTALL)
