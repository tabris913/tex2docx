# coding: utf-8


class NoDocumentException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MultipleDocumentException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
