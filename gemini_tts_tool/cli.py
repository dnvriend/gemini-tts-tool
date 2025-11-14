"""CLI entry point for gemini-tts-tool.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import click

from gemini_tts_tool.commands.list_commands import list_models, list_voices
from gemini_tts_tool.commands.multi_voice_command import multi_voice
from gemini_tts_tool.commands.synthesize_command import synthesize


@click.group()
@click.version_option(version="1.0.0")
@click.pass_context
def main(ctx: click.Context) -> None:
    """Gemini TTS Tool - AI-powered text-to-speech with 30+ voices.

    Convert text into natural-sounding speech using Google's Gemini TTS API.
    Supports single-voice synthesis, multi-speaker dialogues, and natural
    language style control.

    \b
    Authentication:
      Set GEMINI_API_KEY or GOOGLE_API_KEY environment variable.
      Get your API key from: https://aistudio.google.com/app/apikey

    \b
    For Vertex AI:
      Set GOOGLE_GENAI_USE_VERTEXAI=true
      Set GOOGLE_CLOUD_PROJECT='your-project-id'
      Set GOOGLE_CLOUD_LOCATION='us-central1'

    \b
    Examples:
      gemini-tts-tool synthesize "Hello world" -o greeting.wav
      gemini-tts-tool multi-voice --input-file dialogue.txt -o podcast.wav
      gemini-tts-tool list-voices
      gemini-tts-tool list-models

    \b
    For detailed help on each command:
      gemini-tts-tool synthesize --help
      gemini-tts-tool multi-voice --help
    """
    # Initialize context object for passing client between commands
    ctx.ensure_object(dict)


# Register commands
main.add_command(synthesize)
main.add_command(multi_voice)
main.add_command(list_voices)
main.add_command(list_models)


if __name__ == "__main__":
    main()
