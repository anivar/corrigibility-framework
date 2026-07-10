# Changelog

All notable changes to this project will be documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[SemVer](https://semver.org/spec/v2.0.0.html).

## [3.1.0] — 2026-07-10

### Added
- Q1–Q10 margin-evaluation upgrades across both papers: gradient
  quantifier (argmin/margin evaluation), intermediary-discretion AUDIT
  surface, collective-standing precondition, Bole Clause, Rule A.11
  auditor data duties, subject receipts + citizen-constraint registry,
  R-layer change control, governance-reproducible FORK standard,
  deliberative threshold calibration, four-mechanism political economy.
- Ambedkar primary sources cited at the debt points (Annihilation of
  Caste 1936; What Congress and Gandhi Have Done to the Untouchables
  1945; States and Minorities 1947). References only — the papers'
  three-tradition triangulation is unchanged.

### Fixed
- SSRN reference-parser compatibility: `refs.bib` howpublished/URL
  restructuring, Unicode author names, canonical SSRN DOIs for both
  papers; EPI SSRN DOI in `CITATION.cff`.
- Three unresolvable `\ref` targets (two cross-document references,
  one missing label); Bole Resolution date (1923, Bombay Presidency);
  Injunction Hook attribution.

## [3.0.0] — 2026-04-30

- v3 revision pass (P0–P3): structural revision, normative anchor,
  two-pronged binarity argument, strict interpretability firewall,
  citizen-side GOVERN mechanism families, scope and open problems.
  Full log in `CHANGES.md`. Both papers on SSRN
  (DPI 10.2139/ssrn.6059075; EPI 10.2139/ssrn.6669318).

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

- DPI / EPI split.
