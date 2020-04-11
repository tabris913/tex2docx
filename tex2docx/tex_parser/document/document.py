# coding: utf-8

import re

from ...error import MultipleDocumentException, NoDocumentException
from .command import MakeTitle
from .environment import Environment
from .section import Section
from ..parser.utils import divide_command, trim

REG_META = re.compile(r'^(.+?)(?:(?=\\section))', re.DOTALL)


class Document(Environment):
    def __init__(self, body: str):
        super().__init__('document', body)
        self.constructure = None

    def has_maketitle(self) -> bool:
        return MakeTitle.command in self.body

    def remove_maketitle(self):
        self.replace_body(MakeTitle.command, '\n')

    def make_constructure(self):
        self.constructure = []
        meta = REG_META.findall(self.body_without_comment)
        if len(meta) == 1:
            self.constructure.extend(divide_command(trim(meta[0])))
        self.constructure.extend(
            Section.generate_section(self.body_without_comment))

    @classmethod
    def generate_document(cls, body: str):
        return cls(cls.get_document(body))

    @classmethod
    def get_document(cls, body: str):
        document = Environment.get_env(body, 'document')

        if len(document) == 0:
            raise NoDocumentException()
        if len(document) > 1:
            raise MultipleDocumentException()

        return document[0]
