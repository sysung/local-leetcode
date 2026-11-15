# Waymo senior data engineer: ten Medium/Hard questions

Reviewed November 14, 2026. Target: [Senior Data Engineer, Mountain View, job 7438328](https://careers.withwaymo.com/jobs/senior-data-engineer-mountain-view-california-united-states?gh_jid=7438328&gh_src=e2a2625d1us).

## Evidence and priorities

You reported that the first round is LeetCode-style. The exact posting could not be reliably retrieved, so the applications below are preparation scenarios for data engineering, not verified duties of this team.

[Aced's Container With Most Water entry](https://www.aced.io/questions/4341/container-with-most-water) lists Waymo and Data Engineer, and says it was reported two years ago. This is weak community attribution: it does not establish that the report came from this role or round. The [Waymo question list](https://www.aced.io/questions?company=waymo), [Interview Query guide](https://www.interviewquery.com/interview-guides/waymo), [Dataford DE guide](https://dataford.io/interview-guides/waymo/data-engineer), and [PracHub list](https://prachub.com/companies/waymo) are third-party preparation resources, not a verified question bank. Cross-role lists can overemphasize robotics/pathfinding. The [supplied Claude artifact](https://claude.ai/artifact/Lkz1hQH6qitxSg9ATUttDg#943c5549-8b2b) could not be retrieved and contributes no factual claims here.

The selection deliberately covers hash maps, selection, two pointers, heaps, intervals, directed graphs, binary search, grid traversal, prefix sums, and sliding windows. Official LeetCode statements linked below define the external problems. Local difficulty labels come from their READMEs.

## Practice in this order

Each row is one required attempt. The comparison is an alternative, not an extra assignment. These are recommendations, not claims that Waymo asks these exact ten questions.

| # | Selected question | Difficulty | Main theme and application | Local versus official LeetCode: which to do and why |
| --- | --- | --- | --- | --- |
| 1 | [Local 05. Top failure codes](../05_top_failure_codes/README.md) | Medium, local | Frequency maps and bounded heap selection; rank recurring failures. | Choose local over [LC347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (Medium): the upgraded heap requirement adds selection depth while retaining deterministic ties. Set/multiset variants are discussion follow-ups. |
| 2 | [Local 38. Container With Most Water](../38_container_with_most_water/README.md) | Medium, local | Two pointers and an elimination proof. | Equivalent core to [LC11](https://leetcode.com/problems/container-with-most-water/) (Medium), now with local tests. The local empty-input extension returns zero. Role relevance is indirect; it fills a reasoning gap. |
| 3 | [Local 07. Merge sorted streams](../07_merge_sorted_streams/README.md) | Medium, local | Heap-based k-way merge; combine ordered event feeds. | Choose local over [LC23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard). The heap invariant is shared; ordinary lists and index tracking keep the focus on heap merging without linked-list rewiring or iterator APIs. |
| 4 | [Local 09. Merge intervals](../09_merge_test_intervals/README.md) | Medium, local | Sort and scan; combine overlapping operational intervals. | Choose local over [LC56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) (Medium). Algorithmic depth is comparable; local adds explicit nonmutation, zero-length and touching-boundary contracts. |
| 5 | [Local 10. Order ETL tasks](../10_order_etl_tasks/README.md) | Medium, local | Topological sorting and cycle detection; schedule pipelines. | Choose local over [LC210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) (Medium). Alphabetically smallest ready-task selection adds a heap and deterministic scheduling beyond any valid order. Local raises on cycles; LC returns an empty result. |
| 6 | [Local 37. Historical keyed lookup](../37_historical_key_value/README.md) | Medium, local | Stateful API and predecessor binary search. | Choose local over [LC981](https://leetcode.com/problems/time-based-key-value-store/) (Medium): same append/query core with explicit invalid-write rejection and None for missing values. Empty strings remain valid. |
| 7 | [LC200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium, official | Grid DFS/BFS and connected components; traversal representation practice. | Choose official over [local 27](../27_identity_components/README.md) for implicit grid neighbors and visited-state reasoning. Local identity components has stronger business framing, but different representation practice broadens this route. Spatial framing alone does not establish Waymo role relevance. |
| 8 | [Local 36. Contiguous target sum](../36_contiguous_target_sum/README.md) | Medium, local | Prefix sums and frequency maps; signed contiguous aggregates. | Equivalent core to [LC560](https://leetcode.com/problems/subarray-sum-equals-k/) (Medium), with local tests and explicit empty-input/nonmutation rules. Negative values defeat a monotonic sliding window. |
| 9 | [Local 12. Sliding temperature median](../12_sliding_temperature_median/README.md) | Hard, local | Two heaps, expiration and memory bounds; rolling telemetry statistics. | Choose local over [LC295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) (Hard). Removing expired entries and compacting heaps adds depth beyond append-only medians. [LC480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) (Hard) is the closer static-array analogue. |
| 10 | [Local 35. Required event window](../35_required_event_window/README.md) | Hard, local | Frequency-count sliding window; shortest complete diagnostic span. | Choose local over [LC76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard). Same multiplicity invariant, with event types and explicit half-open indices rather than returning text. Equivalent core depth, better DE framing. |

## Correctness and complexity discussion

Use n for total items, u for distinct values, k for streams/window size as specified, and V/E for graph vertices/edges. These are solution targets, not statements that every implementation achieves them.

| Pick | Explain or test | Complexity target and senior follow-up |
| --- | --- | --- |
| 1 | Deterministic frequency ties; k near u; bounded heap selection. | Counting O(n); heap selection O(u log(k+1)) or buckets O(n+u), with O(u) or O(n+u) space. Discuss skewed keys and distributed top-k. |
| 2 | Why discarding the shorter endpoint cannot lose a better answer; equal heights. | O(n) time, O(1) space. Explain the elimination proof before coding. |
| 3 | Empty lists, equal timestamps, duplicate events and unchanged input. | O(k + n log(k+1)) time, O(k) heap state plus O(n) returned output. Discuss how out-of-order source events would change the assumptions. |
| 4 | Touching endpoints and zero-length intervals; preserve input. | O(n log n) time, O(n) copy/output space. Explain why concurrency counting needs a different sweep. |
| 5 | Self-cycles, duplicate prerequisites and prerequisite-only nodes. | O(E + V log V) time and O(V+E) space with heap-based Kahn traversal. Discuss failed-task retries separately from graph ordering. |
| 6 | Query before first write, absent keys, exact timestamp. | Amortized O(1) valid append, O(1) rejected append, O(log m) lookup for m versions of a key; O(n) total state. Discuss retention and late insertion. |
| 7 | Empty land, isolated cells, narrow grids, recursion depth. | O(rows × columns) time and worst-case auxiliary space. State whether mutation is allowed by the chosen interface. |
| 8 | Initialize prefix frequency zero to one; negative numbers and repeated prefix sums. | Expected O(n) time and O(n) space. Explain why prefix multiplicity matters. |
| 9 | Repeated values, even windows, expiring heap roots and buried stale entries. | O(n log(k+1)) time, O(k) auxiliary space with bounded compaction. Discuss exact versus approximate quantiles. |
| 10 | Repeated requirements, missing events, empty target and earliest ties. | Expected O(n+r) time and O(d) count state for r target entries and d target types. Discuss bounded-state limits for an unbounded stream. |

Use the [catalog](practice_catalog.md) for shared overlap analysis and practice procedure. This Python route does not replace SQL preparation: review joins, grouping, window functions and deterministic latest-row selection separately. Use real experience to discuss pipeline incidents, backfills, skew and late data, without assuming those topics are confirmed for this first round.
