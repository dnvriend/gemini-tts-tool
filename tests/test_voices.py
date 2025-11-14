"""Tests for gemini_tts_tool.core.voices module.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import pytest

from gemini_tts_tool.core.voices import (
    DEFAULT_MODEL,
    DEFAULT_VOICE,
    MODELS,
    VOICES,
    validate_model,
    validate_voice,
)


def test_voices_catalog() -> None:
    """Test VOICES catalog has expected voices."""
    assert "Puck" in VOICES
    assert "Kore" in VOICES
    assert "Zephyr" in VOICES
    assert "Charon" in VOICES
    assert "Fenrir" in VOICES
    assert len(VOICES) == 30  # 30 total voices


def test_models_catalog() -> None:
    """Test MODELS catalog has expected models."""
    assert "flash" in MODELS
    assert "pro" in MODELS
    assert MODELS["flash"] == "gemini-2.5-flash-preview-tts"
    assert MODELS["pro"] == "gemini-2.5-pro-preview-tts"


def test_default_voice() -> None:
    """Test DEFAULT_VOICE is valid."""
    assert DEFAULT_VOICE == "Puck"
    assert DEFAULT_VOICE in VOICES


def test_default_model() -> None:
    """Test DEFAULT_MODEL is valid."""
    assert DEFAULT_MODEL == "gemini-2.5-flash-preview-tts"
    assert DEFAULT_MODEL in MODELS.values()


def test_validate_voice_valid() -> None:
    """Test validate_voice with valid voices."""
    assert validate_voice("Puck") == "Puck"
    assert validate_voice("Kore") == "Kore"
    assert validate_voice("Zephyr") == "Zephyr"


def test_validate_voice_invalid() -> None:
    """Test validate_voice with invalid voice."""
    with pytest.raises(ValueError, match="Invalid voice 'InvalidVoice'"):
        validate_voice("InvalidVoice")

    with pytest.raises(ValueError, match="What to do:"):
        validate_voice("UnknownVoice")


def test_validate_voice_error_message_helpful() -> None:
    """Test validate_voice error message contains helpful information."""
    try:
        validate_voice("BadVoice")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        error_msg = str(e)
        assert "gemini-tts-tool list-voices" in error_msg
        assert "Available voices:" in error_msg
        assert "What to do:" in error_msg


def test_validate_model_alias() -> None:
    """Test validate_model with model aliases."""
    assert validate_model("flash") == "gemini-2.5-flash-preview-tts"
    assert validate_model("pro") == "gemini-2.5-pro-preview-tts"


def test_validate_model_full_name() -> None:
    """Test validate_model with full model names."""
    assert validate_model("gemini-2.5-flash-preview-tts") == "gemini-2.5-flash-preview-tts"
    assert validate_model("gemini-2.5-pro-preview-tts") == "gemini-2.5-pro-preview-tts"


def test_validate_model_invalid() -> None:
    """Test validate_model with invalid model."""
    with pytest.raises(ValueError, match="Invalid model 'invalid-model'"):
        validate_model("invalid-model")

    with pytest.raises(ValueError, match="What to do:"):
        validate_model("bad-model")


def test_validate_model_error_message_helpful() -> None:
    """Test validate_model error message contains helpful information."""
    try:
        validate_model("wrong-model")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        error_msg = str(e)
        assert "gemini-tts-tool list-models" in error_msg
        assert "Available models:" in error_msg
        assert "flash" in error_msg
        assert "pro" in error_msg
        assert "What to do:" in error_msg
