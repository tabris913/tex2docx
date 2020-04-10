# coding: utf-8

import argparse
from .model.tex2docx import Tex2Docx

parser = argparse.ArgumentParser()
parser.add_argument('source', type=str)
parser.add_argument('target', type=str)
args = parser.parse_args()

model = Tex2Docx(**args.__dict__)
model.debug()
model.convert()
