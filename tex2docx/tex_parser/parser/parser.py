# coding: utf-8

from ..document import Document, Meta
from ...error import MultipleDocumentException, NoDocumentException


class Parser(object):
    def __init__(self, text: str = ''):
        self.__text = text
        self.__meta = None
        self.__document = None

    @property
    def document(self) -> Document:
        try:
            if self.__document is None:
                self.__document = Document.generate_document(self.__text)
        except BaseException:
            print('tex has not document environment')

        return self.__document

    @property
    def meta(self) -> Meta:
        try:
            if self.__meta is None:
                self.__meta = Meta.generate_meta(self.__text)
        except BaseException:
            print('tex has not meta information')

        return self.__meta

    def add_text(self, text: str):
        self.__text = text
