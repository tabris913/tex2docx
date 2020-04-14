# coding: utf-8

import re
from typing import List, Union

from .command import *
from .element import TexElement
from .text import Text
from .formula import Formula
from ...error import InvalidEnvironment
from ..parser.utils import divide_command

REG_BEGIN = re.compile(r'\\begin\{(.+?)\}', re.DOTALL)
REG_END = re.compile(r'\\end\{(.+?)\}', re.DOTALL)
REG_FORMULA = re.compile(r'\$\$.+?\$\$', re.DOTALL)
REG_FORMULA_INLINE = re.compile(r'\$.+?\$', re.DOTALL)


def convert_structure(structure: List[Union[str, TexElement]]):
    unknown_command = []
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
            elif elm == Centering.command:
                structure[index] = Centering()
            elif elm == HLine.command:
                structure[index] = HLine()
            elif elm == TopRule.command:
                structure[index] = TopRule()
            elif elm == MidRule.command:
                structure[index] = MidRule()
            elif elm == BottomRule.command:
                structure[index] = BottomRule()
            else:
                cmd = Command(elm).cmd
                if cmd is None:
                    if REG_FORMULA.match(elm):
                        structure[index] = Formula(elm, False)
                    elif REG_FORMULA_INLINE.match(elm):
                        structure[index] = Formula(elm)
                    else:
                        structure[index] = Text(elm)
                elif cmd == Ref.command:
                    structure[index] = Ref(elm)
                elif cmd == Label.command:
                    structure[index] = Label(elm)
                elif cmd == Caption.command:
                    structure[index] = Caption(elm)
                elif cmd == CLine.command:
                    structure[index] = CLine(elm)
                elif cmd == IncludeGraphics.command:
                    structure[index] = IncludeGraphics(elm)
                else:
                    structure[index] = Command(elm)
                    unknown_command.append(elm)
        else:
            print('unknown')

    if unknown_command:
        print(f'unknown: {unknown_command}')
    return structure


def convert_environment(text: str):
    from .environment import Environment, Figure, Table, Tabular
    struct = []
    tags_begin = REG_BEGIN.findall(text)
    tags_end = REG_END.findall(text)
    if len(tags_begin) == len(tags_end):
        if len(tags_begin) == 0:
            return divide_command(text)
        to_search = text
        tag = tags_begin[0]
        search = re.search(
            f'\\\\begin{{{tag}}}.+?\\\\end{{{tag}}}', to_search, re.DOTALL)
        if search is not None:
            struct.extend(divide_command(to_search[:search.start()]))
            env = to_search[slice(*search.span())]
            if tag == Table.command:
                struct.extend(Table.generate_table(env))
            elif tag == Tabular.command:
                struct.extend(Tabular.generate_tabular(env))
            elif tag == Figure.command:
                struct.extend(Figure.generate_figure(env))
                envzer = Figure.generate_figure
            else:
                struct.append(Environment.generate_env(env, tag))
            struct.extend(convert_environment(to_search[search.end():]))
        else:
            print('else')

        return struct
    else:
        raise InvalidEnvironment()
