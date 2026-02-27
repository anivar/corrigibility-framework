---
name: schema-creator
description: >
  Create corrigibility framework schemas for DPI or EPI systems.
  Operators create infrastructure.json manifests (claims).
  Auditors create corrigibility.json assessments (findings).
  Supports schema versions 1.5, 1.6, 1.7. Baseline: v1.7.
  Triggers on: "create infrastructure manifest", "create assessment",
  "generate corrigibility schema", "operator disclosure", "auditor report".
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
  tags: corrigibility, dpi, epi, schema, infrastructure, assessment
---

# Schema Creator

Create machine-readable corrigibility schemas for infrastructure systems.

## Inputs Required

### For Operators (infrastructure.json)

| Input | Required | Description |
|-------|----------|-------------|
| system_name | Yes | Official name of the system |
| operator_name | Yes | Organization operating the system |
| jurisdiction | Yes | Legal jurisdiction |
| system_type | Yes | DPI or EPI |
| layers | Yes | Architectural components (identity, payment, etc.) |
| documentation | Recommended | Links to policies, source code, licenses |

### For Auditors (corrigibility.json)

| Input | Required | Description |
|-------|----------|-------------|
| system_ref | Yes | Reference to infrastructure.json being assessed |
| assessor_org | Yes | Organization performing assessment |
| evidence | Yes | Documentation supporting each test score |
| methodology | Recommended | Assessment methodology used |

## User Roles

### Role: Operator

Creates `infrastructure.json` - declares operational facts about their system.

```
Operator declares:
- System architecture and layers
- Exit conditions (mandatory? penalties?)
- Code availability (source URL, license)
- Audit access (who can audit?)
- Governance structure (who decides?)
- Fork rights (license, artifacts, data portability)

Operator does NOT:
- Assess their own compliance
- Assign scores
- Make pass/fail determinations
```

### Role: Auditor

Creates `corrigibility.json` - evaluates system against five tests.

```
Auditor determines:
- Score for each test (0.0 to 1.0)
- Evidence supporting each score
- Composite score (geometric mean)
- Pass/fail determination

Auditor requires:
- Access to infrastructure.json
- Independent verification of claims
- Evidence documentation
```

## Workflow

```
Step 1: Identify role (Operator or Auditor)
Step 2: Classify system (DPI or EPI)
Step 3: Gather required inputs
Step 4: Generate schema following templates
Step 5: Validate against JSON schema
```

## Output Templates

### DPI Infrastructure (Operator)

```json
{
  "$schema": "schema/dpi/infrastructure.json",
  "system_name": "",
  "operator": {
    "name": "",
    "jurisdiction": "",
    "contact": ""
  },
  "layers": [
    {"name": "", "type": "identity|credential|payment|data_exchange|registry"}
  ],
  "exit": {
    "mandatory": false,
    "offline_equivalent": true,
    "penalty_for_refusal": {"exists": false, "severity": "none"}
  },
  "code": {
    "source_available": true,
    "source_url": "",
    "license": "",
    "build_reproducible": true
  },
  "audit": {
    "independent_audit_permitted": true,
    "audit_reports_public": true
  },
  "govern": {
    "governance_body": "",
    "user_representation": true,
    "binding_constraints": true
  },
  "fork": {
    "legal_right_to_fork": true,
    "technical_artifacts_available": true,
    "data_portability": true
  },
  "metadata": {
    "schema_version": "1.7",
    "last_updated": ""
  }
}
```

### EPI Infrastructure (Operator)

```json
{
  "$schema": "schema/epi/infrastructure.json",
  "system_name": "",
  "operator": {
    "name": "",
    "jurisdiction": "",
    "contact": ""
  },
  "model_architecture": {
    "logic_layer": {"architecture_documented": true, "architecture_url": ""},
    "weights_layer": {"weights_available": true, "weights_url": "", "license": ""},
    "data_layer": {"training_data_documented": true, "data_provenance_chain": true},
    "representation_layer": {"embedding_space_documented": true, "category_boundaries_inspectable": true}
  },
  "deployment_context": {
    "domain": "welfare_eligibility|judicial_risk|credit_scoring|...",
    "decision_authority": "advisory|dispositive|autonomous",
    "human_in_loop": true,
    "affected_population_size": 0
  },
  "action_boundary": {
    "implemented": true,
    "boundary_logic_public": true,
    "output_constrained_to_enum": true
  },
  "compute_requirements": {
    "inference_compute_tflops": 0,
    "training_compute_pflop_days": 0,
    "minimum_viable_hardware": ""
  },
  "metadata": {
    "schema_version": "1.7",
    "last_updated": ""
  }
}
```

### Corrigibility Assessment (Auditor)

```json
{
  "$schema": "schema/dpi/corrigibility.json",
  "system_ref": "",
  "assessment_date": "",
  "assessor": {
    "organization": "",
    "methodology": "Corrigibility Framework v1.7"
  },
  "tests": {
    "EXIT": {"score": 0.0, "notes": ""},
    "CODE": {"score": 0.0, "notes": ""},
    "AUDIT": {"score": 0.0, "notes": ""},
    "GOVERN": {"score": 0.0, "notes": ""},
    "FORK": {"score": 0.0, "notes": ""}
  },
  "composite_score": 0.0,
  "corrigibility_grade": "F",
  "metadata": {
    "schema_version": "1.7"
  }
}
```

## References

- DPI schemas: `schema/dpi/`
- EPI schemas: `schema/epi/`
- Evaluation skill: `skills/schema-evaluator/`
