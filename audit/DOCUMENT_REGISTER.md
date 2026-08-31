# Document register

**Register date:** 2026-08-30  
**Status:** **CANDIDATE CONTROL RECORD — DOES NOT CONFER CANONICAL OR LIVE-USE STATUS**  
**Authority cutoff:** 2026-08-30  
**Candidate branch:** codex/legal-readiness-cures  
**Source baseline:** 3905b470c2ab239cf2aae563e1d7b3a1adb73dd3

## Control hierarchy

1. [ARTIFACT_MANIFEST.json](ARTIFACT_MANIFEST.json) is the machine-readable file-by-file classification authority.
2. [CANONICAL_STATUS.md](CANONICAL_STATUS.md) is the human explanation of posture and Phase 0 limits.
3. This register identifies the durable document set, audience, owner, cutoff, and unresolved release gate.
4. [CANONICAL_CHECKSUMS.md](CANONICAL_CHECKSUMS.md) records byte integrity after content freeze; it does not confer approval.
5. [ARCHIVE_CHECKSUMS.md](ARCHIVE_CHECKSUMS.md) preserves the supplied input bytes.

The checked-in main snapshot is the last canonical publication, but the independent adversarial audit remanded it. All current corrected bytes remain candidate or supplement artifacts unless the machine manifest says otherwise. Every row below has live use set to **No**.

## Durable document set

| Document ID | Path | Version / class | Primary audience and purpose | Responsible owner | Authority cutoff | Publication / live use | Unresolved gate |
|---|---|---|---|---|---|---|---|
| DGG-GOV-001 | [CANONICAL_STATUS.md](CANONICAL_STATUS.md) | 2026-08-30 candidate | Everyone; controlling human posture and Phase 0 boundary | Audit director | 2026-08-30 | No | Reviewed remand supersession |
| DGG-GOV-002 | [PROJECT_CONTROL.md](PROJECT_CONTROL.md) | 2026-08-30 candidate | Research and counsel; mission, red lines, authority hierarchy, gates | Audit director | 2026-08-30 | No | Reviewed remand supersession |
| DGG-GOV-003 | [ARTIFACT_MANIFEST.json](ARTIFACT_MANIFEST.json) | Schema 1 candidate | CI and auditors; every-file classification and supersession | Repository auditor | N/A | No | Validation and independent readback |
| DGG-GOV-004 | [DOCUMENT_REGISTER.md](DOCUMENT_REGISTER.md) | 0.1 candidate | Humans; durable artifact map and release status | Repository auditor | 2026-08-30 | No | Validation and independent readback |
| DGG-GOV-005 | [PR_DEPENDENCY_DISPOSITION.md](PR_DEPENDENCY_DISPOSITION.md) | 0.1 candidate | Maintainers, auditors, and counsel; one five-PR integration path | Audit director | 2026-08-30 | No | PR #4 blocker closure and explicit supersession |
| DGG-MEM-001 | [DGG_WASHINGTON_SWORN_STATEMENT_MEMORANDUM.md](../memorandum/DGG_WASHINGTON_SWORN_STATEMENT_MEMORANDUM.md) | 0.1 candidate correction | DGG and retained counsel; legal theory, adverse authority, recommendation | Legal research lead; counsel approval pending | 2026-08-30 | No | Facts, official reporters, citator, Washington and participant-state counsel |
| DGG-PUB-000 | [DGG_TWO_PAGE_BRIEF.md](../public/DGG_TWO_PAGE_BRIEF.md) | 0.1 candidate | First readers; compact neutral explanation and comprehension ask | Communications owner pending | 2026-08-30 | Repository review only; no promotional release | Owner/contact, counsel, accessibility, methods, comprehension |
| DGG-PUB-001 | [DGG_INFORMATION_PACKET.md](../public/DGG_INFORMATION_PACKET.md) | 0.1 candidate | Reviewers; detailed explanation, example, FAQ, governance map | Communications owner pending | 2026-08-30 | Repository review only; no promotional release | Counsel, accessibility, methods, comprehension |
| DGG-EVD-001 | [FACTS_AND_EVIDENCE_PACKET.md](../evidence/FACTS_AND_EVIDENCE_PACKET.md) | 0.1 candidate | Counsel and fact custodians; verified facts, assumptions, missing facts, elements, exhibits | Fact manager and counsel pending | 2026-08-30 | No | MF-001 through MF-010, custodians, authentication, adverse evidence |
| DGG-OUT-001 | [MESSAGE_AND_CLAIMS_TOOLKIT.md](../outreach/MESSAGE_AND_CLAIMS_TOOLKIT.md) | 0.1 candidate | Communications, methods, and counsel; claims controls and channel tests | Communications lead pending | 2026-08-30 | Repository review only; no campaign, lobbying, paid, or candidate use | Entity/payer classification, counsel, privacy, methods, accessibility |
| DGG-OPS-001 | [DGG_PILOT_CONTROL_PACKET.md](../operations/DGG_PILOT_CONTROL_PACKET.md) | Deprecated-for-live-use candidate | Phase 0 tabletop reviewers; bounded synthetic controls | Operations owner and counsel pending | 2026-08-30 | No | Remand, counsel, notary workflow, privacy/security, live-protocol review |
| DGG-PDF-001 | [01_DGG_Concept_Overview.pdf](../output/pdf/01_DGG_Concept_Overview.pdf) | 2026-08-30 candidate | DGG, counsel, and first readers; numbered concept overview and review request | Communications owner pending | 2026-08-30 | Repository review only; recipient discussion, no promotional release | Remand, counsel, accessibility, methods, comprehension, independent readback |
| DGG-PDF-002 | [02_DGG_Legal_and_Evidence_Memorandum.pdf](../output/pdf/02_DGG_Legal_and_Evidence_Memorandum.pdf) | 2026-08-30 candidate | DGG and counsel; numbered legal, adverse-authority, evidence, and authority attachment | Legal research lead; counsel approval pending | 2026-08-30 | Repository review only; recipient discussion, not legal advice | Remand, official reporters, citator, factual completion, counsel, independent readback |
| DGG-PDF-003 | [03_DGG_Implementation_and_Interview_Toolkit.pdf](../output/pdf/03_DGG_Implementation_and_Interview_Toolkit.pdf) | 2026-08-30 candidate | DGG, counsel, methods, and operations reviewers; numbered fictional/tabletop design toolkit | Operations and communications owners pending | 2026-08-30 | Repository review only; no live interview, notarial act, recruitment, or promotional release | Remand, counsel, methods, accessibility, privacy/security, live-protocol review |
| DGG-RES-001 | [report-source.md](../research/report-source.md) | Candidate correction | Researchers and counsel; primary/adverse source ledger | Legal research lead | 2026-08-30 | No | Official reporters, current citator, open questions |
| DGG-RES-002 | [GAP_MATRIX.md](../research/GAP_MATRIX.md) | Candidate correction | Researchers and counsel; consequential claims and next actions | Legal research lead | 2026-08-30 | No | Open rows and counsel disposition |
| DGG-RES-003 | [AUTHORITY_REGISTER.md](../research/AUTHORITY_REGISTER.md) | 0.1 candidate | Researchers, Zotero single-writer, counsel; item-key and source crosswalk | Legal research lead | 2026-08-30 | No | Supplemental Zotero receipt and citator review |
| DGG-RES-004 | [authorities.bib](../research/authorities.bib) | 37-item candidate batch | Zotero single-writer and auditors; initial legal records | Zotero single-writer for mutation; legal lead for source metadata | 2026-08-30 | No | Existing-item reconciliation and corrected vote_no metadata |
| DGG-RES-005 | [authorities-supplement-2026-08-30.bib](../research/authorities-supplement-2026-08-30.bib) | 69-item supplement | Zotero single-writer and auditors; missing live-corpus legal and official-guidance records | Zotero single-writer task 01a05517-896e-7613-9851-ee623e2e3dfe | 2026-08-30 | No | Digest-bound plan, authorized mutation, readback receipt |
| DGG-RES-006 | [ZOTERO_HANDOFF.md](../research/ZOTERO_HANDOFF.md) | 0.1 supplement | Zotero single-writer and system auditor; deterministic boundary and receipt contract | Legal research lead for handoff; designated task for execution | 2026-08-30 | No | Cross-task delivery and returned receipt |
| DGG-VER-001 | [check_repository.py](../verification/check_repository.py) | Schema 1 candidate | CI and auditors; links, status, manifest, and checksum validation | Repository auditor | N/A | No | Passing run against frozen bytes |

## Supersession and archive

The archival concept paper is superseded for current analysis by DGG-MEM-001. The two archival pilot packets are superseded for current control purposes by DGG-OPS-001. Supersession does not delete or rewrite those inputs. Their immutable byte identities remain in [ARCHIVE_CHECKSUMS.md](ARCHIVE_CHECKSUMS.md).

No current candidate silently supersedes another current candidate. A later reviewed supersession must identify the old and new artifact, exact commits, reviewer, reason, unresolved gates, and effective status.

## Release rule

Repository visibility is not promotional approval. No document becomes audited, canonical, launch-cleared, counsel-approved, or suitable for candidate outreach merely because it is committed or pushed. Release requires the artifact-specific gates above, a current authority/citator check where applicable, a passing verifier and checksum freeze, an independent remote readback, and a traceable status change in the machine manifest.
