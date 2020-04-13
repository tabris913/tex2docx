# coding: utf-8

import docx
import matplotlib.mathtext as mathtext
import uuid

from ..tex_parser.document import Document as TexDoc
from ..tex_parser.document import *
from ..tex_parser.document.command.section import *
from ..tex_parser.document.utils import Children


class Document(docx.document.Document):
    def __init__(self):
        self.__base = docx.Document()
        super().__init__(self.__base.element, self.__base.part)

    def add_title(self, title: str):
        self.add_heading(title, 0)

    def add_author(self, author: str):
        author = self.add_paragraph(author)
        author.alignment = docx.enum.text.WD_PARAGRAPH_ALIGNMENT.RIGHT

    def add_date(self, date: str):
        date = self.add_paragraph(date)
        date.alignment = docx.enum.text.WD_PARAGRAPH_ALIGNMENT.RIGHT

    def parse_document(self, document: TexDoc):
        used_imgs = []
        for child in document.children:
            if isinstance(child, str):
                print(child)
            elif child.children is not None:
                # env, section
                if isinstance(child, SectionBase):
                    if isinstance(child, Section):
                        self.add_section(
                            docx.enum.section.WD_SECTION_START.CONTINUOUS)
                        self.add_heading(child.name, 1)
                    elif isinstance(child, SubSection):
                        self.add_heading(child.name, 2)
                    elif isinstance(child, SubSubSection):
                        self.add_heading(child.name, 3)
                    elif isinstance(child, Paragraph):
                        self.add_heading(child.name, 4)
                    elif isinstance(child, SubParagraph):
                        self.add_heading(child.name, 5)
                    else:
                        print(child)
                elif isinstance(child, Table):
                    print('table')
                elif isinstance(child, Tabular):
                    print('tabular')
                elif isinstance(child, Figure):
                    print('figure')
                used_imgs.extend(self.parse_document(child))
            elif isinstance(child, ClearPage):
                self.add_page_break()
            elif isinstance(child, ClearDoublePage):
                self.add_page_break()
                self.add_page_break()
            elif isinstance(child, Text):
                self.add_paragraph(child.text)
            elif isinstance(child, TableOfContents):
                self.add_paragraph('[toc]')
            elif isinstance(child, Formula):
                figname = f'fig/{uuid.uuid4()}.png'
                p = self.add_paragraph()
                p.alignment = docx.enum.text.WD_PARAGRAPH_ALIGNMENT.CENTER
                r = p.add_run()
                parser = mathtext.MathTextParser('bitmap')
                offset = parser.to_png(figname, child.text)
                fig = r.add_picture(figname)
                used_imgs.append(figname)
            else:
                self.add_paragraph(str(child))
                print(child)
        return used_imgs
