# coding: utf-8

import datetime

TRANSMAP = {
    '\\today': str(datetime.date.today()),
    '\\(': '$',
    '\\)': '$',
    '\\[': '$$',
    '\\]': '$$'
}

ESCAPE = {
    '\\%': '%',
    '\\#': '#',
    '\\$': '$',
    '\\&': '&',
    '\\_': '_',
    '\\{': '{',
    '\\}': '}',
    '\\textbar': '|',
    '\\textless': '<',
    '\\textgreater': '>',
    '\\^{}': '^',
    '\\textasciitilde': '^',
    '\\~{}': '~',
    '\\textasciicircum': '~',
    '\\textasteriskcentered': '*',
    '\\yen': '\\',
    '\\textyen': '\\',
    '\\backslash': '\\',
}
