# test-exit

**Priority**: CRITICAL
**Category**: Test Application

## Rule

EXIT tests whether affected subjects can refuse participation without material penalty.

## DPI Assessment

```yaml
questions:
  - Is enrollment mandatory by law?
  - Does a functional offline alternative exist?
  - What happens if someone refuses?

evidence_required:
  - Legal mandate documentation (if claimed mandatory)
  - Alternative service channels documentation
  - Penalty documentation or terms of service

scoring:
  1.0: Voluntary, no penalty, alternatives exist
  0.7: Voluntary, minor inconvenience for refusal
  0.5: Technically voluntary but strong economic pressure
  0.3: Mandatory but FEE (Functional Exit Equivalence) exists
  0.0: Mandatory + essential service denial + no FEE
```

## EPI Assessment (Additional)

```yaml
additional_questions:
  - Is human fallback guaranteed for AI decisions?
  - Can subjects appeal to human decision-maker?
  - Is there disclosure that AI is being used?

epi_scoring_modifier:
  human_fallback_missing: -0.3
  no_appeal_process: -0.2
  no_ai_disclosure: -0.1
```

## Penalty Severity Levels

| Level | Definition | Example |
|-------|------------|---------|
| none | No consequence | Optional loyalty program |
| inconvenience | Minor friction | Must visit office instead of online |
| economic | Financial impact | Higher fees, lost benefits |
| essential_service_denial | Survival impact | No banking, no food ration, no healthcare |

## FEE (Functional Exit Equivalence)

When literal exit is impossible for essential services, FEE provides architectural guarantees:

1. **Federated providers**: Multiple independent operators
2. **Protocol-level portability**: Can switch without data loss
3. **Statutory fallback**: Legal guarantee of non-digital alternative

FEE satisfies EXIT only if error-signal strength equivalent to market exit.

## Common Failures

- Aadhaar: Mandatory for PDS, banking, SIM → EXIT = 0
- UPI: Voluntary but economic pressure → EXIT ≈ 0.5
- Let's Encrypt: Fully voluntary → EXIT = 1.0

## Schema Field

```json
{
  "tests": {
    "EXIT": {
      "score": 0.0,
      "mandatory_enrollment": true,
      "offline_alternative_exists": false,
      "penalty_severity": "essential_service_denial",
      "functional_exit_equivalence": false,
      "notes": "Required for food ration access"
    }
  }
}
```
