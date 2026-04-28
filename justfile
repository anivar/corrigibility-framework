set shell := ["bash", "-c"]

# Default: build both papers
default: dpi epi

# Build the DPI paper
dpi:
    cd papers/dpi && TEXINPUTS=".:../shared/styles:../shared:" latexmk -pdf -interaction=nonstopmode main.tex

# Build the EPI paper
epi:
    cd papers/epi && TEXINPUTS=".:../shared/styles:../shared:" latexmk -pdf -interaction=nonstopmode main.tex

# Stage release artifacts under dist/ with public filenames
publish: default
    mkdir -p dist
    cp papers/dpi/main.pdf dist/corrigibility-framework-dpi.pdf
    cp papers/epi/main.pdf dist/corrigibility-framework-ai.pdf

# Remove all build artifacts
clean:
    cd papers/dpi && latexmk -C 2>/dev/null || true
    cd papers/epi && latexmk -C 2>/dev/null || true
    rm -rf dist
