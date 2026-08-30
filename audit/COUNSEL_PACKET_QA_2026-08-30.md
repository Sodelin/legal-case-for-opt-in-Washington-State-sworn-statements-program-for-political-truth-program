# DGG counsel packet quality-assurance and provenance record

**Artifact:** `DGG_COUNSEL_REVIEW_AND_QUESTIONING_PACKET_v1.0`  
**Review cutoff:** 2026-08-30  
**Status:** Passed as a counsel-review, blank-form, synthetic-example, and Phase 0 tabletop artifact. **Not approved for live participants, an actual oath, identifiable research, publication, government use, candidate use, remote use, or interstate use.**  
**Target repository:** `Sodelin/legal-case-for-opt-in-Washington-State-sworn-statements-program-for-political-truth-program`  
**Target branch:** `legal/participant-protocol-and-memo-v1.1`  
**Target draft PR:** #2  
**Prepublication parent head observed:** `795d97a1a505d7bdd1d2a04596d484fdd687f963`

## 1. Source inventory

No project PDF was supplied in the source packet. Five Markdown files and three DOCX files were supplied. The two newest substantive DOCX files were extracted and rendered to PDF for page-by-page inspection before the new counsel packet was drafted.

| Supplied source | SHA-256 | Treatment |
|---|---|---|
| `01-washington_sworn_format_concept_paper_v3.md` | `0912eb30b107d8b4a1e498942abc53e84b54b994ae18c5b49d8979444fb0ad57` | Historical concept and provenance |
| `02-washington_sworn_format_pilot_packet_v2.md` | `d0cf137ab279b9e878f251d6c5ca6b97be7dbcff1cb3aab3a41db3021fdf844d` | Historical operating draft; superseded |
| `03-washington_sworn_format_pilot_packet_v2-1.docx` | `bc0aa3f3e7dd21b1dc82c460ca978135ab208890d5c78d714bce3097dd75cee7` | Styled historical draft |
| `04-DGG_Washington_Participant_Sworn_Statement_Protocol_2026-08-30-1-.docx` | `a6f1f703cadb3278b8b9e2d506637eaf2f267fdd0d9e5fbaa76f42e47be31030` | Principal new design source |
| `05-PROJECT_ORIGIN_AND_DESIGN_RATIONALE_SUPPLEMENT-1-.md` | `0c876a74e1e9ae8ab730d0a689eae4563df30afc4a572f944e4a0efad5e2fe2a` | Design rationale and failure tests |
| `06-Washington_Voluntary_Sworn_Format_Legal_Memorandum_v1.0-1-.docx` | `785b6f299d19638661a2e3445a044fd33ebf459ce2f2fbf7f664da1eb07ce547` | Principal new legal source |
| `07-ZOTERO_OBSIDIAN_INTEGRATION-1-.md` | `88bc1812a23265e05ca1ebdff809dfe85ce934917d16a92c399648e2cd12fc93` | Research and citation architecture |
| `08-BEHAVIORAL_EVIDENCE_AND_EVALUATION_PLAN-1-.md` | `e08df5c9ddef6f1b1e557b146649df5dae2eb8f60862a5e3d1809ad82ba2a023` | Behavioral evidence and evaluation plan |

Candidate v1.1 reconciliation inputs:

| Candidate source | SHA-256 |
|---|---|
| `DGG_PARTICIPANT_SWORN_STATEMENT_PROTOCOL_v1.1.md` | `55d0f774e24cd00a94fe9073a2de3151ca99901c66abec4a620b12897c260db3` |
| `WASHINGTON_VOLUNTARY_SWORN_FORMAT_LEGAL_MEMORANDUM_v1.1.md` | `36d04a2e13fbe207ef85e727ae11f57650e555028d931d4b0bdcd33887154ced` |
| `NEW_SOURCE_RECONCILIATION_2026-08-30.md` | `daa1525ecb493282bab27974b71f4c643697bfd68e9f2c91832b47d8340f9bdc` |

## 2. Output inventory

| Output | SHA-256 | Role |
|---|---|---|
| `DGG_COUNSEL_REVIEW_AND_QUESTIONING_PACKET_v1.0.md` | `3294952a1277b9d817e90c3a61e886c0f0e11164fd844a22b6f151290fd62418` | Canonical, citation-stable text |
| `DGG_COUNSEL_REVIEW_AND_QUESTIONING_PACKET_v1.0.docx` | `981458946f0b61521d27e994c71d49b2dc8005ec7aad5a8551d6ce1a7e224037` | Professional counsel-review document |
| `DGG_COUNSEL_REVIEW_AND_QUESTIONING_PACKET_v1.0.pdf` | `b6b8fd75f68f228fe462c3f0dffecf24427211b76c3c224f58086697f6122195` | Fixed-layout review rendering |

The Git commit containing this record is the authoritative publication event. Because a file cannot contain the hash of the commit that contains itself, the post-publication commit SHA and verification result are recorded in PR #2's coordination comment.

## 3. Independent review lanes

| Lane | Assignment | Disposition incorporated |
|---|---|---|
| JUDGE | Skeptical outside-counsel red team | **REVISE.** Approve repository drafting, blank forms, synthetic examples, and Phase 0 tabletop testing only. Hold all live/person-identifiable uses pending written counsel decisions. |
| PARALEGAL | Source reconciliation, quotation/citation control, provenance | All eight supplied sources inventoried and hashed; older/newer conflicts reconciled; exact certificate wording and reporter/citation errors corrected or flagged. |
| Government nexus | Private/state-action and public-records boundary | Phase 1 framed as private DGG activity plus a discrete independent notarial act. Any funding, contracting, co-design, agency access, official reliance, public benefit, or compelled-use fact triggers a new memorandum. |
| Question form | Professional questioning architecture | Only a participant-authored or expressly adopted standalone statement, basis, and qualification enter the sworn CSR. Interviewer questions, source notes, commentary, and PMR remain unsworn. |
| Research | Human-subjects and empirical validation | Written HRPP/IRB determination before randomized, publishable, identifiable, or speaker research; preregistered safety and effectiveness gates before expansion. |

## 4. Legal-source control

Official sources were preferred for current statutory text, rules, cases, and agency guidance. The authority review included:

- chapter 42.45 RCW and the exact RCW 42.45.140 verification short form;
- Washington recording, criminal, evidence, personality-rights, privacy/data, public-records, retention, ethics, procurement, shield, and public-expression authorities identified in the packet;
- federal state-action cases including *Lugar*, *Blum*, *Rendell-Baker*, *Brentwood*, and *Halleck*;
- Washington public-records authorities including *Nissen* and the 2025 *Horvath* functional-equivalency decision; and
- 45 C.F.R. part 46 and OHRP decision materials.

Known citation-control items are stated as limitations rather than hidden:

- *State v. Lewis* is corrected to 85 Wn.2d 769, 539 P.2d 677 (1975), subject to current citator review.
- *Smith* and *Otton* are treated as evidence-rule analogies, not holdings that this private format is an official proceeding.
- RCW 42.45.140's short form is quoted exactly; factual blanks remain for the notary.
- First-degree perjury is not presented as a public-facing project claim.
- False swearing is described as a textually plausible candidate theory, not a settled application.
- Notarization is not represented as proof of truth, government approval, automatic admissibility, or immunity.

No commercial citator was available. Current Washington counsel must Shepardize/KeyCite all consequential authorities, approve the exact oath and certificate, and issue a signed, fact-specific opinion before live use.

## 5. Content and design verification

The final packet contains:

- an executive decision brief and explicit reliance limits;
- a plain-language explanation of what the format is, how it is used, and why it might be useful;
- a government-connection and state-action matrix;
- a professional question-admission test and detachable worksheet;
- a one-question-per-block CSR form, source/counter-source disclosure, response taxonomy, adopted-proposition index, adoption clause, exact statutory certificate, notary control sheet, correction process, and public-copy rule;
- legal argument/counterargument matrices covering notarial, criminal, evidentiary, publication, privacy, IP, campaign, entity, tax, data, accessibility, public-records, and research issues;
- research questions, Common Rule decision path, candidate safety bounds, stop rules, and expansion gates;
- a counsel decision sheet, outside-counsel red-team disposition, authority list, citation warnings, Zotero/Obsidian workflow, process-integrity review, and synthetic example.

## 6. DOCX structural and accessibility QA

Automated accessibility audit:

- high findings: 0;
- medium findings: 0;
- low findings: 0.

Package and layout audit:

- one Letter section (`12240 × 15840` twips);
- one-inch margins on all four sides (`1440` twips);
- 435 paragraphs, 86 styled headings, 15 tables, and 57 hyperlinks;
- all 15 tables use fixed page-safe width and indentation (`9360`, `120` twips);
- all 107 table rows carry no-split control;
- all 15 header rows repeat across pages;
- no tracked changes, track-revision setting, comment nodes, or comment references;
- no custom document properties; creator field is blank;
- page-number field is present;
- required status, government, question-form, certificate, review-disposition, decision-sheet, and conclusion sections are present.

An empty `comments.xml` package part created by the document converter remains, but it contains zero comments and has zero references in the document. It does not expose reviewer identity or content.

## 7. PDF/render QA

The final DOCX was rendered after privacy scrubbing. The final PDF is:

- 37 pages;
- US Letter, 612 × 792 points;
- tagged;
- unencrypted;
- free of JavaScript;
- PDF 1.7.

All 37 pages were inspected at original-resolution render quality in ten contact sheets. The initial render revealed split table rows. The formatter was corrected to apply no-split control to every row and repeat all table headers; the packet was rebuilt, rerendered, and all 37 pages were re-inspected. The final pass found no clipping, overflow, stranded table fragments, or unintended blank pages. Section-transition whitespace is intentional.

## 8. GitHub coordination and collision control

Before publication, PR #2 was observed as draft, clean, and mergeable at head `795d97a1a505d7bdd1d2a04596d484fdd687f963`, with five preexisting changed files and no issue comments, review comments, or newer update packet. Immediately before updating the branch, the PR head, changed files, comments, and review state must be read again. If the head differs, reconcile the new work before writing.

The post-publication PR comment must:

1. identify the new commit and output paths;
2. record the JUDGE and PARALEGAL dispositions;
3. ask collaborators to submit future update packets by commit SHA and path rather than overwriting these files;
4. keep the PR in draft; and
5. state that no participant or privileged material belongs in the public repository.

## 9. Final QA conclusion

**PASS for counsel review and Phase 0 only.** The packet is professionally formatted, traceable, adversarially reviewed, and explicit about the strongest arguments and strongest counterarguments. It is intentionally not labeled “airtight.” Live validity depends on the exact signer, question, oath or affirmation, certificate, notary, venue, consent, custody, participant risk, research status, publication plan, government relationship, and current law. Those facts require written Washington-counsel approval.
