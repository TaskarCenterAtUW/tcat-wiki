"""Pytest suite for utilities/akb_build_glossary.py."""

import importlib.util
import sys
from pathlib import Path


MODULE_PATH = Path(__file__).parent / "akb_build_glossary.py"
spec = importlib.util.spec_from_file_location(
    "akb_build_glossary", MODULE_PATH)
if spec is None or spec.loader is None:
    raise ImportError(f"could not load module spec from {MODULE_PATH}")
glossary = importlib.util.module_from_spec(spec)
sys.modules["akb_build_glossary"] = glossary
spec.loader.exec_module(glossary)


def test_review_date_only_difference_is_ignored():
    old = "---\nlast_reviewed: 2026-07-06\n---\n\n# Glossary\n"
    new = "---\nlast_reviewed: 2026-08-28\n---\n\n# Glossary\n"

    assert glossary._only_last_reviewed_differs(old, new)


def test_substantive_difference_is_not_ignored():
    old = "---\nlast_reviewed: 2026-07-06\n---\n\n# Glossary\n"
    new = "---\nlast_reviewed: 2026-08-28\n---\n\n# Changed Glossary\n"

    assert not glossary._only_last_reviewed_differs(old, new)
