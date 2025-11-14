"""Tests for gemini_tts_tool.core.synthesizer module.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

from unittest.mock import MagicMock, patch

import pytest

from gemini_tts_tool.core.synthesizer import (
    SynthesisError,
    read_stdin,
    synthesize_multi_voice,
    synthesize_speech,
)


def create_mock_client() -> MagicMock:
    """Create a mock Gemini client."""
    mock_client = MagicMock()
    return mock_client


def create_mock_response(audio_data: bytes = b"fake-audio-data") -> MagicMock:
    """Create a mock API response with audio data."""
    mock_part = MagicMock()
    mock_part.inline_data.data = audio_data

    mock_content = MagicMock()
    mock_content.parts = [mock_part]

    mock_candidate = MagicMock()
    mock_candidate.content = mock_content

    mock_response = MagicMock()
    mock_response.candidates = [mock_candidate]

    return mock_response


def test_synthesize_speech_basic() -> None:
    """Test basic speech synthesis."""
    mock_client = create_mock_client()
    mock_response = create_mock_response(b"test-audio")
    mock_client.models.generate_content.return_value = mock_response

    result = synthesize_speech(mock_client, "Hello world")

    assert result == b"test-audio"
    mock_client.models.generate_content.assert_called_once()


def test_synthesize_speech_with_voice() -> None:
    """Test speech synthesis with custom voice."""
    mock_client = create_mock_client()
    mock_response = create_mock_response()
    mock_client.models.generate_content.return_value = mock_response

    synthesize_speech(mock_client, "Hello", voice="Kore")

    # Verify voice was passed in config
    call_args = mock_client.models.generate_content.call_args
    assert call_args is not None


def test_synthesize_speech_with_system_instruction() -> None:
    """Test speech synthesis with system instruction."""
    mock_client = create_mock_client()
    mock_response = create_mock_response()
    mock_client.models.generate_content.return_value = mock_response

    synthesize_speech(mock_client, "Hello", system_instruction="Speak cheerfully")

    call_args = mock_client.models.generate_content.call_args
    assert "system_instruction" in call_args.kwargs


def test_synthesize_speech_empty_text_raises_error() -> None:
    """Test synthesize_speech raises error for empty text."""
    mock_client = create_mock_client()

    with pytest.raises(ValueError, match="Text cannot be empty"):
        synthesize_speech(mock_client, "")

    with pytest.raises(ValueError, match="Text cannot be empty"):
        synthesize_speech(mock_client, "   ")


def test_synthesize_speech_empty_text_error_message_helpful() -> None:
    """Test error message for empty text contains helpful information."""
    mock_client = create_mock_client()

    try:
        synthesize_speech(mock_client, "")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        error_msg = str(e)
        assert "What to do:" in error_msg
        assert "gemini-tts-tool synthesize" in error_msg
        assert "--stdin" in error_msg


def test_synthesize_speech_invalid_voice_raises_error() -> None:
    """Test synthesize_speech validates voice."""
    mock_client = create_mock_client()

    with pytest.raises(ValueError, match="Invalid voice"):
        synthesize_speech(mock_client, "Hello", voice="InvalidVoice")


def test_synthesize_speech_no_candidates_raises_error() -> None:
    """Test synthesize_speech handles empty response."""
    mock_client = create_mock_client()
    mock_response = MagicMock()
    mock_response.candidates = []
    mock_client.models.generate_content.return_value = mock_response

    with pytest.raises(SynthesisError, match="No audio generated"):
        synthesize_speech(mock_client, "Hello")


def test_synthesize_speech_no_audio_data_raises_error() -> None:
    """Test synthesize_speech handles response without audio."""
    mock_client = create_mock_client()
    mock_part = MagicMock()
    mock_part.inline_data = None

    mock_content = MagicMock()
    mock_content.parts = [mock_part]

    mock_candidate = MagicMock()
    mock_candidate.content = mock_content

    mock_response = MagicMock()
    mock_response.candidates = [mock_candidate]
    mock_client.models.generate_content.return_value = mock_response

    with pytest.raises(SynthesisError, match="No audio data found"):
        synthesize_speech(mock_client, "Hello")


def test_synthesize_multi_voice_basic() -> None:
    """Test basic multi-voice synthesis."""
    mock_client = create_mock_client()
    mock_response = create_mock_response(b"multi-voice-audio")
    mock_client.models.generate_content.return_value = mock_response

    dialogue = "Host: Hello\nGuest: Hi there"

    # Mock the types module to avoid SDK validation errors
    with patch("gemini_tts_tool.core.synthesizer.types") as mock_types:
        # Configure mocks to return mock objects
        mock_types.GenerateContentConfig.return_value = MagicMock()
        mock_types.SpeechConfig.return_value = MagicMock()
        mock_types.VoiceConfig.return_value = MagicMock()
        mock_types.MultiSpeakerVoiceConfig.return_value = MagicMock()
        mock_types.SpeakerVoiceConfig.return_value = MagicMock()
        mock_types.PrebuiltVoiceConfig.return_value = MagicMock()

        result = synthesize_multi_voice(mock_client, dialogue)

        assert result == b"multi-voice-audio"
        mock_client.models.generate_content.assert_called_once()


def test_synthesize_multi_voice_custom_voices() -> None:
    """Test multi-voice synthesis with custom voices."""
    mock_client = create_mock_client()
    mock_response = create_mock_response()
    mock_client.models.generate_content.return_value = mock_response

    dialogue = "Alice: Hello\nBob: Hi"

    # Mock the types module to avoid SDK validation errors
    with patch("gemini_tts_tool.core.synthesizer.types") as mock_types:
        # Configure mocks to return mock objects
        mock_types.GenerateContentConfig.return_value = MagicMock()
        mock_types.SpeechConfig.return_value = MagicMock()
        mock_types.VoiceConfig.return_value = MagicMock()
        mock_types.MultiSpeakerVoiceConfig.return_value = MagicMock()
        mock_types.SpeakerVoiceConfig.return_value = MagicMock()
        mock_types.PrebuiltVoiceConfig.return_value = MagicMock()

        synthesize_multi_voice(
            mock_client, dialogue, speaker1_voice="Zephyr", speaker2_voice="Aoede"
        )

        mock_client.models.generate_content.assert_called_once()


def test_synthesize_multi_voice_empty_dialogue_raises_error() -> None:
    """Test synthesize_multi_voice raises error for empty dialogue."""
    mock_client = create_mock_client()

    with pytest.raises(ValueError, match="Dialogue cannot be empty"):
        synthesize_multi_voice(mock_client, "")


def test_synthesize_multi_voice_one_speaker_raises_error() -> None:
    """Test synthesize_multi_voice requires at least 2 speakers."""
    mock_client = create_mock_client()

    with pytest.raises(ValueError, match="requires at least 2 speakers"):
        synthesize_multi_voice(mock_client, "Host: Hello\nHost: How are you?")


def test_synthesize_multi_voice_too_many_speakers_raises_error() -> None:
    """Test synthesize_multi_voice limits to 2 speakers."""
    mock_client = create_mock_client()
    dialogue = "Alice: Hi\nBob: Hello\nCharlie: Hey there"

    with pytest.raises(ValueError, match="supports up to 2 speakers"):
        synthesize_multi_voice(mock_client, dialogue)


def test_synthesize_multi_voice_error_message_helpful() -> None:
    """Test multi-voice error messages are helpful."""
    mock_client = create_mock_client()

    try:
        synthesize_multi_voice(mock_client, "Host: Hello")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        error_msg = str(e)
        assert "What to do:" in error_msg
        assert "SpeakerName:" in error_msg


def test_read_stdin_with_input() -> None:
    """Test read_stdin with valid input."""
    with patch("sys.stdin") as mock_stdin:
        mock_stdin.isatty.return_value = False
        mock_stdin.read.return_value = "Hello from stdin"

        result = read_stdin()
        assert result == "Hello from stdin"


def test_read_stdin_no_pipe_raises_error() -> None:
    """Test read_stdin raises error when not piped."""
    with patch("sys.stdin") as mock_stdin:
        mock_stdin.isatty.return_value = True

        with pytest.raises(ValueError, match="No input provided via stdin"):
            read_stdin()


def test_read_stdin_empty_input_raises_error() -> None:
    """Test read_stdin raises error for empty input."""
    with patch("sys.stdin") as mock_stdin:
        mock_stdin.isatty.return_value = False
        mock_stdin.read.return_value = "   "

        with pytest.raises(ValueError, match="Empty input from stdin"):
            read_stdin()
