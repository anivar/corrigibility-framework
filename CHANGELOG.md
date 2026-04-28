# Changelog

All notable changes to this project will be documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[SemVer](https://semver.org/spec/v2.0.0.html).

## [2.1.0] — 2026-04-28

### Changed
- Reorganized repository into `papers/{dpi,epi,shared}/` layout.
- Canonical sources renamed to `main.tex` / `main.pdf` under each paper directory.
- Shared figures and styles consolidated under `papers/shared/`.
- Added `justfile` with `dpi`, `epi`, `publish`, `clean` targets.
- Added root `.gitignore` covering LaTeX build artifacts.

### Removed
- Vendored `acmart.cls` and `IEEEtran.cls` (provided by the
  `texlive-publishers` package; install via `apt`).

### Archived (moved to `papers/_archive/`, not deleted)
- Abandoned wrappers: `corrigibility-framework{,-acm,-ieee,-full}.tex`
- Abandoned drafts: `corrigibility-framework-{dpi,ai}-full.tex`, `body-cs.tex`
- Unused modular sources: `paper/sections/` (no longer referenced by any build).

### Added
- Empty stubs `papers/shared/glossary.tex` and `papers/shared/refs.bib`
  to anchor the v3 revision (shared bibliography + glossary).

## [2.0.0] — earlier

- DPI / EPI split. v1.1 published to Zenodo
  ([10.5281/zenodo.18215327](https://doi.org/10.5281/zenodo.18215327)).
