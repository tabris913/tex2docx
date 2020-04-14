# coding: utf-8

from __future__ import annotations

import re
from typing import List, Union

from ...converter import convert_environment, convert_structure
from .base import SectionBase
from .subparagraph import SubParagraph

REG_META = re.compile(r'^(.+?)(?:(?=\\paragraph)|\Z)', re.DOTALL)
REG_GET_BODY = re.compile(
    r'\\paragraph\*?\{.+?\}(.+?)(?:(?=\\section)|(?=\\subsection)|(?=\\subsubsection)|(?=\\paragraph)|\Z)',
    re.DOTALL)
REG_GET_COMMAND = re.compile(r'\\paragraph\*?\{.+?\}', re.DOTALL)


class Paragraph(SectionBase):
    def __init__(self, command: str, body: str):
        super().__init__(command, body)
        self.make_constructure()

    @classmethod
    def paragraphize(cls, text: str) -> List[Union[str, Paragraph]]:
        meta = REG_META.findall(text)
        if len(meta) > 0:
            return meta + cls.generate_paragraph(text)
        else:
            return [''] + cls.generate_paragraph(text)

    @classmethod
    def generate_paragraph(cls, text: str) -> List[Paragraph]:
        cmds = REG_GET_COMMAND.findall(text)
        bodies = cls.get_paragraph(text)
        if len(cmds) == len(bodies):
            return [cls(cmd, body) for cmd, body in zip(cmds, bodies)]
        print('wrong length of paragraph')

    @classmethod
    def get_paragraph(cls, body: str) -> List[str]:
        return REG_GET_BODY.findall(body)

    def make_constructure(self):
        self.children.extend(SubParagraph.subparagraphize(self.body))
        # env系抜き出す
        self.children.expand(convert_environment(self.children[0]), 0)
        convert_structure(self.children)
        self._set_label()
