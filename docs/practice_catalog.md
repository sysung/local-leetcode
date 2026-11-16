# Practice catalog: 20 focused questions

Reviewed November 14, 2026. The bank now contains 20 Medium/Hard exercises: 17 retained or upgraded questions and three additions. Folder IDs stay stable. The two role guides each assign ten questions; shared questions need one implementation and role-specific discussion.

Relevance is a preparation judgment based on the user's roles and interview experience, not a verified team requirement. Local difficulty comes from each README. The [Waymo route](waymo_interview_prep.md) and [NVIDIA route](nvidia_interview_prep.md) own the role-specific selections, official LeetCode comparisons and complexity discussion.

| Exercise | Difficulty | Theme | Why retain it |
| --- | --- | --- | --- |
| [05](../05_top_failure_codes/README.md) | Medium | Bounded top-k selection | Upgraded from Easy: select with a heap; deterministic ties. Audience sets and multiset reconciliation become discussion follow-ups. |
| [07](../07_merge_sorted_streams/README.md) | Medium | K-way sorted-list merge | Ordinary lists, position tracking and stable timestamp ties; heap merging remains the core skill. |
| [08](../08_rolling_failure_alerts/README.md) | Medium | Rolling per-key counts | Time-based eviction and threshold emission; distinct from sessionization. |
| [09](../09_merge_test_intervals/README.md) | Medium | Interval union | Merge overlapping/touching intervals; does not count concurrency. |
| [10](../10_order_etl_tasks/README.md) | Medium | Topological ordering | Cycle detection and deterministic ready-task selection. |
| [12](../12_sliding_temperature_median/README.md) | Hard | Sliding median | Heap balancing, expiration and bounded memory. |
| [13](../13_partition_processing_batches/README.md) | Hard | Binary search on answer | Monotonic batch-feasibility predicate; distinct from predecessor lookup. |
| [15](../15_event_time_windows/README.md) | Hard | Event-time windows | Late-event rejection, watermark finalization and open-window state. |
| [24](../24_peak_running_jobs/README.md) | Medium | Peak concurrency | Half-open interval sweep; distinct from union. |
| [25](../25_shortest_ordered_log_match/README.md) | Hard | Ordered minimum window | Subsequence order matters; distinct from unordered coverage. |
| [27](../27_identity_components/README.md) | Medium | Identity components | Undirected components with canonical IDs. |
| [28](../28_behavioral_sessions/README.md) | Medium | Behavioral sessions | Per-user sorting and inactivity gaps; high marketing relevance. |
| [29](../29_last_touch_attribution/README.md) | Medium | Last-touch attribution | Temporal lookup with lookback and deterministic campaign ties. |
| [32](../32_cdc_profile_state/README.md) | Medium | Versioned CDC state | Tombstones and replay; deduplication and consent are policy follow-ups. |
| [33](../33_completed_offset_prefix/README.md) | Medium | Completed prefix | Gaps, partitions and safe checkpoint advancement. |
| [34](../34_lineage_erasure_reachability/README.md) | Medium | Downstream reachability | Directed lineage traversal; neither components nor topological order. |
| [35](../35_required_event_window/README.md) | Hard | Multiset minimum window | Frequency counts, duplicate requirements and earliest index ties. |
| [36](../36_contiguous_target_sum/README.md) | Medium | Prefix-sum counting | New: signed contiguous aggregates; repeated prefixes require counts. |
| [37](../37_historical_key_value/README.md) | Medium | Historical key-value API | New: online append and binary-search query; batch attribution does not teach API state. |
| [38](../38_container_with_most_water/README.md) | Medium | Two-pointer optimization | New: standard container geometry and elimination proof; no forced business story. |

## What was removed or combined

All 35 original questions are accounted for here: 17 remain, 17 were removed in this cleanup, and 11 was removed previously. The three new IDs are 36–38.

| Original IDs | Decision | Preserved learning or reason |
| --- | --- | --- |
| 01, 03, 04, 16, 17, 18 | Delete | Basic parsing, grouped ratios, hash join, filename validation, composite selection and alias normalization offer less incremental value for these Medium/Hard routes. |
| 02, 26 | Fold into 32; delete standalone folders | Latest-event and as-of consent are keyed-reduction follow-ups. Their policies remain explicit; they are not identical to tombstone handling. |
| 30, 31 | Fold into upgraded 05; delete standalone folders | Discuss audience sets versus duplicate-preserving reconciliation after frequency selection. These are not extra functions in the main exercise. |
| 06, 14, 19, 20, 21, 22, 23 | Delete | Tree flattening, Euler trails, path ownership, quoted/Boolean parsing, state validation and pagination teach distinct skills, but have lower priority than the retained patterns for these interviews. This is deliberate scope reduction, not a claim of equivalence. |
| 11 | Previously folded into 35 | Minimum set coverage is a special case of multiset coverage. Old inclusive endpoints and empty-target behavior differ from 35's half-open indices and `(0, 0)` empty-target result. |

Completed learner work from deleted folders is recoverable from Git commit `f562453`, the snapshot before this cleanup. No retained learner implementation was replaced. Problem 05 keeps its signature and expected outputs; the reference solution and complexity requirement are upgraded.

## How to practice

Clarify the contract, implement the learner file without the reference, run that folder's existing tests, and explain correctness and complexity. A 35-minute coding limit followed by discussion is an optional study choice, not a verified interview duration. Tests check learner implementations, so unfinished stubs intentionally fail. Reference-solution execution is a separate validation step.

Keep 09/24, 08/15/28, 10/27/34, and 25/35 separate: their invariants differ substantially. Use follow-ups for small policy changes rather than maintaining a separate exercise for every tie rule. Output tests and large inputs do not prove asymptotic time or memory bounds; inspect and explain those separately.
