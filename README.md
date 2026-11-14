---
type: interview-practice
created: 2026-09-30
updated: 2026-11-14
---
# Local LeetCode

34 standalone Python exercises, plus two curated Medium/Hard interview routes.

## Choose a route

- [Waymo data engineering](docs/waymo_interview_prep.md)
- [NVIDIA marketing data engineering](docs/marketing_interview_prep.md)
- [Full exercise catalog and overlap analysis](docs/practice_catalog.md)

## Setup and practice

Install Git and Python 3.10 or later. No additional packages are required.

```bash
git clone https://github.com/sysung/local-leetcode.git
cd local-leetcode
```

Choose a question from a route, read its problem statement, and implement `main.py`. For a local exercise, run its existing tests before comparing with `solution.py`:

```bash
cd 35_required_event_window
python3 -m unittest -v test_case.py
python3 main.py
```

Replace the folder with your chosen exercise. Tests import your learner implementation; unfinished stubs intentionally fail. Repository-wide discovery (`python3 -m unittest discover -v`) also includes those stubs. Folder numbers remain stable when an exercise is removed.
