# Corrigibility Framework

A structural framework for evaluating **Digital Public Infrastructure (DPI)** and **Epistemic Public Infrastructure (EPI)**.

**Corrigibility**: The structural capacity of those affected by a system to detect error, signal harm, and trigger correction—without incurring material loss or irreversible consequence.

## Downloads

[![Release](https://img.shields.io/github/v/release/anivar/corrigibility-framework)](https://github.com/anivar/corrigibility-framework/releases/latest)

| Paper | Focus | Download |
|-------|-------|----------|
| **Paper I: DPI** | Deterministic infrastructure (ledgers, registries, payment rails) | [PDF](https://github.com/anivar/corrigibility-framework/releases/latest/download/corrigibility-framework-dpi.pdf) |
| **Paper II: EPI** | Learned/agentic systems (AI, ML models) | [PDF](https://github.com/anivar/corrigibility-framework/releases/latest/download/corrigibility-framework-ai.pdf) |

## The Five Tests

| Test | Question | DPI Focus | EPI Focus |
|------|----------|-----------|-----------|
| **EXIT** | Can users refuse participation without penalty? | Non-digital alternative | Human fallback guaranteed |
| **CODE** | Is the system's execution observable? | Source code | LWD-R (Logic, Weights, Data, Representation) |
| **AUDIT** | Can independent parties verify behavior? | Transaction logs | Statistical bounds + drift monitoring |
| **GOVERN** | Do affected populations have binding authority? | RFC/charter process | Action boundary protocol |
| **FORK** | Can the system be replaced without permission? | Code + data portability | Compute accessibility |

**Fatal Failure Property**: Failure of any single test disqualifies a system from designation as public infrastructure.

## Schemas

Schemas and assessment skills are maintained in the [corrigibility-schema](https://github.com/anivar/corrigibility-schema) repository.

### DPI Schemas
- [infrastructure.json](https://github.com/anivar/corrigibility-schema/blob/main/schema/dpi/infrastructure.json) - Operator disclosure manifest
- [audit.json](https://github.com/anivar/corrigibility-schema/blob/main/schema/dpi/audit.json) - Five-test assessment

### EPI Schemas
- [infrastructure.json](https://github.com/anivar/corrigibility-schema/blob/main/schema/epi/infrastructure.json) - LWD-R transparency manifest
- [audit.json](https://github.com/anivar/corrigibility-schema/blob/main/schema/epi/audit.json) - Five-test + EPI metrics

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

## Assessment Skills

Machine-readable skills for evaluating infrastructure corrigibility are in the [corrigibility-schema](https://github.com/anivar/corrigibility-schema) repository.

| Skill | Purpose |
|-------|---------|
| [assess](https://github.com/anivar/corrigibility-schema/blob/main/skills/assess/SKILL.md) | Evaluate infrastructure against five corrigibility tests |
| [rules/](https://github.com/anivar/corrigibility-schema/tree/main/skills/assess/rules) | Test definitions: EXIT, CODE, AUDIT, GOVERN, FORK |

## Repository Structure

```
corrigibility-framework/          # This repo - Papers
├── paper/
│   ├── corrigibility-framework-dpi.tex
│   ├── corrigibility-framework-dpi.pdf
│   ├── corrigibility-framework-ai.tex
│   └── corrigibility-framework-ai.pdf
└── website/

corrigibility-schema/             # Separate repo - Schemas & Skills
├── schema/
│   ├── dpi/
│   │   ├── infrastructure.json
│   │   └── audit.json
│   └── epi/
│       ├── infrastructure.json
│       └── audit.json
├── skills/assess/
│   ├── SKILL.md
│   └── rules/
└── examples/
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
