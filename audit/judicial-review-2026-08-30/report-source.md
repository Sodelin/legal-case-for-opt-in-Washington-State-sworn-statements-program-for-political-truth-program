# Judicial review record: DGG Washington voluntary sworn-record project

**Review date:** 2026-08-30  
**Function:** Independent adversarial review / project court  
**Status:** Final research docket; not legal advice; not a launch authorization  
**Controlling disposition:** **REMANDED — NOT LAUNCH-CLEARED**

## 0. Disposition

The project has a legally plausible core: a willing participant may sign a defined factual record and take an oath or affirmation before a properly authorized Washington notary. That proposition does **not** establish that a false statement will be prosecutable, that the private act is first-degree perjury, that Washington has jurisdiction over every signer, or that the notary has certified factual truth.

Candidate v1.1 materially improves the design by making the tangible Canonical Sworn Record (CSR) the only sworn object and by quarantining remote, public-figure, livestream, and public-refusal features. A later counsel-review packet and independent paralegal audit improve the government-nexus, questioning, interstate, defamation, campaign-threshold, and power-calculation record. The project is nevertheless remanded. The live branches and canonical packet contain contradictory operating instructions, several notary-role and campaign-law defects remain, two criminal-law citations require correction, and the behavioral gates do not yet support the claimed safety decisions.

| Record | Disposition | Effect |
|---|---|---|
| `main` at `3905b470c2ab239cf2aae563e1d7b3a1adb73dd3` | **Remanded** | Existing control packet remains research/dry-run material only; no live or named-participant use. |
| Draft PR #1 at `9b695f3e45e13d60767db71ed91cf4cc668c9d09` | **Changes requested** | Do not merge until its remote-first instructions, evidence summary, statistical gates, bibliography, and source metadata are corrected. |
| Draft PR #2 at `96c5388421ed6e221c8520878458feba96e14aac` | **Changes requested** | Preserve the v1.1 and counsel-review packets as nonoperative candidates, but do not canonicalize until the mandatory directives below are satisfied and the stack is rebased or retargeted coherently. |
| Draft PR #3 at `08283fc190f23d69406b5f9cc810fbbc00d8b068` | **Substantially sustained; comment/coordination required** | Admit the independent authority audit and handoff as supplemental research. Its new corrections do not silently amend PR #2 or the canonical packet and must be implemented through tracked changes. |
| Supplied DOCX/Markdown packets | **Admitted as source material** | Preserve byte-for-byte in archive; they do not independently control operations. |

No finding in this review is a prediction that a prosecutor, court, election regulator, tax authority, or notary will accept the project’s legal theory.

## 1. Question presented

Whether the present materials support a defensible Washington pilot in which a willing participant places carefully bounded factual propositions into a fixed record, signs under oath or affirmation before a notary, and permits a related media product—without overstating criminal consequences, notarial meaning, empirical efficacy, or regulatory safe harbors.

## 2. Record and method

### 2.1 GitHub record

- Repository: `Sodelin/legal-case-for-opt-in-Washington-State-sworn-statements-program-for-political-truth-program`
- Canonical branch reviewed at `3905b470c2ab239cf2aae563e1d7b3a1adb73dd3`.
- PR #1, `research/conversation-synthesis-and-evaluation-v1`, reviewed at `9b695f3e45e13d60767db71ed91cf4cc668c9d09`.
- PR #2, `legal/participant-protocol-and-memo-v1.1`, initially reviewed at `795d97a1a505d7bdd1d2a04596d484fdd687f963` and re-reviewed at `96c5388421ed6e221c8520878458feba96e14aac` after the counsel-review packet landed. PR #2 is stacked on PR #1.
- PR #3, `audit/paralegal-independent-reaudit-2026-08-30`, reviewed at `08283fc190f23d69406b5f9cc810fbbc00d8b068`. PR #3 is stacked on PR #2 at `96c5388421ed6e221c8520878458feba96e14aac`.
- Open-PR state, changed paths, comments, reviews, and head commits were rechecked immediately before publication of this docket.

### 2.2 Supplied-file record

| Input | SHA-256 |
|---|---|
| `washington_sworn_format_concept_paper_v3.md` | `0912eb30b107d8b4a1e498942abc53e84b54b994ae18c5b49d8979444fb0ad57` |
| `washington_sworn_format_pilot_packet_v2.md` | `d0cf137ab279b9e878f251d6c5ca6b97be7dbcff1cb3aab3a41db3021fdf844d` |
| `washington_sworn_format_pilot_packet_v2-1.docx` | `bc0aa3f3e7dd21b1dc82c460ca978135ab208890d5c78d714bce3097dd75cee7` |
| `DGG_Washington_Participant_Sworn_Statement_Protocol_2026-08-30.docx` | `a6f1f703cadb3278b8b9e2d506637eaf2f267fdd0d9e5fbaa76f42e47be31030` |
| `PROJECT_ORIGIN_AND_DESIGN_RATIONALE_SUPPLEMENT.md` | `0c876a74e1e9ae8ab730d0a689eae4563df30afc4a572f944e4a0efad5e2fe2a` |
| `Washington_Voluntary_Sworn_Format_Legal_Memorandum_v1.0.docx` | `785b6f299d19638661a2e3445a044fd33ebf459ce2f2fbf7f664da1eb07ce547` |
| `ZOTERO_OBSIDIAN_INTEGRATION.md` | `88bc1812a23265e05ca1ebdff809dfe85ce934917d16a92c399648e2cd12fc93` |
| `BEHAVIORAL_EVIDENCE_AND_EVALUATION_PLAN.md` | `e08df5c9ddef6f1b1e557b146649df5dae2eb8f60862a5e3d1809ad82ba2a023` |

The three DOCX files were text-extracted, rendered, and inspected page by page: 14 pages for the archived pilot, 43 pages for the participant protocol, and 21 pages for the memorandum. The protocol has a clipped Appendix B heading and several clipped claim-ledger labels; the archived pilot has literal blockquote markers, numbering defects, and the typo “DDG-style.” These are secondary to the legal rulings but must be repaired before professional distribution.

### 2.3 Review standard

Each consequential claim was tested for:

1. an exact supporting proposition in current primary authority;
2. adverse authority, limiting language, and effective-date conditions;
3. a valid inference from authority to the proposed facts;
4. operational consistency across all live files and branches;
5. empirical transport from study population and outcome to the claimed product effect; and
6. a falsifiable launch gate rather than an aspiration or disclaimer.

Rulings use four labels:

- **Sustained:** supported as written or with only a stated boundary.
- **Qualified:** defensible only with the stated limitation.
- **Rejected:** unsupported, misleading, or contradicted.
- **Remanded:** potentially defensible, but missing facts, authority, or a required control.

## 3. Holdings at a glance

| Proposition | Ruling |
|---|---|
| Washington notaries may generally administer oaths and perform a verification on oath of a statement in a record. | **Sustained.** |
| The CSR paper original can be the sole sworn object while interview audio, transcript, PMR, annotations, and source commentary remain unsworn. | **Sustained, subject to eliminating incorporation by reference.** |
| The notary certifies factual truth, legal sufficiency, proposition content, competence, capacity, or voluntariness. | **Rejected.** |
| A knowingly false CSR necessarily constitutes false swearing. | **Rejected as certainty; plausible but untested application.** |
| A private-media verification necessarily constitutes first-degree perjury. | **Rejected; colorable but unresolved.** |
| Same-session or later correction guarantees a statutory retraction defense. | **Rejected.** |
| A Washington notary or Washington server automatically creates territorial jurisdiction. | **Rejected.** |
| RCW 10.88.250 governs Washington’s demand for a signer located in another state. | **Rejected; direction of the statute was reversed.** |
| Private voluntariness is a constitutional safe harbor. | **Rejected; it is risk-reducing, not dispositive.** |
| A private DGG invitation is constitutionally required to be viewpoint-neutral. | **Rejected as a First Amendment duty; may be retained as an internal editorial, study, tax, and risk-control rule.** |
| FEC AO 2008-14 creates a blanket Internet-press exemption. | **Rejected; fact-bound analogy only.** |
| The $100 amount printed in RCW 29B.25.120(2) is the current reporting threshold. | **Rejected; WAC 390-05-400 adjusts it to $1,000 effective 2026-01-01.** |
| Existing oath studies establish that this format will make political speakers truthful. | **Rejected.** |
| Observed 90% comprehension, nonsignificance, or zero incidents proves the safety gate passed. | **Rejected.** |
| Phase 0 synthetic tests and a nonpublic, in-person, Washington-only wet-ink feasibility phase are the current conservative path. | **Sustained, after the control packet is reconciled.** |

## 4. Washington criminal-law rulings

### 4.1 Authorized oath and valid record

**Sustained.** [RCW 5.28.010](https://app.leg.wa.gov/RCW/default.aspx?cite=5.28.010) separately authorizes Washington notaries to administer oaths and affirmations. [RCW 42.45.030(2)](https://app.leg.wa.gov/RCW/default.aspx?cite=42.45.030) defines a verification on oath or affirmation as the individual declaring that a statement in a record is true. Personal appearance, identity, signature, and certificate requirements remain separately governed by [RCW 42.45.040](https://app.leg.wa.gov/RCW/default.aspx?cite=42.45.040), [.050](https://app.leg.wa.gov/RCW/default.aspx?cite=42.45.050), and [.130](https://app.leg.wa.gov/RCW/default.aspx?cite=42.45.130).

This establishes administrator authority and a lawful notarial form. It does not establish falsity, knowledge, materiality, an official proceeding, territorial jurisdiction, admissibility, or prosecution.

### 4.2 False swearing

**Sustained as plausible; qualified as untested.** [RCW 9A.72.010(5)](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.72.010) recognizes an oath administered by a person authorized by law, and [RCW 9A.72.040](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.72.040) addresses knowingly making a false statement under an oath required or authorized by law; its text does not require an official proceeding or materiality. The 1995 amendment added the authorized-administrator route, so *State v. Hovrud*, 60 Wn. App. 573, cannot be treated as applying unchanged to present text. Strict construction and fair-warning concerns remain.

No reported Washington appellate criminal decision located in this review applies the amended route to a wholly voluntary private political-media verification. The public description must therefore remain: **“possible false-swearing exposure; exact private-media application unresolved.”**

The *Pearsall-Stipek* false-swearing discussion is at 141 Wn.2d 774–78, and retraction at 779. The canonical 766–71 pinpoint must be corrected.

### 4.3 First-degree perjury

**Sustained only as colorable and unresolved.** [RCW 9A.72.020](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.72.020) requires a materially false statement in an official proceeding. [RCW 9A.72.010](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.72.010) includes a notary in the definition, but no controlling case located decides whether this proposed private-media verification is a “proceeding heard before” a notary, what the proceeding’s course or outcome would be, or what could be material to it.

*State v. Jacobson*, 74 Wn. App. 715, 725–26, involved an affidavit prepared, submitted, and used to support a court hearing. It does not hold that every private notarization is an official proceeding. *State v. Smith*, 97 Wn.2d 856, and *State v. Otton*, 185 Wn.2d 673, interpret an evidence rule; they are analogies, not holdings on RCW 9A.72.010(4).

The memorandum’s *Lewis* discussion also requires precision. *State v. Lewis*, 85 Wn.2d 769, 770–72, repeated the *Douglas/Dodd* rule about signing before a notary but itself involved signing before the notary’s employee while the notary was absent. The Court treated the absence as an irregularity and limited its holding to those facts.

Second-degree perjury under [RCW 9A.72.030](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.72.030) is not a general fallback for this design; its enumerated settings must be satisfied. The packet should not imply that every materially false written oath automatically falls into that offense.

### 4.4 Knowledge, proof, and qualifications

**Qualified.** [RCW 9A.72.080](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.72.080) treats an unqualified assertion of a proposition the speaker does not know to be true as equivalent to a knowingly false statement. Providing “unknown,” “cannot verify,” “not recalled,” “decline,” and participant-authored qualifications is therefore a sound control, not an immunity device.

*State v. Arquette*, 178 Wn. App. 273, 283–90, applies the traditional two-witness/strong-corroboration rule to perjury. No square appellate holding was located extending that rule to false swearing; a pattern instruction is not controlling authority.

### 4.5 Retraction and correction

**Categorical protection rejected.** [RCW 9A.72.060](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.72.060) requires retraction in the same proceeding, before exposure is manifest, and before the falsity substantially affects the proceeding. Whether this private event is a proceeding remains unresolved. *Pearsall-Stipek*, 141 Wn.2d at 779, rejected a correction made in a separate proceeding.

Operationally, the v1.1 rule is sound: correct only before freeze; after oath/signature/certificate, preserve the original and require a completely new CSR and notarial act for any substantive replacement. Never call that process statutory immunity.

### 4.6 Limitations, jurisdiction, and interstate process

The three-year felony and two-year gross-misdemeanor periods, with statutory tolling language, are accurately grounded in [RCW 9A.04.080](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.04.080), but never-resident and travel facts remain case-dependent.

**Automatic jurisdiction rejected.** [RCW 9A.04.030](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.04.030) requires qualifying Washington conduct or a statutorily specified Washington result. Notary location, server location, audience, or subject matter is not an independent hook unless tied to an offense element or qualifying effect.

**Extradition analysis remanded.** [RCW 10.88.250](https://app.leg.wa.gov/RCW/default.aspx?cite=10.88.250) authorizes Washington’s governor to surrender a person found in Washington to another state. It does not govern a Washington demand for a signer found elsewhere; the asylum state’s UCEA analogue and executive process control. Remove all enforcement forecasts such as “practically unlikely,” “more plausible outcomes,” or “fight likely.” List legal gates, not predictions.

Collateral witness-tampering or intimidation law is also **unresolved on these novel facts**. Do not reassure participants that every such provision is categorically irrelevant, and do not threaten or market those laws. Any benefit, threat, retaliation, referral bargain, or effort to alter testimony-like information is a stop event requiring counsel review of the exact statute and facts.

## 5. Notarial and operational rulings

### 5.1 Sworn-object boundary

**Sustained with one mandatory correction.** The paper CSR may be the sole sworn object. The PMR, interview, transcript, captions, source packet, fact-checking commentary, and later media statements must remain expressly unsworn.

The remaining “incorporated record” field leaks outside text into the sworn payload. Prohibit incorporation by reference. If outside text is deliberately adopted, reproduce or physically append it inside the CSR, page-number it, assign proposition IDs, and include it in the adoption clause. Otherwise it remains unsworn.

The supplemental counsel packet’s questioning rule is **sustained**: the interviewer’s question is unsworn, while the participant must author or expressly adopt a complete standalone statement, basis, and visible qualification. A bare yes/no that silently imports a disputed DGG premise is prohibited. A decline makes no sworn assertion and must be omitted from the adopted-proposition index. Knowledge, recall, and inability-to-verify responses require deliberate scope treatment in the exact adoption clause.

### 5.2 Notary role and certificate

The notary determines identity and signature requirements, witnesses the oath/signature as applicable, completes the certificate, and may refuse under [RCW 42.45.060](https://app.leg.wa.gov/RCW/default.aspx?cite=42.45.060). The certificate establishes compliance with the required notarial act; it does not certify truth, content, legal sufficiency, competence, capacity, or voluntariness.

Delete every requirement that the notary approve proposition admission, record wording, source choice, or certificate interpretation. Counsel and the participant control content. A nonattorney notary may confirm willingness and operational ability, but [WAC 308-30-240](https://app.leg.wa.gov/WAC/default.aspx?cite=308-30-240) and [RCW 42.45.230](https://app.leg.wa.gov/RCW/default.aspx?cite=42.45.230) prohibit unauthorized legal assistance.

Describe capacity and voluntariness as grounds for the notary to refuse—not findings certified to the audience.

### 5.3 Identity, journal, privacy, and loss

Add an in-person identity route under [RCW 42.45.050](https://app.leg.wa.gov/RCW/default.aspx?cite=42.45.050): personal knowledge or satisfactory evidence. KBA/credential analysis is not the Phase 1 mechanism. DGG must not copy identification or record credential numbers.

The participant notice must disclose that the journal contains required identifying information, including the signer’s name, address, identification method, and in-person journal signature; withdrawing DGG publication authorization cannot erase the notary’s statutory journal record. State the exact retention rule in [RCW 42.45.180](https://app.leg.wa.gov/RCW/default.aspx?cite=42.45.180): ten years after the last act chronicled in that journal, subject to the attorney-notary exception. The tangible journal remains the notary’s exclusive property and under direct control. Lost or stolen journals are reported by the notary to DOL; DGG keeps only its own incident record.

### 5.4 Fees, promotion, recording, and medium

- Under [WAC 308-30-220](https://app.leg.wa.gov/WAC/default.aspx?cite=308-30-220), $15 is a maximum for the verification, not a fixed or mandatory fee. Actual copying costs may be added. Travel charges must be agreed in advance and disclosed as separate and not legally required; they need not be described as actual cost.
- Add a [WAC 308-30-230](https://app.leg.wa.gov/WAC/default.aspx?cite=308-30-230) promotion control: do not use the seal or notarial title to endorse DGG, an interview, testimonial, thumbnail, contest, or product.
- Keep signed pre-consent as project policy, but correct the legal rationale. [RCW 9.73.030(3)](https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.030) expressly recognizes a recorded announcement. State that DGG elects not to rely on that method alone.
- Wet-ink, tangible, in-person operation is the conservative Phase 1 path. Cite enacted [2026 Wash. Laws ch. 21](https://lawfilesext.leg.wa.gov/biennium/2025-26/Htm/Bills/Session%20Laws/House/2158-S.SL.htm), not only a bill report, for the January 1, 2027 remote change. Any later remote/electronic branch requires a fresh statutory, rule, provider, technology, and privacy review.

### 5.5 Record integrity

Define an “access-safe scan.” If it is redacted, it is a derivative and needs its own digest. The internal executed-scan digest cannot be presented as authenticating different public bytes. Keep the executed original, executed scan, redacted derivative, manifest, and public copy as distinct objects with distinct identifiers and hashes.

After the notarial act, no same-session edit, page substitution, interlineation, white-out, or oral cure is permitted. A substantive change requires a new version and complete new act.

## 6. Federal, election, media, privacy, and entity rulings

### 6.1 Private action and speech

Private, optional editorial conduct ordinarily is not state action. A commissioned notary does not automatically turn DGG’s invitation, editing, status labels, or publication into government conduct. Reopen the analysis if government coerces, significantly encourages, jointly controls, funds with operative conditions, or uses DGG to threaten consequences. See [*Manhattan Community Access Corp. v. Halleck*](https://www.supremecourt.gov/opinions/18pdf/17-1702_h315.pdf), [*Blum v. Yaretsky*](https://tile.loc.gov/storage-services/service/ll/usrep/usrep457/usrep457991/usrep457991.pdf), and [*NRA v. Vullo*](https://www.supremecourt.gov/opinions/23pdf/22-842_6kg7.pdf).

“Viewpoint-neutral invitation” is an internal editorial, study-integrity, tax/entity, and risk-control choice—not a private First Amendment duty. Government-compelled access or script control would raise different editorial-speech concerns under [*Miami Herald v. Tornillo*](https://tile.loc.gov/storage-services/service/ll/usrep/usrep418/usrep418241/usrep418241.pdf) and [*303 Creative LLC v. Elenis*](https://www.supremecourt.gov/opinions/22pdf/21-476_c185.pdf).

Political falsehood is not categorically outside First Amendment review. [*United States v. Alvarez*](https://tile.loc.gov/storage-services/service/ll/usrep/usrep567/usrep567709/usrep567709.pdf) does not immunize all knowing falsehoods, but it forecloses a casual assumption that falsity alone ends constitutional analysis.

The supplemental counsel packet’s government-separation matrix is **sustained as conservative policy**. No public grant, contract, co-branding, official consequence, government-selected participant/question/source, data feed, standing referral, or agency publication control belongs in the present design. Any such fact requires a new memorandum. Federal state action and Washington public-records/functional-equivalency are different questions. Government use or retention of project records, official-device communications, public funding, delegated function, or government creation/involvement may create separate records, ethics, procurement, retention, or open-meetings consequences under the exact facts. See [*Nissen v. Pierce County*](https://www.courts.wa.gov/opinions/pdf/908753.pdf) and [*Horvath v. DBIA Services*](https://www.courts.wa.gov/opinions/pdf/1033397.pdf).

### 6.2 Nonparticipant labels and defamation

The v1.1 nonpublication rule for identified invitee status in Phases 0–2 is sustained. If a later phase considers status publication, “invited; declined this format” is usable only when exactly documented; silence requires “no response as of [date].” Never publish “refused truth,” “failed the oath,” “would not risk perjury,” or a credibility badge.

Audience testing and disclaimers are safety controls, not tort-law immunity. Washington recognizes a false implication created by material omitted facts when the omissions contradict the publication’s false impression. It does not recognize defamation by implication based only on the negative implication of entirely true statements. See *Mohr v. Grant*, 153 Wn.2d 812, and *Yeakey v. Hearst Communications, Inc.*, 156 Wn. App. 787. A factual error, material omission, misleading edit, false-light theory, or another state’s law can still create exposure, and ignoring adverse test results may worsen fault evidence. Federal constraints include [*Milkovich v. Lorain Journal*](https://tile.loc.gov/storage-services/service/ll/usrep/usrep497/usrep497001/usrep497001.pdf), [*Masson v. New Yorker Magazine*](https://tile.loc.gov/storage-services/service/ll/usrep/usrep501/usrep501496/usrep501496.pdf), and [*New York Times v. Sullivan*](https://tile.loc.gov/storage-services/service/ll/usrep/usrep376/usrep376254/usrep376254.pdf).

Personality-rights consent under [RCW 63.60.050](https://app.leg.wa.gov/RCW/default.aspx?cite=63.60.050) may be written or oral, express or implied, and [RCW 63.60.070](https://app.leg.wa.gov/RCW/default.aspx?cite=63.60.070) contains broad authentic political, newsworthy, public-interest, comment, criticism, and specified-media exemptions. Those rules defeat categorical “written consent is always legally required” language. DGG should still require a use-specific written release covering production, excerpts, thumbnails, promotion, syndication, fundraising, reuse, corrections, and advertising. Forged or synthetic likeness, material voice/image alteration, or endorsement-like promotion requires a separate current-law review.

### 6.3 Federal campaign and broadcast decision tree

FEC AO 2008-14 is a fact-bound press-exemption analogy, not blanket protection. It left volunteer briefings unresolved and limited protection for fundraising links, solicitation mechanisms, and functions outside ordinary press activity.

Before any candidate-specific publication or promotion, the memorandum must apply, as a decision tree:

1. [11 C.F.R. § 100.26](https://www.ecfr.gov/current/title-11/chapter-I/subchapter-A/part-100/subpart-A/section-100.26): whether the communication is a public communication; organic own-site content differs from paid third-party placement.
2. [11 C.F.R. §§ 100.73](https://www.ecfr.gov/current/title-11/chapter-I/subchapter-A/part-100/subpart-C/section-100.73) and [100.132](https://www.ecfr.gov/current/title-11/chapter-I/subchapter-A/part-100/subpart-E/section-100.132): ownership/control and bona fide press-function analysis.
3. [11 C.F.R. § 109.21](https://www.ecfr.gov/current/title-11/chapter-I/subchapter-A/part-109/subpart-C/section-109.21): request/suggestion, material involvement, substantial discussion, candidate-prepared material, common vendor, former employee, compensation, and paid amplification.
4. [11 C.F.R. § 110.13](https://www.ecfr.gov/current/title-11/chapter-I/subchapter-A/part-110/section-110.13): if DGG stages a candidate debate, require an eligible staging organization, at least two candidates, no promotion of one, and pre-established objective criteria. A one-candidate interview is not a debate.
5. [47 C.F.R. § 73.1941](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-C/part-73/subpart-H/section-73.1941): ordinary Internet video has no general equal-time rule, but licensed-station carriage requires a use/exemption analysis.

### 6.4 Washington campaign law and entity/tax status

- [RCW 29B.10.160](https://app.leg.wa.gov/RCW/default.aspx?cite=29B.10.160) creates fact gates for contributions, coordination, republication, fair-market value, and a conditional regular-news-medium exclusion.
- [RCW 29B.10.220(2)(c)](https://app.leg.wa.gov/RCW/default.aspx?cite=29B.10.220) is a qualifying news-item exclusion from the definition of electioneering communication—not a universal media safe harbor.
- [RCW 29B.25.120](https://app.leg.wa.gov/RCW/default.aspx?cite=29B.25.120) applies only after the activity qualifies as the specified independent expenditure. The `$100` amount printed in subsection (2) is not the current threshold: [WAC 390-05-400](https://app.leg.wa.gov/WAC/default.aspx?cite=390-05-400) adjusts it to **$1,000 effective 2026-01-01**. Classification, timing, medium, registration, attribution, sponsor identification, and other adjusted thresholds remain separate.

Entity documents, funding, candidate contacts, requests, material involvement, fair-market value, distribution, press structure, insurance, and tax status are launch facts, not assumptions. [IRS guidance](https://www.irs.gov/charities-non-profits/other-non-profits/social-welfare-organizations) permits some political activity by a §501(c)(4) only when it is not the organization’s primary activity; there is no fixed safe percentage, and §527(f) tax may apply. A §501(c)(3) cannot intervene in candidate campaigns.

### 6.5 Pennsylvania comparator

Use narrow language. Pennsylvania ordinarily lacks the proposed parallel private false-swearing route because 18 Pa.C.S. §4903(b) requires a statement legally required to be sworn, while §4903(a) concerns an official proceeding or intent to mislead a public servant. Recognition of a Washington notarial act does not import Washington criminal law or prove jurisdiction. This is a comparator, not an interstate workaround.

## 7. Behavioral-evidence rulings

### 7.1 What the evidence supports

The 2024 meta-analysis by Zickfeld and colleagues synthesized 445 effects from 121 articles, 91,683 participants, and 33 countries. The oath/pledge subset was approximately `g = .27`, 95% CI `[.19, .36]`, with heterogeneity and publication-bias concerns. This supports testing an ex ante commitment mechanism; it does not establish efficacy in political interviews.

The later megastudy is mandatory adverse/limiting authority: Zickfeld et al., *Nature Human Behaviour* 9 (2025) 169–187, DOI [`10.1038/s41562-024-02009-0`](https://doi.org/10.1038/s41562-024-02009-0). Across 21 oath conditions and 21,506 participants, only 10 conditions produced significant improvements, gains were about 4.5–8.5 percentage points, and the pooled effect was roughly 3.9 points / `d ≈ .09`. Content mattered substantially. A publication-bias-corrected estimate for the earlier literature could be around `g = .14`.

Pennycook and Rand’s 20 experiments (`N = 26,863`) support an accuracy-prompt mechanism for online sharing intentions. False-headline sharing declined from about `.341` to `.309`: about 3.2–3.4 absolute points and 10% relative, not ten percentage points. The result does not measure a political speaker’s truthfulness.

Fact-checking and correction meta-analyses support source and correction design, not oath efficacy. Add the two Jacquemet studies as transport/adverse sources: effects depended on a loaded laboratory setting, and individual lying could not always be observed.

### 7.2 Required causal design

Separate the estimands:

- **Audience framing:** holding content constant can estimate what the sworn-format label does to understanding, trust calibration, and stigma. It cannot estimate speaker truthfulness.
- **Speaker process:** randomize before answer generation, use multiple speakers and propositions, and model crossed speaker/item effects. Actors can validate presentation and process, not real-world honesty.
- **Ground truth:** predefine an evidence hierarchy, independent blinded adjudicators, disagreement rules, and inter-rater reliability. Agreement with a DGG packet is not automatically truth.

Retain an IRB/HRPP determination gate. Private research is not automatically federally covered, but institutional and funding conditions, sensitive political data, recording, deception, and plans for generalizable publication require a documented determination.

### 7.3 Numeric gates

Replace the current gates as follows:

| Current phrase | Required gate |
|---|---|
| “At least 90% comprehend the notary role” | One-sided 95% lower confidence bound is at least `.90`; an observed `.90` is insufficient. |
| “No practically meaningful increase” | Pre-specify an absolute risk-difference noninferiority margin `Δ`; require the upper one-sided 95% bound to be below `Δ`. |
| “No material partisan interaction” | Pre-specify an interaction smallest effect size of interest and require equivalence/precision analysis plus stratum estimates. |
| “Zero critical incidents” | Treat as a stop rule, report opportunity denominator and upper bound; with zero independent incidents, the approximate 95% upper bound is `3/N`. |
| “Process-integrity score: 70/100” | Publish and validate a rubric or remove the number. |

The supplemental counsel packet’s rule—observed comprehension of at least 90% but a one-sided 95% lower bound of only 85%—is **rejected**. If 90% is the safety threshold, the lower confidence bound, not just the point estimate, must be at least 90%.

For the existing orientation table, exact standalone calculations at two-sided `.05` and 80% power are 788/506/352 total for two equal groups at `d=.20/.25/.30`, and 969/432/246 total for three balanced groups at `f=.10/.15/.20`. Those remain lower-bound orientation values. The newer evidence suggests smaller effects: under the same independent two-group assumptions, `d=.14` requires roughly 802 per arm and `d=.09` roughly 1,939 per arm—before clustering, attrition, multiplicity, co-primary safety outcomes, or interactions.

## 8. Cross-document and version-control rulings

### 8.1 Dispositive contradiction

PR #1’s README, First Reader Brief, and Continuation Guide recommend a 2026 remote, electronic-record pilot and an experienced remote notary. PR #2 expressly limits the current candidate to nonpublic, in-person, Washington-only, tangible wet-ink operation and quarantines remote work. Because PR #2 is stacked on PR #1 and does not amend those files, merging both would publish incompatible instructions.

The main canonical `operations/DGG_PILOT_CONTROL_PACKET.md` also remains operative-looking and conflicts with v1.1 by mandating remote Lane A, giving the notary a “voluntariness” role, requiring notary content approval, and permitting same-session correction after the act.

**Holding:** choose one controlling architecture. For the present phase, the court adopts v1.1’s in-person, paper-only approach. Retarget/rebase the stack, remove remote instructions from current operational routes, and either deprecate or conform the old control packet before any candidate is called canonical.

### 8.2 Supplemental packet received during review

PR #2’s later counsel-review packet is **admitted and substantially sustained for counsel review/Phase 0 only**. Its conspicuous nonuse banner, complete-standalone-statement rule, government-separation matrix, state-action caveats, professional question worksheet, and written-gate structure improve the project. They do not cure the base memorandum/protocol automatically. Its remaining defects include the incorporation pathway, the 90%-point-estimate/85%-lower-bound comprehension gate, the zero-incident inference, and any source copy that repeats an adjusted campaign amount as though the printed statute were current.

PR #3’s independent authority audit and cross-project handoff are **admitted as supplemental research**. The court sustains its corrected WAC threshold, *Mohr/Yeakey* distinction, exact orientation sample totals, personality-rights nuance, witness-law caution, public-repository boundary, and update-packet protocol. Its separately gated 2026 fixed-record RON discussion does not alter this order’s current in-person-paper restriction. Because PR #3 is stacked on PR #2, its findings must be implemented by traceable edits; they do not silently rewrite the candidate or canonical files.

### 8.3 Archive and hierarchy

- Keep the archived pilot as superseded source material. It contains the obsolete public-refusal label, an incorrect *Lewis* reporter citation, remote preference, and overbroad interstate language.
- Add an explicit status banner to every noncanonical memorandum, brief, protocol, and archived form.
- Maintain one machine-readable manifest mapping each file to `canonical`, `candidate`, `supplement`, `archive`, or `withdrawn` status, plus the governing commit and supersession target.
- Never place real participant CSR/PMR material, releases, identities, journal data, incident records, or privileged advice in the public repository.

### 8.4 Zotero and Obsidian

Before merge, `research/authorities.bib` must add the 2025 megastudy, both Jacquemet studies, missing federal/campaign/defamation authorities, Pennsylvania provisions, the three Title 29B provisions, FEC AO 2008-14, and IRS guidance.

Replace generic legal `@misc` records with legal metadata including court, reporter, jurisdiction, docket, enactment/effective date, official URL, and verification date. Do not present `year={2026}` as the enactment year of a continuously updated statute. Extend authority notes with:

- `version/effective_date`
- `last_verified`
- `official_url`
- `negative_treatment/citator_date`
- `supersedes/superseded_by`

A current commercial citator check remains a release gate for every case. This review did not perform Shepard’s, KeyCite, or an equivalent subscription citator.

## 9. Mandatory directives

The following are merge and launch gates, not suggestions.

| ID | Directive | Gate |
|---|---|---|
| D-01 | Declare the in-person, Washington-only, tangible wet-ink Phase 1 architecture controlling; remove or quarantine present-tense remote instructions. | Merge PRs #1/#2 |
| D-02 | Deprecate or conform the existing `DGG_PILOT_CONTROL_PACKET.md`; eliminate notary content approval, voluntariness certification, and post-act same-session correction. | Canonicalization |
| D-03 | Prohibit incorporation by reference into the CSR; physically include any adopted outside text. | Canonicalization |
| D-04 | Rewrite notary role/certificate language to track RCW 42.45.030/.040/.050/.060/.130 and WAC 308-30-240. | Canonicalization |
| D-05 | Correct identity, journal, lost/stolen-journal, privacy, fee, travel, and promotion controls. | Phase 0 exit |
| D-06 | Correct recording-consent rationale while retaining stricter signed pre-consent as project policy. | Canonicalization |
| D-07 | Distinguish internal executed scan and redacted public derivative with separate identifiers and digests. | Phase 0 exit |
| D-08 | Correct *Pearsall-Stipek* and *Lewis* treatments. | Merge |
| D-09 | Reverse the RCW 10.88.250 extradition analysis and delete enforcement predictions. | Merge |
| D-10 | Preserve false swearing as plausible/untested and first-degree perjury as colorable/unresolved; prohibit prosecution claims. | Permanent public-claim rule |
| D-11 | Add the federal campaign/broadcast decision tree and fact-specific AO 2008-14 limitations. | Candidate-specific planning |
| D-12 | Narrow Washington news/election exclusions; apply WAC 390-05-400’s current adjusted amounts; and document all entity, funding, coordination, distribution, and tax facts. | Phase 3 |
| D-13 | Label viewpoint neutrality as project policy, not a private constitutional duty. | Merge |
| D-14 | Retain nonpublication of identified invitee statuses through Phase 2; subject exact later language to powered safety testing and media review. | Phase 3 |
| D-15 | Add Zickfeld 2025 and adverse/transport evidence; remove any promise that science proves political truthfulness. | Merge |
| D-16 | Correct the orientation power totals and replace observed-percentage/nonsignificance/zero-event gates with confidence-bound, noninferiority/equivalence, and denominator-based rules. | Study preregistration |
| D-17 | Separate audience and speaker estimands; randomize before answer generation and establish blinded ground-truth adjudication. | Study preregistration |
| D-18 | Repair bibliography/legal-item metadata and complete a current commercial citator check. | Publication-ready memorandum |
| D-19 | Repair DOCX rendering defects and add status banners plus a canonical-file manifest. | External distribution |
| D-20 | Obtain written Washington criminal/notary, media/privacy/defamation, election/tax/entity, records-security, and independent methods reviews on the exact final artifacts and facts. | Any live/named pilot |
| D-21 | Make no categorical witness-law reassurance or threat; treat benefits, threats, retaliation, referral bargaining, or testimony-influence concerns as stop/counsel events. | Permanent participant-safety rule |

## 10. Launch-gate order

The project remains in Phase 0. Synthetic and tabletop testing may continue with no real participant record, no named public figure, no publication, no livestream, and no claim of criminal enforceability.

Advancement requires all of the following:

1. one reconciled canonical architecture and file hierarchy;
2. exact CSR, oath/adoption, verification certificate, consent, release, and journal notice reviewed in writing by Washington counsel and an independent notary;
3. documented venue, participant location, entity, funding, campaign contact, distribution, tax, insurance, custody, retention, legal hold, breach, and demand-response facts;
4. repeated synthetic process tests of wrong-version, post-freeze change, identity/privacy capture, journal loss, custody, scan/hash, correction, demand letter, and campaign coordination scenarios;
5. preregistered, independently reviewed audience and speaker research with the corrected numeric gates;
6. current primary-law recheck and commercial citator report; and
7. a final independent readback showing no public file implies truth certification, automatic liability, dishonesty from nonparticipation, or launch authorization.

## 11. Robustness and failure-mode analysis

The design is defensible only if it resists the following category errors:

| Failure mode | Required reconstruction |
|---|---|
| Lawful notarization → factual truth | Publish the exact notary-limitation notice and keep source adjudication separate. |
| Possible offense → predictable prosecution | Treat criminal law as unresolved background; sell no deterrence guarantee. |
| Disclaimer → no defamatory implication | Test the complete message and context; retain independent media review and stop power. |
| One valid file → coherent project | Enforce a canonical manifest and cross-PR conflict check before merge. |
| Statistical nonsignificance → safety | Use noninferiority/equivalence margins and confidence bounds. |
| Zero observed events → low risk | Report exposure denominator and upper bound; keep zero events as an operational stop rule. |
| Oath-lab result → truthful politicians | Test content, population, setting, outcome, and mechanism separately. |
| Notary independence → notary product approval | Limit the notary to the authorized act; separate content, counsel, release, and records roles. |
| Hash of original → hash of redacted public file | Give every derivative its own identity and digest. |
| Washington act → nationwide criminal reach | Analyze conduct/effects and the signer state independently. |

Confidence is high on the text of cited statutes and regulations, high on the identified internal contradictions, moderate on applying false-swearing text to the novel private facts, and deliberately unresolved on first-degree perjury, territorial jurisdiction, prosecution, extradition, and final regulatory treatment. Those unresolved questions are not defects that rhetoric can cure; they are the reason for a counsel-gated feasibility design.

## 12. Primary-source ledger

### Washington law

- [RCW 5.28.010 — officials authorized to administer oaths](https://app.leg.wa.gov/RCW/default.aspx?cite=5.28.010)
- [Chapter 42.45 RCW — notarial acts](https://app.leg.wa.gov/rcw/default.aspx?cite=42.45&full=true)
- [Chapter 308-30 WAC — notary rules](https://app.leg.wa.gov/wac/default.aspx?cite=308-30&full=true)
- [2026 Wash. Laws ch. 21 — remote changes effective 2027-01-01](https://lawfilesext.leg.wa.gov/biennium/2025-26/Htm/Bills/Session%20Laws/House/2158-S.SL.htm)
- [Chapter 9A.72 RCW — perjury and false swearing](https://app.leg.wa.gov/rcw/default.aspx?cite=9A.72&full=true)
- [RCW 9A.04.030 — territorial applicability](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.04.030)
- [RCW 9A.04.080 — limitations](https://app.leg.wa.gov/RCW/default.aspx?cite=9A.04.080)
- [RCW 10.88.250 — nonfugitive surrender](https://app.leg.wa.gov/RCW/default.aspx?cite=10.88.250)
- [RCW 9.73.030 — recording consent](https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.030)
- [RCW 63.60.050 — consent to personality-right use](https://app.leg.wa.gov/RCW/default.aspx?cite=63.60.050)
- [RCW 63.60.070 — personality-rights exemptions](https://app.leg.wa.gov/RCW/default.aspx?cite=63.60.070)
- [RCW 29B.10.160 — contribution and news conditions](https://app.leg.wa.gov/RCW/default.aspx?cite=29B.10.160)
- [RCW 29B.10.220 — electioneering communication](https://app.leg.wa.gov/RCW/default.aspx?cite=29B.10.220)
- [RCW 29B.25.120 — independent-expenditure reporting](https://app.leg.wa.gov/RCW/default.aspx?cite=29B.25.120)
- [WAC 390-05-400 — current adjusted campaign-finance amounts](https://app.leg.wa.gov/WAC/default.aspx?cite=390-05-400)
- [*Nissen v. Pierce County* — official-device/private-account public records](https://www.courts.wa.gov/opinions/pdf/908753.pdf)
- [*Horvath v. DBIA Services* — functional-equivalency analysis](https://www.courts.wa.gov/opinions/pdf/1033397.pdf)

### Federal law and guidance

- [*Manhattan Community Access Corp. v. Halleck*](https://www.supremecourt.gov/opinions/18pdf/17-1702_h315.pdf)
- [*NRA v. Vullo*](https://www.supremecourt.gov/opinions/23pdf/22-842_6kg7.pdf)
- [*United States v. Alvarez*](https://tile.loc.gov/storage-services/service/ll/usrep/usrep567/usrep567709/usrep567709.pdf)
- [*Miami Herald v. Tornillo*](https://tile.loc.gov/storage-services/service/ll/usrep/usrep418/usrep418241/usrep418241.pdf)
- [*303 Creative LLC v. Elenis*](https://www.supremecourt.gov/opinions/22pdf/21-476_c185.pdf)
- [11 C.F.R. §§ 100.26, 100.73, 100.132, 109.21, 110.13](https://www.ecfr.gov/current/title-11/chapter-I)
- [47 C.F.R. § 73.1941](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-C/part-73/subpart-H/section-73.1941)
- [FEC AO 2008-14](https://www.fec.gov/updates/ao-2008-14-internet-tv-station-qualifies-for-press-exemption/)
- [IRS — social-welfare organizations](https://www.irs.gov/charities-non-profits/other-non-profits/social-welfare-organizations)

### Behavioral evidence

- Zickfeld et al., “Committed (dis)honesty,” DOI [`10.1037/bul0000429`](https://doi.org/10.1037/bul0000429)
- Zickfeld et al., “Effectiveness of ex ante honesty oaths in reducing dishonesty depends on content,” DOI [`10.1038/s41562-024-02009-0`](https://doi.org/10.1038/s41562-024-02009-0)
- Pennycook et al., “Shifting attention to accuracy can reduce misinformation online,” DOI [`10.1038/s41467-022-30073-5`](https://doi.org/10.1038/s41467-022-30073-5)
- Jacquemet et al., “Truth Telling Under Oath,” DOI [`10.1287/mnsc.2017.2892`](https://doi.org/10.1287/mnsc.2017.2892)
- Jacquemet, James & Luchini, 2021, DOI [`10.1371/journal.pone.0244958`](https://doi.org/10.1371/journal.pone.0244958)

## 13. Final conclusion

The project should continue as a carefully bounded research and protocol-design effort. Its strongest product is not a “perjury interview”; it is a provenance architecture that separates a fixed participant-authored factual record from unsworn media commentary, preserves corrections, exposes sources and uncertainty, and empirically tests whether the audience understands the boundary.

That product is worth testing. It is not yet ready to launch, and neither live PR is ready to merge without the corrections ordered above.
