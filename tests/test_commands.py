"""Tests for gemini_tts_tool CLI commands.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

from pathlib import Path
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from gemini_tts_tool.cli import main


@pytest.fixture
def runner() -> CliRunner:
    """Create Click CLI test runner."""
    return CliRunner()


def test_synthesize_invalid_output_format(runner: CliRunner) -> None:
    """Test synthesize rejects non-wav output files."""
    result = runner.invoke(main, ["synthesize", "Hello", "-o", "output.mp3"])

    assert result.exit_code == 1
    assert "Output file must end with .wav extension" in result.output
    assert "Got: output.mp3" in result.output
    assert "What to do:" in result.output


def test_synthesize_valid_wav_output(runner: CliRunner, tmp_path: Path) -> None:
    """Test synthesize accepts .wav output files."""
    output_file = tmp_path / "output.wav"

    with patch("gemini_tts_tool.commands.synthesize_command.create_client"):
        with patch("gemini_tts_tool.commands.synthesize_command.synthesize_speech") as mock_synth:
            mock_synth.return_value = b"fake-audio-data"

            result = runner.invoke(main, ["synthesize", "Hello", "-o", str(output_file)])

            assert result.exit_code == 0
            assert output_file.exists()


def test_synthesize_case_insensitive_wav(runner: CliRunner, tmp_path: Path) -> None:
    """Test synthesize accepts .WAV (uppercase) extension."""
    output_file = tmp_path / "OUTPUT.WAV"

    with patch("gemini_tts_tool.commands.synthesize_command.create_client"):
        with patch("gemini_tts_tool.commands.synthesize_command.synthesize_speech") as mock_synth:
            mock_synth.return_value = b"fake-audio-data"

            result = runner.invoke(main, ["synthesize", "Hello", "-o", str(output_file)])

            assert result.exit_code == 0
            assert output_file.exists()


def test_multi_voice_invalid_output_format(runner: CliRunner, tmp_path: Path) -> None:
    """Test multi-voice rejects non-wav output files."""
    dialogue_file = tmp_path / "dialogue.txt"
    dialogue_file.write_text("Host: Hello\nGuest: Hi there")

    result = runner.invoke(
        main, ["multi-voice", "--input-file", str(dialogue_file), "-o", "output.mp3"]
    )

    assert result.exit_code == 1
    assert "Output file must end with .wav extension" in result.output
    assert "Got: output.mp3" in result.output
    assert "What to do:" in result.output


def test_multi_voice_valid_wav_output(runner: CliRunner, tmp_path: Path) -> None:
    """Test multi-voice accepts .wav output files."""
    dialogue_file = tmp_path / "dialogue.txt"
    dialogue_file.write_text("Host: Hello\nGuest: Hi there")
    output_file = tmp_path / "output.wav"

    with patch("gemini_tts_tool.commands.multi_voice_command.create_client"):
        with patch(
            "gemini_tts_tool.commands.multi_voice_command.synthesize_multi_voice"
        ) as mock_synth:
            mock_synth.return_value = b"fake-audio-data"

            result = runner.invoke(
                main, ["multi-voice", "--input-file", str(dialogue_file), "-o", str(output_file)]
            )

            assert result.exit_code == 0
            assert output_file.exists()


def test_synthesize_txt_extension_rejected(runner: CliRunner) -> None:
    """Test synthesize rejects .txt files."""
    result = runner.invoke(main, ["synthesize", "Hello", "-o", "output.txt"])

    assert result.exit_code == 1
    assert "Output file must end with .wav extension" in result.output
    assert "only WAV format is supported" in result.output


def test_synthesize_no_extension_rejected(runner: CliRunner) -> None:
    """Test synthesize rejects files without extension."""
    result = runner.invoke(main, ["synthesize", "Hello", "-o", "output"])

    assert result.exit_code == 1
    assert "Output file must end with .wav extension" in result.output


def test_multi_voice_txt_extension_rejected(runner: CliRunner, tmp_path: Path) -> None:
    """Test multi-voice rejects .txt output files."""
    dialogue_file = tmp_path / "dialogue.txt"
    dialogue_file.write_text("Host: Hello\nGuest: Hi there")

    result = runner.invoke(
        main, ["multi-voice", "--input-file", str(dialogue_file), "-o", "output.txt"]
    )

    assert result.exit_code == 1
    assert "Output file must end with .wav extension" in result.output
