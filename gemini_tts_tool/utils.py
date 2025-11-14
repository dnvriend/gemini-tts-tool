"""Utility functions for gemini-tts-tool.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import os
import wave
from pathlib import Path


class AudioError(Exception):
    """Base exception for audio processing errors."""

    pass


def save_audio_wav(audio_data: bytes, output_path: str | Path) -> None:
    """Save PCM audio data as WAV file.

    Gemini TTS returns raw PCM data (24kHz, mono, 16-bit).
    This function adds the WAV header.

    Args:
        audio_data: Raw PCM audio bytes from Gemini TTS
        output_path: Path to save WAV file

    Raises:
        AudioError: If saving fails
    """
    try:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with wave.open(str(output_path), "wb") as wav_file:
            # Gemini TTS specs: 24kHz, mono, 16-bit
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 16-bit = 2 bytes
            wav_file.setframerate(24000)  # 24kHz
            wav_file.writeframes(audio_data)

    except Exception as e:
        raise AudioError(f"Failed to save WAV file: {e}") from e


def validate_output_format(output_path: str | Path) -> str:
    """Validate and extract audio format from output path.

    Args:
        output_path: Output file path

    Returns:
        Audio format (wav, mp3, ogg, m4a, flac)

    Raises:
        ValueError: If format is unsupported
    """
    output_path = Path(output_path)
    ext = output_path.suffix.lower().lstrip(".")

    supported_formats = ["wav", "mp3", "ogg", "m4a", "flac"]
    if ext not in supported_formats:
        raise ValueError(
            f"Unsupported audio format '{ext}'. Supported formats: {', '.join(supported_formats)}"
        )

    return ext


def expand_path(path: str) -> Path:
    """Expand user home and environment variables in path.

    Args:
        path: Path string potentially containing ~ or env vars

    Returns:
        Expanded absolute Path object
    """
    return Path(os.path.expanduser(os.path.expandvars(path))).resolve()


def read_file(file_path: str | Path) -> str:
    """Read text file contents.

    Args:
        file_path: Path to text file

    Returns:
        File contents as string

    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If file cannot be read
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        return file_path.read_text(encoding="utf-8")
    except Exception as e:
        raise OSError(f"Failed to read file {file_path}: {e}") from e
