# coding: utf-8

import docx


class Document(docx.document.Document):
    def __init__(self):
        self.__base = docx.Document()
        super().__init__(self.__base.element, self.__base.part)

    def add_title(self, title: str):
        self.add_heading(title, 0)

    def add_author(self, author: str):
        author = self.add_paragraph(author)
        author.alignment = docx.enum.text.WD_PARAGRAPH_ALIGNMENT.RIGHT

    def add_date(self, date: str):
        date = self.add_paragraph(date)
        date.alignment = docx.enum.text.WD_PARAGRAPH_ALIGNMENT.RIGHT
