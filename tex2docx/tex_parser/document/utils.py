# coding: utf-8


class Children(list):
    def __init__(self, *args):
        super().__init__(*args)

    def expand(self, array: list, index: int):
        new = self[:index] + array + self[index + 1:]
        self.replace(new)

    def replace(self, array: list):
        self.clear()
        self.extend(array)
