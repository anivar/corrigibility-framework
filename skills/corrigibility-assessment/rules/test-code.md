# test-code

**Priority**: CRITICAL
**Category**: Test Application

## Rule

CODE tests whether the system's governing logic is publicly inspectable.

## DPI Assessment

```yaml
questions:
  - Is source code publicly available?
  - What license governs the code?
  - Are builds reproducible?
  - Is the specification public?

evidence_required:
  - Source repository URL
  - License file
  - Build instructions
  - Specification documents

scoring:
  1.0: Open source + permissive license + reproducible builds
  0.7: Open source + copyleft license + reproducible
  0.5: Source available but restricted license
  0.3: Specification public but implementation closed
  0.0: Proprietary/closed source
```

## EPI Assessment - LWD-R

For learned systems, CODE requires four-layer transparency:

```yaml
lwdr_layers:
  L_logic:
    question: Is model architecture documented?
    weight: 0.25
    evidence: Architecture papers, model cards

  W_weights:
    question: Are trained parameters publicly available?
    weight: 0.25
    evidence: Weight files, download URLs

  D_data:
    question: Is training data documented with provenance?
    weight: 0.25
    evidence: Datasheets, data manifests

  R_representation:
    question: Are categorical schemas disclosed?
    weight: 0.25
    evidence: Embedding documentation, category definitions

epi_scoring:
  all_four: 1.0
  three_layers: 0.75
  two_layers: 0.5
  one_layer: 0.25
  none: 0.0
```

## The R Layer (Representation)

Most critical for EPI. When AI classifies citizens as "eligible" or "risky":

- These categories become administrative facts
- Hidden in latent space = Ontological Capture
- Must disclose: category definitions, boundary logic, justification

**Failure**: Publishing weights without R layer = open-washing.

## Common Failures

| System | CODE Score | Reason |
|--------|------------|--------|
| Aadhaar | 0.3 | Specs public, implementation closed |
| Llama 3 | 0.5 | L+W available, D+R missing |
| OLMo | 1.0 | Full LWD-R disclosure |
| Linux | 1.0 | GPL, reproducible, documented |

## Schema Field (DPI)

```json
{
  "tests": {
    "CODE": {
      "score": 0.3,
      "source_available": false,
      "license_permits_inspection": false,
      "build_reproducible": false,
      "specification_public": true,
      "notes": "UIDAI specifications public but core implementation proprietary"
    }
  }
}
```

## Schema Field (EPI)

```json
{
  "tests": {
    "CODE": {
      "score": 0.5,
      "logic_inspectable": true,
      "weights_inspectable": true,
      "data_inspectable": false,
      "representation_inspectable": false,
      "action_boundary_logic_public": true,
      "notes": "Weights available but training data and category schemas proprietary"
    }
  }
}
```
