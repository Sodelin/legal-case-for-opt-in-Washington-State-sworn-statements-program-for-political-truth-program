# Synthetic Claim Record — counting practice counters

**Entirely fictional, nonpolitical tabletop fixture. No person, institution, event or source is represented as real.** No actual participant approval, independent review, publication, permission or notification occurred.

`record_id=SYN-COUNTERS-001` · `record_type=non_sworn` · cutoff `T1`

> SYNTHETIC DEMONSTRATION • NON-SWORN • NOT UNDER PENALTY OF PERJURY • NOT A GOVERNMENT FILING • PARTICIPATION DOES NOT ESTABLISH TRUTH

**Question:** At T1, do the three batches listed in the practice ledger total 30 counters? “Total” means addition of ledger entries, not an independent physical inventory.

**Source packet:** The complete fixture contains one internally authored ledger, `SYN-SRC-001`, below. Batch A has 12, B has 9, C has 7. No external search or factual claim is involved.

**Participant section, v1 — simulated exact words:** “The ledger totals 30 counters. I used mental arithmetic; I have not checked a physical inventory.” Basis: listed entries and arithmetic. Qualification: no physical count. Response: agree within the ledger-only scope.

**Separate editorial finding, v1:** Contradicted by the fixture: 12 + 9 + 7 = 28, which is 2 fewer than 30. This finding concerns arithmetic only and supports no conclusion about the simulated speaker's honesty.

**Review log:** Role A adds 12 + 9 = 21; 21 + 7 = 28. Role B checks 12 + (9 + 7) = 12 + 16 = 28. These are two simulated checks within one authored demonstration, not independent human review. Packet search: inventory all one source; include it as directly relevant; exclude none. The conclusion does not extend beyond this packet.

**Composite approval scenario:** The simulated participant receives the question, exact quote, qualification and contradictory editorial finding. Permission concerns attribution in this context; it does not mean agreement with the finding. Removing “I have not checked a physical inventory” from an excerpt fails context review.

**Correction v2:** The simulated participant changes the first sentence to “The ledger totals 28 counters.” The qualification remains. The editorial finding becomes supported by this packet. This is a substantive correction requiring a newly reviewed composite. Link v1 → v2 and v2 → superseded v1; keep the two versions identifiable. No result about physical inventory is added.

For a reproducible byte-identity exercise, the following are exact UTF-8 payloads with **no trailing newline**. The public payloads are minimal test exports, not complete participant records. Their hashes do not describe this Markdown file or certify approval.

```json
{"a":12,"b":9,"c":7}
```

```json
{"claim":30,"finding":"contradicted","record_type":"non_sworn","total":28,"version":1}
```

```json
{"claim":28,"finding":"supported","record_type":"non_sworn","total":28,"version":2}
```

| Asset | SHA-256 | Relationship/status |
|---|---|---|
| SYN-SRC-001 | `53060771ebea70a16f44bf5ffe1c0140c94eac2c831007e1b641cc4f0d628ea5` | Shared source; unchanged. |
| SYN-PUB-v1 | `0020c9657b73100be33537d60321f3c89d75f1609fea64ea099edab7965b67e8` | Derived from source; superseded by v2 in simulation. |
| SYN-PUB-v2 | `f110b8f9ddaa44933d751e7631e007ff4ae85584f2cb8625b1fb37d26be0567a` | Derived from source; correction parent v1; simulated current version. |

**Propagation exercise:** A text excerpt derived from v1 must update or display the correction. A simulated recipient acknowledgment closes only its own distribution entry. A missing acknowledgment remains open. Permission for the text does not establish permission for an image or advertisement. A simulated pre-release withdrawal produces no public profile, refusal notice or accusation.

**Checks actually performed:** The three displayed SHA-256 values were computed from the exact payload bytes, and both sums equal 28. Other workflow events above are scenarios to exercise, not executed release controls.
