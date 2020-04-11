# coding: utf-8

from typing import List


class Command(object):
    def __init__(self, command: str):
        self.__raw_command = command

    @property
    def raw_command(self):
        return self.__raw_command

    def __parameter(self):
        ...

    def __option(self):
        ...

    def __command_name(self):
        ...


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


def command_converter(self, command_list: List[str]):
    ...
