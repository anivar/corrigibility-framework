# Corrigibility Framework

A structural framework for evaluating **Digital Public Infrastructure (DPI)** and **Epistemic Public Infrastructure (EPI)**.

**Corrigibility**: The structural capacity of those affected by a system to detect error, signal harm, and trigger correction—without incurring material loss or irreversible consequence.

## The Five Tests

| Test | Question | DPI Focus | EPI Focus |
|------|----------|-----------|-----------|
| **EXIT** | Can users refuse participation without penalty? | Non-digital alternative | Human fallback guaranteed |
| **CODE** | Is the system's execution observable? | Source code | LWD-R (Logic, Weights, Data, Representation) |
| **AUDIT** | Can independent parties verify behavior? | Transaction logs | Statistical bounds + drift monitoring |
| **GOVERN** | Do affected populations have binding authority? | RFC/charter process | Ontology governance |
| **FORK** | Can the system be replaced without permission? | Code + data portability | Compute accessibility |

**Fatal Failure Property**: Failure of any single test disqualifies a system from designation as public infrastructure.

## Two Papers

| Paper | Focus | Pages |
|-------|-------|-------|
| **Paper 1: DPI** | Deterministic infrastructure (ledgers, registries, payment rails) | 47 |
| **Paper 2: EPI** | Learned/agentic systems (AI, ML models) | 22 |

## Schemas

### DPI Schemas
- [infrastructure.json](schema/dpi/infrastructure.json) - Operator disclosure manifest
- [corrigibility.json](schema/dpi/corrigibility.json) - Five-test assessment

### EPI Schemas
- [infrastructure.json](schema/epi/infrastructure.json) - LWD-R transparency manifest
- [corrigibility.json](schema/epi/corrigibility.json) - Five-test + EPI metrics

## Key Concepts

### DPI (Paper 1)
- **Functional Exit Equivalence (FEE)**: Architectural guarantees that recreate error-signal strength when literal exit is impossible
- **Rule of the Ledger**: When authority is exerted through synchronized, self-executing artifacts
- **Sovereignty-Scale-Neutrality Tension**: Under centralized enforcement, maximizing sovereignty and scale compresses governance variety

### EPI (Paper 2)
- **LWD-R**: Four-layer transparency (Logic, Weights, Data, Representation)
- **Ontological Capture**: When a model's categories become non-contestable administrative facts
- **Variety Drift**: The growing gap between frozen model variety and evolving environmental variety
- **Compute Capture**: When "open weights" fails FORK due to prohibitive retraining costs
- **Action Boundary Protocol**: Deterministic envelope around stochastic inference
- **GDoS (Governance Denial of Service)**: Governance collapse under agentic scaling

## Repository Structure

```
corrigibility-framework/
├── paper/                  # LaTeX source and PDFs
│   ├── corrigibility-framework-dpi.tex
│   ├── corrigibility-framework-dpi.pdf
│   ├── corrigibility-framework-ai.tex
│   └── corrigibility-framework-ai.pdf
├── schema/
│   ├── dpi/                # DPI schemas
│   │   ├── infrastructure.json
│   │   └── corrigibility.json
│   └── epi/                # EPI schemas
│       ├── infrastructure.json
│       └── corrigibility.json
└── docs/                   # Additional documentation
```

## Citation

```bibtex
@article{aravind2026corrigibility-dpi,
  author = {Aravind, Anivar A},
  title = {Corrigibility as a Structural Precondition for Digital Public Infrastructure: A Cybernetic Framework},
  year = {2026}
}

@article{aravind2026corrigibility-epi,
  author = {Aravind, Anivar A},
  title = {Epistemic Capture and the Action Boundary: Corrigibility for Learned and Agentic Systems},
  year = {2026}
}
```

## License

[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (Public Domain)

## Author

**Anivar A Aravind**
[ORCID: 0009-0009-8995-0005](https://orcid.org/0009-0009-8995-0005)
