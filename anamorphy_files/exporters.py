"""
Provides exporters for image and PDF file formats.

Also, provides threads to compute file in parallel 8e.g. while
querying a file name).
"""

import threading
import tempfile

import pdf
import os


class ImageExporter(object):
    def __init__(self, renderer, width, height, progressPcentFn=None):
        self.renderer = renderer
        self.width = int(width + 0.5)
        self.height = int(height + 0.5)
        self.transparent = True
        self.progressPcentFn = progressPcentFn

    def generate(self):
        self.bmp = self.renderer(self.width, self.height, self.progressPcentFn)

    def save(self, name):
        if name is not None:
            self.bmp.getPil().save(name)


class PdfExporter(ImageExporter):
    def __init__(self, renderer, img_width, img_height,
                 pdf_width_mm, pdf_height_mm, progressPcentFn=None):
        super(PdfExporter, self).__init__(
            renderer, img_width, img_height)
        self.pdf_width_mm = pdf_width_mm
        self.pdf_height_mm = pdf_height_mm
        self.bmp = None
        self.progressPcentFn = progressPcentFn

    def save(self, pdf_path):
        if pdf_path is not None:
            # save bitmap
            f, img_path = tempfile.mkstemp(suffix='.png')
            print "PdfExporter: saving tmp image:", img_path
            pil = self.bmp.getPilOpaque('WHITE')
            pil.save(img_path)
            # make pdf
            print "PdfExporter: generating pdf:", pdf_path
            pdf.generate(img_path, self.pdf_width_mm, self.pdf_height_mm,
                         pdf_path)
            # clean
            try:
                os.remove(img_path)
                print "PdfExporter: tmp file removed"
            except OSError:
                pass
