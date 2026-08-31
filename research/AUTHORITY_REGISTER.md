# Authority register and Zotero crosswalk

**Register date:** 2026-08-30  
**Status:** Candidate research infrastructure; not canonical and not launch-cleared.  
**Authority cutoff:** 2026-08-30  
**Zotero destination:** `My Library / Codex Submissions`, collection key `RKFIXEK4`, tagged `project/washington-sworn-format`  
**Source packages:** [`authorities.bib`](authorities.bib) and [`authorities-supplement-2026-08-30.bib`](authorities-supplement-2026-08-30.bib)  
**Mutation boundary:** This task is Zotero read-only. See the designated single-writer [`ZOTERO_HANDOFF.md`](ZOTERO_HANDOFF.md).

## Purpose and rules

This register connects consequential project claims to the legal items prepared for Zotero. It is an audit crosswalk, not a substitute for reading the sources. The matching substantive summaries and unresolved questions remain in [`report-source.md`](report-source.md) and [`GAP_MATRIX.md`](GAP_MATRIX.md).

Every imported legal item must use Zotero's **Case** or **Statute** type where applicable and carry:

- the official title or case name and full citation;
- court, jurisdiction, docket, reporter, enactment, or effective-date metadata as applicable;
- an official URL when one is available;
- `last_verified: 2026-08-30`;
- the linked project claim IDs;
- a proposition-and-limit note;
- `negative_treatment: counsel citator check required` for consequential cases; and
- the tags `project/washington-sworn-format`, `origin/codex-ai`, `research/deep`, and `review/human-required`.

An official URL establishes source provenance, not current positive treatment. No consequential case is release-cleared until counsel records a current citator result and date.

## Core constitutional and election-speech authorities

| ID | Authority and official source | Project use | Material limit / adverse point | BibLaTeX key | Zotero item key |
|---|---|---|---|---|---|
| CON-US-01 | [U.S. Const. amend. I](https://constitution.congress.gov/constitution/amendment-1/) | Government speech restrictions, compelled speech, association, and political-speech baseline. | Does not regulate a genuinely private publisher merely because a commissioned notary performs an act. State action and coercion remain fact-dependent. | `us_const_amendment_i` | `8H7YQY3X` |
| CON-WA-01 | [Wash. Const. art. I, §§ 5–7, 12](https://leg.wa.gov/state-laws-and-rules/washington-state-constitution/?showall=true) | Washington free-speech, oath, privacy, and privileges/immunities baselines. | Section 6 validates conscience-binding modes of oath; it does not make every sworn statement a prosecutable offense. | `wash_const_article_i` | `E2B9CLWC` |
| WA-ELECT-01 | [RCW 29B.30.070](https://app.leg.wa.gov/RCW/default.aspx?cite=29B.30.070) | Current, narrow Washington false-political-advertising statute and legislative findings. | Requires specified defamatory content, actual malice, and clear-and-convincing proof; it is not a general truth commission. Title 29B took effect in 2026. | `wash_rcw_29b_30_070` | `DUP82BF7` |
| CASE-WA-RICKERT | [*Rickert v. Public Disclosure Commission*, 161 Wn.2d 843, 168 P.3d 826 (2007)](https://www.courts.wa.gov/opinions/index.cfm?fa=opinions.showOpinion&filename=777691MAJ) | Controlling warning against government adjudication of nondefamatory campaign falsity. | Official-court page supplies docket metadata but redirects the current opinion text to Washington Reports; obtain reporter copy and citator treatment before reliance. | `rickert_2007` | `ISEBXIZ9` |
| CASE-WA-119 | *State ex rel. Public Disclosure Commission v. 119 Vote No! Committee*, 135 Wn.2d 618, 957 P.2d 691 (1998) | Plurality warning that government may not direct political debate or serve as guardian of the public mind. | Plurality posture; official opinion copy and current treatment remain counsel gates. Current legislative findings summarize the decision. | `vote_no_1998` | `AAN5PM3L` |
| CASE-US-ALVAREZ | [*United States v. Alvarez*, 567 U.S. 709 (2012)](https://www.supremecourt.gov/opinions/boundvolumes/567bv.pdf) | Falsity alone is not a categorical exception to the First Amendment; broad content-based criminalization is constitutionally dangerous. | No single rationale controlled all applications. Narrow laws tied to legally cognizable harm, fraud, perjury, or government process require separate analysis. | `alvarez_2012` | `2R94AN3B` |
| CASE-US-SBA | [*Susan B. Anthony List v. Driehaus*, 573 U.S. 149 (2014)](https://www.supremecourt.gov/opinions/boundvolumes/573BV.pdf) | Demonstrates pre-enforcement standing risk created by a broad campaign-falsity complaint regime. | Standing decision, not a merits holding that every false-campaign-speech rule is invalid. | `sba_list_2014` | `BXXCTM3G` |
| CASE-US-AID | [*Agency for International Development v. Alliance for Open Society International*, 570 U.S. 205 (2013)](https://www.supremecourt.gov/opinions/boundvolumes/570bv.pdf) | Government may define a funded program but cannot ordinarily compel a participant's belief or speech outside the program. | A genuinely private, optional format presents a different state-action question. | `aid_aosi_2013` | `9VCZZP3C` |
| CASE-US-SHURTLEFF | [*Shurtleff v. Boston*, 596 U.S. 243 (2022)](https://www.supremecourt.gov/opinions/21pdf/20-1800_7lho.pdf) | Government-speech/private-forum classification turns on history, public perception, and actual control. | A neutral repository open to private speakers may be a forum rather than government speech; branding alone is not dispositive. | `shurtleff_2022` | `B6MFN89E` |
| CASE-US-AFPF | [*Americans for Prosperity Foundation v. Bonta*, 594 U.S. 595 (2021)](https://www.supremecourt.gov/opinions/20pdf/19-251_p86b.pdf) | Compelled disclosure can burden association and must be narrowly tailored under exacting scrutiny. | Does not prohibit voluntary, informed disclosure by participants; collection and publication must remain genuinely optional and minimized. | `afpf_bonta_2021` | `JPXFJGBN` |
| CASE-US-MCINTYRE | [*McIntyre v. Ohio Elections Commission*, 514 U.S. 334 (1995)](https://www.supremecourt.gov/opinions/boundvolumes/514bv.pdf) | Anonymous political advocacy receives strong protection. | Does not prevent a speaker from voluntarily attaching identity to a record; government-conditioned identity disclosure is a separate issue. | `mcintyre_1995` | `T4DXWNR6` |
| CASE-US-BURDICK | [*Burdick v. Takushi*, 504 U.S. 428 (1992)](https://www.supremecourt.gov/opinions/boundvolumes/504bv.pdf) | Election regulations are assessed according to the character and magnitude of the burden and the state's interests. | Does not validate a candidate truth badge, ballot label, or oath condition. | `burdick_1992` | `GXK4SSHI` |
| CASE-US-WHITE | [*Republican Party of Minnesota v. White*, 536 U.S. 765 (2002)](https://www.supremecourt.gov/opinions/boundvolumes/536bv.pdf) | Candidate speech lies at the core of First Amendment protection. | Judicial-election context; exact rule and governmental role matter. | `republican_party_white_2002` | `5M9JXEWC` |
| CASE-HI-ANCHETA | [*Ancheta v. Watada*, 135 F. Supp. 2d 1114 (D. Haw. 2001)](https://law.justia.com/cases/federal/district-courts/FSupp2/135/1114/2503374/) | Closest located adverse comparator: optional pledge plus public non-signer identification and censure can still coerce and chill speech. | Federal trial-court decision outside Washington; source mirror is not an official court repository. Verify full docket, later history, and citator status. | `ancheta_2001` | `Q5H8NB2E` |

## Oath, notarial, criminal-process, and evidence authorities

| ID | Authority and official source | Project use | Material limit / adverse point | BibLaTeX key | Zotero item key |
|---|---|---|---|---|---|
| WA-OATH-STAT | [Chapter 5.28 RCW](https://app.leg.wa.gov/rcw/default.aspx?cite=5.28&full=true) | General authority and form for administering Washington oaths. | Does not answer every certificate question under chapter 42.45 RCW. | `wash_rcw_5_28` | `BM6B5JPV` |
| WA-FS-STAT | [Chapter 9A.72 RCW](https://app.leg.wa.gov/rcw/default.aspx?cite=9A.72&full=true) | Defines oath, official proceeding, first- and second-degree perjury, false swearing, proof, retraction, and lack-of-knowledge rules. | Offense elements, territorial jurisdiction, proof, discretion, and constitutional application remain independent gates. | `wash_rcw_9a_72` | `JS7J38CN` |
| WA-NOTARY-STAT | [Chapter 42.45 RCW](https://app.leg.wa.gov/RCW/default.aspx?cite=42.45&full=true) | Governs verifications, presence, identity, refusal, certificates, journals, prohibited conduct, and remote acts. | A notary authenticates the act, identity, signature, and oath—not factual truth; pending 2027 changes require version control. | `wash_rcw_42_45` | `VXLPKSUN` |
| WA-NOTARY-WAC | [Chapter 308-30 WAC](https://app.leg.wa.gov/WAC/default.aspx?cite=308-30&full=true) | Operational rules for Washington notaries, fees, journals, technology, and remote acts. | Rules are subject to active implementation work; recheck before any use, particularly after 2027-01-01. | `wash_wac_308_30` | `FEUBE69N` |
| WA-2027-NOTARY | [2026 Wash. Laws ch. 21](https://lawfilesext.leg.wa.gov/biennium/2025-26/Htm/Bills/Session%20Laws/House/2158-S.SL.htm) | Enacted future-law expansion for remote tangible records and standalone remote oaths. | Effective 2027-01-01, not on the research cutoff; rulemaking and certificate treatment remain open. | `wash_laws_2026_ch_21` | `VK59GNPA` |
| CASE-WA-HOVRUD | [*State v. Hovrud*, 60 Wn. App. 573, 805 P.2d 250 (1991)](https://law.justia.com/cases/washington/court-of-appeals/1991/60-wash-app-573.html) | Strict-construction and fair-warning adverse authority under the pre-1995 oath definition. | Predates the 1995 authorized-administrator amendment; official opinion and current treatment remain gates. | `hovrud_1991` | `UKZHS2GT` |
| CASE-WA-PEARSALL | [*In re Recall of Pearsall-Stipek*, 141 Wn.2d 756, 10 P.3d 1034 (2000)](https://caselaw.findlaw.com/court/wa-supreme-court/1486118.html) | Confirms false swearing lacks an official-proceeding/materiality element and discusses retraction. | Recall-sufficiency posture, not a criminal conviction; nonofficial mirror pending official reporter verification. | `pearsall_stipek_2000` | `JUTZ8X2W` |
| CASE-WA-LEWIS | [*State v. Lewis*, 85 Wn.2d 769, 539 P.2d 677 (1975)](https://law.justia.com/cases/washington/supreme-court/1975/43613-1.html) | Narrow oath-formality proposition. | Notary-absence facts and limited holding do not validate defective notarization generally. | `lewis_1975` | `HEXGIC9C` |
| CASE-WA-JACOBSON | [*State v. Jacobson*, 74 Wn. App. 715, 876 P.2d 916 (1994)](https://law.justia.com/cases/washington/court-of-appeals/1994/74-wash-app-715.html) | Affidavit submitted and used in court can be “in” an official proceeding; illustrates strong Washington effects. | Does not decide whether a private media session is an official proceeding or whether ordinary political publication creates territorial jurisdiction. | `jacobson_1994` | `KNWZCJY7` |
| CASE-WA-ARQUETTE | [*State v. Arquette*, 178 Wn. App. 273, 314 P.3d 426 (2013)](https://www.courts.wa.gov/opinions/pdf/D2%2042546-7-II%20%20Published%20Opinion.pdf) | Washington's heightened corroboration rule for perjury. | Does not establish every false-swearing proof rule or prove guilt from a contradiction or fact-check. | `arquette_2013` | `JMJF2GWQ` |
| CASE-WA-STOUT | [*In re Citizen Complaint by Stout v. Felix*, 198 Wn.2d 180, 493 P.3d 1170 (2021)](https://www.courts.wa.gov/opinions/pdf/986134.pdf) | Criminal charging remains an executive/public function; a private affidavit does not create a prosecution. | Majority and concurrence must be distinguished; use only after reporter/citator verification. | `stout_felix_2021` | `L2PGKDK8` |

## Publication, privacy, records, and outreach authorities

| ID | Authority and official source | Project use | Material limit / adverse point | BibLaTeX key | Zotero item key |
|---|---|---|---|---|---|
| WA-ANTI-SLAPP-01 | [Chapter 4.105 RCW](https://app.leg.wa.gov/RCW/default.aspx?cite=4.105&full=true) | Washington Uniform Public Expression Protection Act; procedural risk in suits based on public-expression activity. | Does not immunize defamation, privacy violations, or unsupported accusations; exclusions and burden-shifting require exact analysis. | `wash_rcw_4_105` | `9RFTE4GX` |
| WA-PRA-01 | [Chapter 42.56 RCW](https://app.leg.wa.gov/rcw/default.aspx?cite=42.56&full=true) | Public-records and privacy rules if a Washington agency receives or maintains program records. | No generic exemption was located for candidate sworn submissions; exemptions are specific and must be applied record by record. | `wash_rcw_42_56` | `K9XFWRGT` |
| WA-RETENTION-01 | [RCW 40.14.010](https://app.leg.wa.gov/rcw/default.aspx?cite=40.14.010) | Broad public-record definition relevant to agency retention. | Retention periods come from applicable schedules and agency function, not this definition alone. | `wash_rcw_40_14_010` | `YZ4A32U7` |
| WA-UETA-01 | [Chapter 1.80 RCW](https://app.leg.wa.gov/rcw/default.aspx?cite=1.80&full=true) | Legal recognition and agency controls for electronic records/signatures. | Does not override specific notarial, public-records, security, or agency-acceptance requirements. | `wash_rcw_1_80` | `YVNYINKV` |
| WA-LOBBY-01 | [Chapter 29B.50 RCW](https://app.leg.wa.gov/RCW/default.aspx?cite=29B.50&full=true) | Lobbying and grassroots-lobbying classification for outreach meant to influence legislation. | Current PDC-adjusted thresholds, definitions, exemptions, payer facts, and timing must be rechecked before a public campaign. | `wash_rcw_29b_50` | `XJQ779Q2` |
| CASE-WA-TAN | [*Tan v. Le*, 177 Wn.2d 649, 300 P.3d 356 (2013)](https://www.courts.wa.gov/opinions/pdf/860211.pdf) | Washington defamation elements, public-figure fault, and context/rhetorical-hyperbole analysis. | Court-hosted slip opinion may be superseded by reporter edits; current treatment remains a counsel gate. | `tan_v_le_2013` | `CPCJEMUI` |
| CASE-WA-SISLEY | [*Sisley v. Seattle Public Schools*, 180 Wn. App. 83 (2014)](https://www.courts.wa.gov/opinions/pdf/693166.pdf) | Defamation-by-implication and falsity requirements. | Exact context and omissions control; a disclaimer is not a safe harbor. | `sisley_2014` | `4MA5S664` |
| CASE-WA-JHA | [*Jha v. Khan*, 24 Wn. App. 2d 377 (2022)](https://www.courts.wa.gov/opinions/pdf/837681.pdf) | Washington false-light and implication limits. | Verify current reporter and treatment; substantially true facts may still require contextual analysis. | `jha_2022` | `TAJ94DX7` |

## Voluntary-program comparators

| ID | Authority and official source | Project use | Material limit / adverse point | BibLaTeX key | Zotero item key |
|---|---|---|---|---|---|
| COMP-IL-01 | [10 ILCS 5/29B-10](https://www.ilga.gov/documents/legislation/ilcs/documents/001000050K29B-10.htm) | Official example of a voluntary fair-campaign pledge. | Does not establish efficacy or validate a notarized truth-enforcement system. | `illinois_fair_campaign_pledge` | `TYSH62FR` |
| COMP-ME-01 | [21-A M.R.S. § 1101](https://legislature.maine.gov/statutes/21-a/title21-Asec1101.pdf) | Official moral fair-campaign pledge comparator. | Aspirational language and local administration differ from DGG's proposed record format. | `maine_fair_campaign_pledge` | `BSLF2J5Q` |
| COMP-UT-01 | [Utah Code § 20A-9-206](https://le.utah.gov/xcode/Title20A/Chapter9/C20A-9-S206_1800010118000101.pdf) | Official voluntary, public-record pledge with a short retention rule. | Public filing does not prove constitutional safety for refusal labels, truth adjudication, or criminal framing. | `utah_fair_campaign_pledge` | `V3RWWQ9M` |
| COMP-WV-01 | [W. Va. Code § 3-1B-5](https://code.wvlegislature.gov/3-1B-5/) | Official voluntary fair-campaign pledge comparator. | Comparator only; wording, enforcement, and constitutional history require separate review. | `west_virginia_fair_campaign_pledge` | `RCCF96WP` |

## Supplemental live-corpus reconciliation

A second read-only reconciliation compared every nonarchive legal citation in the memorandum, source ledger, public packet, outreach toolkit, evidence packet, operations packet, and audit controls against the initial 37 records. A final closeout also captured materially relied-on official reports and administrative guidance. Together they produced a deduplicated 69-item delta:

- 17 cases, including the remaining Washington criminal/evidence decisions, state-action and compelled-speech cases, defamation/false-light cases, disclosure counterweights, and the Pennsylvania media comparator;
- 17 Washington session laws, statutes, regulations, or court-rule entries;
- 13 federal statutes or regulations;
- five Pennsylvania authorities; and
- three full-framework expansions for the Illinois, Maine, and West Virginia pledge comparators; and
- 14 official supporting records: ten Web Pages, three Reports, and one Document covering WPIC 118.12, HB 2158 history/report/rulemaking, the Washington DOL portal/guide and two specifically relied-on notarial-act pages, State Archives and PDC guidance, FCC DA 26-68, and Pennsylvania DOS guidance.

The complete delta and item-level notes are in [`authorities-supplement-2026-08-30.bib`](authorities-supplement-2026-08-30.bib). It has **not** been imported by this task. The deterministic destination, metadata, source-rights, attachment, duplicate, correction, digest, and readback requirements are in [`ZOTERO_HANDOFF.md`](ZOTERO_HANDOFF.md), assigned to single-writer task `01a05517-896e-7613-9851-ee623e2e3dfe`.

## Design conclusions supported by the combined record

1. **Private-first is the most defensible path.** While remanded, Phase 0 is only a private, nonpublic fictional mock with no signer, oath, or notarial act. A later private nonprofit repository is lower risk than a state truth-adjudication office, but still requires reviewed supersession and defamation, privacy, campaign-law, notarial, methods, and neutrality review.
2. **Authenticate provenance, never “truth.”** The durable public object, if later authorized, is the exact statement, identity/act provenance, source bundle, version, and correction history. The notary does not adjudicate content.
3. **No coercive status architecture.** Do not publish a nonparticipant blacklist, ballot badge, refusal label, censure, benefit/penalty, or enforcement recommendation. *Ancheta*, *Rickert*, *119 Vote No!*, and *Alvarez* make those features central adverse risks.
4. **No automatic criminal claim.** Potential false swearing is fact-specific and constitutionally untested in this setting; perjury, jurisdiction, proof, charging, and interstate process require additional predicates.
5. **Outreach starts with comprehension, not conversion.** The current transparent-repository ask is to review and critique the packet. A later controlled comprehension test requires the missing owner, response, privacy/consent, accessibility, retention, and methods infrastructure; neither stage asks anyone to take an oath or pressure a candidate.

## Zotero verification record

| Field | Current value |
|---|---|
| Local API / connector | Operational on 2026-08-30 |
| Authorized parent collection | `Codex Submissions` (collection key `RKFIXEK4`) |
| Selection control | Initial probe found unrelated `TV shows`; no write occurred until `Codex Submissions` was selected and read back for the first batch |
| Project child collection | Not created as of this register version |
| Imported batch | 37 entries from [`authorities.bib`](authorities.bib); unique tag count read back as 37 |
| Item-key crosswalk | Populated above after local-API readback confirmed all 37 records as Zotero `Case` or `Statute` items in collection `RKFIXEK4` |
| Supplemental reconciliation | 69 entries prepared in [`authorities-supplement-2026-08-30.bib`](authorities-supplement-2026-08-30.bib); not imported or mutated by this read-only task |
| Single-writer dependency | Task `01a05517-896e-7613-9851-ee623e2e3dfe`; digest-bound plan and readback receipt pending |
| Known metadata correction | Existing `vote_no_1998` record used the current-statute URL; corrected Git metadata points to the opinion mirror and requires a Washington Reports copy. Single-writer correction/duplicate policy pending |
| Required human gate | Counsel citator and official-reporter review for every consequential case |

## Update protocol

For each later research pass:

1. recheck the primary source and effective date;
2. update the legal item and its proposition/limit note in Zotero;
3. prepare a digest-bound BibLaTeX delta and update [`ZOTERO_HANDOFF.md`](ZOTERO_HANDOFF.md);
4. update this register, [`report-source.md`](report-source.md), and [`GAP_MATRIX.md`](GAP_MATRIX.md) in that order;
5. record supersession, adverse treatment, and the reason for any changed public wording; and
6. route mutations only through the designated Zotero single-writer and reconcile its readback receipt; and
7. regenerate repository manifests only after all content edits stop.
