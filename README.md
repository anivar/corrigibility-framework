# Corrigibility Framework

A structural framework for evaluating Digital Public Infrastructure (DPI).

**Corrigibility**: The structural capacity of those affected by a system to detect error, signal harm, and trigger correction—without incurring material loss or irreversible consequence.

## The Five Tests

| Test | Question |
|------|----------|
| **EXIT** | Can users refuse participation without penalty? |
| **CODE** | Is the system's execution observable? |
| **AUDIT** | Can independent parties verify behavior? |
| **GOVERN** | Do affected populations have binding authority? |
| **FORK** | Can the system be replaced without permission? |

**Fatal Failure Property**: Failure of any single test disqualifies a system from designation as public infrastructure.

## Quick Links

- [Website](https://indiastack.in/dpi/)
- [Schema: infrastructure.json](schema/infrastructure.json)
- [Schema: corrigibility.json](schema/corrigibility.json)

## Repository Structure

```
corrigibility-framework/
├── schema/                 # JSON schemas
│   ├── infrastructure.json # Operator manifest (facts)
│   ├── corrigibility.json  # Auditor assessment (verdicts)
│   └── examples/           # Example manifests and assessments
├── assessments/            # Community-contributed assessments
├── tools/                  # Validators and utilities
└── docs/                   # Methodology and guides
```

## Schemas

### Two-Manifest Architecture

The framework separates operator facts from auditor judgments:

1. **Infrastructure Manifest** (`infrastructure.json`)
   Published by system operators. Declares operational facts—deployment state, dependencies, access channels, governance model. Does not assert compliance or legitimacy.

2. **Corrigibility Assessment** (`corrigibility.json`)
   Authored by auditors, not operators. Evaluates structural correction capacity against the five tests. Contains pass/fail judgments with evidence.

**Principle**: Operators declare facts; auditors render verdicts.

## Example Assessments

| System | Tests Passed | Assessment |
|--------|--------------|------------|
| Aadhaar | 0/5 | [assessment](schema/examples/aadhaar-assessment.json) |
| Linux Kernel | 5/5 | *coming soon* |
| Let's Encrypt | 5/5 | *coming soon* |
| Wikipedia | 5/5 | *coming soon* |

## Contributing

Contributions welcome:

- **Assessments**: Evaluate a system against the five tests
- **Schema improvements**: Propose additions via issues
- **Tools**: Validators, diff tools, dashboards
- **Translations**: Documentation in other languages

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Citation

```bibtex
@misc{corrigibility-framework,
  author = {Aravind, Anivar A},
  title = {Corrigibility Framework},
  year = {2026},
  url = {https://indiastack.in/dpi/}
}
```

## License

[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (Public Domain)

## Author

**Anivar A Aravind**
[anivar.net](https://anivar.net) · [ORCID](https://orcid.org/0009-0009-8995-0005)
