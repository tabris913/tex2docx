# coding: utf-8

import functools
import re
from typing import List

REG_SPACE = re.compile(r'\s')
REG_NL = re.compile(r'\n')
REG_TRIM = re.compile(r'[\s\n]')
REG_DIVIDE_CMD = re.compile(r'(\\.+?)(?:(?=\\)|\Z)')


def is_comment(line: str) -> bool:
    return re.match(r'^\s*%.*', line) is not None


def has_comment(line: str) -> bool:
    return re.match(r'.*%.*', line) is not None


def remove_comment(line: str) -> str:
    return re.sub(r'(?<!\\)%.*', '', line)


def is_empty(line: str) -> bool:
    return re.match(r'^\s+$', line) is not None


def trim_empty(line: str) -> str:
    return re.sub(r'^\s+$', '\n', line)


def replace_with_map(line: str, translate: dict) -> str:
    return functools.reduce(
        lambda x, y: x.replace(*y), translate.items(), line)


def remove_spaces(line: str) -> str:
    return REG_SPACE.sub('', line)


def remove_newline(line: str) -> str:
    return REG_NL.sub('', line)


def trim(line: str) -> str:
    return REG_TRIM.sub('', line)


def divide_command(line: str) -> str:
    return REG_DIVIDE_CMD.findall(line)
