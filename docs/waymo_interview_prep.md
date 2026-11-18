# Waymo senior data engineer interview prep

Updated November 17, 2026.

The initial interview is **45 minutes of general coding, up to LeetCode Medium**. Use Python for the practice below. The recruiter also lists C++ and Java. Review arrays, hash maps, sets, strings, sorting, grouping and aggregation, and sliding windows. Skip advanced graphs, bit manipulation, and complex dynamic programming for this screen. [Recruiter email and attached Coding Prep Guide](https://mail.google.com/mail/u/0/#inbox/FMfcgzQjgqQBNCjfKZtpLMgXzqHHRmJF)

## One-day practice order

Do the first three problems in order. Budget about two hours for 45 minutes on Local 28, 25 minutes each on LC 49 and LC 3, and 20 minutes to redo the weakest part and explain time, space, and edge cases aloud. If you only have 45 minutes, do Local 28 as a mock. If you can already solve it from scratch, use Local 32 for the mock and skip its optional slot below.

| Rank | Problem | Level | What to review |
| --- | --- | --- | --- |
| 1 | [Local 28. Sessionize behavioral events](../28_behavioral_sessions/README.md) | Medium | Sort and scan groups. Check shuffled rows, exact duplicates, and a gap equal to the timeout. Explain memory use if one user has most of the events. |
| 2 | [LC 49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Group strings by a stable key. Compare sorted keys with character-count keys for a fixed alphabet. Try duplicate and empty strings. |
| 3 | [LC 3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Variable sliding window. Explain what makes the window valid and why each pointer moves only forward. Dry-run `abba`. |

### If you have more time

Work down this list after reviewing the first three.

| Rank | Problem | Level | What to review |
| --- | --- | --- | --- |
| 4 | [Local 32. Materialize profile state from CDC](../32_cdc_profile_state/README.md) | Medium | Keep one winning version per key. Check replayed rows, out-of-order updates, delete ties, and the cost of sorting the output. |
| 5 | [Local 09. Combine hardware test sessions](../09_merge_test_intervals/README.md) or [LC 56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Sort and scan intervals. Use the local version for the input-mutation contract. Both let you rehearse touching endpoints. |
| 6 | [LC 643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | Fixed-size sliding window with a running aggregate. Check all-negative input, `k = 1`, and `k = n`. |
| 7 | [Local 08. Detect repeated device failures](../08_rolling_failure_alerts/README.md) | Medium | Track a time window per key. Explain eviction at the cutoff and how many entries stay in memory, including when inactive keys retain stale entries. |
| 8 | [LC 217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Array scan, set membership, early exit, and the memory cost of tracking distinct values. |
| 9 | [Local 05. Rank the most frequent failure codes](../05_top_failure_codes/README.md) | Medium | Revisit your frequency map. Explain full sorting as a baseline and when a bounded heap helps. Include tie ordering, distinct-key memory, and sorting the final selection. |

## Run one 45-minute mock

The attachment’s technical interview section (pp. 18–22) emphasizes clarifying underspecified inputs, explaining decisions aloud, and demonstrating clean, runnable code with edge cases. It asks candidates to work independently during the interview and to tell the interviewer before looking anything up. Rehearse in a plain editor. The following time split is for practice.

| Time | What to do |
| --- | --- |
| 0–5 min | Restate the contract. Ask about empty input, missing values, duplicate handling, tie order, and whether the input is sorted. |
| 5–10 min | Walk through a small example. Explain your data structure choice and the condition your loop maintains. |
| 10–30 min | Write runnable code with clear names. Talk through the decisions that affect correctness. |
| 30–40 min | Run a normal case and two edge cases. For Local 28, use a gap equal to the timeout and a duplicate row. Discuss what should happen if an invalid or null field arrives. |
| 40–45 min | State Big-O time and space. Include sorting, retained state, and output size where relevant. Explain what changes if one key dominates or the data does not fit in RAM. |

For the scale follow-up, distinguish the number of rows, the number of distinct keys, and the size of the largest group. For Local 28, explain which state a scan needs if input already arrives sorted by user and timestamp, and what it costs to establish that order otherwise.

## Full-loop prep

The recruiter describes a commercial data role involving dimensional modeling, Python pipelines, cloud warehousing, and data governance. The email lists three later 45-minute sessions. [Recruiter email](https://mail.google.com/mail/u/0/#inbox/FMfcgzQjgqQBNCjfKZtpLMgXzqHHRmJF)

- **Data systems and architecture.** Practice designing a commercial event pipeline from ingestion to a fact table. Define the grain, choose a star or snowflake schema, and explain what changes at 10× volume.
- **SQL and modeling.** Revisit Local 32 as a SQL drill. Use window functions for deterministic latest-row selection, then discuss tombstones, history, join cardinality, execution plans, and schema evolution.
- **Leadership and behavioral.** Prepare STAR stories about owning an outcome, making progress with ambiguous requirements, and choosing a solution that benefited multiple teams.
