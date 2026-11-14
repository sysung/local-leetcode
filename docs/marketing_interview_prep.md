# NVIDIA marketing senior data engineer: ten Medium/Hard questions

Reviewed November 14, 2026. Target: [NVIDIA job 893398235048](https://jobs.nvidia.com/careers/job/893398235048), described by the user as a senior data engineer role in marketing.

## Evidence and priorities

[NVIDIA's hiring guide](https://www.nvidia.com/en-us/about-nvidia/careers/how-we-hire/) says technical candidates may receive a coding exercise, usually through HackerRank. It does not provide a marketing-team question bank. The live job page did not yield reliable role text. The previous guide referenced an external job-description file that is absent from this checkout; its detailed requirements are therefore not treated as verified facts.

You reported that earlier interviews emphasized real-world scenarios with a DSA twist. The marketing examples here follow that experience and the existing exercise contracts. Consent, identity, attribution and streaming scenarios are preparation choices, not confirmed requirements of this specific posting. None of these ten questions is claimed to be an actual NVIDIA interview question.

This route emphasizes keyed state, deterministic precedence, graphs, sorted-time processing, gaps, event-time aggregation and sliding windows. Official LeetCode counterparts provide a comparison; local contracts and difficulty labels remain authoritative for local exercises.

## Practice in this order

Each row is one required attempt. Do the selected version; the counterpart explains the tradeoff rather than adding homework.

| # | Selected question | Difficulty | Main theme and marketing application | Local versus official LeetCode: which to do and why |
| --- | --- | --- | --- | --- |
| 1 | [Local 05. Top failure codes](../05_top_failure_codes/README.md) | Medium, local | Frequency map and heap selection; rank campaign event categories. | Choose local over [LC347](https://leetcode.com/problems/top-k-frequent-elements/) (Medium): upgraded selection complexity plus deterministic ties. Audience sets and duplicate-preserving reconciliation are follow-ups here. |
| 2 | [Local 07. Merge sorted streams](../07_merge_sorted_streams/README.md) | Medium, local | Heap merge with bounded buffering; combine campaign event feeds. | Choose local over [LC23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard): same heap invariant, with incremental iterators rather than linked-list rewiring. |
| 3 | [Local 32. CDC profile state](../32_cdc_profile_state/README.md) | Medium, local | Version ordering and tombstones; materialize replayed customer updates safely. | Choose local over [LC981](https://leetcode.com/problems/time-based-key-value-store/) (Medium). This is a partial analogue: keyed history is shared, but the challenge here is state reduction and deletion precedence, not binary search. Tombstones prevent older replayed upserts from resurrecting a profile. |
| 4 | [Local 27. Identity components](../27_identity_components/README.md) | Medium, local | Undirected components; resolve linked customer identifiers. | Choose local over [LC721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) (Medium). Same graph/union-find core; canonical ID selection makes the result directly usable in an identity mapping. LC721 adds email/account packaging, not a fundamentally different graph invariant. |
| 5 | [Local 28. Behavioral sessions](../28_behavioral_sessions/README.md) | Medium, local | Per-user sorting and adjacent-gap scan; group behavioral activity. | Choose local over [LC56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) (Medium) for marketing applicability. They share sorted scans, but sessionization is not interval union: compare each event with its predecessor and define timeout equality. |
| 6 | [Local 29. Last-touch attribution](../29_last_touch_attribution/README.md) | Medium, local | Per-key temporal lookup; credit each conversion to an eligible campaign. | Choose local over [LC981](https://leetcode.com/problems/time-based-key-value-store/) (Medium) for lookback boundaries, unattributed conversions and deterministic campaign ties. LC981 adds an online API; local adds business rules around predecessor lookup. |
| 7 | [Local 33. Completed offsets](../33_completed_offset_prefix/README.md) | Medium, local | Sets and contiguous-prefix advancement; avoid committing past ingestion gaps. | Choose local over [LC1656. Design an Ordered Stream](https://leetcode.com/problems/design-an-ordered-stream/) (Easy). Local adds partitions, duplicate completions and existing checkpoints, making the data-processing contract deeper. LC1656 is comparison only, not assigned practice. |
| 8 | [Local 10. ETL dependency order](../10_order_etl_tasks/README.md) | Medium, local | Topological sort, heap and cycle detection; sequence ingestion and audience publication. | Choose local over [LC210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) (Medium). Deterministic ready-task ordering adds complexity beyond any valid topological order. |
| 9 | [Local 15. Event-time windows](../15_event_time_windows/README.md) | Hard, local | Heap-based finalization and incremental aggregation; process late engagement events. | Choose local over [LC239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (Hard) for streaming applicability. This is a contrast, not equivalence: LC239 teaches deque-based extrema in fixed index windows; local teaches watermark lifecycle and out-of-order arrivals. Neither subsumes the other. |
| 10 | [Local 35. Required event window](../35_required_event_window/README.md) | Hard, local | Minimum multiset sliding window; find the shortest span containing required behaviors. | Choose local over [LC76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard). Equivalent count/window invariant, with event types and explicit index ties. Required behaviors can occur in any order; this is not an ordered funnel. |

## Correctness, complexity and realistic extensions

Use n for input rows, u for unique keys, V/E for graph vertices/edges, p for partitions, and b for buffered open window/device groups. Bounds include sorted output where required and assume expected hash-map operations.

| Pick | Explain or test | Complexity target and interview extension |
| --- | --- | --- |
| 1 | k near the number of categories; heap versus buckets. | O(n + u log(k+1)) with heap selection or O(n+u) buckets; discuss exact versus approximate heavy hitters and skew. |
| 2 | Empty feeds, equal timestamps, one-shot iterators and deferred consumption. | O(n log(k+1)) time and O(k) buffered state for k streams. Discuss late arrivals and backpressure. |
| 3 | Delete/upsert ties, stale replay, empty-string values, later recreation. | O(n + u log u) time, O(u) state. Explain why deletion versions must survive replay and how retention interacts with backfills. |
| 4 | Self-links, repeated/reversed edges, long chains and disconnected groups. | Iterative traversal O(V+E), plus O(V log V) output sorting; O(V+E) space. Discuss mistaken merges and why splitting is harder than unioning. |
| 5 | Gap equal to timeout, interleaved users, duplicates and out-of-order input. | O(n log n) time and O(n) space. Explain how late events can merge previously emitted sessions. |
| 6 | Touch at either lookback boundary, tied campaigns, absent touches, repeated touches. | Sort/index in O(n log n); each conversion lookup O(log m) within that user's m touches, plus output sorting. O(n) index/output space. Discuss corrections after late touch arrival. |
| 7 | Gap at checkpoint, completions below it, duplicates and independent partitions. | Expected O(n + p log p) time and O(n+p) space. Explain that prefix tracking alone does not guarantee exactly-once writes; coordinate checkpointing with sink effects. |
| 8 | Cycles, self-dependencies, duplicate edges and prerequisite-only tasks. | O(E + V log V) time and O(V+E) space. Distinguish retry state from dependency ordering. |
| 9 | Timestamp equal to watermark, rejected late events, final flush, invalid parameters. | Heap operations O(n log(b+1)), plus O(s log s) sorting for s output summaries; O(b) live state and O(n) worst-case returned data. Discuss allowed lateness and state retention without claiming the state is universally bounded. |
| 10 | Repeated requirements, irrelevant events, missing types, empty target and earliest ties. | Expected O(n+r) time and O(d) count state for r required entries and d required types. For ordered funnel rules, the invariant changes; see the catalog's distinction from local 25. |

## SQL and senior discussion

These remain separate from the ten coding assignments. Use problem 32’s consent follow-up to practice deterministic latest-consent selection with `ROW_NUMBER`, audience anti-joins, duplicate-preserving campaign reconciliation, sessionization with `LAG`, and last-touch attribution with an outer join that retains unattributed conversions. Review join multiplicity, `NULL` behavior and window frames using the [PostgreSQL window-function tutorial](https://www.postgresql.org/docs/current/tutorial-window.html).

After coding, explain partition keys, skew, late data, retry behavior, replay and backfill corrections. Prepare concrete examples from your own work for an incident, a migration, and a reliability-versus-cost decision. Simplified consent rules are exercise contracts; identity components, offset prefixes and graph scope do not by themselves implement production privacy or delivery guarantees.

See the [catalog](practice_catalog.md) for the shared practice procedure, overlap analysis, and the consolidation decisions.
