# coding: utf-8

import re
from typing import List

from .command import Command

REG_GET_SEC = re.compile(
    r'\\section\*?\{.+?\}(.+?)(?:(?=\\section)|\Z)',
    re.DOTALL)
REG_GET_SSEC = re.compile(
    r'\\subsection\*?\{.+?\}(.+?)(?:(?=\\section)|(?=\\subsection)|\Z)',
    re.DOTALL)
REG_GET_SSSEC = re.compile(
    r'\\subsubsection\*?\{.+?\}(.+?)(?:(?=\\section)|(?=\\subsection)|(?=\\subsubsection)|\Z)',
    re.DOTALL)
REG_GET_PAR = re.compile(
    r'\\paragraph\*?\{.+?\}(.+?)(?:(?=\\section)|(?=\\subsection)|(?=\\subsubsection)|(?=\\paragraph)|\Z)',
    re.DOTALL)
REG_GET_SPAR = re.compile(
    r'\\subparagraph\*?\{.+?\}(.+?)(?:(?=\\section)|(?=\\subsection)|(?=\\subsubsection)|(?=\\paragraph)|(?=\\subparagraph)|\Z)',
    re.DOTALL)
REG_SEC_TAG = re.compile(r'\\section\*?\{(.+?)\}', re.DOTALL)
REG_SSEC_TAG = re.compile(r'\\subsection\*?\{(.+?)\}', re.DOTALL)
REG_SSSEC_TAG = re.compile(r'\\subsubsection\*?\{(.+?)\}', re.DOTALL)
REG_PAR_TAG = re.compile(r'\\paragraph\*?\{(.+?)\}', re.DOTALL)
REG_SPAR_TAG = re.compile(r'\\subparagraph\*?\{(.+?)\}', re.DOTALL)


class Section(Command):
    def __init__(
            self,
            section_name: str,
            body: str,
            raw_command: str = '\\section'):
        super().__init__(raw_command)
        self.name = section_name
        self.body = body

    @classmethod
    def generate_section(cls, body: str):
        tags = REG_SEC_TAG.findall(body)
        sec = cls.get_section(body)
        if len(tags) == len(sec):
            return [cls(t, s) for t, s in zip(tags, sec)]
        print('wrong length of section')

    @classmethod
    def get_section(cls, body: str) -> List[str]:
        return REG_GET_SEC.findall(body)


class SubSection(Section):
    def __init__(self, section_name: str, body):
        super().__init__(section_name, body)

    @classmethod
    def get_subsection(cls, body: str) -> List[str]:
        return REG_GET_SSEC.findall(body)


class SubSubSection(Section):
    def __init__(self, section_name: str, body):
        super().__init__(section_name, body)

    @classmethod
    def get_subsubsection(cls, body: str) -> List[str]:
        return REG_GET_SSSEC.findall(body)


class Paragraph(Section):
    def __init__(self, section_name: str, body):
        super().__init__(section_name, body)

    @classmethod
    def get_paragraph(cls, body: str):
        tags = REG_GET_PAR.findall(body)


class SubParagraph(Section):
    def __init__(self, section_name: str, body):
        super().__init__(section_name, body)

    @classmethod
    def get_subparagraph(cls, body: str):
        tags = REG_GET_SPAR.findall(body)
