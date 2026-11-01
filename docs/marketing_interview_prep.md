# NVIDIA marketing data engineer interview preparation

Researched November 1, 2026. This guide targets the Senior Data Engineer role in Digital Marketing Operations described in `../Job Description 3 - Marketing.md`.

## What the evidence supports

[NVIDIA's hiring guide](https://www.nvidia.com/en-us/about-nvidia/careers/how-we-hire/) says technical candidates may receive a coding exercise, usually through HackerRank. It does not publish a question bank or a team-specific interview format.

The supplied job description explicitly calls for Python, strong SQL, Spark, batch and streaming pipelines, consent propagation, identity resolution, idempotency, replay, and late-arriving data. The [linked job page](https://jobs.nvidia.com/careers/job/893398235048) was accessible, but its browser extraction did not provide a reliable copy of the role text. The supplied document is the source for the role-specific requirements here.

A [public NVIDIA senior data engineer discussion](https://www.reddit.com/r/dataengineeringjobs/comments/1lqzou4/interview_advice_nvidia_senior_data_engineer/) includes one candidate's report that their screening focused on experience and project scenarios. Another commenter recommends SQL and dimensional modeling. These are unverified anecdotes across unspecified teams. They do not establish what this interview will contain.

The practice priorities below are my inference from the supplied role, rather than reported NVIDIA questions. The ten new exercises are original preparation material.

## What to prioritize

| Priority | Coding pattern | Why prepare it for this role |
| --- | --- | --- |
| Highest | Hash maps, sets, grouping, deduplication | Customer events, audience membership, reconciliation, and replay |
| Highest | Sorting, latest-record selection, deterministic ties | Consent changes, CDC, late arrivals, and reproducible data products |
| Highest | SQL joins, aggregation, window functions | The role explicitly requires strong SQL and analytical consumption |
| High | Timestamp boundaries, sessionization, binary search | Behavioral events and campaign attribution |
| High | Graph traversal and connected components | Identity resolution and downstream lineage |
| High | Sliding windows and frequency counts | Behavioral sequences and bounded event analysis |
| Useful review | Heaps, top-k, interval merging, topological sorting | Stream merges, campaign rankings, scheduling, and pipeline dependencies |

Start with clear easy and medium solutions. Explain correctness, ties, empty input, duplicate events, complexity, and why inputs remain unchanged. Practice one harder sliding-window problem after those fundamentals.

Generic company lists often mix hardware, CUDA, and software roles. This marketing data role gives stronger grounds to prioritize SQL and data processing than CUDA or C++ puzzles. Exact interview difficulty remains unknown.

## Ten local exercises

| Problem | Practice task | Main pattern | Interview follow-up |
| --- | --- | --- | --- |
| 26 | Latest consent snapshot | Map with deterministic latest-record selection | How does a revocation propagate? |
| 27 | Identity components | Connected components | What happens after a mistaken identity merge? |
| 28 | Behavioral sessions | Grouping and sorted scans | How do late events change sessions? |
| 29 | Last-touch attribution | Ordered lookup by customer and time | How do you handle attribution corrections? |
| 30 | Audience membership | Set intersection and exclusion | How do you avoid activating stale membership? |
| 31 | Campaign reconciliation | Multiset counts and full comparison | How do you distinguish missing data from duplicates? |
| 32 | CDC materialization | Versioned keyed state | Why must deletion versions survive replay? |
| 33 | Safe offset advancement | Contiguous prefix tracking | When is acknowledging a message safe? |
| 34 | Erasure lineage | Directed graph reachability | How do you prove every destination completed deletion? |
| 35 | Minimum event window | Sliding window with frequency counts | How does bounded stream state change the solution? |

Each folder contains a problem statement, an unfinished `main.py`, visible `test_case.py` tests, and a reference `solution.py`. Run the tests against your own implementation before opening the reference.

The tuple records and simplified rules make each exercise solvable in one sitting. The consent rules are practice contracts, not legal guidance. Graph reachability alone does not implement an erasure workflow, and offset tracking alone does not guarantee exactly-once delivery.

## Related LeetCode practice

These are pattern matches, not claims that NVIDIA asks these exact questions.

- [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) practices connected components for identity resolution.
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) practices windows with duplicate requirements.
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) practices frequency aggregation and selection. Revisit local problem 05 as well.
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) practices interval boundaries. Compare its closed intervals with the contracts in local problems 09 and 24.
- [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) practices dependency ordering. Revisit local problem 10.

## Prepare SQL alongside Python

These ten additions follow this repository's Python format. They do not replace SQL preparation. Use the same small datasets to practice these separate SQL prompts.

1. Select the latest consent per customer and purpose with `ROW_NUMBER`, including deterministic ties.
2. Count distinct activated customers per campaign and day without multiplying rows through a one-to-many join.
3. Find customers missing from an activation destination using an anti-join. Explain `NULL` behavior.
4. Sessionize events with `LAG`, a new-session flag, and a cumulative sum. Define the frame explicitly.
5. Attribute each conversion to its latest eligible touch. Preserve unattributed conversions with an outer join.
6. Reconcile source and destination event multiplicities rather than comparing only distinct IDs.

The [PostgreSQL window-function tutorial](https://www.postgresql.org/docs/current/tutorial-window.html) explains partitions, ordering, and default frames. Pay attention to tied ordering values and cumulative calculations.

## Prepare senior-level follow-ups

After solving each Python problem, explain how it changes when the data no longer fits in memory. Cover partition keys, skew, incremental updates, retries, schema changes, and late arrivals where relevant.

Prepare concrete examples from your own work for an incident investigation, a safe backfill, a schema migration, and a reliability-versus-cost decision. For this role, also prepare a design discussion about consent changes reaching downstream audience services and activation platforms.

A useful practice sequence is 26, 30, 31, 32, 28, 29, 33, 27, 34, then 35. Start with state selection and sets, then move to time, graphs, and windows. Use a 35-minute coding limit as a practice choice, followed by a correctness and complexity explanation. This timing is not a verified NVIDIA interview format.
