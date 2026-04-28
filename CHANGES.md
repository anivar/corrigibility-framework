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

## P1 — Theoretical Expansion

### EPI (complete)

- §3.1.1 *Operative Representation vs. Nominal Representation* (new) —
  added at line 281 with Proposition 3.1 (Operative-R Falsifiability).
- §3.1.2 *Synthetic Data and the Limits of Transferable Transparency*
  (new) — added at line 304 with Provenance Transitivity principle and
  three-regime taxonomy (open / mixed / opaque-anchored).
- §5.2 *Data Capture* (new) — added at line 461 with the
  $D_{required} > \kappa_D \cdot D_{accessible}$ formalization, the
  upstream-dependency taxonomy (synthetic, distilled, evaluation,
  RLHF, reward, tokenizer), and the Joint Forkability Condition
  (Proposition 5.1).
- §6.1 *Agent Systems as Composable Architectures* — added at line 571
  with the $A = (M, H, B, S, T, C)$ tuple, component-level disclosure
  map (Table 6.1), and Retrieval Opacity principle (line 618).
- WCC harmonic-mean note: glossary entry and §7.2 prose both state
  that WCC is computed as a harmonic mean to ensure weakness in any
  dimension cannot be hidden by strength in others.

### EPI (additional in v3.0.0-rc.1)

- §6.6 *Action Boundary Protocol* expanded with a worked argument for
  why outside-context enforcement is categorically different from
  in-context guardrails (not merely safer), one concrete failure mode
  (prompt injection bypassing in-context guardrails), and one concrete
  success pattern (deterministic validator rejecting an out-of-policy
  action).
- §6.7 *Tool and Retrieval Surfaces* (new) — disclosure standards for
  tool definitions (capability scope, side-effect class, revocation
  paths) and retrieval pipelines (source provenance, ranking logic,
  filter sets), cross-referencing Principle 6.1 (Retrieval Opacity).
- Register softening: §9.1 paragraph heading "The Alternative is
  Surrender" → "The Cost of Abandoning Structural Evaluation"; the
  "we mathematically surrender to black-box monopolies" sentence
  rewritten as analytic claim ("structural evaluation methods are
  necessary; without them, governance defers to operators by default").

### EPI (deferred)

- §9 / §10 broader restructuring; broader register sweep beyond the
  three targeted softenings above.

### DPI (complete)

- §4.10 *Contestation of Representational Categories in AI-Mediated
  DPI* (new) — added at line 561 with Remark on Extension of GOVERN
  to Ontological Choices, completing the deterministic framework's
  bridge to the EPI companion paper.
- Open-washing taxonomy compressed from 7 flat categories to 3
  strategic patterns (symbolic-openness, coerced-legitimacy,
  substantive-substitution) with the 7 named tactics retained as
  illustrations within each pattern; subsection cross-refs to
  DID-Washing and Climate-Washing preserved.
- §8.4 Limitations consolidated from 12 enumerated items to 6:
  methodological scope (binary + control theory illustrative),
  solution validation gaps (FORK essentiality + FEE + prescriptive
  limits), evaluation interpretive limits (governance judgment +
  timescale scope), network effects unmodeled, empirical scope
  (India focus + political economy + baseline mortality), value
  commitments. All substantive points preserved.

### DPI (additional in v3.0.0-rc.1)

- Null-Feedback Instability reframed from Theorem to **Proposition**
  (subtitle "Structural Analogy"). Proof prepended with an in-text
  scope sentence: the apparatus illustrates the consequence of broken
  loop closure under generic disturbance, not the predicted dynamics
  of any specified DPI implementation. All three downstream cross-
  references updated ("Theorem~\ref{...}" → "Proposition~\ref{...}";
  the corresponding figure caption phrasing also updated). §8.4
  limitations item 1 trimmed: the apologetic walk-back about the
  control model being pedagogical-not-predictive is dropped, since
  the proposition itself now flags its scope.

### DPI (deferred)

- Executive Summary thesis deduplication.
- §7 Discussion structural relocations (Methodological Foundations
  position; Pathways/Transition Paths promotion).

### Shared (complete)

- `papers/shared/glossary.tex` populated with 22 cross-paper entries.

## P2 — Polish

### Shared bibliography migration (complete)

- `papers/shared/refs.bib` populated with all unique references from
  both papers (38 entries total) plus the `revision-seed.md` §P2.27
  additions.
- New BibTeX keys added: `bommasani2023fmti` (Foundation Model
  Transparency Index, arXiv:2310.12941), `nist2023airmf` (NIST AI RMF
  1.0, NIST AI 100-1, doi 10.6028/NIST.AI.100-1), `liang2022helm`
  (HELM, arXiv:2211.09110), `carlini2021extracting` (USENIX Security
  2021), `shumailov2023curse` (already added in P1).
- DOIs added where available (gebru2021, mitchell2019, grother2019,
  shumailov2023curse, bommasani2021, bommasani2023fmti, nist2023airmf,
  liang2022helm).
- Both papers' inline `thebibliography` blocks replaced with
  `\bibliography{../shared/refs}`. Latexmk successfully resolves all
  `\citep{}` sites; no Citation undefined warnings.

### Shared glossary wiring (complete)

- `papers/shared/glossary.tex` (22 cross-paper entries from P1) is now
  `\input` from each paper's appendix.
- DPI: pre-existing inline glossary at §A replaced with the shared
  one; cross-paper note added.
- EPI: new appendix added before References; same shared glossary
  block.

### Cross-reference cleanup (complete)

- DPI: figure path made explicit (`figures/...` →
  `../shared/figures/...`).
- DPI: added missing labels `subsec:post-execution`,
  `subsec:discrete-integrator`, `thm:null-feedback`.
- DPI: 5 hardcoded references converted to `\ref{}` ("Appendix B" →
  `Appendix~\ref{appendix:proofs}`, "Section 4.4" →
  `Section~\ref{subsec:post-execution}`, "Theorem 1" ×2 →
  `Theorem~\ref{thm:null-feedback}`, "Section B.6.2" →
  `Section~\ref{subsec:discrete-integrator}`, "Proposition 2" →
  "The Essentiality-Corrigibility Tension").
- EPI: hardcoded cross-paper "Section 6.7.2" footnote replaced with
  `\citep{aravind2026dpi}`; appendix order normalized
  (Acknowledgments / License / Data and Code Availability moved
  before `\appendix`).

### DPI policy-constants table consolidation (complete)

- Three additional constants surfaced in the framework-wide table:
  $\tau_{\text{exit}}$ (exit-penalty material-exclusion threshold),
  $\Sigma^*$ (portability threshold), $\kappa$ (Cohen's kappa
  inter-rater target), $Sc^*$ (scale threshold).
- Caption notes that per-test pass/fail thresholds are listed in the
  operational-proxies and three-indicator tables.

### Sentence-level copyedit pass (complete)

- "audit theatre" → "audit theater" (DPI §B.4) for American-English
  consistency with the rest of both papers.
- DPI Data and Code Availability: "Assessment Skills" /
  `skills/assess/` → "Assessment Rules" / `rules/assess/` to match
  EPI and complete the agentskills.io terminology excision.
- Verified no double-space typos, duplicate words, common spelling
  errors, a/an article slips, mixed quote styles, or remaining
  hardcoded section/theorem references.
- Verified all 36 unique `\citep{}` keys resolve against
  `papers/shared/refs.bib`; no `Citation undefined` warnings.
- Full end-to-end re-read of both papers (DPI 2527 lines, EPI 1249
  lines) confirms no further P0/P2 residue. P1 items (Executive
  Summary deduplication, open-washing taxonomy 7→3 compression, §7.1
  relocation, §7.5 promotion, §8.4 limitations 12→6-8) remain
  pending and are correctly tracked in the P1 section.

### Pending

- Final tag (v3.0.0).

## Build verification

| Paper | Pages | Size   |
|-------|-------|--------|
| DPI   | 50    | 937 KB |
| EPI   | 26    | 670 KB |

Latexmk completes without errors. Remaining warnings are typographic
(`Underfull` / `Overfull \hbox`) plus one `T1/lmr/bx/sc undefined font
shape` substitution from \scshape inside \bf in the title rule, which
is a known Latin Modern + arxiv.sty interaction and harmless.
