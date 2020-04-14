# coding: utf-8

from docx.text.paragraph import Paragraph


class Reference(object):
    def __init__(self, tag: str, paragraph: Paragraph):
        self.__tag = tag
        self.__par = paragraph

    @property
    def tag(self):
        return self.__tag

    @property
    def paragraph(self):
        return self.__par
