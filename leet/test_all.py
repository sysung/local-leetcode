"""Expose standalone exercises to unittest discovery and VS Code's Testing panel."""

import importlib.util
from pathlib import Path
import sys
import unittest


def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()
    root = Path(__file__).resolve().parent
    for test_file in sorted(root.glob("[0-9][0-9]_*/test_case.py")):
        # Unique names keep test IDs and source locations separate by exercise.
        module_name = f"{test_file.parent.name}.test_case"
        spec = importlib.util.spec_from_file_location(module_name, test_file)
        module = importlib.util.module_from_spec(spec)

        # Each test file imports its own sibling main.py, not a cached neighbor.
        previous_main = sys.modules.pop("main", None)
        sys.path.insert(0, str(test_file.parent))
        try:
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            suite.addTests(loader.loadTestsFromModule(module))
        finally:
            sys.path.pop(0)
            sys.modules.pop("main", None)
            if previous_main is not None:
                sys.modules["main"] = previous_main
    return suite
