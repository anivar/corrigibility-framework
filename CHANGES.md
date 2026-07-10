# Revision Changelog

Tracks the revision passes for the v3.0.0 ArXiv submission, organized
by priority tier and paper. P0/P1/P2 closed the structural revision pass
(arXiv submission baseline); P3 added the consensus-driven revisions
(normative anchor, two-pronged argument, strict interpretability
firewall, citizen-side GOVERN mechanism families, scope and open
problems). All four tiers ship under v3.0.0. The Q-series
margin-evaluation upgrades and the SSRN reference-processing fixes ship
as the July 2026 revision.

## Q — Margin-Evaluation Upgrades (July 2026 revision)

Ten reviewer-question upgrades (Q1–Q10) applied across both papers,
plus the political-economy expansion. Cherry-picked tex-only from
`claude/ambedkar-matrix-revisions-XVZQP` (335ee44); the accompanying
six-tradition theory notes were deliberately kept out of the repo (no
visible fourth spine — the intellectual debt is carried by primary-source
citations instead).

### DPI (`papers/dpi/main.tex`)

- New subsection *The Dual Exercise of the Tests* (`subsec:dual-exercise`,
  after Structural Symmetry of Power) with Table `tab:dual-exercise`:
  each test partitioned into its inward exercise (operator, auditor,
  regulator) and outward exercise (the governed), mapping existing
  instruments (Rules A.9–A.11, FEE, subject receipts, state portability,
  category contestation) to their column. Consolidates the outward-facing
  Q-series instruments into one surface and anchors them to the gradient
  quantifier.
- Q1: New Remark *The Gradient Quantifier: Corrigibility at the Margin*
  (`rem:argmin`, appendix, after the Binarity corollary). $H$ and $K$
  become distributions $H(x)$, $K(x)$ over participant position;
  corrigibility requires loop closure $\forall x$; pass/fail is taken at
  $x^* = \arg\min_x H(x) \cdot K(x)$ (recommended $p_{10}$ stratum),
  not the population mean.
- Q2: *Bole Clause* — evidentiary standard for statutory fallbacks
  (Rule A.9 applied at the margin stratum; documented margin-stratum
  invocations required). Historical anchor corrected: the 1923 Bole
  Resolution (Bombay Presidency), enforced at Mahad in 1927.
- Q3: *Collective-Standing Precondition (Ostrom Principle 7)* appended
  to the GOVERN contestation subsection.
- Q4: *Intermediary-Discretion Surface* appended to AUDIT — per-rung
  variance disclosure, delegated-discretion role enumeration, Rule A.9
  enforcement evidence against intermediaries.
- Q5/Q7: New *Rule A.11: Auditor Data Duties* — purpose-bound audit
  access; the two-sided AUDIT requirement ("no one can prevent
  auditing" / "no one can strip-mine the governed").
- Q9/Q10: Policy-constants table caption rewritten — thresholds are
  policy choices requiring deliberative calibration (affected-class
  participation, documented rationale, periodic external review).
- Political economy: the Limitations item expanded into the
  four-mechanism analysis (graded inequality, artifact openness as
  legitimacy cover, administrative synopticism, certification capture).
- New citations at the debt points: `ambedkar1936annihilation` (graded
  inequality), `ambedkar1945congress` (joint electorate),
  `ambedkar1947states` (enforcement history vs. legislative text).
- Fixes: added missing `\label{subsec:limitations}`; cross-document
  `\ref{rem:subject-receipt-epi}` replaced with a textual reference plus
  `\citep{aravind2026epi}` (the papers build standalone; no xr package).

### EPI (`papers/epi/main.tex`)

- Q1: *Gradient Quantifier in Tier Audits* — distributional reporting;
  lower-decile pass/fail for `high_stakes`; cross-document
  `\ref{rem:argmin}` replaced with a textual reference plus
  `\citep{aravind2026dpi}`.
- Q5: *Subject Receipt Requirement* — per-determination signed receipts
  with transparency-log inclusion proofs (RFC 9162-style),
  subject-facing, independently verifiable, machine-readable — plus the
  citizen-constraint registry at the action boundary.
- Q6: *R-Layer Change Control* — pre-deployment notice with review
  window, suspensive objections from recognized affected-class
  representatives, versioned schema diffs; emergency path with
  retroactive review.
- Q8: *Artifact-Reproducible vs. Governance-Reproducible* FORK levels;
  `fork_viability` stated as an audit-artifact requirement (the
  schema-repo field itself is tracked separately).
- Fix: "companion paper" mis-attribution removed from the Injunction
  Hook cross-reference (it is EPI's own Section 6.9).

### SSRN reference-processing fixes

Cherry-picked from `claude/ssrn-reference-parsing-7A5RZ` (3 commits).

- `refs.bib`: no raw `\url{}` remains in `howpublished` (rtfc2018,
  npci2026, biometricupdate2025, xroad2026, osi2024 restructured with
  proper publisher strings + url fields); Unicode author-name encodings
  corrected (Daumé III, Tramèr, Úlfar); companion-paper entries carry
  canonical SSRN DOIs (DPI 10.2139/ssrn.6059075, EPI
  10.2139/ssrn.6669318 — both verified resolving).
- `CITATION.cff`: EPI SSRN DOI added; EPI Zenodo DOI demoted to
  archival.
- `papers/epi/SSRN.md`: DPI SSRN cross-reference filled in.

### July sharpenings

Deployment-reality pass, written as criteria only (no mechanisms):

- EPI §2 *Deployment Variables*: human position, agent cardinality,
  orchestration depth, scale, and exerciser species are variables the
  tests bind over; the invariants are chain termini, checker
  independence, and freshness of grants.
- EPI §3.3 machine-verifiable legitimacy gains (e) *origination
  marking*: records state who operated; absence is never evidence of
  human operation; markers only narrow authority. Unifying criterion:
  authority and attribution are record-borne acts, never inferences
  from artifacts.
- EPI §6 *Nested Delegation*: the tuple is recursive; tests compose
  across delegation depth by weakest link; effect-surface enforcement
  makes internal fan-out invisible to the validator.
- EPI §6 EXIT layers: regeneration resistance added to Memory and
  Workflow EXIT (termination counts only if resumption requires a
  fresh grant).
- EPI §6: *Stochastic Redundancy Is Not Validation* (judge panels share
  the substrate they check); *Untyped Action Channels* (browser/desktop
  agents; the boundary migrates to the effect surface); *The Normalized
  Boundary* (possession no longer discriminates; the questions move to
  whose constraints and outside verifiability; specification lifetimes;
  the accountable-authority checkpoint stated functionally, not
  positionally).
- EPI §6 GDoS recast around orchestration fan-out; §7 Rule of Workflow
  declared arrived (workflow layer as default assessment target);
  open problems gain *Scale as a Governed Variable* (fan-out, rate, and
  blast-radius caps as first-class GOVERN instruments).
- EPI tier table and EXIT verification row rewritten species-free
  (accountable-authority checkpoint; accountable fallback).
- DPI layer decomposition gains the delegation-depth axis pointer.
- Both papers carry a revision date line (10 July 2026).

### Build Verification (July 2026 revision)

| Paper | Pages |
|-------|-------|
| DPI   | 51    |
| EPI   | 34    |

Zero undefined references and zero undefined citations in both logs;
the only remaining LaTeX warning is a cosmetic float-specifier
adjustment (`h` → `ht`).

## P3 — Consensus Revisions (v3.0.0)

Five decision-points (DP1–DP5) addressed across both papers on branch
`revise/p3-consensus`.

### DP5 — Normative grounding (both papers)

- New `\paragraph{Normative Anchor.}` introduces non-domination (Pettit
  primary; Habermas / Sen / Mouffe alternatives) as the framework's
  legitimacy criterion, with explicit "analytical convenience, not
  commitment to a full republican political program" hedge.
- DPI: anchor placed at the head of §3 *Theoretical Foundations*
  (sec:theory) and merged with the existing triangulation paragraph
  (Cybernetics / Commons Governance / Free Software). §1 retains a
  one-sentence forward reference. New bib entries: `pettit1997`,
  `habermas1996`, `sen1999`, `mouffe2000`.
- EPI: anchor placed in §1 (no parallel §3 *Theoretical Foundations*
  exists in EPI).

### DP1 — Binary corrigibility, two-pronged argument

- DPI §1 Introduction reframed: "Open-Loop Instability Theorem" →
  "Open-Loop Instability Argument" with explicit two-pronged structure
  (control-theoretic mechanism + political-theoretic legitimacy). DPI
  §7.1.2 renamed *Legitimacy Threshold vs Physical Claim: A Two-Pronged
  Argument* (`subsubsec:two-pronged`); three named paragraphs distinguish
  the mechanism argument, the legitimacy argument (sham governance,
  non-monotonic returns), and why both are needed ("Neither alone forces
  the conclusion; together they overdetermine it from independent
  grounds").
- DPI appendix Executive Summary updated to call the formalization "one
  half" of the argument with cross-ref to §7.1.2.
- DPI corollary "Binarity of Corrigibility" justification revised: rests
  on the conjunction of mechanism (Proposition~\ref{thm:null-feedback})
  and legitimacy (sham governance) arguments.
- EPI §1 *Open-Loop Instability Argument* paragraph carries the parallel
  two-pronged framing.

### DP2 — Strict Interpretability Firewall (EPI §3.2 + DPI cross-ref)

- New EPI §3.2 *Strict Interpretability Firewall* (`subsec:firewall`)
  with Principle (`prin:firewall`): when operative R cannot be disclosed
  to the standard of Proposition~\ref{prop:operative-r-test}, the system
  fails CODE for high-stakes deployments and "should not, consistent
  with this framework's legitimacy criteria, be adopted as Epistemic
  Public Infrastructure" in rights-affecting tiers.
- Wording chosen deliberately: structural-criteria language, not
  jurisdiction-specific lawfulness language.
- *Why strict, not graduated* paragraph: graduated regimes ratchet to
  permanent partial compliance via the same political-economy mechanism
  that converts "proportionate" contestation into sham governance.
- *Human-Discretion Objection* and response: bias-plus-corrigibility
  beats bias-minus-corrigibility; the asymmetry is structural (appeal,
  retraining, replacement, institutional memory) rather than rhetorical.
- *Cost of the Strict Position* paragraph: every current frontier
  high-stakes deployment fails CODE under this framework; the diagnostic
  instrument is calibrated to surface this failure rather than ratify
  current systems.
- DPI §4.10 bridge clause extended with one-sentence cross-reference to
  the firewall.

### DP4 — Citizen-Side GOVERN: Mechanism Families (EPI §6.8)

- New EPI §6.8 (`subsec:govern-mechanisms`) identifies five
  non-exclusive mechanism families: juridical, administrative/executive,
  distributed/class-action, deliberative, federation-based.
- Composition requirement at high-stakes tier: at least two of
  {juridical, distributed/class-action, deliberative}, with structural
  justification (each covers a failure mode the others cannot:
  individual remedy vs systemic patterns vs categorical-schema
  contestation).
- Footnote on informal complements (journalism, scholarly criticism,
  market reputation, public pressure) as necessary but non-substitutive.

### DP3 — Scope and Open Problems (new EPI §12)

- New EPI §12 *Scope and Open Problems* (`sec:open-problems`) with one
  paragraph per open regime: federated learning, continuous learning,
  multi-tenant deployments, international/jurisdictional layer, political
  economy of $\kappa$ calibration. Strict per-paragraph length
  discipline.
- §1 paper-structure paragraph updated to reference the new section.

### Build Verification (v3.0.0)

| Paper | Pages | Size   |
|-------|-------|--------|
| DPI   | 51    | 943 KB |
| EPI   | 29    | 690 KB |

Latexmk completes without errors (one harmless `T1/lmr/bx/sc undefined`
font-shape warning persists from arxiv.sty + Latin Modern interaction).



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

- ~~Final tag (v3.0.0)~~ — tagged. July 2026 revision: one release tag +
  SSRN re-upload of both rebuilt PDFs (so the reference parser
  reprocesses) pending. Delete stale pre-release tags at push.

## Build verification

| Paper | Pages | Size   |
|-------|-------|--------|
| DPI   | 50    | 937 KB |
| EPI   | 26    | 670 KB |

Latexmk completes without errors. Remaining warnings are typographic
(`Underfull` / `Overfull \hbox`) plus one `T1/lmr/bx/sc undefined font
shape` substitution from \scshape inside \bf in the title rule, which
is a known Latin Modern + arxiv.sty interaction and harmless.
