"""gemini-tts-tool: Convert text into natural-sounding speech using Gemini TTS

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

__version__ = "1.0.0"

# Public API exports for library usage
from gemini_tts_tool.core.client import create_client
from gemini_tts_tool.core.synthesizer import synthesize_multi_voice, synthesize_speech
from gemini_tts_tool.core.voices import MODELS, VOICES

__all__ = [
    "create_client",
    "synthesize_speech",
    "synthesize_multi_voice",
    "VOICES",
    "MODELS",
]
