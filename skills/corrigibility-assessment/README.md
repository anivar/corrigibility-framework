# Corrigibility Assessment Skill

Evaluate infrastructure systems against the five corrigibility tests: EXIT, CODE, AUDIT, GOVERN, FORK.

## Overview

This skill implements the Corrigibility Framework for assessing whether public infrastructure meets structural accountability requirements. Compatible with any AI agent platform supporting the [SKILL.md specification](https://agentskills.io).

## The Five Tests

| Test | Question |
|------|----------|
| **EXIT** | Can users refuse participation without penalty? |
| **CODE** | Is the system's logic publicly inspectable? |
| **AUDIT** | Can independent parties verify behavior? |
| **GOVERN** | Do affected populations have binding authority? |
| **FORK** | Can the system be reproduced without permission? |

**Fatal Failure Property**: Failure of ANY single test = system is NOT corrigible.

## Schemas

| Type | Schema |
|------|--------|
| DPI Infrastructure | `schema/dpi/infrastructure.json` |
| DPI Assessment | `schema/dpi/corrigibility.json` |
| EPI Infrastructure | `schema/epi/infrastructure.json` |
| EPI Assessment | `schema/epi/corrigibility.json` |

## Rules

| Rule | Description |
|------|-------------|
| `test-exit` | EXIT test application |
| `test-code` | CODE test + LWD-R for EPI |
| `test-fork` | FORK test + Compute Capture |
| `score-composite` | Geometric mean scoring |
| `classify-system` | DPI vs EPI classification |

## Framework Reference

- Paper 1 (DPI): Corrigibility as a Structural Precondition for Digital Public Infrastructure
- Paper 2 (EPI): Epistemic Capture and the Action Boundary
- GitHub: [github.com/anivar/corrigibility-framework](https://github.com/anivar/corrigibility-framework)

## License

CC0 1.0 (Public Domain)

## Author

Anivar A Aravind · [ORCID: 0009-0009-8995-0005](https://orcid.org/0009-0009-8995-0005)
