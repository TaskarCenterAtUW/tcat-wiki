"""Tests for utilities/akb_compress_transcript.py."""

import subprocess
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).parent / "akb_compress_transcript.py"


def test_compresses_both_webvtt_timestamp_formats(tmp_path: Path) -> None:
    transcript = tmp_path / "transcript.vtt"
    transcript.write_text(
        "WEBVTT\n\n"
        "1\n"
        "00:00.000 --> 00:01.000\n"
        "Amy Kate Bordenave: Please report um, but continue.\n\n"
        "2\n"
        "00:00:02.000 --> 00:00:03.000\n"
        "TCAT Team: We uh-huh, mm-hmm help.\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), str(transcript)],
        check=True,
        capture_output=True,
        text=True,
    )

    compressed = tmp_path / "transcript.compressed.txt"
    assert compressed.read_text(encoding="utf-8") == (
        "AKB: Please report but continue.\n"
        "TT: We help.\n"
    )
    assert str(compressed) in result.stdout
