# Corrigibility Framework

[![Release](https://img.shields.io/github/v/release/anivar/corrigibility-framework)](https://github.com/anivar/corrigibility-framework/releases/latest)
[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0009--8995--0005-green.svg)](https://orcid.org/0009-0009-8995-0005)

A structural framework for evaluating **Digital Public Infrastructure (DPI)** and **Epistemic Public Infrastructure (EPI)**.

**Corrigibility**: The structural capacity of those affected by a system to detect error, signal harm, and trigger correction—without incurring material loss or irreversible consequence.

## Downloads

| Paper | Focus | Source | Latest PDF |
|-------|-------|--------|------------|
| **Paper I: DPI** | Deterministic infrastructure (ledgers, registries, payment rails) | [`papers/dpi/main.tex`](papers/dpi/main.tex) | [PDF](https://github.com/anivar/corrigibility-framework/releases/latest/download/corrigibility-framework-dpi.pdf) |
| **Paper II: EPI** | Learned/agentic systems (AI, ML models) | [`papers/epi/main.tex`](papers/epi/main.tex) | [PDF](https://github.com/anivar/corrigibility-framework/releases/latest/download/corrigibility-framework-ai.pdf) |

## Build

Requires TeX Live (`texlive-latex-extra`, `texlive-science`, `texlive-publishers`),
`latexmk`, and `biber`. Then:

```bash
just         # build both papers
just dpi     # DPI only
just epi     # EPI only
just publish # stage release artifacts under dist/
```

## The Five Tests

| Test | Question | DPI Focus | EPI Focus |
|------|----------|-----------|-----------|
| **EXIT** | Can users refuse participation without penalty? | Non-digital alternative | Human fallback guaranteed |
| **CODE** | Is the system's execution observable? | Source code | LWD-R (Logic, Weights, Data, Representation) |
| **AUDIT** | Can independent parties verify behavior? | Transaction logs | Statistical bounds + drift monitoring |
| **GOVERN** | Do affected populations have binding authority? | RFC/charter process | Action boundary protocol |
| **FORK** | Can the system be replaced without permission? | Code + data portability | Compute accessibility |

**Fatal Failure Property**: Failure of any single test disqualifies a system from designation as public infrastructure.

## Schemas & Skills

See [corrigibility-schema](https://github.com/anivar/corrigibility-schema) repository for:

- **Schemas**: `infrastructure.json` and `audit.json` for DPI/EPI
- **Assessment Skills**: `skills/assess/` with test rules (EXIT, CODE, AUDIT, GOVERN, FORK)
- **Examples**: Reference implementations

## Key Concepts

### DPI (Paper I)
- **Functional Exit Equivalence (FEE)**: Architectural guarantees that recreate error-signal strength when literal exit is impossible
- **Rule of the Ledger**: When authority is exerted through synchronized, self-executing artifacts

### EPI (Paper II)
- **LWD-R**: Four-layer transparency (Logic, Weights, Data, Representation)
- **Action Boundary Protocol**: Deterministic envelope around stochastic inference
- **Variety Drift**: The growing gap between frozen model variety and evolving environmental variety
- **Compute Capture**: When "open weights" fails FORK due to prohibitive retraining costs

## Citation

```bibtex
@article{aravind2026corrigibility-dpi,
  author = {Aravind, Anivar A},
  title = {Corrigibility as a Structural Precondition for Digital Public Infrastructure},
  year = {2026}
}

@article{aravind2026corrigibility-epi,
  author = {Aravind, Anivar A},
  title = {Epistemic Capture and the Action Boundary},
  year = {2026}
}
```

## License

[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (Public Domain)

## Author

**Anivar A Aravind** · [ORCID: 0009-0009-8995-0005](https://orcid.org/0009-0009-8995-0005)
