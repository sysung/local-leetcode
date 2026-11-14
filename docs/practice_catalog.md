# Exercise catalog and overlap analysis

Reviewed November 14, 2026. Relevance is a preparation judgment for the two roles described by the user, not a verified hiring requirement. High means directly transferable; Useful means supporting practice; Lower means lower priority for these interviews. Difficulty below is the local README classification, not an official LeetCode rating.

The role guides select only Medium/Hard questions. This catalog assesses all 35 original exercises; 34 remain. Similar primitives do not imply identical correctness requirements. Easy exercises stay available but are outside the routes.

| Exercise | Difficulty | Main theme | Waymo | NVIDIA marketing | Decision and distinguishing requirement |
| --- | --- | --- | --- | --- | --- |
| [01](../01_parse_test_logs/README.md) | Easy | Delimited log validation | High | Useful | Keep: malformed-row handling; unlike quoted or expression parsers. |
| [02](../02_deduplicate_events/README.md) | Easy | Keyed latest-record reduction | High | High | Keep: last-input tie policy differs from 26/32; optional review. |
| [03](../03_device_test_summary/README.md) | Easy | Grouped counts and ratios | High | Useful | Keep: aggregation baseline; Easy, outside both routes. |
| [04](../04_enrich_device_events/README.md) | Easy | Hash join and copy semantics | High | High | Keep: missing metadata and overwrite rules; Easy, outside routes. |
| [05](../05_top_failure_codes/README.md) | Easy | Frequency counting and ordered top-k | High | High | Keep: deterministic ties; routes choose LC347 for selection depth. |
| [06](../06_flatten_nested_telemetry/README.md) | Medium | Iterative tree flattening | Useful | Useful | Keep: deep nested traversal and path construction. |
| [07](../07_merge_sorted_streams/README.md) | Medium | Heap-based k-way iterator merge | High | Useful | Keep: bounded buffering, consumption and stable ties. |
| [08](../08_rolling_failure_alerts/README.md) | Medium | Per-key rolling counts | High | High | Keep: time expiry and alert emission, unlike 15/28/35. |
| [09](../09_merge_test_intervals/README.md) | Medium | Sort and interval union | High | Useful | Keep: merge overlaps/touching; does not count concurrency. |
| [10](../10_order_etl_tasks/README.md) | Medium | Topological sorting and cycles | High | High | Keep: prerequisites and deterministic ready-task choice. |
| 11 (removed) | Hard | Minimum set-coverage window | High | High | Remove: algorithm subsumed by 35; see migration below. |
| [12](../12_sliding_temperature_median/README.md) | Hard | Sliding median with expiration | High | Useful | Keep: two heaps, lazy deletion and bounded memory. |
| [13](../13_partition_processing_batches/README.md) | Hard | Binary search on an answer | High | Useful | Keep: monotonic batch-feasibility test, not an ordinary sorted lookup. |
| [14](../14_reconstruct_pipeline_trace/README.md) | Hard | Eulerian trail reconstruction | Useful | Lower | Keep: use every edge once; differs from dependency order/reachability. |
| [15](../15_event_time_windows/README.md) | Hard | Event-time aggregation and watermarks | High | High | Keep: late-event rejection and window finalization. |
| [16](../16_parse_package_names/README.md) | Easy | Strict filename grammar validation | Lower | Lower | Keep: exact grammar; Easy, outside routes. |
| [17](../17_select_manifest/README.md) | Easy | Composite priority selection | Useful | Lower | Keep: filename/depth/lexical ordering; Easy, outside routes. |
| [18](../18_normalize_record_aliases/README.md) | Easy | Schema alias normalization | Useful | High | Keep: key presence versus truthiness; Easy, outside routes. |
| [19](../19_assign_folder_roots/README.md) | Medium | Deepest path-prefix ownership | Useful | Lower | Keep: whole-component ancestry, unlike generic graph traversal. |
| [20](../20_parse_quoted_fields/README.md) | Medium | Quoted-field scanner | Useful | Useful | Keep: lexical state and all-or-nothing validation. |
| [21](../21_filter_boolean_queries/README.md) | Hard | Boolean parsing and evaluation | Useful | Useful | Keep: precedence, nesting and invalid syntax; unlike audience sets. |
| [22](../22_validate_job_transitions/README.md) | Medium | Per-key finite-state transitions | High | Useful | Keep: reject invalid events without changing accepted state. |
| [23](../23_collect_paginated_results/README.md) | Medium | Cursor traversal with cycle handling | High | High | Keep: first-seen order, last value and chain termination. |
| [24](../24_peak_running_jobs/README.md) | Medium | Sweep-line peak concurrency | High | Useful | Keep: half-open occupancy count, unlike interval union. |
| [25](../25_shortest_ordered_log_match/README.md) | Hard | Minimum ordered subsequence window | Useful | High | Keep: required order differs from unordered coverage in 35. |
| [26](../26_latest_consent_snapshot/README.md) | Medium | As-of consent snapshot | Useful | High | Keep: eligible timestamp and revocation ties, unlike 02/32. |
| [27](../27_identity_components/README.md) | Medium | Undirected connected components | Useful | High | Keep: canonical identities; not directed reachability. |
| [28](../28_behavioral_sessions/README.md) | Medium | Per-user inactivity sessions | High | High | Keep: adjacent-event gap rules, not interval union. |
| [29](../29_last_touch_attribution/README.md) | Medium | Temporal predecessor lookup | High | High | Keep: per-user lookback and attribution ties. |
| [30](../30_audience_set_rules/README.md) | Easy | Set intersection and exclusion | Useful | High | Keep: universe/empty-group semantics; Easy, outside routes. |
| [31](../31_campaign_reconciliation/README.md) | Easy | Multiset reconciliation | High | High | Keep: duplicate counts must survive; Easy, outside routes. |
| [32](../32_cdc_profile_state/README.md) | Medium | Versioned state and tombstones | High | High | Keep: prevent stale resurrection; not simple latest-row selection. |
| [33](../33_completed_offset_prefix/README.md) | Medium | Contiguous completed prefix | High | High | Keep: partition gaps and duplicate completions. |
| [34](../34_lineage_erasure_reachability/README.md) | Medium | Directed downstream reachability | High | High | Keep: direction, roots and cycles; not components/topological order. |
| [35](../35_required_event_window/README.md) | Hard | Minimum multiset-coverage window | High | High | Keep: replaces 11 and adds repeated requirements. |

## Consolidation and migration

Problem 11 was physically removed in favor of [35](../35_required_event_window/README.md). Its required set is the special case where every target count is one. Both use an expanding/shrinking frequency window and earliest-start ties. Problem 35 additionally tests multiplicity. Their API conventions differ: 11 used inclusive endpoints and returned `None` for an empty target; 35 uses half-open endpoints and returns `(0, 0)`. Use 35's contract when practicing; no callers are migrated to a different signature.

Keep the other overlaps: 02/26/32 use different state precedence; 08/15/28 handle different notions of time; 09/24 compute different outputs; 10/14/27/34 require different graph invariants; 25 requires ordered matching while 35 ignores target order. Low relevance alone is not redundancy.

## Use the routes efficiently

Follow [Waymo](waymo_interview_prep.md) or [NVIDIA marketing](marketing_interview_prep.md). Solve shared selections once, then discuss the other role's application. Official LeetCode selections run on LeetCode; they do not add new local folders. Local contracts remain authoritative for local tests.

For each attempt, clarify the contract, code without the reference, run existing tests, and explain correctness and time/space bounds. Use a 35-minute practice limit if helpful, followed by discussion; this is a study choice, not a confirmed interview duration. Unfinished learner stubs are expected to fail. Do not treat complete-suite success as the completion criterion.
