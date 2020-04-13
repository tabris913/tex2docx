# coding: utf-8

from ....error import MultipleDocumentException, NoDocumentException
from ..command import MakeTitle
from ..command.section import Section, SubSection, SubSubSection, Paragraph, SubParagraph
from .environment import Environment
from ..converter import convert_structure, convert_environment


class Document(Environment):
    def __init__(self, body: str):
        super().__init__('document', body)
        # self.make_constructure()

    def has_maketitle(self) -> bool:
        return MakeTitle.command in self.body

    def remove_maketitle(self):
        self.replace_body(MakeTitle.command, '\n')

    def make_constructure(self):
        self.children.extend(Section.sectionize(self.body_without_comment))
        self.children.expand(SubSection.subsectionize(self.children[0]), 0)
        self.children.expand(
            SubSubSection.subsubsectionize(self.children[0]), 0)
        self.children.expand(Paragraph.paragraphize(self.children[0]), 0)
        self.children.expand(SubParagraph.subparagraphize(self.children[0]), 0)
        # env系抜き出す
        self.children.expand(convert_environment(self.children[0]), 0)
        convert_structure(self.children)

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
