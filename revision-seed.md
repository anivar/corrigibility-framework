# Revision Seed Material

Pre-drafted snippets for new content sections. Each is conceptually
correct but under-length — roughly 1/3 to 1/2 of target. Use as scaffold,
not finished section. See revision prompt for expansion targets.

## P0.1 — Citation Correction (Aadhaar Starvation Deaths)

The "57 starvation deaths / 19 directly attributed" figure derives from
the Right to Food Campaign fact-finding reports compiled between 2015 and
2018, subsequently analyzed by Khera, Drèze, and Dutta. Use rtfc2018 as
primary citation; khera2017 may remain as secondary for broader PDS
exclusion analysis.

```bibtex
@techreport{rtfc2018,
  author = {{Right to Food Campaign}},
  title = {Starvation Deaths in India: Documented Cases and the Role of Aadhaar},
  institution = {Right to Food Campaign Secretariat},
  year = {2018},
  address = {New Delhi, India},
  url = {http://www.righttofoodcampaign.in/}
}
```

## P0.4 — Standard-Agnostic Action Boundary Protocol (EPI §6.4 Rewrite)

All references to agentskills.io / SKILL.md / "Agentic Skills" excised.
Section reframed around architectural invariants.

> **6.4 The Action Boundary Protocol**
>
> As infrastructure transitions to the Rule of the Workflow, the
> fundamental unit of governance can no longer be the static database
> record, nor can it be the stochastic model weight. To subject autonomous
> systems to democratic constraint, the architecture must adopt a new
> structural primitive: the Action Boundary.
>
> **Principle 6.2 (Action Boundary Protocol).** *If the state cannot
> govern the neural network's weights, it must govern the action
> boundary: the deterministic envelope that wraps stochastic inference.*
>
> In agentic systems, learned inference must not directly trigger
> irreversible action. Inference outputs must pass through a deterministic
> validation layer that enforces policy constraints and safety rules. The
> Action Boundary Protocol specifies five architectural requirements for
> agentic interoperability:
>
> 1. **Deterministic Validation:** Inference outputs must pass through a
>    hard-coded policy layer before execution.
> 2. **Context-Window Isolation:** Constraints must be encoded in the
>    execution environment, independent of the model's probabilistic
>    context window (preventing prompt-injection bypass).
> 3. **Exception Handling (EXIT):** The specification must dictate
>    explicit fallback paths and termination triggers, preventing the
>    infinite loops that cause Governance Denial of Service (GDoS).
> 4. **Machine-Readable Specifications (CODE & AUDIT):** The agent's
>    workflow and tool permissions must be defined in declarative,
>    independently auditable schemas, rendering the system's operational
>    ontology public.
> 5. **Binding Constraints (GOVERN):** The validator acts as a
>    non-overrideable controller; actions that fail the schema are
>    rejected and logged, providing an auditable failure signal.
>
> Multiple open protocols can instantiate these requirements. The
> structural necessity is that the validator enforces hard constraints
> independent of the model's internal alignment.

## P1.8 — EPI §3 Expansion (R-as-Deployed-System)

Subsection: "3.1.1 Operative Representation vs. Nominal Representation".

> Existing frameworks frequently conflate a model's latent categorical
> structure at training time with its categorical structure at deployment.
> This framework distinguishes *nominal representation* (the latent space
> of the trained artifact in isolation) from *operative representation*
> (the categorical schema that emerges during inference under specific
> deployment conditions).
>
> Deployment-time variables fundamentally modify the representational
> boundary. Quantization alters representational granularity; pruning
> removes edge-case distinctions; Mixture of Experts (MoE) routing
> produces task-conditional ontologies; output filtering shapes which
> categories the user actually encounters.
>
> Disclosure must describe operative representation, not nominal
> representation. Nominal transparency fails affected communities because
> the categorical structure they interact with in the deployed
> infrastructure differs from what the base model suggests.
>
> **Falsifiable Test:** *Can an independent auditor reproduce the
> observed classification distribution of the deployed system using only
> the disclosed representational schema?* If the deployment variables
> obscure the derivation chain, the system fails the R requirement.

**Note for expansion:** the original seed example (RAG from opaque
municipal DB) blends two arguments — deployment-time modification of R,
and opaque retrieval capturing R. The second belongs in §6 (harness
disclosure). When expanding §3.1.1, lead with cleaner cases where R is
modified by deployment alone (quantization, distillation, MoE routing)
before introducing retrieval as a complicating factor.

## P1.9 — EPI §3 Expansion (Synthetic Data Provenance)

Subsection: "3.1.2 Synthetic Data and the Limits of Transferable
Transparency".

> Transparency is not transferable through synthetic generation. A model
> trained on synthetic data generated by an opaque frontier model has not
> satisfied the Data (D) layer, regardless of how meticulously the
> resulting synthetic dataset is documented.
>
> Documenting what is *in* a synthetic dataset is structurally distinct
> from accounting for how its content was shaped by the upstream model's
> biases, systemic omissions, and latent constraints. When synthetic data
> trains a model that in turn generates synthetic data, accountability
> degrades recursively.
>
> Let the provenance chain be defined as $P = [g_0, g_1, ..., g_n]$, where
> each $g_i$ is the generator producing training data for $g_{i+1}$. The
> LWD-R disclosure obligation extends through the entire chain. A fully
> synthetic dataset generated by an openly trained model (where full
> LWD-R is available for the chain) is structurally distinct from
> synthetic data generated by a proprietary frontier model. If the chain
> breaks at a frontier-model link, the downstream infrastructure is
> epistemically opaque, triggering a failure of the CODE condition.

## P1.10 — EPI §5 Expansion (Data Capture)

Subsection: "5.2 Data Capture" (renumber existing §5.2+).

> Training forkability requires more than compute access; it requires
> data sovereignty. Compute Capture and Data Capture act as independent
> multipliers of the Workflow Capture Coefficient.
>
> **Definition 5.2 (Data Capture).** *Data Capture occurs when the data
> required to train a functionally equivalent model can only be produced
> by infrastructure the open community cannot reproduce.*
>
> This barrier extends beyond raw text corpora into a taxonomy of
> upstream training dependencies: synthetic datasets, distilled expert
> outputs, proprietary evaluation sets, RLHF reasoning traces, and reward
> models.
>
> Formally, Data Capture occurs when the data corpus required for
> reproduction ($D_{required}$) exceeds the data accessible to
> non-operator actors ($D_{accessible}$) beyond a policy-determined
> friction threshold:
>
> $$D_{required} > \kappa_D \cdot D_{accessible}$$
>
> Training forkability is genuinely available if and only if a system
> evades both Compute Capture and Data Capture simultaneously.

## P1.11 — EPI §6 Restructure (Harness Disclosure Framework)

Covers §6.1 and §6.2 only. §6.3–§6.6 to be written during expansion.

> **6.1 Agent Systems as Composable Architectures**
>
> An agent system is not a model; it is a composable architecture.
> Formally, an agent system $A$ is the tuple $A = (M, H, B, S, T, C)$,
> where $M$ is the model, $H$ is the orchestration harness, $B$ is the
> action boundary, $S$ are the skill specifications, $T$ are the tool
> definitions, and $C$ represents the deployment-time configuration
> (system prompts, retrieval pipelines, output filters).
>
> Each component bears distinct governance requirements. Behavior is a
> property of the system $A$, not the model $M$. The same model deployed
> in a different harness produces materially different administrative
> outcomes.
>
> **6.2 Why System Behavior is Not Model Behavior**
>
> Because $H$, $S$, $T$, and $C$ modify behavior independent of $M$,
> model-level LWD-R disclosure is necessary but insufficient. If a state
> deploys an open-weights model but orchestrates its actions through a
> proprietary vendor harness, the infrastructure fails both CODE and
> FORK.
>
> **Principle 6.1 (Retrieval Opacity).** *Retrieval-augmented systems
> are not structurally open if their retrieval components (R) are
> opaque, even when the underlying model (M) is fully disclosed.*

## P1.12 — DPI §4.8 Extension (Community Contestation)

Subsection: "4.8.3 Contestation of Representational Categories".

> When learned systems are deployed within DPI, the categories they use
> to classify citizens (e.g., "eligibility," "risk," "fraud") cease to be
> mere statistical properties; they become consequential administrative
> determinations.
>
> Affected communities must possess the structural capacity to review
> and contest these representational categories, not just dispute
> individual execution decisions. Representation in AI-mediated DPI
> differs fundamentally from representation in deterministic
> administrative systems: the categories are emergent rather than
> deliberately designed. The contestation surface shifts — participants
> must be able to contest the schema itself, not just the application of
> the rule.
>
> The GOVERN test therefore extends to ontological choices when those
> choices produce binding classifications. (The formal constraints
> required to prevent this are detailed in the companion paper's
> analysis of operative representation; see EPI §3.1.1.)

## P2.27 — Required BibTeX Additions

```bibtex
@article{bommasani2023fmti,
  title={The Foundation Model Transparency Index},
  author={Bommasani, Rishi and Klyman, Kevin and Longpre, Shayne and Kapoor, Sayash and Maslej, Nestor and others},
  journal={arXiv preprint arXiv:2310.12941},
  year={2023}
}

@techreport{nist2023airmf,
  title={Artificial Intelligence Risk Management Framework (AI RMF 1.0)},
  author={{National Institute of Standards and Technology}},
  institution={U.S. Department of Commerce},
  number={NIST AI 100-1},
  year={2023},
  doi={10.6028/NIST.AI.100-1}
}

@article{liang2022helm,
  title={Holistic Evaluation of Language Models},
  author={Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and others},
  journal={arXiv preprint arXiv:2211.09110},
  year={2022}
}

@article{shumailov2023curse,
  title={The Curse of Recursion: Training on Generated Data Makes Models Forget},
  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},
  journal={arXiv preprint arXiv:2305.17493},
  year={2023}
}

@inproceedings{carlini2021extracting,
  title={Extracting Training Data from Large Language Models},
  author={Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and others},
  booktitle={30th USENIX Security Symposium (USENIX Security 21)},
  pages={2633--2650},
  year={2021}
}
```
