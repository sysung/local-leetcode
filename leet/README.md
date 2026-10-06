---
type: interview-practice
created: 2026-09-30
updated: 2026-10-05
---
# NVIDIA Data Platform Python Practice

25 standalone data structures and algorithms problems: **8 easy, 10 medium, and 7 hard**. Scenarios draw from the supplied job description's hardware-test logs, ETL frameworks, data transformations, streaming analytics, and data integrity. These are role-relevant practice exercises, not confirmed NVIDIA interview questions.

Use Python 3.10 or later. Everything uses the standard library; no packages, cloud accounts, Spark installation, or database setup are required. The original references were verified on Python 3.12; the additional problems also use only the standard library.

## Problems

### Easy

| Problem | Data structures and algorithms |
| --- | --- |
| [Parse Hardware Test Logs](01_parse_test_logs/README.md) | Strings, arrays, linear scanning |
| [Keep the Newest Event](02_deduplicate_events/README.md) | Hash maps, sorting |
| [Calculate Device Test Yield](03_device_test_summary/README.md) | Hash maps, counting, single-pass aggregation |
| [Join Events with Device Metadata](04_enrich_device_events/README.md) | Hash maps, indexed lookup, hash joins |
| [Rank the Most Frequent Failure Codes](05_top_failure_codes/README.md) | Frequency maps, custom sorting |

### Medium

| Problem | Data structures and algorithms |
| --- | --- |
| [Flatten Nested Telemetry](06_flatten_nested_telemetry/README.md) | Trees, depth-first traversal, explicit stacks |
| [Merge Sorted Hardware Event Streams](07_merge_sorted_streams/README.md) | Min-heaps, k-way merging, iterators |
| [Detect Repeated Device Failures](08_rolling_failure_alerts/README.md) | Sliding windows, deques, hash maps |
| [Combine Hardware Test Sessions](09_merge_test_intervals/README.md) | Sorting, interval algorithms, linear scanning |
| [Resolve ETL Dependencies](10_order_etl_tasks/README.md) | Directed graphs, topological sorting, indegrees, min-heaps |

### Hard

| Problem | Data structures and algorithms |
| --- | --- |
| [Find the Smallest Complete Diagnostic Sequence](11_minimum_test_coverage/README.md) | Variable sliding windows, hash maps, two pointers |
| [Track Sliding Temperature Medians](12_sliding_temperature_median/README.md) | Two heaps, lazy deletion, heap rebalancing |
| [Balance Ordered ETL Workloads](13_partition_processing_batches/README.md) | Binary search on the answer, greedy feasibility checking |
| [Reconstruct a Pipeline Execution Trace](14_reconstruct_pipeline_trace/README.md) | Directed multigraphs, Eulerian paths, iterative Hierholzer traversal |
| [Aggregate Out-of-Order Event-Time Windows](15_event_time_windows/README.md) | Hash maps, min-heaps, incremental aggregation, watermark-based eviction |

## Additional Problems: Parsing and Job Workflows

Problems 16–25 are inspired by the supplied screenshots' general patterns: package-name validation, manifest precedence, nested folder ownership, evolving record fields, log parsing, query filters, job histories, and paginated results. They use generic files, records, and jobs, with no vendor-specific tools or services. These are practice scenarios, not confirmed interview questions. The paths are in-memory strings; no actual archive or filesystem setup is needed.

| Problem | Difficulty | Data structures and algorithms |
| --- | --- | --- |
| [Validate and Parse Package Names](16_parse_package_names/README.md) | Easy | Strings, validation, regular expressions |
| [Choose the Preferred Manifest](17_select_manifest/README.md) | Easy | Tuple ordering, linear scanning, path components |
| [Normalize Evolving Record Fields](18_normalize_record_aliases/README.md) | Easy | Hash maps, schema mapping, presence checks |
| [Assign Files to Their Nearest Manifest](19_assign_folder_roots/README.md) | Medium | Tries, tree ancestry, path component matching |
| [Parse Quoted Key-Value Fields](20_parse_quoted_fields/README.md) | Medium | Tokenization, strings, hash maps |
| [Filter Records with a Boolean Query](21_filter_boolean_queries/README.md) | Hard | Stacks, expression parsing, operator precedence, sets |
| [Validate a Job State History](22_validate_job_transitions/README.md) | Medium | State machines, hash maps, event replay |
| [Collect a Paginated Result Chain](23_collect_paginated_results/README.md) | Medium | Linked traversal, cycle detection, ordered hash maps |
| [Find Peak Concurrent Jobs](24_peak_running_jobs/README.md) | Medium | Sweep lines, sorting, interval boundaries |
| [Find the Shortest Ordered Log Match](25_shortest_ordered_log_match/README.md) | Hard | Dynamic programming, subsequences, reverse updates |

## How to practice

1. Read a problem's `README.md` and examples.
2. Implement the typed function in `main.py` without modifying inputs.
3. Run its visible tests; inspect failures and consider boundary cases.
4. Explain the data structure, algorithm, and time/space complexity aloud.
5. Compare with `solution.py` after your attempt.

Budget roughly 15–25 minutes for easy, 25–45 for medium, and 45–60 for hard problems. The recruiter screenshot describes two 45-minute coding interviews; practice explaining tradeoffs while coding, and use hard problems to stretch beyond a single short exercise.

## Files in every problem

| File | Purpose |
| --- | --- |
| `README.md` | Problem, DSA skills, role context, signature, examples, and constraints |
| `main.py` | Unfinished learner function |
| `solution.py` | Completed reference answer with explanation and complexity |
| `test_case.py` | Visible `unittest` tests importing only `main.py` |

## Run one problem

From the suite root:

```bash
cd 01_parse_test_logs
python3 -m unittest -v test_case.py
```

The tests intentionally fail with `NotImplementedError` until you fill in `main.py`. Generator results are checked by consuming the returned iterator.

## Run all problems

From the suite root, this loop runs each test file in its own folder and returns a failure status if any problem fails:

```bash
suite_status=0
for problem in [0-9][0-9]_*/; do
    (cd "$problem" && python3 -m unittest -v test_case.py) || suite_status=1
done
(exit "$suite_status")
```

Run tests per folder: numbered folders are not importable packages for ordinary recursive `unittest` discovery. No learner test imports `solution.py` or falls back to a reference answer.
