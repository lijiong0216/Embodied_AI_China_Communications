"""Local submission QA and contact sheets; not part of the files to upload."""
import hashlib
import json
import re
from pathlib import Path

from PIL import Image, ImageDraw
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "tmp/pdfs/submission/build"
OUT = ROOT / "output/pdf"
original = (ROOT / "bare_jrnl_new_sample43.tex").read_text(encoding="utf-8")
anonymous = (ROOT / "submission/China_Communications_Main_Document.tex").read_text(encoding="utf-8")
anchor = r"\begin{abstract}"
assert original[original.index(anchor):].rstrip() == anonymous[anonymous.index(anchor):].rstrip(), "Body was changed"
assert r"\thanks{" not in anonymous
assert r"\markboth" not in anonymous
original_sha = hashlib.sha256((ROOT / "bare_jrnl_new_sample43.tex").read_bytes()).hexdigest()
assert original_sha == "4bb925f096a567dcb7c042d6cb449bbb75eadb9a6c990617aae2d7a47e1e49cd"

main = PdfReader(OUT / "China_Communications_Main_Document.pdf")
title = PdfReader(OUT / "China_Communications_Title_Page.pdf")
text = "\n".join(page.extract_text() or "" for page in main.pages)
title_text = "\n".join(page.extract_text() or "" for page in title.pages)
full_names = ["Jihong Li", "Changming Li", "Bo Li", "Zisong Ma", "Qingqing Wu", "Shunqing Zhang"]
private_terms = full_names + ["Shanghai University", "Shanghai Jiao Tong", "62571307", "24DP1500703",
                             "24DP1500500", "2022YFB2902304", "Journal of LaTeX Class Files"]
assert not main.metadata.author
assert not any(term.lower() in text.lower() for term in private_terms)
assert not main.attachments
assert all(name in title_text for name in full_names)
assert len(title.pages) == 1
assert all(grant in title_text for grant in ["62571307", "24DP1500703", "24DP1500500", "2022YFB2902304"])
assert text.strip().endswith("16"), "Expected last-page number"

references = re.findall(r"(?m)^\\bibitem\{([^}]+)\}", anonymous)
report = {
    "original_sha256_unchanged": original_sha,
    "body_from_abstract_through_references_unchanged": True,
    "active_references": len(references),
    "main_pages": len(main.pages),
    "title_page_pages": len(title.pages),
    "main_author_metadata": main.metadata.author,
    "main_no_identifying_author_affiliation_funding_text": True,
    "main_no_embedded_attachments": True,
    "title_has_all_six_authors_and_four_grants": True,
    "pending": ["Corresponding email", "Author biographies and photographs", "Official ccjnl.cls template migration", "Separate author commitment statement"]
}
print(json.dumps(report, indent=2))

images = sorted(BUILD.glob("main-*.png"))
for offset in range(0, len(images), 4):
    sheet = Image.new("RGB", (1420, 1870), "#dddddd")
    draw = ImageDraw.Draw(sheet)
    for n, file in enumerate(images[offset:offset + 4]):
        im = Image.open(file).convert("RGB")
        im.thumbnail((685, 895))
        x = 12 + (n % 2)*710
        y = 28 + (n // 2)*935
        sheet.paste(im, (x, y))
        draw.text((x, y-18), file.stem, fill="black")
    sheet.save(BUILD / f"contact-{offset//4 + 1}.png")
