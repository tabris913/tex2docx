# coding: utf-8

from ...error import MultipleDocumentException, NoDocumentException
from .environment import Environment


class Document(Environment):
    def __init__(self, body: str):
        super().__init__('document', body)
        self.constructure = None

    def has_maketitle(self) -> bool:
        return '\\maketitle' in self.body

    def remove_maketitle(self):
        self.replace_body(r'\\maketitle', '\n')

    def make_constructure(self):
        self.constructure = []

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
