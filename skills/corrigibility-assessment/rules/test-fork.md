# test-fork

**Priority**: CRITICAL
**Category**: Test Application

## Rule

FORK tests whether the community can reproduce the system if governance fails.

## DPI Assessment

```yaml
questions:
  - Is forking legally permitted?
  - Are all technical artifacts available?
  - Is user data portable?
  - Has anyone successfully forked it?

evidence_required:
  - License terms
  - Source code availability
  - Data export mechanisms
  - Fork examples (if any)

scoring:
  1.0: Legal right + artifacts + data portability + demonstrated fork
  0.8: Legal right + artifacts + data portability
  0.5: Legal right + artifacts but data locked
  0.3: License permits but artifacts incomplete
  0.0: Forking prohibited or technically impossible
```

## EPI Assessment - Compute Capture

For learned systems, FORK has additional dimension:

```yaml
fork_types:
  inference_forkability:
    definition: Can run the model
    requires: Weights available
    sufficient_for_fork: NO

  training_forkability:
    definition: Can reproduce from scratch
    requires: Weights + Data + Training code + Accessible compute
    sufficient_for_fork: YES

compute_capture_test:
  formula: C_train <= κ × C_accessible
  variables:
    C_train: Compute cost to retrain
    C_accessible: Compute available to non-operators
    κ: Accessibility multiplier (typically 1-2)

  interpretation:
    passes: Community can retrain if needed
    fails: "Open weights" is performative transparency
```

## Compute Capture Definition

**Compute Capture** occurs when:
- Training cost exceeds community compute capacity
- "Open weights" provides inference but not correction
- Legal permission meaningless without physical capacity

## Fork Barrier Levels

| Layer | Cost | Barrier |
|-------|------|---------|
| Inference code | Minimal | None |
| Running open weights | Low | Minor |
| Fine-tuning | Moderate | Economic |
| Retraining from scratch | Very high | Structural |

## Training Forkability Evidence

```yaml
required_artifacts:
  - inference_code: Required
  - model_weights: Required
  - training_data_manifest: Required
  - training_code: Required
  - compute_cost_estimate: Required
  - successful_reproduction: Decisive (if exists)

fork_determination:
  passes_if:
    - All required artifacts available
    - Compute cost demonstrates feasibility
    - Third-party reproduction exists OR reproduction possible in principle
```

## Common Examples

| System | FORK Score | Type | Reason |
|--------|------------|------|--------|
| Linux | 1.0 | DPI | GPL + full artifacts + many forks |
| Aadhaar | 0.0 | DPI | Proprietary + no data portability |
| Llama 3 | 0.5 | EPI | Inference only, training data closed |
| OLMo | 1.0 | EPI | Full training forkability demonstrated |
| GPT-4 | 0.0 | EPI | Closed weights, compute capture |

## Schema Field (EPI)

```json
{
  "tests": {
    "FORK": {
      "score": 0.5,
      "legal_right_to_fork": true,
      "weights_available": true,
      "training_data_available": false,
      "compute_accessible": false,
      "compute_capture_risk": "high",
      "practical_fork_feasible": false,
      "notes": "Inference forkability only. Training cost ~$100M exceeds community capacity."
    }
  }
}
```
