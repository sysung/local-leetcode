---
type: interview-practice
created: 2026-09-30
updated: 2026-11-01
---
# Local LeetCode

35 standalone Python problems for practicing data structures and algorithms, including 10 exercises for a marketing data engineering interview.

## Installation

Install Git and Python 3.10 or later. The exercises use only the Python standard library, so no additional packages are needed.

```bash
git clone https://github.com/sysung/local-leetcode.git
cd local-leetcode
```

## Getting started

1. Choose a numbered problem folder and read its `README.md`.
2. Implement the function in `main.py`.
3. Run the tests, then compare your approach with `solution.py`.

## Run a problem

From the repository root:

```bash
cd 01_parse_test_logs
python3 -m unittest -v test_case.py
```

Replace `01_parse_test_logs` with the folder you want to practice. The tests check your `main.py`; unfinished functions raise `NotImplementedError` until you implement them.

To run all problems from the repository root:

```bash
python3 -m unittest discover -v
```

## Marketing data engineering interview preparation

Start with the [research and preparation guide](docs/marketing_interview_prep.md). It explains the role-specific priorities, source limitations, related LeetCode patterns, SQL practice, and senior-level follow-ups.

Problems 26 through 35 follow the same format as the original exercises. Their reference solutions can be checked without modifying your learner files:

```bash
python3 scripts/verify_marketing_solutions.py
```

The ordinary unittest commands continue to check `main.py`. New learner stubs intentionally fail until you implement them.

| Problem | Exercise |
| --- | --- |
| 26 | [Build the latest consent snapshot](26_latest_consent_snapshot/README.md) |
| 27 | [Resolve identity components](27_identity_components/README.md) |
| 28 | [Sessionize behavioral events](28_behavioral_sessions/README.md) |
| 29 | [Attribute conversions to the last touch](29_last_touch_attribution/README.md) |
| 30 | [Apply audience inclusion and exclusion rules](30_audience_set_rules/README.md) |
| 31 | [Reconcile campaign event counts](31_campaign_reconciliation/README.md) |
| 32 | [Materialize profile state from CDC](32_cdc_profile_state/README.md) |
| 33 | [Advance completed partition offsets](33_completed_offset_prefix/README.md) |
| 34 | [Find datasets affected by an erasure](34_lineage_erasure_reachability/README.md) |
| 35 | [Find the shortest qualifying event window](35_required_event_window/README.md) |
