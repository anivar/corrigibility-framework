---
name: schema-evaluator
description: >
  Validate and evaluate published corrigibility schemas.
  Checks infrastructure.json against schema spec.
  Verifies corrigibility.json scores and calculations.
  Detects inconsistencies between operator claims and auditor findings.
  Triggers on: "validate schema", "evaluate corrigibility", "check assessment",
  "verify infrastructure manifest", "audit the audit".
license: CC0-1.0
user-invocable: true
agentic: true
metadata:
  author: Anivar A Aravind
  author_url: https://anivar.net
  orcid: 0009-0009-8995-0005
  version: 1.0.0
  schema_versions: ["1.5", "1.6", "1.7"]
  current_schema: "1.7"
  tags: corrigibility, validation, evaluation, schema, audit
---

# Schema Evaluator

Validate and evaluate published corrigibility schemas.

## Inputs Required

| Input | Required | Description |
|-------|----------|-------------|
| infrastructure_json | Yes | URL or path to infrastructure.json |
| corrigibility_json | Optional | URL or path to corrigibility.json |
| schema_version | Optional | Version to validate against (default: 1.7) |

## Evaluation Modes

### Mode 1: Schema Validation

Validates JSON structure against schema specification.

```
Input: infrastructure.json OR corrigibility.json
Output:
  - valid: true/false
  - errors: list of schema violations
  - warnings: list of recommended fields missing
```

### Mode 2: Score Verification

Verifies corrigibility.json calculations are correct.

```
Input: corrigibility.json
Checks:
  - Composite score = geometric mean of five tests
  - Grade matches score range
  - Any zero score → automatic F
  - All scores in valid range [0.0, 1.0]
```

### Mode 3: Consistency Check

Compares operator claims against auditor findings.

```
Input: infrastructure.json + corrigibility.json
Detects:
  - Operator claims source_available=true but CODE score=0
  - Operator claims user_representation=true but GOVERN score=0
  - Contradictions between manifest and assessment
```

### Mode 4: Cross-System Comparison

Compares multiple systems against benchmarks.

```
Input: List of corrigibility.json URLs
Output:
  - Ranked comparison table
  - Per-test breakdown
  - Common failure patterns
```

## Validation Rules

### infrastructure.json

```yaml
required_fields:
  - system_name
  - operator.name
  - operator.jurisdiction
  - layers (at least one)

dpi_required:
  - exit.mandatory
  - code.source_available
  - audit.independent_audit_permitted
  - govern.user_representation
  - fork.legal_right_to_fork

epi_required:
  - model_architecture.logic_layer
  - model_architecture.weights_layer
  - model_architecture.data_layer
  - model_architecture.representation_layer
  - deployment_context.domain
  - action_boundary.implemented
```

### corrigibility.json

```yaml
required_fields:
  - system_ref
  - assessment_date
  - assessor.organization
  - tests.EXIT.score
  - tests.CODE.score
  - tests.AUDIT.score
  - tests.GOVERN.score
  - tests.FORK.score
  - composite_score
  - corrigibility_grade

score_rules:
  - All scores: 0.0 <= score <= 1.0
  - composite_score = (EXIT * CODE * AUDIT * GOVERN * FORK)^0.2
  - grade:
      A: score >= 0.8
      B: score >= 0.6
      C: score >= 0.4
      D: score >= 0.2
      F: score < 0.2
  - any_zero_rule: if any test = 0 then grade = F
```

## Output Format

### Validation Report

```json
{
  "input_file": "infrastructure.json",
  "schema_version": "1.7",
  "validation": {
    "valid": false,
    "errors": [
      {"field": "operator.jurisdiction", "error": "required field missing"}
    ],
    "warnings": [
      {"field": "code.source_url", "warning": "recommended field missing"}
    ]
  },
  "timestamp": ""
}
```

### Score Verification Report

```json
{
  "input_file": "corrigibility.json",
  "verification": {
    "scores_valid": true,
    "composite_correct": true,
    "grade_correct": false,
    "issues": [
      {"field": "corrigibility_grade", "expected": "F", "found": "D", "reason": "EXIT score is 0, automatic F applies"}
    ]
  }
}
```

### Consistency Report

```json
{
  "infrastructure": "system-infrastructure.json",
  "assessment": "system-corrigibility.json",
  "consistency": {
    "consistent": false,
    "contradictions": [
      {
        "field": "code",
        "operator_claim": "source_available: true",
        "auditor_finding": "CODE score: 0.0",
        "explanation": "Operator claims source available but auditor found it inaccessible"
      }
    ]
  }
}
```

## Common Issues Detected

| Issue | Detection | Severity |
|-------|-----------|----------|
| Missing required field | Schema validation | Error |
| Invalid score range | Score check | Error |
| Wrong composite calculation | Math verification | Error |
| Grade doesn't match score | Grade check | Error |
| Zero score without F grade | Zero-rule check | Error |
| Claim/finding contradiction | Consistency check | Warning |
| Outdated schema version | Version check | Warning |

## References

- Creator skill: `skills/schema-creator/`
- DPI schemas: `schema/dpi/`
- EPI schemas: `schema/epi/`
- Test rules: `skills/corrigibility-assessment/rules/`
