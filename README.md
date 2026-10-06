---
type: interview-practice
created: 2026-09-30
updated: 2026-10-05
---
# Local LeetCode

25 standalone Python problems for practicing data structures and algorithms.

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
