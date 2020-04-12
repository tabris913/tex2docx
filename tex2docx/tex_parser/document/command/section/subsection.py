# coding: utf-8

from __future__ import annotations

import re
from typing import List, Union

from .base import SectionBase

REG_META = re.compile(r'^(.+?)(?:(?=\\subsection)|\Z)', re.DOTALL)
REG_GET_BODY = re.compile(
    r'\\subsection\*?\{.+?\}(.+?)(?:(?=\\section)|(?=\\subsection)|\Z)',
    re.DOTALL)
REG_GET_COMMAND = re.compile(r'\\subsection\*?\{.+?\}', re.DOTALL)


class SubSection(SectionBase):
    def __init__(self, command: str, body: str):
        super().__init__(command, body)

    @classmethod
    def subsectionize(cls, text: str) -> List[Union[str, SubSection]]:
        meta = REG_META.findall(text)
        if len(meta) > 0:
            return meta + cls.generate_subsection(text)
        else:
            return [''] + cls.generate_subsection(text)

    @classmethod
    def generate_subsection(cls, text: str) -> List[SubSection]:
        cmds = REG_GET_COMMAND.findall(text)
        bodies = cls.get_subsection(text)
        if len(cmds) == len(bodies):
            return [cls(cmd, body) for cmd, body in zip(cmds, bodies)]
        print('wrong length of subsection')

    @classmethod
    def get_subsection(cls, body: str) -> List[str]:
        return REG_GET_BODY.findall(body)
