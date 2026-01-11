# Assessment Methodology

This document describes how to evaluate a system against the five corrigibility tests.

## Overview

The framework evaluates **structural capacity**, not intent or performance. The question is not whether a system is good, but whether it can be corrected by those it affects.

## The Five Tests

### EXIT: Safe Refusal

**Question**: Can a person decline participation while retaining access to essential services?

**Pass criteria:**
- Refusal carries no penalty
- Non-digital or alternative pathways remain available
- Alternative provides equivalent service (not degraded)

**Fail indicators:**
- Opting out results in exclusion from essential services
- Alternative pathways exist but are significantly slower/costlier
- System is de facto mandatory for government services

**Evidence to gather:**
- List of services requiring the system
- Documentation of alternative channels
- Time/cost comparison (digital vs. alternative)

### CODE: Legible Execution

**Question**: Is the system's actual execution observable in practice?

**Pass criteria:**
- Source code is publicly available
- Build process is reproducible
- Execution logic is inspectable

**Fail indicators:**
- Only API documentation or specifications are public
- Executing code is proprietary
- Key components are closed (e.g., biometric matching algorithms)

**For learned systems (AI):**
- Training data composition documented
- Model architecture and hyperparameters disclosed
- RLHF/preference optimization process documented

**Evidence to gather:**
- Repository links
- License information
- List of closed components

### AUDIT: Independent Verification

**Question**: Can independent parties verify system behavior without operator permission?

**Pass criteria:**
- External auditors can measure error rates, bias, failure modes
- Results can be published without legal restriction
- No permission required from operator

**Fail indicators:**
- Security audits prohibited
- RTI/FOIA requests denied
- Published statistics are operator-asserted only

**Evidence to gather:**
- Published audit reports (independent vs. internal)
- RTI/FOIA responses
- Legal restrictions on research

### GOVERN: Constitutive Input

**Question**: Do affected populations have binding authority in system design and evolution?

**Pass criteria:**
- Governance includes structured participation by those affected
- Rule-making process is documented and open
- Decisions are contestable

**Fail indicators:**
- Decisions made internally by operator
- Consultation is advisory or post hoc
- No public participation in rule-making

**Evidence to gather:**
- Governance structure documentation
- Public participation mechanisms
- History of rule changes and public input

### FORK: Credible Replacement

**Question**: Can the system be replicated or replaced without incumbent permission?

**Pass criteria:**
- Alternative implementations are legally feasible
- Alternative implementations are technically feasible
- Alternative implementations are economically feasible

**Fail indicators:**
- Legal monopoly (statutory, regulatory)
- Technical barriers (proprietary dependencies)
- Economic barriers (network effects, capital requirements)

**Evidence to gather:**
- Legal/regulatory status
- Licensing terms
- Existence of alternatives

## Verdict

A system is **corrigible** if and only if it passes all five tests.

Partial compliance does not satisfy the threshold. A system that passes four tests but fails one remains structurally incorrigible.

## Reporting

Use the `corrigibility.json` schema to structure assessments:

```json
{
  "target": "system-identifier",
  "assessed_by": "Your Name/Organization",
  "assessed_at": "2026-01-11",
  "methodology": "https://link-to-methodology",
  "tests": {
    "exit": { "pass": false, "evidence": "..." },
    "code": { "pass": false, "evidence": "..." },
    "audit": { "pass": false, "evidence": "..." },
    "govern": { "pass": false, "evidence": "..." },
    "fork": { "pass": false, "evidence": "..." }
  },
  "verdict": {
    "corrigible": false,
    "tests_passed": 0,
    "summary": "..."
  }
}
```

## Multiple Assessments

Different auditors may reach different conclusions based on:
- Different evidence sources
- Different interpretations of "pass" threshold
- Different assessment dates (systems change)

The framework is designed to surface disagreement, not suppress it. Multiple assessments of the same system may coexist.
