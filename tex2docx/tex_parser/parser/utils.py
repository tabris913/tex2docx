# coding: utf-8

import functools
import re
from typing import List

REG_SPACE = re.compile(r'\s')
REG_NL = re.compile(r'\n')
REG_TRIM = re.compile(r'^\s*(.*?)\s*$')
REG_LEFT_TRIM = re.compile(r'\s+(?=\S)')
REG_RIGHT_TRIM = re.compile(r'(?<=\S)\s+')
REG_TRIM_NL = re.compile(r'\\(?!\w)')
REG_SP_AFTER_CMD = re.compile(r'(?P<command>\\\w+)\s+')


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
    trimmed = REG_TRIM.findall(line)
    if len(trimmed) == 1:
        return trimmed[0]


def divide_command(line: str) -> List[str]:
    # convert \\ to \n
    line = REG_TRIM_NL.sub(r'\n', line.replace('\\%', '%'))
    line = REG_SP_AFTER_CMD.sub(r'\g<command>\n', line)
    # convert \\ to \n\\
    line = re.sub(r'\\', r'\n\\', line)
    return [line for line in map(trim, line.split('\n')) if line != '']
