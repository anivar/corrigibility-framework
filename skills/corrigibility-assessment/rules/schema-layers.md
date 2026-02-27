# schema-layers

**Priority**: HIGH
**Category**: Schema Generation

## Rule

Infrastructure systems must be decomposed into architectural layers for granular assessment. Each layer may have different corrigibility properties.

## DPI Layer Types

```yaml
layer_types:
  identity:
    description: Systems that establish who someone is
    examples: Aadhaar, national ID, biometric databases
    typical_tests_affected: EXIT (mandatory enrollment), AUDIT (verification access)

  credential:
    description: Systems that prove attributes or permissions
    examples: Digital certificates, licenses, vaccination records
    typical_tests_affected: CODE (verification logic), FORK (portability)

  payment:
    description: Systems that transfer value
    examples: UPI, SWIFT, ACH, cryptocurrency rails
    typical_tests_affected: EXIT (account closure), AUDIT (transaction verification)

  data_exchange:
    description: Systems that share information between entities
    examples: Health information exchanges, credit bureaus
    typical_tests_affected: GOVERN (consent frameworks), FORK (data portability)

  registry:
    description: Systems that maintain authoritative records
    examples: Land registries, business registries, DNS
    typical_tests_affected: CODE (update logic), GOVERN (amendment process)
```

## Layer Decomposition Process

```yaml
step_1_identify:
  question: What distinct functional components exist?
  output: List of layer names

step_2_classify:
  question: What type is each layer?
  output: Layer type from enum

step_3_assess:
  question: Does each layer pass all five tests?
  output: Per-layer scores

step_4_aggregate:
  rule: System score = minimum across all layers
  rationale: Weakest layer determines system corrigibility
```

## Example: India Stack Decomposition

```json
{
  "system_name": "India Stack",
  "layers": [
    {
      "name": "Aadhaar",
      "type": "identity",
      "notes": "Biometric identity database"
    },
    {
      "name": "eKYC",
      "type": "credential",
      "notes": "Identity verification API"
    },
    {
      "name": "UPI",
      "type": "payment",
      "notes": "Unified Payments Interface"
    },
    {
      "name": "DigiLocker",
      "type": "data_exchange",
      "notes": "Document storage and sharing"
    },
    {
      "name": "GSTN",
      "type": "registry",
      "notes": "Goods and Services Tax Network"
    }
  ]
}
```

## Per-Layer Assessment

Each layer gets independent five-test evaluation:

| Layer | EXIT | CODE | AUDIT | GOVERN | FORK | Score |
|-------|------|------|-------|--------|------|-------|
| Aadhaar | 0.0 | 0.3 | 0.0 | 0.0 | 0.0 | 0.0 |
| eKYC | 0.3 | 0.3 | 0.2 | 0.0 | 0.0 | 0.0 |
| UPI | 0.5 | 0.4 | 0.2 | 0.2 | 0.3 | 0.0 |
| DigiLocker | 0.6 | 0.5 | 0.3 | 0.2 | 0.4 | 0.0 |

**System Score**: min(0.0, 0.0, 0.0, 0.0) = **0.0**

## EPI Layer Mapping

For EPI systems, layers map to LWD-R:

```yaml
epi_layers:
  logic:
    maps_to: "L" in LWD-R
    description: Model architecture and inference code

  weights:
    maps_to: "W" in LWD-R
    description: Trained parameters

  data:
    maps_to: "D" in LWD-R
    description: Training corpus

  representation:
    maps_to: "R" in LWD-R
    description: Categorical schema / ontology
```

## Schema Field

```json
{
  "layers": [
    {
      "name": "Payment Rail",
      "type": "payment"
    },
    {
      "name": "Identity Verification",
      "type": "identity"
    },
    {
      "name": "Merchant Registry",
      "type": "registry"
    }
  ]
}
```

## Why Layer Decomposition Matters

1. **Granular diagnosis**: Identifies which component fails
2. **Targeted remediation**: Fix specific layers, not whole system
3. **Dependency analysis**: Layer A may depend on Layer B's corrigibility
4. **Hybrid systems**: Different layers may be DPI vs EPI

## Aggregation Rule

```
System passes ONLY IF every layer passes all five tests.

Rationale: Feedback loop breaks at weakest point.
A corrigible payment layer on an incorrigible identity layer
= incorrigible system (identity failure propagates).
```
