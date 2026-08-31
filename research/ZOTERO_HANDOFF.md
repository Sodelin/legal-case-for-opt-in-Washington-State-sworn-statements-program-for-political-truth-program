# Zotero single-writer handoff

**Handoff date:** 2026-08-30  
**Handoff status:** **READ-ONLY DEPENDENCY — NO ZOTERO MUTATION AUTHORIZED IN THIS TASK**  
**Designated single-writer task:** 01a05517-896e-7613-9851-ee623e2e3dfe  
**Destination:** My Library / Codex Submissions  
**Destination collection key:** RKFIXEK4

## Coordination boundary

The legal-research task prepared the source packages and may inspect Zotero read-only, but it must not import, edit, merge, move, attach, or delete Zotero records. The designated single-writer must return:

1. a deterministic, digest-bound plan before any mutation;
2. an explicit duplicate and correction policy;
3. a post-write readback receipt; and
4. any exception that prevents exact reconciliation.

Direct cross-task delivery was attempted from this task, but no callable task-messaging tool was available and the collaboration channel correctly rejected the thread ID as a non-agent target. This checked-in handoff is therefore the durable payload for the system auditor or user to route to the designated task.

## Exact source artifacts

The byte counts and SHA-256 values below bind the requested plan to the current workspace files. SHA-256 identifies exact bytes; it does not establish legal accuracy.

| Artifact | Purpose | Entries | Workspace bytes | SHA-256 |
|---|---|---:|---:|---|
| [authorities.bib](authorities.bib) | Initial legal batch already reported as 37 Zotero records; do not reimport blindly | 37 | 34,251 | 6098a7508005e013745b77c497ed75dc224b858dc92f2d3209c78e6c5cce9d5f |
| [authorities-supplement-2026-08-30.bib](authorities-supplement-2026-08-30.bib) | Deduplicated legal and official-guidance delta found by full live-corpus reconciliation | 69 | 59,847 | d04be80a0c2d0cb394931ab89e9037d55b327d44861d79fdc66d7989f704c696 |
| [AUTHORITY_REGISTER.md](AUTHORITY_REGISTER.md) | Existing 37-item Zotero-key crosswalk and policy | 37 mapped rows | Changes during repository closeout | Bind to its final repository commit |
| [report-source.md](report-source.md) | Proposition, limitation, and open-question ledger | Not an import file | Changes during repository closeout | Bind to its final repository commit |
| [GAP_MATRIX.md](GAP_MATRIX.md) | Claim IDs and verification status | Not an import file | Changes during repository closeout | Bind to its final repository commit |

The combined BibLaTeX set contains 106 authority records: 92 legal-authority records plus 14 materially relied-on official guidance, report, or instruction records. The supplement consists of:

- 17 cases;
- 17 Washington session-law, statute, regulation, or court-rule entries;
- 13 federal statute or regulation entries;
- five Pennsylvania entries; and
- three state voluntary-pledge comparator expansions; and
- 14 official supporting records mapped as ten Zotero **Web Page** items, three **Report** items, and one **Document** item.

## Canonical metadata and note rules

For every item:

- preserve the BibLaTeX key as the durable Git/Zotero crosswalk key;
- use Zotero **Case** for jurisdiction entries and **Statute** for statutes, session laws, regulations, and court rules where the importer supports those mappings;
- map `@online` supporting records to Zotero **Web Page**, `@report` to **Report**, and `@misc{wash_wpic_118_12}` to **Document**; preserve corporate author, institution, date/version, report number, URL, and source-limit note;
- preserve full title or case name, reporter, volume, first page, court, docket, date, jurisdiction, enactment/number, and version fields when supplied;
- preserve claim_ids, annotation, last_verified, and source-provenance metadata in Zotero fields or Extra;
- apply project/washington-sworn-format, origin/codex-ai, research/deep, and review/human-required;
- apply batch/supplement-2026-08-30 only to the 69-item supplement;
- for every case preserve negative_treatment = Counsel citator check required and citator_date = Pending;
- never turn a proposition note into a holding broader than the source;
- keep fragmented opinions, persuasive-only cases, evidence-rule cases, and official-copy gaps expressly qualified; and
- do not treat a Zotero item key or import success as a citator result.

## Link, rights, and attachment decisions

- Link to the official public legal source when available.
- When no official electronic opinion was located, retain the identified public mirror and the note Washington Reports copy required.
- Do not download or attach PDFs, snapshots, credentials, notarial records, or participant material in this handoff.
- No paywalled or licensed reporter copy is included or requested.
- Rights status is link-only public legal-source metadata; the single-writer must not infer redistribution rights for a linked document.
- The existing vote_no_1998 Zotero record needs metadata reconciliation: the Git source package now points to the opinion mirror and says an official Washington Reports copy is required; the original import used the current-statute URL. Correct the existing item if the single-writer has an authorized deterministic update route, and do not create an unexplained duplicate.

## Required pre-write plan

The single-writer's plan must state:

- the two verified source digests above;
- the destination collection and key;
- the existing 37-item reconciliation method;
- the expected 69-item delta;
- the exact duplicate key;
- how updates differ from creates;
- the legal item-type mapping;
- the field-to-Extra mapping;
- failure and rollback behavior; and
- the exact readback query and receipt format.

No mutation should proceed if the digest, destination, expected count, or duplicate policy differs.

## Required readback receipt

Return a timestamped machine-readable or tabular receipt containing:

- handoff/task ID and source digests;
- destination library and collection key;
- BibLaTeX key;
- Zotero item key;
- Zotero item type;
- title/case name;
- collection membership;
- required tags;
- action (created, updated, unchanged, duplicate-held, or failed);
- metadata exception;
- total existing, created, updated, unchanged, duplicate-held, and failed counts;
- a preserved Zotero export or API readback-log SHA-256; and
- an independent comparison of expected versus returned keys.

Until that receipt is returned and reconciled in [AUTHORITY_REGISTER.md](AUTHORITY_REGISTER.md), the 69-item supplement remains **prepared for handoff, not verified in Zotero**.
