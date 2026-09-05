# Non-sworn Claim Record — Phase 0 protocol

**Status: canonical development specification; synthetic tabletop work only.**

The owner selected the non-sworn design developed in PR #5. This specification carries that design forward for a separate, cross-party project. Nolan is the project owner; that designation does not appoint a legal operator, publisher, records custodian, or research sponsor. DGG is a possible recipient, with no operating role assigned here. Historical sworn materials remain separate reference material.

This document authorizes no real-person recruitment, recording, publication, evaluation, or collection of personal data. All examples, sources, permissions, approvals, and role assignments below are simulated. Phase 0 establishes a reviewable workflow; it provides no evidence of effectiveness or legal clearance for live use.

## 1. Record boundaries

Every record and export must carry `record_type=non_sworn`, a stable record ID, version, status, evidence cutoff, and this visible boundary:

> SYNTHETIC DEMONSTRATION • NON-SWORN • NOT UNDER PENALTY OF PERJURY • NOT A GOVERNMENT FILING • PARTICIPATION DOES NOT ESTABLISH TRUTH

The design contains no oath, affirmation, jurat, notarial seal, or penalty clause. Approval means permission for exact attribution in a displayed context, not a certification of truth. Participation, confidence, uncertainty, correction, and nonparticipation support no inference about honesty or character. Do not use truth scores, credibility badges, or candidate-wide ratings. A non-sworn format supplies no promise of immunity from otherwise applicable law.

Admission requires one bounded, factually assessable proposition with explicit terms, scope, cutoff, and reporting purpose. Split compound propositions. Exclude motives, predictions presented as facts, guilt determinations, unsupported accusations, and demands for private or privileged material. Apply the same criteria across parties. Phase 0 uses fictional, nonpolitical subjects only.

## 2. Distinct authorship and final proof

Maintain these visibly separated components:

| Component | Control and required contents |
|---|---|
| Question | Editorial author; proposition, definitions, scope, cutoff, purpose. |
| Participant statement | Participant-authored exact words; response type; basis of knowledge; adjacent qualifications and uncertainty. |
| Evidence map | Source provenance, support/contradiction/qualification, exact locator, limitations and unresolved conflicts. |
| Editorial findings | Independent reasoning, finding category, scope and uncertainty; clearly attributed to editors. |
| Version history | Exact approved attribution/context, publication state, changes, parents and correction links. |

Response choices include agree, disagree, qualified answer, unable to verify, do not know/recall, outside personal knowledge, and premise needs correction. Declining is private and creates no public record. Basis fields distinguish observation, records, another person's report, expert advice, inference, and a basis that cannot responsibly be published.

Before a simulated release, show the complete composite: question, attributed statement, adjacent limits, evidence map, editorial conclusion, layout, captions, and planned excerpts. The simulated participant reviews exact attribution and context and may request changes to their own words or withdraw before release. They cannot veto or rewrite an independent editorial conclusion. Editors resolve disputes in their own section; participant approval must never be represented as agreement with that conclusion.

Any substantive change to wording, scope, source selection, conclusion, placement, or excerpt context invalidates the prior composite approval and returns the new proof for review. Log purely mechanical fixes and verify meaning and visibility remain unchanged. Record exactly which version and uses were approved. No signature or approval is collected from a real person in Phase 0.

## 3. Evidence and dispute handling

For each source record ID, creator/publisher, title, date, access date, stable locator, relevant passage/data, rights, and limitations. Distinguish participant-supplied material from editorially located material. Record each source's relationship to the proposition, including adverse and qualifying evidence.

A reproducible search log records repositories searched, exact queries/filters, date range, cutoff, inclusion/exclusion reasons, failed retrievals, and negative results. A closed synthetic packet is explicitly a closed packet; its completeness says nothing about a real-world search.

Two independently assigned reviewers must check extraction, calculations, contrary evidence and finding-to-source fit before any future live release. Phase 0 simulates both roles and cannot establish actual reviewer independence. Findings are: supported by located evidence; contradicted by located evidence; mixed/partially supported; insufficient evidence; or not independently assessable. Explain proposition-specific reasoning; do not infer intent from error.

Apply these category rules to the exact bounded proposition:

- **Supported:** adequate relevant evidence supports every material part; no unresolved contrary evidence defeats that finding. Scope is limited to the search and cutoff.
- **Contradicted:** adequate relevant evidence is incompatible with a material asserted fact; identify that fact and the conflict.
- **Mixed/partially supported:** different material parts receive different findings, or credible evidence conflicts. Split the proposition when possible; report the unresolved conflict rather than average it away.
- **Insufficient evidence:** the proposition could be assessed, but the completed search lacks evidence adequate for either support or contradiction.
- **Not independently assessable:** accessible evidence cannot independently test the proposition or its stated basis; explain the access or verification barrier.

Prefer inspectable original records/data directly bearing on the proposition, then well-supported secondary analyses for interpretation and context. Unretrieved quotations and tertiary summaries are discovery leads, not substitutes for the underlying record. Relevance, provenance, completeness and known limitations control weight; primary status alone does not establish truth. Log reasons for departing from this order.

Record each reviewer's finding and material-source codes before reconciliation, disagreements, conflict adjudication and the final reason. Before live work, prespecify reliability measures and precision criteria suitable for the categories and sampling design; inspect category confusion and raw agreement as well as any appropriate chance-corrected measure. One fictional example cannot establish reviewer reliability.

Keep a dispute ID, challenged passage, proposed correction, source basis, reviewing role, response deadline, resolution, and appeal destination. An unresolved material source/calculation dispute blocks the simulated release. An interpretive disagreement may remain visible as disagreement if factual prerequisites pass and the editorial reasoning and participant's attributed response remain distinct. A second review handles appeals; unresolved cases retain their actual status.

## 4. Assets, custody, publication and corrections

Maintain separate approved source text, private master, public derivative, and excerpt/clip assets. Private masters may contain permission and internal review logs; public derivatives contain only approved public content. A record manifest identifies each asset by ID, version, exact-byte SHA-256, visibility, source/parent IDs and digests, transformation/redaction reason, approval reference, rights, status, and current-version locator. Each altered file has its own digest. Digests identify bytes, not truth or consent.

Freeze an approved source before generating derivatives. Validate every derivative against its actual parent. Excerpts retain the necessary qualification, editorial/participant attribution, boundary and durable record/version link. A misleading clip fails even if its byte digest matches its manifest.

Substantive corrections create a new version with reason, date, source basis, approval and review references. Mark prior released versions superseded and link both directions to the correction/current version. Do not silently replace claims. Distinguish corrected attribution from a changed editorial finding. If a claim is withdrawn after release, preserve a proportionate correction trail for that already-published claim; do not repurpose it into a refusal notice. Safety/privacy removals follow a separately adopted retention/removal policy; permanence is not promised.

Pre-release declines, no responses, and withdrawals remain private. Do not publish named refusal pages, invitation lists, empty participant profiles, refusal counts that expose identities, or suspicion labels.

Track reuse permissions **per asset and use**: issuer/rightsholder, permitted excerpt/edit, medium, attribution, term, correction duty, and restrictions. Approval of attribution is not a reuse license. Source rights do not automatically cover derivative images, recordings, music or third-party excerpts. Unspecified rights remain unresolved. Paid promotion, campaign use and onward licensing require separate decisions. Phase 0 uses simulated permissions and changes no repository license.

Maintain a derivative/distribution register. On correction or withdrawal, update controlled assets, notify each permitted recipient through the agreed channel, record acknowledgments/failures, and flag unresolved propagation. Do not promise recall of uncontrolled copies. Tabletop tests simulate notifications; they send none.

Before any live transition, appoint actual operator, publisher, custodians, reviewers, appeal officer and accountable backup; specify access, backups, incident response, retention, deletion, organizational closure and transfer. Keep ordinary identity checks separate from substantive editorial review. Phase 0 stores no real identity documents or participant records.

## 5. Synthetic tabletop acceptance sequence

1. **Boundary/admission:** Reject a sworn import, compound question, real-person record or missing `record_type`; accept one bounded fictional proposition.
2. **Authorship:** Strengthen a simulated quote without permission; require failure. Restore exact wording, basis and adjacent qualification.
3. **Evidence:** Recalculate the packet, search its complete inventory, inspect contrary evidence, and simulate separate reviewer decisions. Missing sources or material unresolved discrepancies block release.
4. **Composite proof:** Change a conclusion or crop a qualification after approval; invalidate approval. Permit participant disagreement without granting control of the editorial finding.
5. **Assets:** Generate separate derivatives and hashes; alter one byte and verify the prior digest no longer matches. Reject a clip with correct hash but misleading context.
6. **Permissions:** Give only text permission, then request an image or paid advertisement; leave that request unresolved rather than inventing a license.
7. **Correction:** Issue v2, retain v1's superseded status, update current pointers and trace all derivatives and simulated recipient acknowledgments.
8. **Withdrawal/custody:** Withdraw before release and verify no public refusal output. Exercise post-release correction/removal, inaccessible custodian and organizational closure scenarios.

Log expected/observed result, responsible simulated role and remaining defect. Passing tabletop cases demonstrates specification consistency only. Real participation, organizational commitments and research require their own resolved conditions and explicit transition decision. See [the synthetic example](NONSWORN_SYNTHETIC_EXAMPLE.md).

Source: [PR #5 historical explainer](../archive/pr5-2026-08-30/DGG_CLAIM_RECORD_HUMAN_EXPLAINER_v1.0.md). Its branding, efficacy claims and operating assumptions are not incorporated wholesale.
