"""Tests for utilities/process_screenshot.py."""

import importlib.util
import sys
from pathlib import Path

import pytest
from PIL import Image

MODULE_PATH = Path(__file__).parent / "process_screenshot.py"
spec = importlib.util.spec_from_file_location(
    "process_screenshot", MODULE_PATH)
process_screenshot = importlib.util.module_from_spec(spec)
sys.modules["process_screenshot"] = process_screenshot
spec.loader.exec_module(process_screenshot)


@pytest.fixture
def profiles():
    return (
        process_screenshot.LIGHT_PROFILE,
        process_screenshot.DARK_PROFILE,
    )


def test_process_file_replaces_source_with_lossless_avif(tmp_path, profiles):
    source = tmp_path / "capture.png"
    original = Image.new("RGBA", (32, 24), (15, 25, 35, 255))
    original.putpixel((3, 4), (255, 127, 1, 255))
    original.save(source)

    outputs = process_screenshot.process_file(
        source,
        None,
        "both",
        2,
        8,
        *profiles,
        overwrite=False,
    )

    assert outputs == [
        tmp_path / "capture-light.avif",
        tmp_path / "capture-dark.avif",
    ]
    assert not source.exists()
    converted = tmp_path / "capture.avif"
    assert converted.exists()
    with Image.open(converted) as decoded:
        assert decoded.convert("RGBA").tobytes() == original.tobytes()
    for output in outputs:
        with Image.open(output) as image:
            assert image.format == "AVIF"
            assert image.size == (52, 44)


def test_process_file_uses_near_lossless_variant_quality(tmp_path, profiles):
    source = tmp_path / "capture.avif"
    Image.new("RGB", (16, 16), (100, 120, 140)).save(
        source, quality=100, speed=0)

    outputs = process_screenshot.process_file(
        source,
        None,
        "light",
        2,
        8,
        *profiles,
    )

    assert outputs == [tmp_path / "capture-light.avif"]
    assert source.exists()
    with Image.open(outputs[0]) as image:
        assert image.format == "AVIF"


def test_process_file_rejects_existing_legacy_output_without_overwrite(
    tmp_path, profiles
):
    source = tmp_path / "capture.png"
    Image.new("RGB", (8, 8), "white").save(source)
    (tmp_path / "capture-light.png").write_bytes(b"legacy")

    try:
        process_screenshot.process_file(
            source,
            None,
            "light",
            2,
            8,
            *profiles,
        )
    except FileExistsError as error:
        assert "capture-light.png" in str(error)
    else:
        raise AssertionError("Expected existing legacy output to be rejected")

    assert source.exists()


def test_is_output_file_recognizes_avif_and_png_outputs():
    assert process_screenshot.is_output_file(Path("capture-light.avif"))
    assert process_screenshot.is_output_file(Path("capture-dark.png"))
    assert not process_screenshot.is_output_file(Path("capture.light.avif"))
