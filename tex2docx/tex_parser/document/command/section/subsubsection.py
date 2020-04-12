# coding: utf-8

from __future__ import annotations

import re
from typing import List, Union

from .base import SectionBase

REG_META = re.compile(r'^(.+?)(?:(?=\\subsubsection)|\Z)', re.DOTALL)
REG_GET_BODY = re.compile(
    r'\\subsubsection\*?\{.+?\}(.+?)(?:(?=\\section)|(?=\\subsection)|(?=\\subsubsection)|\Z)',
    re.DOTALL)
REG_GET_COMMAND = re.compile(r'\\subsubsection\*?\{.+?\}', re.DOTALL)


class SubSubSection(SectionBase):
    def __init__(self, command: str, body: str):
        super().__init__(command, body)

    @classmethod
    def subsubsectionize(cls, text: str) -> List[Union[str, SubSubSection]]:
        meta = REG_META.findall(text)
        if len(meta) > 0:
            return meta + cls.generate_subsubsection(text)
        else:
            return [''] + cls.generate_subsubsection(text)

    @classmethod
    def generate_subsubsection(cls, text: str) -> List[SubSubSection]:
        cmds = REG_GET_COMMAND.findall(text)
        bodies = cls.get_subsubsection(text)
        if len(cmds) == len(bodies):
            return [cls(cmd, body) for cmd, body in zip(cmds, bodies)]
        print('wrong length of subsubsection')

    @classmethod
    def get_subsubsection(cls, body: str) -> List[str]:
        return REG_GET_BODY.findall(body)
