"""
Lazily print, by generating a PDF temporary document, and calling the
system's PDF viewer on it,
"""

import exporters
import tempfile
import subprocess
import os
import sys


def printPdf(renderer, update_fn, done_fn,
             img_w, img_h, pdf_w_mm, pdf_h_mm):
    f, pdf_path = tempfile.mkstemp(prefix='anamorphy_', suffix='.pdf')

    update_fn("Making PDF for printing...")
    exporter = exporters.PdfExporter(renderer, img_w, img_h,
                                     pdf_w_mm, pdf_h_mm)
    exporter.generate()

    update_fn("Saving PDF for printing...")
    exporter.save(pdf_path)

    done_fn("Opening PDF viewer...")
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', pdf_path))
    elif os.name == 'nt':
        os.startfile(pdf_path)
    elif os.name == 'posix':
        subprocess.call(('xdg-open', pdf_path))
