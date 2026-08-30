# New-source reconciliation and audit record

**Audit date:** August 30, 2026  
**Project:** Digital Ground Game Washington voluntary sworn-record format  
**Purpose:** preserve the newly supplied packet, show what changed in candidate v1.1, and keep source/design/legal conclusions traceable  
**Status:** public-safe process audit; contains no participant data or privileged advice

## 1. What was actually supplied

The user referred to a “new PDF,” but no new PDF was present in the supplied workspace. The two new principal artifacts were DOCX files. They were treated as the intended new design and legal packet, rendered for visual review, and preserved unchanged.

| Supplied artifact | Bytes | SHA-256 | Treatment |
|---|---:|---|---|
| `DGG_Washington_Participant_Sworn_Statement_Protocol_2026-08-30(1).docx` | 97,209 | `a6f1f703cadb3278b8b9e2d506637eaf2f267fdd0d9e5fbaa76f42e47be31030` | Immutable archive input; design source, not launch clearance |
| `Washington_Voluntary_Sworn_Format_Legal_Memorandum_v1.0(1).docx` | 67,140 | `785b6f299d19638661a2e3445a044fd33ebf459ce2f2fbf7f664da1eb07ce547` | Immutable archive input; legal source, superseded by candidate v1.1 subject to counsel |
| `PROJECT_ORIGIN_AND_DESIGN_RATIONALE_SUPPLEMENT(1).md` | 12,400 | `0c876a74e1e9ae8ab730d0a689eae4563df30afc4a572f944e4a0efad5e2fe2a` | Already preserved by draft PR #1 as `memorandum/PROJECT_ORIGIN_AND_DESIGN_RATIONALE_SUPPLEMENT.md` |
| `ZOTERO_OBSIDIAN_INTEGRATION(1).md` | 2,763 | `88bc1812a23265e05ca1ebdff809dfe85ce934917d16a92c399648e2cd12fc93` | Already preserved by draft PR #1 as `research/ZOTERO_OBSIDIAN_INTEGRATION.md` |
| `BEHAVIORAL_EVIDENCE_AND_EVALUATION_PLAN(1).md` | 13,538 | `e08df5c9ddef6f1b1e557b146649df5dae2eb8f60862a5e3d1809ad82ba2a023` | Already preserved by draft PR #1 as `research/BEHAVIORAL_EVIDENCE_AND_EVALUATION_PLAN.md` |

The earlier concept paper and pilot packet remain governed by `audit/ARCHIVE_CHECKSUMS.md`. Supplemental Markdown already on draft PR #1 remains governed by `audit/SUPPLEMENT_CHECKSUMS.md`. This change does not overwrite either set.

### Derived candidate checksums

| Candidate artifact | Bytes | SHA-256 |
|---|---:|---|
| `operations/DGG_PARTICIPANT_SWORN_STATEMENT_PROTOCOL_v1.1.md` | 27,490 | `55d0f774e24cd00a94fe9073a2de3151ca99901c66abec4a620b12897c260db3` |
| `memorandum/WASHINGTON_VOLUNTARY_SWORN_FORMAT_LEGAL_MEMORANDUM_v1.1.md` | 36,125 | `36d04a2e13fbe207ef85e727ae11f57650e555028d931d4b0bdcd33887154ced` |

The reconciliation file does not list its own checksum because adding that value to the file would change it. Its Git blob and enclosing commit provide the immutable repository identity.

## 2. Extraction and visual review

- The new legal memorandum extracted to approximately 8,272 words and rendered to 21 pages. No material clipping or overlap was found in the reviewed rendering.
- The new participant protocol extracted to approximately 16,395 words and rendered to 43 pages. The substance was readable, but the review found layout defects in the supplied rendering, including a stranded heading and clipped appendix/claim-ledger labels on several pages.
- Candidate v1.1 is therefore supplied as citation-stable Markdown. The original DOCX files remain immutable evidence of the source packet rather than silently edited “final” copies.

## 3. Core design retained

Candidate v1.1 preserves the new packet's strongest commitments:

- a Washington-first, voluntary, counsel-gated, “criminal-law quiet” pilot;
- an exact **Canonical Sworn Record (CSR)** separated from the unsworn **Public Media Record (PMR)**;
- participant authorship or express adoption of each answer;
- unknown, cannot-verify, not-recalled, qualification, and question-specific decline choices;
- an independent notary who controls the act but does not certify substantive truth;
- a green/amber/red/green “sworn airlock” around the exact record;
- no named nonparticipation status until audience-safety testing passes;
- append-only version and correction history;
- staged dry-run, feasibility, audience, speaker, public, and later remote gates; and
- success measured by precision, provenance, uncertainty, correction, and calibrated trust—not prosecution.

## 4. Material corrections made

| Source-packet issue | Candidate v1.1 correction | Why it matters |
|---|---|---|
| Phase 1 medium allowed a “stable PDF/electronic record” without fully fixing electronic-notary requirements. | Phase 1 is tangible, wet-ink, in-person, Washington-only. Electronic/RON instructions are quarantined. | An electronic record requires an endorsed electronic-records notary and selected tamper-evident technology; an ordinary PDF/e-signature is insufficient. |
| The record appeared to contain or publish its own hash. | External pre-sign content manifest plus a separate final-executed-scan digest. | A document cannot straightforwardly contain its own final-byte digest, and signature/stamp changes the bytes. |
| Publication language conflicted with the nonpublic early phases. | Phases 0–1 close, quality-check, and archive; named publication begins only at Phase 3 after safety/release gates. | Removes a direct operating contradiction. |
| Recorded verbal consent could occur only after capture had begun. | Layered written consent precedes capture; a clear recorded opening follows; late entrants trigger a pause and renewed consent. | Avoids circular consent and unconsented capture. |
| A postpublication “separately signed supplemental CSR” could be described as sworn without a new act. | Three exclusive paths: administrative notice, fully new sworn CSR/notarial act, or expressly unsworn participant note. | A signature alone does not create a new sworn verification. |
| The boundary of the sworn payload could include sources/metadata by implication. | Exact pages and proposition IDs are adopted; source annotations and administration annexes are expressly unsworn. | Makes the legal and evidentiary object identifiable. |
| Custody of the executed original was unclear. | Named original custodian, handoff receipt, sealed storage, access log, scan reconciliation, retention, destruction, and legal hold. | The notary journal is not the CSR; the paper original needs its own chain. |
| One operator held too many incompatible powers. | Dual signoff for freeze, correction, certificate/scan reconciliation, publication, and incident restart. | Adds maker/checker separation. |
| Camera controls could expose ID and journal data. | Mandatory notarial privacy blackout and quarantine rule. | The journal contains identifying information and remains under notary control. |
| No mandatory pre-oath hold covered known falsity/material contradiction. | Counsel hold for known/probable falsity, material inconsistency, deceptive ambiguity, inadequate basis, or defamatory implication. | DGG should not knowingly facilitate or publish a defective factual commitment. |
| “Notary verified procedure” could imply more than the certificate supports. | “The notary certified the required notarial act; the notary did not investigate or certify factual truth.” | Matches the statutory certificate function. |
| “Notarized factual statement” could create a truth halo. | Preferred description: “participant statement signed under oath before a Washington notary.” | Allows audience testing before using a higher-risk label. |
| The supplied memo framed voluntariness as a “constitutional safe harbor.” | Voluntariness is a risk-reducing design feature, not a safe harbor. | A later prosecution would still be state action; private design cannot pre-decide constitutional application. |
| The source protocol categorically said chapter 63.60 RCW requires a written likeness license. | A release remains an operational control, but counsel must analyze statutory political/news/public-interest/program exemptions and commercial/fundraising uses. | RCW 63.60.070 contains broad conditional exemptions; the categorical statement was overbroad. |
| The source memo's table asked whether pre-2027 remote oral authority was clear, while recommending not to rely on it. | Direct conclusion: do not rely on remote authority in v1.1; recheck the 2027 branch after the effective date. | Eliminates ambiguity and avoids premature use of future law. |
| Earlier material allowed a public “Declined Sworn Format” label. | No identified invitee/nonparticipant status through Phase 2; any later wording must pass a no-adverse-inference experiment. | DGG knows many innocent reasons to decline; a dishonesty implication is avoidable. |
| Campaign law could be cited under superseded Title 42.17A numbering or treated as a footnote. | Candidate v1.1 uses current Title 29B and makes entity, coordination, press, expenditure, tax, funding, and insurance facts launch gates. | These classifications can determine reporting, disclaimer, tax, and coordination risk. |

## 5. Revised legal holding

### Strong statutory basis

Washington defines a verification on oath as a declaration before a notarial officer that a statement **in a record** is true. It authorizes notarial acts, requires identification/signature findings for a verification, requires a contemporaneous certificate, and separately authorizes notaries to administer oaths. These texts strongly support a short signed record with a verification/jurat. [Chapter 42.45 RCW](https://app.leg.wa.gov/RCW/default.aspx?cite=42.45&full=true); [RCW 5.28.010](https://app.leg.wa.gov/RCW/default.aspx?cite=5.28.010).

### Plausible, untested false-swearing theory

False swearing requires a knowingly false statement under an oath required or authorized by law. The definition treats an oath as authorized when administered by a person authorized by law to administer oaths. That creates a coherent textual theory for a proper notarial verification, but no located Washington appellate case applies it to this private political-media design. [RCW 9A.72.010(5), .040](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.72&full=true).

### Colorable but unresolved first-degree-perjury theory

First-degree perjury adds materiality and an official proceeding. The official-proceeding definition includes a “notary” in its list, but it does not say that every private notarization is a “proceeding heard before” a notary, and materiality remains separate. No product claim may convert that open issue into a holding. [RCW 9A.72.010(2), (4), .020](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.72&full=true).

### Not product claims

Candidate v1.1 does not claim truth certification, guaranteed deterrence, automatic criminal exposure, Washington jurisdiction over all nonresidents, automatic extradition, correction immunity, a campaign/media exemption, or direct empirical proof of politician accuracy.

## 6. Evidence and evaluation reconciliation

The supplied behavioral plan correctly labels the evidence as indirect. Candidate v1.1 preserves that limitation and separates:

- an **audience-safety experiment**, which can test comprehension, calibrated confidence, truth-certification error, correction uptake, and refusal stigma while holding content constant; and
- a **speaker-process experiment**, which is separately required to test accuracy, qualification, source use, evasion, correction, coercion, and selection effects.

The next research version must specify estimands, randomization unit, speaker/item clustering, ground-truth adjudication, treatment fidelity, coding reliability, follow-up, multiplicity, attrition, equivalence margins, numeric thresholds, and null/adverse publication. A voluntary field pilot alone cannot identify causal speaker effects because participation is selected.

## 7. Primary-source verification set

Official sources checked for the revision include:

- [Chapter 42.45 RCW](https://app.leg.wa.gov/RCW/default.aspx?cite=42.45&full=true)
- [RCW 5.28.010](https://app.leg.wa.gov/RCW/default.aspx?cite=5.28.010)
- [Chapter 9A.72 RCW](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.72&full=true)
- [RCW 9A.04.030](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.04.030)
- [Chapter 308-30 WAC](https://app.leg.wa.gov/WAC/default.aspx?cite=308-30&full=true)
- [RCW 9.73.030](https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.030)
- [Chapter 63.60 RCW](https://app.leg.wa.gov/RCW/default.aspx?cite=63.60&full=true)
- [SHB 2158 official bill report](https://lawfilesext.leg.wa.gov/biennium/2025-26/Htm/Bill%20Reports/House/2158-S%20HBR%20PL%2026.htm)
- [RCW 29B.10.160](https://app.leg.wa.gov/RCW/default.aspx?cite=29B.10.160)
- [RCW 29B.10.220](https://app.leg.wa.gov/RCW/default.aspx?cite=29B.10.220)
- [RCW 29B.25.120](https://app.leg.wa.gov/RCW/default.aspx?cite=29B.25.120)

The official sources were read for current statutory text and effective-date distinctions. A commercial citator, privileged entity/fact investigation, and counsel signoff were not performed and remain explicit gates.

## 8. Repository landing plan and conflict control

The Washington project already has concurrent work on draft PR #1, branch `research/conversation-synthesis-and-evaluation-v1`, head `9b695f3e45e13d60767db71ed91cf4cc668c9d09`. Candidate v1.1 is intentionally stacked from that exact head so it includes, but does not overwrite, the origin, Zotero, behavioral, outreach, and continuation work.

This change adds only:

- `archive/input-drafts/2026-08-30/DGG_Washington_Participant_Sworn_Statement_Protocol_2026-08-30.docx`
- `archive/input-drafts/2026-08-30/Washington_Voluntary_Sworn_Format_Legal_Memorandum_v1.0.docx`
- `operations/DGG_PARTICIPANT_SWORN_STATEMENT_PROTOCOL_v1.1.md`
- `memorandum/WASHINGTON_VOLUNTARY_SWORN_FORMAT_LEGAL_MEMORANDUM_v1.1.md`
- `audit/NEW_SOURCE_RECONCILIATION_2026-08-30.md`

It deliberately does not edit `README.md`, PR #1's files, the current canonical memorandum, the current Phase 0 packet, or the separate general memorandum-framework repository. Candidate v1.1 may become canonical only through a later, explicit review/merge decision.

## 9. Audit responsibility and bounded agent use

Five read-only lanes were used: live GitHub state, source-memo delta, operator design, supplements/evaluation, and Washington primary law. No lane was allowed to write, spawn more agents, or expand beyond its assigned question. Each lane closed after reporting. The audit director retained synthesis, source verification, file generation, and repository-write control.

## 10. Open gates

1. Washington counsel approval of the exact CSR adoption, oath, and verification certificate.
2. Updated case citator and reporter-pinpoint check.
3. DGG legal entity, EIN/status, funding, governance, insurance, publisher, and campaign-relationship documents.
4. Election/tax/media/privacy/defamation/personality-rights analysis on actual facts.
5. Independent notary selection and written tangible-record workflow approval.
6. Custodian, retention, destruction, legal hold, breach, and demand-response policies.
7. Participant notice, layered consent, release, withdrawal cutoff, and AI-use terms.
8. Separate audience and speaker-study preregistration with powered numeric safety gates.
9. Recheck of remote law, DOL rules, approved providers, and signer-location matrix after January 1, 2027 before any remote branch.
10. GitHub readback of every added blob, tree, commit, and pull-request diff.

Until those gates close, the correct disposition is **continue Phase 0; do not launch a named public pilot**.
