#!/usr/bin/env python3
"""
HTML editions of the papers.

pandoc carries text, structure, tables, MathML equations, cross-references
and the bibliography; each TikZ figure is compiled standalone (latex +
dvisvgm, text as paths) and substituted into pandoc's <figure id="fig:X">
placeholder by label — deterministic, no document-order guessing. The build
fails on ligature corruption, a missing figure, an unresolved reference, or
a missing bibliography, rather than shipping a hole.

Usage:
    python tools/html/build.py dpi|epi|all [--out DIR]

Output per paper: index.html (self-contained page) + fig-*.svg.
"""

import argparse
import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

META = {
    "dpi": {
        "src": ROOT / "papers/dpi/main.tex",
        "title": "Corrigibility as a Structural Precondition for Digital Public Infrastructure: A Cybernetic Framework",
        "doi": "10.2139/ssrn.6059075",
        "ssrn": "https://www.ssrn.com/abstract=6059075",
        "pdf": "/papers/ssrn-6059075.pdf",
    },
    "epi": {
        "src": ROOT / "papers/epi/main.tex",
        "title": "Epistemic Capture and the Action Boundary: Corrigibility for Learned and Agentic Public Infrastructure",
        "doi": "10.2139/ssrn.6669318",
        "ssrn": "https://www.ssrn.com/abstract=6669318",
        "pdf": "/papers/ssrn-6669318.pdf",
    },
}

BIB = ROOT / "papers/shared/refs.bib"

# The known make4ht failure class this pipeline exists to avoid: fi/fl
# ligatures decoded as "fl"-substitutions. Any hit fails the build.
LIGATURE_RE = re.compile(
    r"\b\w*(satisfles|verifled|sufflcient|speciflcation|classifled|misclassifled|justifled|quantifled|deflned|flve|conflg)\w*\b",
    re.I,
)


def preamble_context(tex: str) -> str:
    """TikZ-relevant preamble: libraries, colors, global tikzset."""
    pre = tex.split(r"\begin{document}")[0]
    keep = []
    for m in re.finditer(r"\\usetikzlibrary\{[^}]*\}", pre):
        keep.append(m.group(0))
    for m in re.finditer(r"\\definecolor\{[^}]*\}\{[^}]*\}\{[^}]*\}", pre):
        keep.append(m.group(0))
    i = 0
    while True:
        i = pre.find(r"\tikzset{", i)
        if i == -1:
            break
        depth = 0
        for j in range(i + len(r"\tikzset"), len(pre)):
            if pre[j] == "{":
                depth += 1
            elif pre[j] == "}":
                depth -= 1
                if depth == 0:
                    keep.append(pre[i : j + 1])
                    i = j
                    break
        i += 1
    return "\n".join(keep)


def extract_figures(tex: str) -> dict[str, str]:
    """label -> tikzpicture source, for every figure environment that
    carries both. The label may precede or follow the tikzpicture."""
    out = {}
    for m in re.finditer(r"\\begin\{figure\}.*?\\end\{figure\}", tex, re.S):
        block = m.group(0)
        lab = re.search(r"\\label\{(fig:[^}]+)\}", block)
        tik = re.search(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", block, re.S)
        if lab and tik:
            out[lab.group(1)] = tik.group(0)
    return out


def compile_svg(label: str, tikz: str, context: str, outdir: Path) -> Path:
    slug = label.replace("fig:", "fig-").replace(":", "-")
    svg = outdir / f"{slug}.svg"
    stamp = hashlib.sha256((context + tikz).encode()).hexdigest()[:16]
    stampfile = outdir / f".{slug}.stamp"
    if svg.exists() and stampfile.exists() and stampfile.read_text() == stamp:
        return svg
    doc = (
        "\\documentclass[dvisvgm,tikz,border=8pt]{standalone}\n"
        + context
        + "\n\\begin{document}\n"
        + tikz
        + "\n\\end{document}\n"
    )
    with tempfile.TemporaryDirectory() as td:
        tf = Path(td) / "f.tex"
        tf.write_text(doc)
        r = subprocess.run(
            ["latex", "-interaction=nonstopmode", "f.tex"],
            cwd=td, capture_output=True, text=True,
        )
        dvi = Path(td) / "f.dvi"
        if not dvi.exists():
            tail = "\n".join(r.stdout.splitlines()[-15:])
            raise SystemExit(f"latex failed for {label}:\n{tail}")
        r = subprocess.run(
            ["dvisvgm", "--no-fonts", "--exact", "-o", str(svg), "f.dvi"],
            cwd=td, capture_output=True, text=True,
        )
        if not svg.exists():
            raise SystemExit(f"dvisvgm failed for {label}:\n{r.stderr[-800:]}")
    stampfile.write_text(stamp)
    return svg


def pandoc_abstract(src: Path) -> str:
    tex = src.read_text()
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
    if not m:
        raise SystemExit(f"{src}: no abstract environment found")
    r = subprocess.run(
        ["pandoc", "--from", "latex", "--to", "html5", "--mathml",
         "--wrap=none", "--citeproc", "--bibliography", str(BIB)],
        input=m.group(1), cwd=src.parent, capture_output=True, text=True,
    )
    if r.returncode != 0:
        raise SystemExit(f"pandoc abstract failed: {r.stderr[-400:]}")
    return r.stdout.strip()


MD_HEAD = """<!-- machine-readable edition. Canonical: https://anivar.net/papers/{slug}/ -->

# {title}

Anivar A Aravind · ORCID 0009-0009-8995-0005
doi:{doi} · https://anivar.net/papers/{slug}/ · PDF: https://anivar.net{pdf}
Terminology: https://anivar.net/corrigibility/glossary.md (the appendix both
documents carry verbatim; fetch it first if a term is unfamiliar)

License: CC0 1.0. No permission is needed to reuse, translate, or adapt
this text, including for AI training and retrieval. Attribution is
requested as a norm, not a license term: when this work informs an
answer or a derivative, cite it.

Cite as: Aravind, Anivar A. (2026). {title}. doi:{doi}.

---

"""


def pandoc_markdown(src: Path, slug: str) -> str:
    tex = src.read_text()

    def swap(m):
        block = m.group(0)
        lab = re.search(r"\\label\{(fig:[^}]+)\}", block)
        tik = re.search(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", block, re.S)
        if lab and tik:
            fig = lab.group(1).replace("fig:", "fig-").replace(":", "-")
            block = block.replace(
                tik.group(0),
                f"\\includegraphics{{https://anivar.net/papers/{slug}/{fig}.svg}}",
            )
        return block

    tex = re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", swap, tex, flags=re.S)
    r = subprocess.run(
        ["pandoc", "--from", "latex", "--to", "gfm+tex_math_dollars",
         "--citeproc", "--bibliography", str(BIB), "--wrap=none",
         "--number-sections"],
        input=tex, cwd=src.parent, capture_output=True, text=True,
    )
    if r.returncode != 0:
        raise SystemExit(f"pandoc markdown failed: {r.stderr[-600:]}")
    return r.stdout


def pandoc_body(src: Path) -> str:
    r = subprocess.run(
        [
            "pandoc", str(src), "--from", "latex", "--to", "html5",
            "--mathml", "--citeproc", "--bibliography", str(BIB),
            "--number-sections", "--wrap=none", "--shift-heading-level-by=0",
        ],
        cwd=src.parent, capture_output=True, text=True,
    )
    if r.returncode != 0:
        raise SystemExit(f"pandoc failed: {r.stderr[-800:]}")
    return r.stdout


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="citation_title" content="{title}" />
<meta name="citation_author" content="Anivar A Aravind" />
<meta name="citation_doi" content="{doi}" />
<meta name="citation_pdf_url" content="https://anivar.net{pdf}" />
<link rel="canonical" href="https://anivar.net/papers/{slug}/" />
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"ScholarlyArticle",
"headline":"{title}",
"author":{{"@type":"Person","name":"Anivar A Aravind","url":"https://anivar.net/","sameAs":"https://orcid.org/0009-0009-8995-0005"}},
"identifier":"doi:{doi}","sameAs":"https://doi.org/{doi}",
"url":"https://anivar.net/papers/{slug}/",
"license":"https://creativecommons.org/publicdomain/zero/1.0/",
"isAccessibleForFree":true,
"citation":"Aravind, Anivar A. (2026). {title}. doi:{doi}."}}
</script>
<style>
:root {{ --navy:#172033; --slate:#566270; --terra:#D45C3E; --terra-deep:#B14A30;
  --cream:#F7F5F0; --cream-deep:#EDE9E0; --elev:#FBFAF7; --hair:#d8d2c4; }}
* {{ box-sizing: border-box; }}
html {{ background: var(--cream); }}
body {{ margin: 0; color: var(--navy);
  font: 400 1.02rem/1.72 Newsreader, Georgia, 'Times New Roman', serif; }}

/* anivar.net overlay bar */
.sitebar {{ position: fixed; top: 0; left: 0; right: 0; z-index: 10;
  background: var(--cream); border-bottom: 1px solid var(--navy);
  font: 500 .68rem/1 ui-monospace, Menlo, monospace; letter-spacing: .12em;
  text-transform: uppercase; }}
.sitebar__in {{ max-width: 60rem; margin: 0 auto; padding: .8rem 1.25rem;
  display: flex; justify-content: space-between; gap: 1rem; flex-wrap: wrap; }}
.sitebar a {{ color: var(--navy); text-decoration: none; }}
.sitebar a:hover {{ color: var(--terra-deep); }}
.sitebar .dim {{ color: var(--slate); }}
.sitebar .right a {{ color: var(--terra-deep); margin-left: 1.1rem; }}

/* the sheet */
.sheet {{ max-width: 60rem; margin: 4.4rem auto 4rem; background: var(--elev);
  border: 1px solid var(--hair); padding: 4.5rem clamp(1.25rem, 8vw, 6.5rem) 5rem; }}

/* title page */
.front {{ text-align: center; margin-bottom: 3.2rem; }}
.front .eyebrow {{ font: 500 .68rem/1 ui-monospace, Menlo, monospace;
  letter-spacing: .16em; text-transform: uppercase; color: var(--slate); }}
h1.paper-title {{ font: 600 clamp(1.5rem, 3.4vw, 2.1rem)/1.28 'IBM Plex Sans',
  system-ui, sans-serif; letter-spacing: -.015em; margin: 1.1rem auto .9rem;
  max-width: 34ch; }}
.byline {{ font-size: 1.02rem; margin: 0 0 .35rem; }}
.byline .orcid {{ color: var(--slate); font-size: .85rem; }}
.artifact {{ font: 400 .74rem/1.9 ui-monospace, Menlo, monospace;
  color: var(--slate); }}
.artifact a {{ color: var(--terra-deep); text-decoration: none;
  border-bottom: 1px solid var(--terra); }}

/* abstract */
.abstract {{ max-width: 36rem; margin: 0 auto 3rem; }}
.abstract h2 {{ font: 600 .78rem/1 'IBM Plex Sans', system-ui, sans-serif;
  letter-spacing: .18em; text-transform: uppercase; text-align: center;
  color: var(--navy); margin: 0 0 .9rem; }}
.abstract p {{ font-size: .95rem; line-height: 1.65; text-align: justify;
  hyphens: auto; margin: 0 0 .8em; }}
.rule {{ border: 0; border-top: 1px solid var(--navy); margin: 0 0 2.6rem; }}

/* body typography */
.paper p {{ text-align: justify; hyphens: auto; }}
h1,h2,h3,h4 {{ font-family: 'IBM Plex Sans', system-ui, sans-serif;
  line-height: 1.25; letter-spacing: -.01em; }}
.paper > h1, .paper section > h1 {{ font-size: 1.32rem; margin-top: 2.8em; }}
.paper h2 {{ font-size: 1.12rem; margin-top: 2.2em; }}
.paper h3 {{ font-size: 1rem; margin-top: 1.8em; }}
.paper .header-section-number {{ color: var(--slate); margin-right: .6em; }}
a {{ color: var(--terra-deep); }}

figure {{ counter-increment: fig; margin: 2.2rem 0; padding: 1.1rem;
  background: var(--cream); border: 1px solid var(--hair); overflow-x: auto; }}
figure img {{ display: block; max-width: 100%; height: auto; margin: 0 auto; }}
figcaption {{ font: 400 .82rem/1.6 'IBM Plex Sans', system-ui, sans-serif;
  color: var(--slate); margin-top: .85rem; text-align: left; }}
figcaption::before {{ content: "Figure " counter(fig) ". ";
  font-weight: 600; color: var(--navy); }}
.paper {{ counter-reset: fig tbl; }}
table {{ counter-increment: tbl; border-collapse: collapse; font-size: .84rem;
  margin: 1.8rem 0; font-family: 'IBM Plex Sans', system-ui, sans-serif;
  display: block; overflow-x: auto; }}
table caption {{ font-size: .82rem; color: var(--slate); text-align: left;
  margin-bottom: .5rem; }}
table caption::before {{ content: "Table " counter(tbl) ". ";
  font-weight: 600; color: var(--navy); }}
th, td {{ border: 1px solid var(--hair); padding: .45rem .6rem;
  text-align: left; vertical-align: top; }}
th {{ background: var(--cream-deep); }}
code, pre {{ font-family: ui-monospace, Menlo, monospace; font-size: .85em; }}
pre {{ background: var(--cream-deep); border: 1px solid var(--hair);
  padding: .9rem 1rem; overflow-x: auto; }}
blockquote {{ margin: 1.5rem 0; padding-left: 1.1rem;
  border-left: 2px solid var(--terra); }}
#refs > div {{ margin-bottom: .75rem; font-size: .92rem; }}
math {{ font-size: 1.02em; }}
.endnote {{ margin-top: 4rem; border-top: 1px solid var(--navy);
  padding-top: 1rem; font: 400 .78rem/1.7 ui-monospace, Menlo, monospace;
  color: var(--slate); }}

@media print {{
  .sitebar {{ display: none; }}
  .sheet {{ border: 0; margin: 0; padding: 0; background: white; }}
  html {{ background: white; }}
}}
</style>
</head>
<body>
<nav class="sitebar"><div class="sitebar__in">
<span><a href="/">Anivar A Aravind</a> <span class="dim">·</span> <a href="/corrigibility/">Corrigibility</a> <span class="dim">· HTML edition</span></span>
<span class="right"><a href="/corrigibility/glossary/">Glossary</a><a href="https://doi.org/{doi}">DOI</a><a href="{ssrn}">SSRN</a><a href="{pdf}">PDF</a></span>
</div></nav>
<main class="sheet">
<header class="front">
<p class="eyebrow">Preprint · CC0 1.0 · no permission needed to reuse, translate, or adapt</p>
<h1 class="paper-title">{title}</h1>
<p class="byline">Anivar A Aravind <span class="orcid">· ORCID 0009-0009-8995-0005</span></p>
<p class="artifact">doi <a href="https://doi.org/{doi}">{doi}</a></p>
</header>
<section class="abstract">
<h2>Abstract</h2>
{abstract}
</section>
<hr class="rule" />
<div class="paper">
{body}
</div>
<div class="endnote">Terminology is defined in the <a href="/corrigibility/glossary/">shared glossary</a>, the appendix both documents carry. The PDF of record is at the DOI above; this HTML edition is built from the same LaTeX source. CC0 1.0.</div>
</main>
</body>
</html>
"""


def verify(html: str, n_figs: int, paper: str) -> None:
    errs = []
    hits = LIGATURE_RE.findall(html)
    if hits:
        errs.append(f"ligature corruption: {sorted(set(hits))[:5]}")
    if 'id="refs"' not in html:
        errs.append("no bibliography section")
    if ">??<" in html:
        errs.append("unresolved cross-reference (??)")
    got = html.count("<figure")
    if html.count('<img src="fig-') != n_figs:
        errs.append(f"substituted figures {html.count('<img src=\"fig-')} != compiled {n_figs}")
    if errs:
        raise SystemExit(f"{paper}: VERIFY FAILED — " + "; ".join(errs))
    print(f"{paper}: verify ok — {n_figs} figures, {got} figure envs, refs present, no corruption")


def build(paper: str, outbase: Path) -> None:
    meta = META[paper]
    tex = meta["src"].read_text()
    outdir = outbase / paper
    outdir.mkdir(parents=True, exist_ok=True)

    context = preamble_context(tex)
    figures = extract_figures(tex)
    print(f"{paper}: {len(figures)} tikz figures: {sorted(figures)}")
    for label, code in figures.items():
        compile_svg(label, code, context, outdir)

    abstract = pandoc_abstract(meta["src"])
    body = pandoc_body(meta["src"])
    # LaTeX numbers to subsubsection depth; pandoc numbers \paragraph too
    # (x.y.z.w, and 0.-prefixed for pre-section paragraphs). Strip those.
    body = re.sub(
        r'<span\s+class="header-section-number">(?:0\.[0-9.]+|[0-9]+(?:\.[0-9]+){3,})</span>\s*',
        "", body,
    )

    seen = set(re.findall(r'<figure[^>]*id="(fig:[^"]+)"', body))
    missing_svg = seen - set(figures)
    missing_ph = set(figures) - seen
    if missing_svg:
        raise SystemExit(f"{paper}: placeholders without compiled figures: {sorted(missing_svg)}")
    if missing_ph:
        raise SystemExit(f"{paper}: compiled figures without placeholders: {sorted(missing_ph)}")
    body = re.sub(
        r'(<figure[^>]*id="(fig:[^"]+)"[^>]*>)',
        lambda m: m.group(1)
        + f'<img src="{m.group(2).replace("fig:", "fig-").replace(":", "-")}.svg" alt="" loading="lazy" />',
        body,
    )

    html = PAGE.format(body=body, abstract=abstract, slug=paper, **meta)
    (outdir / "index.html").write_text(html)
    md = MD_HEAD.format(slug=paper, **meta) + pandoc_markdown(meta["src"], paper)
    (outbase / f"{paper}.md").write_text(md)
    verify(html, len(figures), paper)
    print(f"{paper}: wrote {outdir}/index.html ({len(html)//1024} KB) + {len(figures)} svg")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("paper", choices=["dpi", "epi", "all"])
    ap.add_argument("--out", default=str(ROOT.parent / "anivar.net/public/papers"))
    a = ap.parse_args()
    outbase = Path(a.out)
    for p in ["dpi", "epi"] if a.paper == "all" else [a.paper]:
        build(p, outbase)


if __name__ == "__main__":
    main()
