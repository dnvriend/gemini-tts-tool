"""Tests for gemini_tts_tool.utils module.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import os
import wave
from pathlib import Path

import pytest

from gemini_tts_tool.utils import (
    AudioError,
    expand_path,
    read_file,
    save_audio_wav,
    validate_output_format,
)


def test_validate_output_format_valid() -> None:
    """Test validate_output_format with valid formats."""
    assert validate_output_format("output.wav") == "wav"
    assert validate_output_format("output.mp3") == "mp3"
    assert validate_output_format("output.ogg") == "ogg"
    assert validate_output_format("output.m4a") == "m4a"
    assert validate_output_format("output.flac") == "flac"
    assert validate_output_format("OUTPUT.WAV") == "wav"  # Case insensitive
    assert validate_output_format(Path("dir/output.wav")) == "wav"


def test_validate_output_format_invalid() -> None:
    """Test validate_output_format with invalid formats."""
    with pytest.raises(ValueError, match="Unsupported audio format"):
        validate_output_format("output.txt")

    with pytest.raises(ValueError, match="Unsupported audio format"):
        validate_output_format("output.pdf")


def test_expand_path() -> None:
    """Test expand_path with various inputs."""
    # Test with home directory
    result = expand_path("~/test/file.txt")
    assert result.is_absolute()
    assert "~" not in str(result)

    # Test with environment variable
    os.environ["TEST_VAR"] = "/tmp/test"
    result = expand_path("$TEST_VAR/file.txt")
    assert "/tmp/test/file.txt" in str(result)

    # Test with relative path
    result = expand_path("./file.txt")
    assert result.is_absolute()


def test_read_file(tmp_path: Path) -> None:
    """Test read_file with valid file."""
    test_file = tmp_path / "test.txt"
    test_content = "Hello, World!\nThis is a test."
    test_file.write_text(test_content, encoding="utf-8")

    result = read_file(test_file)
    assert result == test_content


def test_read_file_not_found() -> None:
    """Test read_file with non-existent file."""
    with pytest.raises(FileNotFoundError, match="File not found"):
        read_file("/nonexistent/file.txt")


def test_save_audio_wav(tmp_path: Path) -> None:
    """Test save_audio_wav creates valid WAV file."""
    # Create fake PCM audio data (1 second of silence at 24kHz, 16-bit)
    sample_rate = 24000
    duration_seconds = 1
    num_samples = sample_rate * duration_seconds
    # 16-bit samples = 2 bytes per sample
    audio_data = b"\x00\x00" * num_samples

    output_path = tmp_path / "output.wav"
    save_audio_wav(audio_data, output_path)

    # Verify file exists
    assert output_path.exists()

    # Verify WAV file properties
    with wave.open(str(output_path), "rb") as wav_file:
        assert wav_file.getnchannels() == 1  # Mono
        assert wav_file.getsampwidth() == 2  # 16-bit
        assert wav_file.getframerate() == 24000  # 24kHz
        assert wav_file.getnframes() == num_samples


def test_save_audio_wav_creates_directories(tmp_path: Path) -> None:
    """Test save_audio_wav creates parent directories."""
    audio_data = b"\x00\x00" * 1000
    output_path = tmp_path / "subdir1" / "subdir2" / "output.wav"

    save_audio_wav(audio_data, output_path)

    assert output_path.exists()
    assert output_path.parent.exists()


def test_save_audio_wav_error(tmp_path: Path) -> None:
    """Test save_audio_wav error handling."""
    # Create invalid audio data (wrong format)
    invalid_path = tmp_path / "subdir"
    invalid_path.mkdir()

    # Try to save with invalid path (directory instead of file)
    with pytest.raises(AudioError, match="Failed to save WAV file"):
        save_audio_wav(b"test", invalid_path)
