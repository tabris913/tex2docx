# coding: utf-8


class InvalidCommandName(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
