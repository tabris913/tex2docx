# coding: utf-8

from __future__ import annotations

import re
from typing import List, Union

from .base import SectionBase
from .paragraph import Paragraph
from .subparagraph import SubParagraph
from .subsection import SubSection
from .subsubsection import SubSubSection
from ..command import Command
from ...converter import convert_environment, convert_structure

REG_META = re.compile(r'^(.+?)(?:(?=\\section)|\Z)', re.DOTALL)
REG_GET_BODY = re.compile(
    r'\\section\*?\{.+?\}(.+?)(?:(?=\\section)|\Z)',
    re.DOTALL)
REG_GET_COMMAND = re.compile(r'\\section\*?\{.+?\}', re.DOTALL)


class Section(SectionBase):
    def __init__(self, command: str, body: str):
        super().__init__(command, body)
        self.make_constructure()

    @classmethod
    def sectionize(cls, text: str) -> List[Union[str, Section]]:
        meta = REG_META.findall(text)
        if len(meta) > 0:
            return meta + cls.generate_section(text)
        else:
            return [''] + cls.generate_section(text)

    @classmethod
    def generate_section(cls, text: str) -> List[Section]:
        cmds = REG_GET_COMMAND.findall(text)
        bodies = cls.get_section(text)
        if len(cmds) == len(bodies):
            return [cls(cmd, body) for cmd, body in zip(cmds, bodies)]
        print('wrong length of section')

    @classmethod
    def get_section(cls, text: str) -> List[str]:
        return REG_GET_BODY.findall(text)

    def make_constructure(self):
        self.children.extend(SubSection.subsectionize(self.body))
        self.children.expand(
            SubSubSection.subsubsectionize(self.children[0]), 0)
        self.children.expand(Paragraph.paragraphize(self.children[0]), 0)
        self.children.expand(SubParagraph.subparagraphize(self.children[0]), 0)
        # env系抜き出す
        self.children.expand(convert_environment(self.children[0]), 0)
        convert_structure(self.children)
        self._set_label()
