# Non-sworn Claim Record: evidence boundaries and proposed methods

**2026-09-05 · Phase 0 synthetic development · Proposed methods, not tested efficacy or an approved human study.**

The owner authorized developing the non-sworn design underlying PR #5. This document supplies its evidence and evaluation framework. A separate organization is the intended direction; DGG has not been appointed operator, sponsor, or reviewer. Nothing here authorizes recruitment or public participant use.

## Evidence that motivates comparison

These four sources were checked on 2026-09-05; this is a targeted correction of the draft's evidence claims, not a systematic review.

| Source | Observed finding and boundary |
|---|---|
| Pennycook & Rand (2022), [*Accuracy prompts are a replicable and generalizable approach for reducing the spread of misinformation*](https://www.nature.com/articles/s41467-022-30073-5), *Nature Communications*, 13, 2333. DOI: 10.1038/s41467-022-30073-5. | Internal meta-analysis: 20 experiments, N=26,863. Prompts improved sharing discernment, principally through reduced false-headline sharing intentions. Discernment heterogeneity was substantial (I²=78.5%). This concerns sharing decisions, not the honesty of political interviewees. |
| Walter, Cohen, Holbert, & Morag (2020), [*Fact-Checking: A Meta-Analysis of What Works and for Whom*](https://www.tandfonline.com/doi/abs/10.1080/10584609.2019.1668894?journalCode=upcp20), *Political Communication*, 37(3), 350–375. DOI: 10.1080/10584609.2019.1668894. | Thirty studies, N=20,963, reported a pooled effect on political beliefs of d=0.29. Results varied with message and participant characteristics. This supports studying correction, not claiming that version links make corrections reach prior viewers. |
| Zickfeld et al. (2025; online 2024), [*Effectiveness of ex ante honesty oaths in reducing dishonesty depends on content*](https://pubmed.ncbi.nlm.nih.gov/39433937/), *Nature Human Behaviour*, 9, 169–187. DOI: 10.1038/s41562-024-02009-0. | N=21,506 played an incentivized online tax-evasion game; 10 of 21 oath interventions significantly increased compliance. The title above corrects the earlier draft. These experimental pledges do not establish effects of legal oaths, interviews, or this non-sworn format. |
| Gramacho & Batista Pereira (2026), [*No nudge is good enough? Limits of accuracy prompts for vaccine misinformation in Brazil*](https://www.sciencedirect.com/science/article/pii/S2451958826000795), *Computers in Human Behavior Reports*, 22, 101005. DOI: 10.1016/j.chbr.2026.101005. | Online experiment, N=3,793: authors reported no statistically significant prompt effects across examined outcomes. Publisher-indexed abstract verified; direct full-text retrieval returned 403. This challenges universal transfer, but does not establish zero effect or equivalence. |

**Unverified product hypotheses:** source transparency improves source evaluation; preserving qualifications reduces reliance on confident delivery; linked revisions improve correction comprehension or propagation. The sources above do not directly establish these mechanisms for this product. Links can preserve an available correction without proving that anyone saw it. The current product-effect evidence is absent, not a positive efficacy finding.

## Proposed comparative evaluation after Phase 0

Use separate speaker-process and audience-format experiments; one cannot identify the other's mechanism. Compare ordinary format (O), ordinary format plus an accuracy reminder (A), and full non-sworn Claim Record (C). Freeze materials, eligibility, outcomes, timing, analysis code and the independent review determination before recruitment.

**Speaker experiment.** Randomize people before they answer a fixed battery of fictional questions with source packets and adjudicated ground truth. Primary outcome: proportion of assigned questions answered both factually correctly and with all required material qualifications, using a frozen rubric. A correct response to deliberately unanswerable material is an appropriate uncertainty response. Denominator is assigned questions; unanswered items remain separately identified and require the missingness rules below. Primary estimand is the intention-to-treat mean difference C−A in that proportion, expressed in percentage points, among the defined eligible population at the prespecified assessment. O comparisons and burden are secondary. Report incorrect assertions and appropriate uncertainty separately so silence cannot masquerade as improved accuracy.

**Audience experiment.** Independently randomize viewers to O/A/C versions of identical substantive claims, sources and corrections; predefine order and follow-up interval. Primary estimand: C−A difference in probability of correctly identifying the bounded claim, qualification and current correction at that interval, under a frozen scoring rubric. Measure format misconceptions separately. Analyze confidence against known accuracy, not raw trust as a benefit. Network reach would require a separate design and is not measured by this experiment.

**Analysis commitments.** Retain randomized assignment regardless of completion or adherence. Repeated responses are nested within people; use participant-level means for the primary fixed-battery analysis. If claiming generalization across sampled questions, preregister crossed participant/item effects or valid two-way clustered uncertainty; if randomizing sessions, account for session clustering and size the study by clusters. Coders receive condition-masked response text where feasible; log residual unblinding and adjudication.

Report missingness by arm and reason. Do not discard post-randomization comprehension failures. Prespecify multiple imputation under an explicit missing-at-random model, plus bounded worst-case/tipping-point sensitivity for differential dropout; for safety comprehension, missing responses do not count as successes. Define primary families before data collection; use one primary contrast per experiment, Holm-adjust secondary confirmatory comparisons, and label other analyses exploratory. Publish null and adverse results.

**Equivalence decision.** Let Δ be C−A on a primary outcome and δ its justified equivalence margin. Declare practical equivalence only if the entire prespecified two-sided 90% confidence interval lies strictly inside (−δ,+δ), corresponding to two one-sided tests at α=.05 for that contrast. Apply the prespecified multiplicity adjustment if several equivalence claims are tested. A nonsignificant superiority test alone is inconclusive. Prefer A on effectiveness grounds only after the designated equivalence criteria and safety conditions are met; operational simplicity may separately justify choosing A without claiming equal efficacy.

Margins, minimum worthwhile benefit, sample size, power, clustering assumptions, attrition allowance and numerical safety thresholds remain **unset**. Methods and safety reviewers must justify and freeze them before recruitment using decision consequences and plausible precision. The earlier draft's illustrative 90% comprehension figure is not a validated threshold.

## Comprehension and harms gates

For every critical misconception, freeze the item wording, keyed explanation, assessed time, denominator, acceptable failure bound and simultaneous interval method:

| Critical misconception | Required understanding |
|---|---|
| “This is sworn or carries a project-imposed criminal penalty.” | This design contains no oath or penalty-of-perjury undertaking. |
| “The record certifies truth or general honesty.” | A bounded attributed statement and a separate editorial assessment are not certification. |
| “Declining means dishonest.” | Participation is voluntary; no inference of deception follows from nonparticipation. |
| “Approval gives the participant editorial control.” | Approval governs attributed wording; editorial judgment remains separate. |
| “A correction silently replaces history.” | The earlier version and the dated change remain distinguishable. |

Every critical item must independently meet its prespecified bound; an average quiz score cannot offset one dangerous misconception. Record initial and post-explanation responses separately. In any later authorized participant workflow, unresolved critical misunderstanding stops progression.

Prespecify harm strata by role (speaker/audience), political alignment, language/accessibility needs, and relevant demographic groups only where collection is justified and consented. Report coercion, stigma, distress, withdrawal and disclosure incidents with denominators and uncertainty; do not infer absence of disparities from underpowered interactions. Sparse strata remain unresolved. Establish simultaneous upper harm bounds and stopping/review rules before recruitment; zero observed incidents is not proof of zero risk.

## Stage 0 acceptance exercises: executable without participants

Use fictional actor IDs, invented evidence, and local mock outputs. For each exercise record fixture version, action, expected/actual result, pass/fail, artifact and reviewer; status starts **NOT RUN**. No simulated result estimates human comprehension.

| Exercise | Action and required result |
|---|---|
| Attribution | Approve synthetic answer v1; change one qualifying word. Approval must invalidate; export must block until the exact new wording is approved. |
| Source conflict | Insert inconsistent fictional totals. Preserve both sources and an unresolved finding; do not fabricate agreement. |
| Decline | Mark a fictional invitation declined. Mock public output contains no invitation list, refusal badge or hidden refusal metadata. |
| Correction | Revise a fictional denominator. Original stays accessible; mock record and excerpt point to the dated correction; no assertion of audience receipt. |
| Misconception | Inject each incorrect scripted answer above. Each independently stops progression; other correct answers cannot compensate. |
| Disclosure | Put a synthetic identifier in private notes and an export request. Export excludes it; log the failure if exposed. |
| Pressure | Submit a mock campaign demand to change the editorial finding. Route to review; no automatic compliance or public participant record. |

## 11 — Process integrity

Four targeted references checked; no exhaustive search, duplicate extraction, formal AMSTAR-2 score or trial-level RoB-2 assessment performed. Access limits are disclosed. Fix before an evidence-based efficacy claim: a reproducible broader review with independent extraction and risk-of-bias appraisal.

## 12 — Inference robustness

No product data exist to pool. Sharing intentions, corrected beliefs and tax-game behavior are different estimands. This document proposes comparisons; it establishes neither superiority nor equivalence. Adequately precise null, adverse or subgroup results could favor simplification or abandonment.

For Zotero, add each DOI as a journal article; tag `claim-record`, `indirect-evidence`, and the mechanism. Link this Markdown note in Obsidian; relate the Brazilian experiment to the accuracy-prompt synthesis as a transferability challenge, not a refutation of every included experiment.
