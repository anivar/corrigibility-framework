# classify-system

**Priority**: MEDIUM
**Category**: System Classification

## Rule

Before assessment, classify the target system as DPI or EPI to select appropriate schema and criteria.

## Classification Decision Tree

```
Is the system's behavior determined by learned parameters?
├── YES → EPI (Epistemic Public Infrastructure)
│   ├── Uses ML/AI models for decisions
│   ├── Behavior emerges from training data
│   └── Outputs are probabilistic
│
└── NO → DPI (Digital Public Infrastructure)
    ├── Deterministic logic
    ├── Behavior determined by source code
    └── Outputs are reproducible given same input
```

## DPI Characteristics

- **Ledgers**: Payment systems, transaction logs
- **Registries**: Identity databases, land records
- **Payment Rails**: UPI, SWIFT, ACH
- **Protocols**: HTTP, DNS, email

**Key Property**: Same input → Same output (deterministic)

## EPI Characteristics

- **Inference Systems**: Eligibility models, risk scoring
- **Classification**: Fraud detection, content moderation
- **Generation**: Chatbots with administrative authority
- **Agents**: Autonomous systems in mandatory infrastructure

**Key Property**: Behavior shaped by training data (stochastic)

## Hybrid Systems

Some systems have both components:

```yaml
example: "AI-enhanced payment fraud detection"
components:
  dpi_layer: Payment rail (deterministic transaction processing)
  epi_layer: Fraud model (learned risk scoring)

assessment_approach:
  - Assess DPI layer with DPI schema
  - Assess EPI layer with EPI schema
  - Composite = min(DPI_score, EPI_score)
```

## Schema Selection

| Classification | Infrastructure Schema | Assessment Schema |
|----------------|----------------------|-------------------|
| DPI | `schema/dpi/infrastructure.json` | `schema/dpi/corrigibility.json` |
| EPI | `schema/epi/infrastructure.json` | `schema/epi/corrigibility.json` |
| Hybrid | Both | Both (take minimum) |

## Common Misclassifications

| System | Appears As | Actually Is | Reason |
|--------|------------|-------------|--------|
| Aadhaar | DPI | DPI | Biometric matching is deterministic lookup |
| UPI | DPI | DPI | Payment routing is deterministic |
| Fraud Detection | DPI | EPI | Model-based risk scoring |
| ChatGPT | EPI | EPI | Learned language model |
| Welfare Chatbot | DPI | Hybrid | Deterministic rules + AI interface |

## Output

```json
{
  "system_name": "Example System",
  "classification": "EPI",
  "classification_rationale": "System uses ML model for eligibility determination",
  "schema_version": "1.7",
  "schemas_used": {
    "infrastructure": "schema/epi/infrastructure.json",
    "assessment": "schema/epi/corrigibility.json"
  }
}
```
