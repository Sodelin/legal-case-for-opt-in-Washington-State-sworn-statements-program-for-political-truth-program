# Canonical status manifest

**Status date:** 2026-08-30  
**Repository posture:** **REMANDED — CHANGES REQUIRED — NOT LAUNCH-CLEARED**  
**Public-repository rule:** Do not add privileged advice, participant data, identity-proofing material, unreleased recordings, notarial journals, credentials, incident files, or legal-hold material.

## Controlling review record

The checked-in `main` snapshot at `3905b470` is the last canonical publication, but it is not the last review word. Open [PR #4, “Judicial audit: remand current DGG packets pending corrections”](https://github.com/Sodelin/legal-case-for-opt-in-Washington-State-sworn-statements-program-for-political-truth-program/pull/4), at reviewed head `b99f7df6`, records an independent adversarial audit that sustains a Phase 0-only core and remands the canonical packet and draft PRs for specified corrections. Despite the PR title, it is an internal review—not a court order or judicial ruling. The PR implements no operational protocol and remains open and noncanonical.

Draft PRs #1–#3 and #5 are proposals or supplemental research. A higher commit count or later timestamp does not make a branch canonical, merge-ready, or approved for use.

The binding [pull-request disposition matrix](PR_DEPENDENCY_DISPOSITION.md) selects PR #4 at `b99f7df6712a063e824922ede87b2c7ecca726f0` as the sole **CANONICAL REVIEW** gate. PRs #1 and #5 are parked; PRs #2 and #3 depend on explicit blocker closure. No open PR presently supersedes the remand, and no sixth PR is authorized.

## File status

| Path | Current role | May be used live? |
|---|---|---|
| `README.md` | Repository orientation and remand notice | No |
| `memorandum/DGG_WASHINGTON_SWORN_STATEMENT_MEMORANDUM.md` | Research memorandum under correction; not legal advice | No |
| `public/DGG_INFORMATION_PACKET.md` and `public/DGG_TWO_PAGE_BRIEF.md` | Publicly visible review drafts; not approved for promotional release or recruitment | No |
| `evidence/FACTS_AND_EVIDENCE_PACKET.md` | Candidate litigation-readiness workpaper; not a pleading or privileged file | No |
| `outreach/MESSAGE_AND_CLAIMS_TOOLKIT.md` | Candidate outreach, claims-control, and comprehension-testing toolkit | No |
| `research/report-source.md` | Primary-source ledger with disclosed gaps | No |
| `research/GAP_MATRIX.md` | Consequential-claim tracker | No |
| `research/AUTHORITY_REGISTER.md`, `research/authorities*.bib`, and `research/ZOTERO_HANDOFF.md` | Candidate Zotero crosswalk, legal-source submissions, and read-only single-writer dependency | No |
| `operations/DGG_PILOT_CONTROL_PACKET.md` | Deprecated live-use packet; Phase 0 synthetic/tabletop reference only | No |
| `audit/DOCUMENT_REGISTER.md` and `audit/ARTIFACT_MANIFEST.json` | Artifact status and supersession controls; do not confer approval | No |
| `audit/PR_DEPENDENCY_DISPOSITION.md` | Five-PR head-SHA, contradiction, dependency, and counsel-gate control | No |
| `archive/input-drafts/` | Immutable supplied inputs; unaudited and noncanonical | No |

## Present Phase 0 boundary

While the remand remains open, Phase 0 may use only a pure mock in which fictional facts are never placed under oath and no notarial act occurs. A later reviewed supersession may propose an actual in-person test verification containing only literally true, personal-knowledge statements about the test itself, but that mode is not presently authorized. Its minimum design would be voluntary, nonpublic, Washington-only, and paper-based, with one tangible Canonical Sworn Record as the sole oath object. The ordinary interview, production record, source packet, annotations, and later commentary would remain unsworn. A participant-controlled correction would occur before execution; any substantive correction after execution would require a completely new act and an append-only link to the superseded record.

No real signer or notarial act, named target/public-figure participant, participant/program publication, livestream, remote DGG act, public refusal/nonresponse label, or criminal-enforcement claim is authorized. If a future supersession authorizes an actual test, it may use a real signer only for literally true statements about the test itself; that signer's identity, credentials, and notarial records must remain outside the public repository and may not be published. Current Washington law does contain a safeguarded record-based remote-notarization route; the described future in-person restriction is a proposed project risk control, not a claim that remote notarization is generally unavailable.

## Canonicalization rule

No candidate or audit branch may silently amend another. Canonical status changes only through a traceable reviewed change that:

1. reconciles all conflicting instructions;
2. maps consequential claims to current authority and identifies inference;
3. passes repository validation and checksum regeneration;
4. records the exact reviewed heads; and
5. preserves every applicable counsel, notary, security, methods, and publication gate.
