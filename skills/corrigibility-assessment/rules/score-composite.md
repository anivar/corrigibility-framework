# score-composite

**Priority**: HIGH
**Category**: Scoring

## Rule

The composite corrigibility score uses geometric mean to ensure any single failure cascades to total failure.

## Formula

```
Composite = (EXIT × CODE × AUDIT × GOVERN × FORK)^(1/5)
```

## Why Geometric Mean?

1. **Fatal Failure Property**: Any score of 0 → composite = 0
2. **No Compensation**: High scores cannot compensate for failures
3. **Cybernetic Basis**: Feedback loop requires ALL components

## Grading Scale

| Grade | Score Range | Interpretation |
|-------|-------------|----------------|
| A | ≥ 0.80 | Structurally corrigible |
| B | 0.60 - 0.79 | Minor deficits, correctable |
| C | 0.40 - 0.59 | Significant deficits |
| D | 0.20 - 0.39 | Severe deficits |
| F | < 0.20 | Structurally incorrigible |

## Automatic F Conditions

Regardless of composite score, system receives **automatic F** if:

- Any single test = 0.0
- EXIT = 0 (coercive system)
- GOVERN = 0 AND FORK = 0 (no correction path)

## Example Calculations

### Linux Kernel
```
EXIT=1.0, CODE=1.0, AUDIT=1.0, GOVERN=1.0, FORK=1.0
Composite = (1×1×1×1×1)^0.2 = 1.0
Grade: A
```

### Aadhaar
```
EXIT=0.0, CODE=0.3, AUDIT=0.2, GOVERN=0.0, FORK=0.0
Composite = (0×0.3×0.2×0×0)^0.2 = 0.0
Grade: F (automatic - EXIT=0)
```

### Hypothetical "Almost Good" System
```
EXIT=0.9, CODE=0.9, AUDIT=0.9, GOVERN=0.9, FORK=0.0
Composite = (0.9×0.9×0.9×0.9×0)^0.2 = 0.0
Grade: F (automatic - FORK=0)
```

## Binary vs Continuous

The framework uses **binary legitimacy threshold** despite continuous scores:

- Scores are diagnostic (which tests need work)
- Grade is binary (corrigible or not)
- "Mostly corrigible" is structurally impossible

## Schema Field

```json
{
  "composite_score": 0.0,
  "corrigibility_grade": "F",
  "automatic_fail_reason": "EXIT score is 0.0 - mandatory enrollment with essential service denial",
  "determination": "FAIL - System does not meet corrigibility threshold for public infrastructure designation"
}
```

## Scoring Guidance

When in doubt:
- Round DOWN, not up
- Absence of evidence = 0, not "unknown"
- Claims without verification = 0
- Partial compliance = partial score, not pass
