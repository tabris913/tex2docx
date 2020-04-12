# coding: utf-8

from typing import List

from .command import Command


class Title(Command):
    def __init__(self, command: str):
        super().__init__(command)


class Author(Command):
    def __init__(self, command: str):
        super().__init__(command)


class Date(Command):
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
    def __init__(self):
        super().__init__('\\caption')


class Label(Command):
    def __init__(self):
        super().__init__('\\label')


class Ref(Command):
    def __init__(self):
        super().__init__('\\ref')
