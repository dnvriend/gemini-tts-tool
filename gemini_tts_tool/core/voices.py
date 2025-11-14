"""Voice and model catalog for Gemini TTS.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

# Gemini TTS Models
MODELS = {
    "flash": "gemini-2.5-flash-preview-tts",
    "pro": "gemini-2.5-pro-preview-tts",
}

# Default model
DEFAULT_MODEL = "gemini-2.5-flash-preview-tts"

# Available Gemini TTS Voices (30 total)
VOICES = [
    "Zephyr",
    "Puck",
    "Charon",
    "Kore",
    "Fenrir",
    "Leda",
    "Orus",
    "Aoede",
    "Callirrhoe",
    "Autonoe",
    "Enceladus",
    "Iapetus",
    "Umbriel",
    "Algieba",
    "Despina",
    "Erinome",
    "Algenib",
    "Rasalgethi",
    "Laomedeia",
    "Achernar",
    "Alnilam",
    "Schedar",
    "Gacrux",
    "Pulcherrima",
    "Achird",
    "Zubenelgenubi",
    "Vindemiatrix",
    "Sadachbia",
    "Sadaltager",
    "Sulafat",
]

# Default voice
DEFAULT_VOICE = "Puck"


def validate_voice(voice: str) -> str:
    """Validate voice name.

    Args:
        voice: Voice name to validate

    Returns:
        Validated voice name

    Raises:
        ValueError: If voice is not valid
    """
    if voice not in VOICES:
        raise ValueError(
            f"Invalid voice '{voice}'.\n\n"
            f"Available voices: {', '.join(VOICES[:5])}... (30 total)\n\n"
            "What to do:\n"
            "  1. View all voices: gemini-tts-tool list-voices\n"
            "  2. Try a popular voice: --voice Puck (default), --voice Kore, or --voice Zephyr\n"
            "  3. Use any voice from the list with: --voice <VoiceName>"
        )
    return voice


def validate_model(model: str) -> str:
    """Validate and resolve model name.

    Args:
        model: Model name or alias to validate

    Returns:
        Full model name

    Raises:
        ValueError: If model is not valid
    """
    # Check if it's an alias
    if model in MODELS:
        return MODELS[model]

    # Check if it's a full model name
    if model in MODELS.values():
        return model

    raise ValueError(
        f"Invalid model '{model}'.\n\n"
        "Available models:\n"
        "  • flash (default) - Fast synthesis, ~500ms latency\n"
        "  • pro - High quality, ~1-2s latency\n\n"
        "What to do:\n"
        "  1. View all models: gemini-tts-tool list-models\n"
        "  2. Use model alias: --model flash or --model pro\n"
        "  3. Use full name: --model gemini-2.5-flash-preview-tts"
    )
