# coding: utf-8

import os

from .document import Document
from ..tex_parser import TexParser
from ..tex_parser.document import Document as ParserDoc, Meta


class Tex2Docx:
    def __init__(self, source: str, target: str):
        self.__source = source
        self.__target = target

        self.__doc = Document()

    def debug(self):
        print(f'source: {self.__source}')
        print(f'target: {self.__target}')

        # self.__doc.add_title('hello, world')
        # self.__doc.save(self.__target)

    def convert(self):
        self.__parse()
        self.__write()

    def __parse(self):
        self.__parser = TexParser(self.__source).parser
        self.__parse_doc(self.__parser.document)

    def __parse_meta(self, meta: Meta):
        self.__doc.add_title(meta.title)
        self.__doc.add_author(meta.author)
        self.__doc.add_date(meta.date)

    def __parse_doc(self, doc: ParserDoc):
        if doc.has_maketitle():
            self.__parse_meta(self.__parser.meta)
            doc.remove_maketitle()
        # print(doc.body_without_comment)
        doc.make_constructure()
        print(doc.children)

    def __write(self):
        self.__doc.save(self.__target)
