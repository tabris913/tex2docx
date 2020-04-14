# coding: utf-8

from __future__ import annotations

import re
from typing import List, Union

from ...converter import convert_environment, convert_structure
from .base import SectionBase

REG_META = re.compile(r'^(.+?)(?:(?=\\subparagraph)|\Z)', re.DOTALL)
REG_GET_BODY = re.compile(
    r'\\subparagraph\*?\{.+?\}(.+?)(?:(?=\\section)|(?=\\subsection)|(?=\\subsubsection)|(?=\\paragraph)|(?=\\subparagraph)|\Z)',
    re.DOTALL)
REG_GET_COMMAND = re.compile(r'\\subparagraph\*?\{.+?\}', re.DOTALL)


class SubParagraph(SectionBase):
    def __init__(self, command: str, body: str):
        super().__init__(command, body)
        self.make_constructure()

    @classmethod
    def subparagraphize(cls, text: str) -> List[Union[str, SubParagraph]]:
        meta = REG_META.findall(text)
        if len(meta) > 0:
            return meta + cls.generate_subparagraph(text)
        else:
            return [''] + cls.generate_subparagraph(text)

    @classmethod
    def generate_subparagraph(cls, text: str) -> List[SubParagraph]:
        cmds = REG_GET_COMMAND.findall(text)
        bodies = cls.get_subparagraph(text)
        if len(cmds) == len(bodies):
            return [cls(cmd, body) for cmd, body in zip(cmds, bodies)]
        print('wrong length of subparagraph')

    @classmethod
    def get_subparagraph(cls, text: str) -> List[str]:
        return REG_GET_BODY.findall(text)

    def make_constructure(self):
        self.children.extend(convert_environment(self.body))
        convert_structure(self.children)
        self._set_label()
