# coding: utf-8

import re
from typing import List, Union

from .command import *
from .element import TexElement
from .environment import *
from ...error import InvalidEnvironment
from ..parser.utils import divide_command, trim

REG_BEGIN = re.compile(r'\\begin\{(.+?)\}', re.DOTALL)
REG_END = re.compile(r'\\end\{(.+?)\}', re.DOTALL)


def convert_structure(structure: List[Union[str, TexElement]]):
    for index in range(len(structure)):
        elm = structure[index]
        if isinstance(elm, TexElement):
            ...
        elif isinstance(elm, str):
            if elm == MakeTitle.command:
                structure[index] = MakeTitle()
            elif elm == ClearPage.command:
                structure[index] = ClearPage()
            elif elm == ClearDoublePage.command:
                structure[index] = ClearDoublePage()
            elif elm == NewLine.command:
                structure[index] = NewLine()
            elif elm == TableOfContents.command:
                structure[index] = TableOfContents()
        else:
            print('unknown')

    return structure


def convert_environment(text: str):
    struct = []
    tags_begin = REG_BEGIN.findall(text)
    tags_end = REG_END.findall(text)
    if len(tags_begin) == len(tags_end):
        if len(tags_begin) == 0:
            return divide_command(trim(text))
        to_search = text
        tag = tags_begin[0]
        search = re.search(
            f'\\\\begin{{{tag}}}.+?\\\\end{{{tag}}}', to_search, re.DOTALL)
        if search is not None:
            struct.extend(divide_command(trim(to_search[:search.start()])))
            env = to_search[slice(*search.span())]
            if tag == Table.command:
                struct.extend(Table.generate_table(env))
            elif tag == Tabular.name:
                struct.extend(Tabular.generate_table(env))
            elif tag == Figure.name:
                struct.extend(Figure.generate_table(env))
                envzer = Figure.generate_figure
            else:
                struct.append(Environment.generate_env(env, tag))
            struct.extend(convert_environment(to_search[search.end():]))
        else:
            print('else')
        return struct
    else:
        raise InvalidEnvironment()
