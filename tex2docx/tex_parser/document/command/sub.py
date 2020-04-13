# coding: utf-8

from typing import List

from .command import Command


class Title(Command):
    command = '\\title'

    def __init__(self, command: str):
        super().__init__(command)


class Author(Command):
    commnad = '\\author'

    def __init__(self, command: str):
        super().__init__(command)


class Date(Command):
    command = '\\date'

    def __init__(self, command: str):
        super().__init__(command)


class MakeTitle(Command):
    command = '\\maketitle'

    def __init__(self):
        super().__init__(self.command)


class ClearPage(Command):
    command = '\\clearpage'

    def __init__(self):
        super().__init__(self.command)


class ClearDoublePage(Command):
    command = '\\cleardoublepage'

    def __init__(self):
        super().__init__(self.command)


class NewLine(Command):
    command = '\\newline'

    def __init__(self):
        super().__init__(self.command)


class TableOfContents(Command):
    command = '\\tableofcontents'

    def __init__(self):
        super().__init__(self.command)


class Centering(Command):
    command = '\\centering'

    def __init__(self):
        super().__init__(self.command)


class Caption(Command):
    command = '\\caption'

    def __init__(self, command: str):
        super().__init__(command)


class Label(Command):
    command = '\\label'

    def __init__(self, command: str):
        super().__init__(command)


class Ref(Command):
    command = '\\ref'

    def __init__(self, command: str):
        super().__init__(command)
