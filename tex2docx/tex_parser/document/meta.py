# coding: utf-8

import datetime
import re

REG_GET = re.compile(r'\\begin\{document\}.+$', re.DOTALL)
REG_TITLE = re.compile(r'\\title\{(.+?)\}')
REG_AUTHOR = re.compile(r'\\author\{(.+?)\}')
REG_DATE = re.compile(r'\\date\{(.+?)\}')


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
        title = REG_TITLE.findall(self._raw)
        self.__title = title[-1] if len(title) > 0 else '(Title)'

    def set_author(self):
        author = REG_AUTHOR.findall(self._raw)
        self.__author = author[-1] if len(author) > 0 else '(Author)'

    def set_date(self):
        date = REG_DATE.findall(self._raw)
        self.__date = date[-1] if len(
            date) > 0 else f'{str(datetime.date.today())} (auto)'

        if self.__date == '\\YYYYMMDD':
            self.__date = str(datetime.date.today())

    @classmethod
    def generate_meta(cls, tex: str):
        return cls(cls.get_meta(tex))

    @classmethod
    def get_meta(cls, tex: str) -> str:
        return REG_GET.sub('', tex)
