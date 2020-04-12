# coding: utf-8

from ....error import MultipleDocumentException, NoDocumentException
from ..command import MakeTitle, Section, SubSection, SubSubSection, Paragraph, SubParagraph
from .environment import Environment
from ..converter import convert_structure, convert_environment


class Document(Environment):
    def __init__(self, body: str):
        super().__init__('document', body)

    def has_maketitle(self) -> bool:
        return MakeTitle.command in self.body

    def remove_maketitle(self):
        self.replace_body(MakeTitle.command, '\n')

    def make_constructure(self):
        self.children = Section.sectionize(self.body_without_comment)
        self.children = SubSection.subsectionize(
            self.children[0]) + self.children[1:]
        self.children = SubSubSection.subsubsectionize(
            self.children[0]) + self.children[1:]
        self.children = Paragraph.paragraphize(
            self.children[0]) + self.children[1:]
        self.children = SubParagraph.subparagraphize(
            self.children[0]) + self.children[1:]
        # env系抜き出す
        # not command, not env: search subsec, subsubsec, ...
        self.children = convert_environment(
            self.children[0]) + self.children[1:]
        self.children = convert_structure(self.children)

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
