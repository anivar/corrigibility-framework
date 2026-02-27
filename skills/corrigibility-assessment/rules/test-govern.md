# test-govern

**Priority**: CRITICAL
**Category**: Test Application

## Rule

GOVERN tests whether affected populations have binding authority over the system—not advisory input, but enforceable constraint.

## Core Distinction

```
Advisory governance: Operator MAY consider feedback
Binding governance: Operator MUST comply with decisions

Only binding governance passes GOVERN.
```

## Assessment Criteria

```yaml
questions:
  - Does a governance body exist?
  - Do affected users/subjects have representation?
  - Are governance decisions legally binding on operators?
  - Is there an amendment process?
  - Can governance override operator decisions?

evidence_required:
  - Governance charter or bylaws
  - Membership/representation structure
  - Legal enforcement mechanism
  - Decision history showing binding effect
  - Amendment procedures

scoring:
  1.0: Multi-stakeholder + binding + demonstrated enforcement
  0.7: Multi-stakeholder + binding but untested
  0.5: Governance exists but advisory only
  0.3: User feedback mechanisms but no authority
  0.0: No user representation OR governance non-binding
```

## Binding vs Advisory

| Indicator | Advisory | Binding |
|-----------|----------|---------|
| Language | "should", "may consider" | "shall", "must" |
| Enforcement | None | Legal/contractual |
| Override | Operator can ignore | Operator must comply |
| Recourse | Complaint | Lawsuit/injunction |

## DPI-Specific Criteria

```yaml
dpi_governance:
  questions:
    - Who controls protocol changes?
    - Can users block harmful updates?
    - Is there judicial review of operator decisions?

  governance_models:
    captured:
      description: Operator controls governance
      example: UIDAI (executive authority, no oversight)
      score: 0.0

    advisory:
      description: User input without authority
      example: Most "community feedback" programs
      score: 0.3

    multi_stakeholder:
      description: Shared control, binding decisions
      example: IETF, W3C standards bodies
      score: 0.8

    user_sovereign:
      description: Users have veto power
      example: Open source with fork rights
      score: 1.0
```

## EPI-Specific Criteria

```yaml
epi_governance:
  additional_questions:
    - Who controls training objectives?
    - Can affected parties contest model categories?
    - Is there governance over value tradeoffs?
    - Can users trigger retraining?

  ontology_governance:
    question: Can affected subjects challenge categorical definitions?
    why_critical: Model categories become administrative facts
    example_fail: Vendor defines "high-risk" with no appeal
    example_pass: Category definitions subject to public comment

  gdos_mitigation:
    question: Is governance designed for agentic scale?
    why_critical: Human-speed governance fails under agent load
    required: Automated enforcement, not manual review
```

## The "Rule of Ledger" Problem

When authority flows through infrastructure rather than institutions:

```
Traditional: Law → Bureaucracy → Citizen (appealable)
DPI/EPI: Code → Execution → Citizen (fait accompli)
```

GOVERN requires that the infrastructure itself be subject to democratic constraint, not just the policies it implements.

## Common Failures

| System | GOVERN Score | Reason |
|--------|-------------|--------|
| Linux | 1.0 | Maintainer process + fork rights = binding |
| IETF | 0.9 | Rough consensus + running code |
| Wikipedia | 0.8 | Community governance, binding policies |
| Aadhaar | 0.0 | UIDAI is executive authority, no user representation |
| UPI | 0.2 | NPCI governed by banks, not users |
| OpenAI | 0.3 | Board exists but not user-representative |

## Democratic Authorization ≠ GOVERN

```yaml
critical_distinction:
  claim: "Democratically enacted law authorized this system"
  response: "Legislative mandate does not convert incorrigible systems into corrigible ones"

  analogy: "A democratically enacted prison is still a prison"

  what_govern_requires:
    - Ongoing user authority over operation
    - Not just initial authorization
    - Structural constraint, not political permission
```

## Schema Field (DPI)

```json
{
  "tests": {
    "GOVERN": {
      "score": 0.0,
      "governance_body_exists": true,
      "user_representation": false,
      "binding_constraints_on_operator": false,
      "amendment_process_defined": false,
      "notes": "UIDAI operates under executive authority. No parliamentary oversight. No user representation on governing body."
    }
  }
}
```

## Schema Field (EPI)

```json
{
  "tests": {
    "GOVERN": {
      "score": 0.3,
      "governance_body_exists": true,
      "affected_subject_representation": false,
      "category_contestation_process": false,
      "retraining_triggers_defined": false,
      "gdos_mitigation_implemented": false,
      "notes": "Ethics board exists but advisory only. No process for contesting model categories. No user representation."
    }
  }
}
```

## Cybernetic Interpretation

GOVERN is the **actuator function** in the feedback loop:

- Converts detected errors (AUDIT) into correction
- Without GOVERN, errors are detected but not fixed
- Advisory GOVERN = actuator with no authority
- The loop requires binding actuation to close
