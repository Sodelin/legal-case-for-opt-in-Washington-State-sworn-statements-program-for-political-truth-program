# Non-sworn implementation and verification record

Date: 2026-09-05. Status: synthetic Phase 0 documentation; no live-use approval.

## Scope and provenance

This implements the owner's selected non-sworn development path on PR #5. Intake heads are in the owner decision. Substantive content commit: `60da070e4465d0ce9e7b5ab572c6975235b6a157`. The follow-up metadata commit records evidence against that earlier content commit, avoiding a self-referential hash. CSV metadata is normalized to UTF-8/LF and the current-source manifest regenerated for this follow-up.

The development tree integrates main at `fc4ebbd9095c1e0160e31dbe0b1690fb7a5b31dc`, including the September handoff. No other PR is implicitly merged or its historical review conditions declared resolved.

## Checks performed locally

| Check | Observed result and limitation |
|---|---|
| Decision register | All CR-01–16 present once; owner choices separated from future-use facts |
| Condition crosswalk | All PB-01–18, D-01–21 and P5-01–08 present once; inactive/partial/open states retained |
| Fictional arithmetic | 12 + 9 + 7 = 28; v1 claim 30 corrected to v2 claim 28 |
| Fixture integrity | Three exact UTF-8/no-final-newline SHA-256 payloads recomputed; changed byte changes digest |
| Relative links | New/current document links checked against the proposed repository tree |
| Information review | Current examples are explicitly fictional; no real participant record, private legal advice or operational credential added |
| Independent project review | A separate review accepted the revised packet as synthetic Phase 0 documentation after checking scope, authority, exact original directives and false-closure risks; category definitions and the current-authority gate were strengthened |
| Remote readback | All 23 text files matched the staged UTF-8 content at `60da070e4465d0ce9e7b5ab572c6975235b6a157`; five archived Git blobs matched their original identities; both legacy active binary paths were absent |

Runtime/export enforcement and the listed tabletop acceptance sequences are not implemented software and have not been executed as a real workflow. Scenario expectations remain expectations. No person was recruited, no approval or license collected, no media recorded and no organization contacted by these exercises. The fixture checks do not establish human comprehension, efficacy or independent reviewer reliability.

## Reproduce

From a checkout containing this revision, with Python 3.12 (initial local run: 3.12.13):

```sh
python research/verify_non_sworn_documents.py
```

The script verifies the current-source manifest, register completeness and fictional arithmetic/digests. It does not reach the network or determine legal/launch readiness. The manifest excludes itself; any later content or metadata edit requires manifest regeneration.

## Legacy artifacts

The original PR #5 Markdown, cover note, QA, DOCX and PDF are copied to the historical archive using the exact original Git blob IDs. Legacy binary files leave the active outreach directory and are renamed LEGACY_NOT_FOR_USE. Their bytes are preserved, not rendered or re-certified.

The old export QA's sixteen medium accessibility warnings remain unresolved historical findings. This revision designates Markdown as the current development format. Any future DOCX/PDF requires a new build recipe, semantic comparison, visual/accessibility review and file hashes before it can be designated current.

## Disposition limits

Repository review can accept this as synthetic development documentation while future professional approvals remain open. It cannot certify the historical sworn arguments, change a third party's acceptance, declare practical equivalence with unset margins, or authorize real use. The original project-review lanes and professional reviewers have not been represented as accepting these changes.
