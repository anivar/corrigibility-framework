# Revision Changelog

Tracks the three-priority revision pass for the v3.0.0 ArXiv submission.
Organized by priority tier and paper. P0 is complete; P1 and P2 are
in-progress.

## P0 — Blocking Edits (complete in v3.0.0-alpha.1)

### EPI (`papers/epi/main.tex`)

- §6.4 *Action Boundary Protocol*: replaced agentskills.io contamination
  block with standard-agnostic content. Added five architectural
  requirements (Deterministic Validation, Context-Window Isolation,
  Exception Handling, Machine-Readable Specifications, Binding
  Constraints). Reframed Principle 6.2 as **Action Boundary Governance**.
- *Bounding Stochasticity* and *Defeating Workflow Capture* subsections
  rewritten to refer to "open action specifications" instead of
  "Agentic Skills."
- *Critical Limitation* enumeration: "skill" → "action specification"
  throughout.
- §8.4 limitation #6 (SBOM disclosure tradeoff): rewritten generically.
- §9 conclusion implication for technologists: replaced reference to the
  Agentic Skills standard with the Action Boundary Protocol.
- §5.4 model-status update: refreshed open-model examples to Llama
  3.1/3.3, DeepSeek-V3 / DeepSeek-R1, Gemma 2, Mistral, OLMo 2, Pythia.
- Appendix A *Agentic Skills Schema Specifications* renamed to *Action
  Boundary Schema Specifications* and rewritten with protocol-agnostic
  field names: `action_specification_format`,
  `execution_environment_isolation`, `independent_audit_path`,
  `model_agnostic`.
- Schema-mapping table updated to use new field names.
- Data and Code Availability section: removed claim that the schema
  follows the "Agentic Skills specification." Replaced with a statement
  that the schema is intentionally agnostic to any specific
  action-specification standard.
- Bibliography:
  - Removed `agentskills2025` bibitem.
  - Renamed `paper1` → `aravind2026dpi`; updated all five
    `\citep{paper1}` sites to use the new key.

### DPI (`papers/dpi/main.tex`)

- Cross-paper references converted from prose ("a companion paper") to
  citations: §1 (line 255), §7 future work (line 1726), §7 schema list
  (line 1755) all now use `\citep{aravind2026epi}`.
- Khera citation (Aadhaar starvation deaths): now cites
  `rtfc2018,khera2017` jointly with the Right to Food Campaign as
  primary source.
- Bibliography:
  - Removed orphaned `agentskills2025` bibitem.
  - Added `rtfc2018` (Right to Food Campaign 2018 fact-finding report).
  - Added `aravind2026epi` (companion paper).

## P1 — Theoretical Expansion (pending)

### EPI

- §3.1.1 *Operative Representation vs. Nominal Representation* (new).
- §3.1.2 *Synthetic Data and the Limits of Transferable Transparency*
  (new).
- §5.2 *Data Capture* (new) with WCC integration.
- §6.1 *Agent Systems as Composable Architectures*: introduce the
  $A = (M, H, B, S, T, C)$ tuple and Retrieval Opacity principle.
- §6.3–§6.6 expansion of the harness-disclosure framework.
- §9 / §10 restructuring (relocation, register softening, WCC harmonic-
  mean fix).

### DPI

- §4.8.3 *Contestation of Representational Categories* (new).
- Theorem 1 reframe; thesis deduplication; open-washing taxonomy
  compression; §7 relocations; §8.4 limitations consolidate.

### Shared

- `papers/shared/glossary.tex` populated.

## P2 — Polish (pending)

- natbib + `papers/shared/refs.bib` migration; remove inline
  `thebibliography` blocks.
- BibTeX entries from `revision-seed.md` §P2.27: `bommasani2023fmti`,
  `nist2023airmf`, `liang2022helm`, `shumailov2023curse`,
  `carlini2021extracting`.
- Sentence-level copyedit; DPI policy-constants table consolidation.

## Build verification

| Paper | Pages | Size  |
|-------|-------|-------|
| DPI   | 50    | 597 KB |
| EPI   | 24    | 566 KB |

Latexmk completed without errors; only typesetting (`Underfull` /
`Overfull \hbox`) warnings. See `grep-check.txt` for excision
verification.
