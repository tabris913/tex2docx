# coding: utf-8

import re


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
