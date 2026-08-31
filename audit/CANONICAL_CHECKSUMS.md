# Candidate research-freeze checksum manifest

**Freeze date:** 2026-08-30  
**Purpose:** Byte-level comparison of the complete governed Git/GitHub file set. Text paths use the repository's UTF-8/LF representation; platform worktree line-ending conversion is not part of the frozen byte stream.

| Repository path | Bytes | SHA-256 |
|---|---:|---|
| `.gitattributes` | 174 | `7e6d5171568f73eb701295728227d92a735dbf6a2a3fef8df6aec44362528231` |
| `.github/workflows/repository-audit.yml` | 405 | `bee3041f8cfc2fa25c2ffb36151da47692af6f41878a0f62717f81278bf881fa` |
| `README.md` | 6,710 | `e5178e4198881401f2bdccb5070229aba65e2facba363706fdce46a45e3b3c76` |
| `audit/ARCHIVE_CHECKSUMS.md` | 824 | `54272f635d3acf12f9042d1ee056903c5d7c11b97a7218d4ad8f37bbacb49657` |
| `audit/ARTIFACT_MANIFEST.json` | 8,535 | `0c8452d42266b1d1a09b30e5a5afdf3adf65fc8c3e8806267248af8eab494e98` |
| `audit/CANONICAL_STATUS.md` | 5,047 | `ef27be4bb50b263bbdd4d262dbd89863b60149fcc0ebb89f9f6308f8b9a14c53` |
| `audit/DOCUMENT_REGISTER.md` | 7,366 | `45e9ca04d4631da4d895ea1143dc4a82c3bdd9c8f76511e21dd094dd0b91b0b7` |
| `audit/PROJECT_CONTROL.md` | 8,593 | `277d921e82892af09aa1c3e61ba05a032ed88f5c743c775a3b36acb3520f031d` |
| `audit/PR_DEPENDENCY_DISPOSITION.md` | 7,417 | `e15d7570208be0cd0a996e2b40fa7f824cece937df3f88cf1b2260ad2cd1532a` |
| `evidence/FACTS_AND_EVIDENCE_PACKET.md` | 28,912 | `9c17d9642af3298c30247fdf34dda72cb3d0c2d6eab4b037c9d7c919a5f39f71` |
| `memorandum/DGG_WASHINGTON_SWORN_STATEMENT_MEMORANDUM.md` | 74,740 | `5594f9297fe98f131c83b1aad42d6bfd1df23f6b1c0dbd5090807b9dbcbf20a4` |
| `operations/DGG_PILOT_CONTROL_PACKET.md` | 19,235 | `15a3c10d67bb4d75a7de5d4e33fcb18a0242beb5243edb411f5689dd003a133c` |
| `outreach/MESSAGE_AND_CLAIMS_TOOLKIT.md` | 20,656 | `b8aaa2e31f44f16532d912925269e8fb90f2dc06ebfaefa64ee3f3573ae3ce98` |
| `public/DGG_INFORMATION_PACKET.md` | 17,489 | `fce60d8270c04b54e008057ec2874481e30ebad66f4d56579e781293cc3b52cc` |
| `public/DGG_TWO_PAGE_BRIEF.md` | 5,829 | `187bbf26cdad06377ee6ec255db5c586a4dbf274aafdc9e75011a3b8fa51a6eb` |
| `research/AUTHORITY_REGISTER.md` | 21,144 | `5279c18ed46400f6fcfdd175cdcfc5f8de9559e20342b352bed453defb3076e6` |
| `research/GAP_MATRIX.md` | 20,922 | `f770fe62e92a4e1b5e53d2a7337fde89a88ae60d7db03981df09c0c502b7413e` |
| `research/ZOTERO_HANDOFF.md` | 6,446 | `86f67474efdddbfeff5c6d8488ede4c06883fc9b4435acab2d77f2060c23b0f1` |
| `research/authorities-supplement-2026-08-30.bib` | 59,847 | `d04be80a0c2d0cb394931ab89e9037d55b327d44861d79fdc66d7989f704c696` |
| `research/authorities.bib` | 34,251 | `6098a7508005e013745b77c497ed75dc224b858dc92f2d3209c78e6c5cce9d5f` |
| `research/report-source.md` | 44,521 | `53f40cdb1c6e051a5cdf51ac1401cfff27a26b42627af0777353263ececa5309` |
| `verification/check_repository.py` | 27,715 | `4a79d57f11dd0186a1a5765d0d684d1815045e0c2ae196da3b529557b0f4cc52` |

The supplied input drafts have their own checksums in `audit/ARCHIVE_CHECKSUMS.md`. This manifest proves only the integrity and coverage of this candidate research freeze. It does not make any candidate artifact canonical, close the remand, satisfy an external review gate, or authorize live use.
