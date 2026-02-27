---
name: corrigibility-assessment
description: >
  Evaluate Digital Public Infrastructure (DPI) or Epistemic Public Infrastructure (EPI)
  against the five corrigibility tests: EXIT, CODE, AUDIT, GOVERN, FORK.
  Generates structured JSON assessments following framework schemas.
  Supports schema versions 1.5, 1.6, 1.7. Baseline: v1.7.
  Triggers on: "corrigibility", "DPI assessment", "EPI assessment",
  "infrastructure evaluation", "EXIT test", "FORK test", "governance audit".
license: CC0-1.0
user-invocable: true
agentic: true
compatibility: "Any system with documentation, APIs, or inspection access"
metadata:
  author: Anivar A Aravind
  author_url: https://anivar.net
  orcid: 0009-0009-8995-0005
  version: 1.0.0
  schema_versions: ["1.5", "1.6", "1.7"]
  current_schema: "1.7"
  tags: corrigibility, dpi, epi, governance, infrastructure, accountability, audit
---

# Corrigibility Assessment

This skill implements the Corrigibility Framework for evaluating public infrastructure. The five tests (EXIT, CODE, AUDIT, GOVERN, FORK) are structural requirements derived from cybernetics (Ashby's Law), commons governance (Ostrom), and free software (Stallman). Failure of ANY single test means the system is NOT corrigible.

## When to Use This Skill

| Need | Use This Skill |
|------|----------------|
| Evaluate DPI (ledgers, registries, payment rails) | Yes - use DPI schemas |
| Evaluate EPI (AI/ML systems, learned models) | Yes - use EPI schemas |
| Generate procurement compliance gates | Yes |
| Compare systems against benchmarks | Yes |
| General security audit | No - use security-specific tools |

## Schema Versions

| Version | Status | Changes |
|---------|--------|---------|
| 1.7 | **Current** | Added EPI schemas, LWD-R, Compute Capture |
| 1.6 | Supported | Added FEE (Functional Exit Equivalence) |
| 1.5 | Legacy | Original five-test framework |

## Rule Categories

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Test Application | CRITICAL | `test-` |
| 2 | Evidence Collection | CRITICAL | `evidence-` |
| 3 | Scoring | HIGH | `score-` |
| 4 | Schema Generation | HIGH | `schema-` |
| 5 | System Classification | MEDIUM | `classify-` |
| 6 | Version Migration | MEDIUM | `migrate-` |

## The Five Tests

### 1. EXIT (Reversibility)

```
Question: Can users refuse participation without penalty?

DPI: Voluntary enrollment OR functional offline alternative
EPI: Human fallback guaranteed for AI decisions

FAIL if: Mandatory + essential_service_denial + no FEE
```

### 2. CODE (Inspectability)

```
Question: Is the system's logic publicly inspectable?

DPI: Source code available, reproducible builds
EPI: LWD-R (Logic, Weights, Data, Representation)

FAIL if: Proprietary OR (EPI) any LWD-R layer hidden
```

### 3. AUDIT (Verification)

```
Question: Can independent parties verify system behavior?

Both: Independent audit permitted WITHOUT operator authorization

FAIL if: Audit requires operator permission
```

### 4. GOVERN (Constraint)

```
Question: Do affected populations have binding authority?

Both: User representation + legally binding decisions

FAIL if: No user representation OR governance non-binding
```

### 5. FORK (Reproduction)

```
Question: Can the system be reproduced without permission?

DPI: Legal right + artifacts + data portability
EPI: Training forkability (not just inference)

FAIL if: Forking prohibited OR (EPI) compute capture
```

## Composite Score

```
Score = (EXIT × CODE × AUDIT × GOVERN × FORK)^(1/5)
```

| Grade | Range | Meaning |
|-------|-------|---------|
| A | ≥ 0.8 | Structurally corrigible |
| B | ≥ 0.6 | Minor deficits |
| C | ≥ 0.4 | Significant deficits |
| D | ≥ 0.2 | Severe deficits |
| F | < 0.2 | Incorrigible |

**Any test = 0 → automatic F**

## Output Files

1. `infrastructure.json` - Operator manifest (claims)
2. `corrigibility.json` - Auditor assessment (findings)

## References

- Paper 1 (DPI): Deterministic infrastructure framework
- Paper 2 (EPI): Learned/agentic systems extensions
- Schemas: `schema/dpi/` and `schema/epi/`
- Skill spec: [agentskills.io](https://agentskills.io)
