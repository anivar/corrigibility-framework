# test-audit

**Priority**: CRITICAL
**Category**: Test Application

## Rule

AUDIT tests whether independent parties can verify system behavior without operator permission.

## Core Principle

```
AUDIT ≠ "everyone audits"
AUDIT = "no one can prevent auditing"
```

The test is about **structural possibility**, not universal participation.

## Assessment Criteria

```yaml
questions:
  - Can independent parties audit WITHOUT operator authorization?
  - Are audit reports publicly available?
  - Is real-time monitoring possible?
  - Can auditors measure actual error rates?

evidence_required:
  - Audit access policies
  - Published audit reports
  - Monitoring interfaces/APIs
  - Historical audit findings

scoring:
  1.0: Unrestricted independent audit + public reports + real-time access
  0.7: Independent audit permitted + public reports
  0.5: Audit permitted but reports restricted
  0.3: Audit requires notification but not permission
  0.0: Audit blocked OR requires operator authorization
```

## DPI-Specific Criteria

```yaml
dpi_audit_requirements:
  transaction_verification:
    question: Can auditors verify individual transactions?
    example_pass: Bitcoin (any node can verify)
    example_fail: UPI (requires NPCI authorization)

  error_rate_measurement:
    question: Can auditors measure system failure rates?
    example_pass: Let's Encrypt CT logs
    example_fail: Aadhaar (failure data not public)

  dispute_tracking:
    question: Can auditors track dispute resolution?
    example_pass: Court records (public)
    example_fail: Internal grievance systems (opaque)
```

## EPI-Specific Criteria

```yaml
epi_audit_requirements:
  statistical_bounds:
    question: Can auditors establish performance bounds?
    evidence: Benchmark results, confidence intervals

  bias_testing:
    question: Can auditors test for demographic bias?
    evidence: Red team access, adversarial testing results

  variety_drift_monitoring:
    question: Can auditors measure model drift over time?
    evidence: Continuous monitoring data, drift metrics

  representation_audit:
    question: Can auditors inspect categorical boundaries?
    evidence: Embedding analysis access, category documentation
```

## Audit Theatre (Common Failure Pattern)

Systems that permit nominal inspection while preventing real verification:

| Theatre Type | Appearance | Reality |
|--------------|------------|---------|
| Sanitized logs | Read access granted | Logs are filtered/redacted |
| Scheduled audits | Audits permitted | Only at pre-announced times |
| Component access | Technical access | Access to non-critical components |
| Compliance badges | Certifications displayed | Certifications don't test real behavior |

**Detection**: If auditor cannot detect errors operator wants hidden → AUDIT fails.

## The Journalism Analogy

Not everyone investigates corruption. Democracy depends on the *possibility* of investigation.

- Passing AUDIT: Anyone *can* audit (whether they do or not)
- Failing AUDIT: Operator can *prevent* auditing

## Common Examples

| System | AUDIT Score | Reason |
|--------|-------------|--------|
| Bitcoin | 1.0 | Any node verifies all transactions |
| Let's Encrypt | 1.0 | Certificate Transparency logs public |
| Linux | 1.0 | Code review by anyone, bug trackers public |
| Aadhaar | 0.0 | UIDAI controls all audit access |
| UPI | 0.2 | RBI audits permitted, independent blocked |
| Llama 3 | 0.5 | Weights auditable, training process opaque |

## Schema Field (DPI)

```json
{
  "tests": {
    "AUDIT": {
      "score": 0.0,
      "independent_audit_permitted": false,
      "audit_reports_public": false,
      "real_time_monitoring_available": false,
      "notes": "All audit access requires UIDAI authorization. No independent error rate data available."
    }
  }
}
```

## Schema Field (EPI)

```json
{
  "tests": {
    "AUDIT": {
      "score": 0.5,
      "independent_audit_permitted": true,
      "red_team_access_granted": false,
      "audit_reports_public": true,
      "continuous_monitoring_available": false,
      "variety_drift_measured": false,
      "notes": "Weights can be tested but no access for adversarial probing or drift monitoring."
    }
  }
}
```

## Cybernetic Interpretation

AUDIT is the **sensor function** in the feedback loop:

- Detects deviation between intended and actual behavior
- Without AUDIT, errors accumulate undetected
- Corrupted AUDIT (audit theatre) = sensor attack
