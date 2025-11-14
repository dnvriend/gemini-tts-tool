"""Core TTS synthesis logic using Gemini API.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import sys
from typing import Any

from google import genai
from google.genai import types

from gemini_tts_tool.core.voices import DEFAULT_MODEL, DEFAULT_VOICE, validate_model, validate_voice


class SynthesisError(Exception):
    """Base exception for TTS synthesis errors."""

    pass


def synthesize_speech(
    client: genai.Client,
    text: str,
    voice: str = DEFAULT_VOICE,
    model: str = DEFAULT_MODEL,
    system_instruction: str | None = None,
) -> bytes:
    """Synthesize speech from text using Gemini TTS.

    Args:
        client: Gemini API client
        text: Text to synthesize
        voice: Voice name (default: Puck)
        model: Model name or alias (default: flash)
        system_instruction: Optional style instructions

    Returns:
        Audio data as bytes (PCM, 24kHz, mono, 16-bit)

    Raises:
        SynthesisError: If synthesis fails
        ValueError: If parameters are invalid
    """
    # Validate inputs
    voice = validate_voice(voice)
    model = validate_model(model)

    if not text or not text.strip():
        raise ValueError(
            "Text cannot be empty.\n\n"
            "What to do:\n"
            "  Provide text to synthesize using one of these methods:\n"
            "  1. Positional argument: gemini-tts-tool synthesize 'Hello world' -o output.wav\n"
            "  2. Named option: gemini-tts-tool synthesize --input 'Hello world' -o output.wav\n"
            "  3. From stdin: echo 'Hello world' | gemini-tts-tool synthesize --stdin -o output.wav"
        )

    try:
        # Configure TTS request
        config = types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)
                )
            ),
        )

        # Build request contents
        contents = [text]

        # Add system instruction if provided
        kwargs: dict[str, Any] = {"model": model, "contents": contents, "config": config}
        if system_instruction:
            kwargs["system_instruction"] = system_instruction

        # Make API call
        response = client.models.generate_content(**kwargs)

        # Extract audio data
        if not response.candidates:
            raise SynthesisError("No audio generated - empty response from API")

        candidate = response.candidates[0]
        if not candidate.content or not candidate.content.parts:
            raise SynthesisError("No content in response")

        # Get the first part with inline data
        for part in candidate.content.parts:
            if part.inline_data and part.inline_data.data:
                return part.inline_data.data

        raise SynthesisError("No audio data found in response")

    except ValueError:
        # Re-raise validation errors
        raise
    except Exception as e:
        raise SynthesisError(f"Failed to synthesize speech: {e}") from e


def synthesize_multi_voice(
    client: genai.Client,
    dialogue: str,
    speaker1_voice: str = "Kore",
    speaker2_voice: str = "Puck",
    model: str = DEFAULT_MODEL,
    system_instruction: str | None = None,
) -> bytes:
    """Synthesize multi-speaker dialogue using Gemini TTS.

    Args:
        client: Gemini API client
        dialogue: Dialogue text with speaker labels (e.g., "Host: Hello\nGuest: Hi there")
        speaker1_voice: Voice for first speaker
        speaker2_voice: Voice for second speaker
        model: Model name or alias
        system_instruction: Optional style instructions

    Returns:
        Audio data as bytes (PCM, 24kHz, mono, 16-bit)

    Raises:
        SynthesisError: If synthesis fails
        ValueError: If parameters are invalid
    """
    # Validate inputs
    speaker1_voice = validate_voice(speaker1_voice)
    speaker2_voice = validate_voice(speaker2_voice)
    model = validate_model(model)

    if not dialogue or not dialogue.strip():
        raise ValueError(
            "Dialogue cannot be empty.\n\n"
            "What to do:\n"
            "  Create a dialogue file with speaker labels. Example (dialogue.txt):\n\n"
            "    Host: Welcome to today's show!\n"
            "    Guest: Thanks for having me!\n"
            "    Host: Let's dive into our topic.\n\n"
            "  Then use: gemini-tts-tool multi-voice --input-file dialogue.txt -o podcast.wav"
        )

    # Auto-detect speaker names from dialogue
    lines = [line.strip() for line in dialogue.split("\n") if line.strip()]
    speakers = set()
    for line in lines:
        if ":" in line:
            speaker = line.split(":", 1)[0].strip()
            speakers.add(speaker)

    if len(speakers) < 2:
        if speakers:
            detected = f"Only 1 speaker detected: {list(speakers)[0]}"
        else:
            detected = "No speakers detected"
        raise ValueError(
            f"Multi-voice requires at least 2 speakers. {detected}\n\n"
            "What to do:\n"
            "  Format your dialogue with speaker labels (SpeakerName: text).\n\n"
            "  Example dialogue file:\n"
            "    Host: Welcome to today's show!\n"
            "    Guest: Thanks for having me!\n"
            "    Host: Let's get started.\n\n"
            "  Each line must start with 'SpeakerName:' followed by their dialogue.\n"
            "  Use consistent speaker names throughout the dialogue."
        )

    if len(speakers) > 2:
        speakers_str = ", ".join(speakers)
        raise ValueError(
            f"Gemini TTS multi-voice supports up to 2 speakers. "
            f"Found {len(speakers)}: {speakers_str}"
        )

    # Map speakers to voices
    speaker_list = sorted(speakers)  # Consistent ordering
    speaker1_name = speaker_list[0]
    speaker2_name = speaker_list[1]

    try:
        # Configure multi-speaker TTS
        config = types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                    speaker_voice_configs=[
                        types.SpeakerVoiceConfig(
                            speaker=speaker1_name,
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name=speaker1_voice
                                )
                            ),
                        ),
                        types.SpeakerVoiceConfig(
                            speaker=speaker2_name,
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name=speaker2_voice
                                )
                            ),
                        ),
                    ]
                )
            ),
        )

        # Build request
        # Note: For multi-voice, style instructions should be included in the prompt
        contents = dialogue
        if system_instruction:
            contents = f"{system_instruction}\n\n{dialogue}"

        kwargs: dict[str, Any] = {"model": model, "contents": [contents], "config": config}

        # Make API call
        response = client.models.generate_content(**kwargs)

        # Extract audio
        if not response.candidates:
            raise SynthesisError("No audio generated - empty response from API")

        candidate = response.candidates[0]
        if not candidate.content or not candidate.content.parts:
            raise SynthesisError("No content in response")

        for part in candidate.content.parts:
            if part.inline_data and part.inline_data.data:
                return part.inline_data.data

        raise SynthesisError("No audio data found in response")

    except ValueError:
        raise
    except Exception as e:
        raise SynthesisError(f"Failed to synthesize multi-voice dialogue: {e}") from e


def read_stdin() -> str:
    """Read text from stdin.

    Returns:
        Text from stdin

    Raises:
        ValueError: If stdin is empty
    """
    if sys.stdin.isatty():
        raise ValueError("No input provided via stdin")

    text = sys.stdin.read().strip()
    if not text:
        raise ValueError("Empty input from stdin")

    return text
