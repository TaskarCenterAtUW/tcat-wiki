"""
akb-compress-transcript.py

Strips VTT headers, entry count numbers, and timestamps from a WebVTT transcript
file, leaving only speaker lines with abbreviated speaker names. Output is
written alongside the original file with a .compressed.txt suffix.

Usage:
    python utilities/akb-compress-transcript.py <path-to-transcript.txt>

Example:
    python utilities/akb-compress-transcript.py local-storage/transcripts/2026-06-23_TCAT_Office_Hours_Transcript.txt
"""

import re
import sys
from pathlib import Path


def compress_transcript(input_path: Path) -> Path:
    text = input_path.read_text(encoding="utf-8")

    lines = text.splitlines()
    speaker_lines: list[str] = []

    # Patterns to skip
    webvtt_header = re.compile(r"^WEBVTT")
    entry_number = re.compile(r"^\d+$")
    timestamp = re.compile(
        r"^\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}")
    blank = re.compile(r"^\s*$")

    for line in lines:
        if webvtt_header.match(line):
            continue
        if entry_number.match(line.strip()):
            continue
        if timestamp.match(line.strip()):
            continue
        if blank.match(line):
            continue
        speaker_lines.append(line.strip())

    def abbreviate_speaker(line: str) -> str:
        """Reduce the speaker name to uppercase initials.

        'Amy Kate Bordenave: text' → 'AKB: text'
        """
        sep = ": "
        idx = line.index(sep)
        name, rest = line[:idx], line[idx + len(sep):]
        initials = "".join(w[0].upper() for w in name.split() if w)
        return initials + sep + rest

    abbreviated: list[str] = []
    for line in speaker_lines:
        if re.match(r"^[A-Za-z].*:", line) and ": " in line:
            abbreviated.append(abbreviate_speaker(line))
        else:
            abbreviated.append(line)

    output_path = input_path.with_name(input_path.stem + ".compressed.txt")
    output_path.write_text("\n".join(abbreviated) + "\n", encoding="utf-8")
    return output_path


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python utilities/akb-compress-transcript.py <path-to-transcript.txt>")
        sys.exit(1)

    input_path = Path(sys.argv[1]).resolve()
    if not input_path.exists():
        print(f"Error: file not found: {input_path}")
        sys.exit(1)

    output_path = compress_transcript(input_path)
    print(f"Compressed transcript written to: {output_path}")


if __name__ == "__main__":
    main()
