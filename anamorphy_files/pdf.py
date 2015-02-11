"""
This module converts an image to a PDF document, using the Reportlab
library (http://www.reportlab.com/).
"""
import reportlab.graphics.shapes as shapes
from reportlab.graphics import renderPDF
import reportlab.lib.pagesizes as ps

# Must import these because reportlab imports them dynamically,
# preventing py2exe/py2app to pull them:
import reportlab.pdfbase._fontdata_enc_macexpert
import reportlab.pdfbase._fontdata_enc_macroman
import reportlab.pdfbase._fontdata_enc_pdfdoc
import reportlab.pdfbase._fontdata_enc_standard
import reportlab.pdfbase._fontdata_enc_symbol
import reportlab.pdfbase._fontdata_enc_winansi
import reportlab.pdfbase._fontdata_enc_zapfdingbats
import reportlab.pdfbase._fontdata_widths_courier
import reportlab.pdfbase._fontdata_widths_courierbold
import reportlab.pdfbase._fontdata_widths_courierboldoblique
import reportlab.pdfbase._fontdata_widths_courieroblique
import reportlab.pdfbase._fontdata_widths_helvetica
import reportlab.pdfbase._fontdata_widths_helveticabold
import reportlab.pdfbase._fontdata_widths_helveticaboldoblique
import reportlab.pdfbase._fontdata_widths_helveticaoblique
import reportlab.pdfbase._fontdata_widths_symbol
import reportlab.pdfbase._fontdata_widths_timesbold
import reportlab.pdfbase._fontdata_widths_timesbolditalic
import reportlab.pdfbase._fontdata_widths_timesitalic
import reportlab.pdfbase._fontdata_widths_timesroman
import reportlab.pdfbase._fontdata_widths_zapfdingbats


def getBitmapSize(name, dpi, is_landscape):
    """
    Given a page format name (like "a4" or "a4 landscape"), a density
    in dpi, and the orientation, returns how many dots it means.

    The caller may use this function to determine the pixel size of
    the image to generate in order to fit the page format.
    """
    points = {
        'a0': ps.A0,
        'a1': ps.A1,
        'a2': ps.A2,
        'a3': ps.A3,
        'a4': ps.A4,
        'a5': ps.A5,
        'a6': ps.A6,
        'b0': ps.B0,
        'b1': ps.B1,
        'b2': ps.B2,
        'b3': ps.B3,
        'b4': ps.B4,
        'b5': ps.B5,
        'b6': ps.B6,
        'elevenSeventeen': ps.elevenSeventeen,
        'legal': ps.legal,
        'letter': ps.letter,
        }[name]
    if is_landscape:
        h_points, w_points = points
    else:
        w_points, h_points = points
    w_inches, h_inches = w_points / 72, h_points / 72
    w_dots, h_dots = w_inches * dpi, h_inches * dpi
    return w_dots, h_dots


def generate(img_path, pdf_width_mm, pdf_height_mm, pdf_path):
    """
    Convert an input image (*) into a PDF output document, having the
    specified size in mm.

    (*) given as an input file path; the caller may have to store it
    in a temporary file.
    """
    mm2point = lambda x: x * 0.0393701 * 72
    w, h = mm2point(pdf_width_mm), mm2point(pdf_height_mm)
    #print w, h
    img = shapes.Image(0, 0, w, h, img_path)
    page = shapes.Drawing(w, h)
    page.add(img)
    renderPDF.drawToFile(page, pdf_path)
    return
