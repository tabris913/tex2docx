# coding: utf-8


class InvalidEnvironment(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
