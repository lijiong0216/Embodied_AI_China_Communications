"""Create the separate author-information PDF, without inventing missing details."""
import json
from functools import partial
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "submission/title_page_data.json").read_text(encoding="utf-8"))
OUT = ROOT / "output/pdf/China_Communications_Title_Page.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

for name, file in (("TimesNR", "times.ttf"), ("TimesNR-Bold", "timesbd.ttf"),
                   ("TimesNR-Italic", "timesi.ttf"), ("TimesNR-BoldItalic", "timesbi.ttf")):
    pdfmetrics.registerFont(TTFont(name, str(Path("C:/Windows/Fonts") / file)))
pdfmetrics.registerFontFamily("TimesNR", normal="TimesNR", bold="TimesNR-Bold",
                            italic="TimesNR-Italic", boldItalic="TimesNR-BoldItalic")

styles = {
    "label": ParagraphStyle("label", fontName="TimesNR", fontSize=10, leading=13,
                            alignment=TA_CENTER, spaceAfter=7),
    "title": ParagraphStyle("title", fontName="TimesNR-Bold", fontSize=18, leading=23,
                            alignment=TA_CENTER, spaceAfter=17),
    "authors": ParagraphStyle("authors", fontName="TimesNR", fontSize=12, leading=19,
                              alignment=TA_CENTER, spaceAfter=14),
    "body": ParagraphStyle("body", fontName="TimesNR", fontSize=11, leading=15,
                           alignment=TA_LEFT, spaceAfter=8),
    "heading": ParagraphStyle("heading", fontName="TimesNR-Bold", fontSize=12,
                              leading=15, spaceBefore=14, spaceAfter=7),
}

def para(text, style="body"):
    return Paragraph(text, styles[style])

author_lines = []
for author in DATA["authors"]:
    marker = author["affiliation"] + (",*" if author["name"] == DATA["corresponding_author"] else "")
    text = escape(author["name"]) + '<super size="8">' + marker + '</super>'
    if author["membership"]:
        text += ', <i>' + escape(author["membership"]) + '</i>'
    author_lines.append(text)

story = [para("CHINA COMMUNICATIONS", "label"), para("TITLE PAGE", "label"),
         Spacer(1, 7 * mm), para(escape(DATA["title"]), "title"),
         para("<br/>".join(author_lines), "authors"),
         HRFlowable(width="100%", thickness=0.6, color=colors.black, spaceAfter=5 * mm)]
affiliation_block = [para("Affiliations", "heading")]
for key, address in DATA["affiliations"].items():
    affiliation_block.append(para('<super size="8">' + key + '</super> ' + escape(address)))
story.append(KeepTogether(affiliation_block))
correspondence = [para("Corresponding Author", "heading"),
                 para("* " + escape(DATA["corresponding_author"])),
                 para(escape(DATA["affiliations"]["1"]))]
if DATA["corresponding_email"]:
    correspondence.append(para("Email: " + escape(DATA["corresponding_email"])))
story.append(KeepTogether(correspondence))
story.append(KeepTogether([para("Acknowledgement", "heading"),
                          para(escape(DATA["acknowledgement"]))]))

if DATA["biographies"]:
    story.append(para("Biographies", "heading"))
    for biography in DATA["biographies"]:
        story.append(para("<b>" + escape(biography["name"]) + ".</b> " + escape(biography["text"])))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("TimesNR", 9)
    canvas.drawCentredString(A4[0] / 2, 17 * mm, str(doc.page))
    canvas.restoreState()

doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=25*mm, rightMargin=25*mm,
                        topMargin=22*mm, bottomMargin=24*mm,
                        title=DATA["title"],
                        author=", ".join(a["name"] for a in DATA["authors"]),
                        subject="Separate title page with author details")
doc.build(story, onFirstPage=footer, onLaterPages=footer,
          canvasmaker=partial(Canvas, initialFontName="TimesNR"))
print(OUT)
if not DATA["corresponding_email"]:
    print("NOTE: Corresponding email not supplied; it has not been invented or replaced with a placeholder.")
if not DATA["biographies"]:
    print("NOTE: Author biographies and photographs are not supplied.")
