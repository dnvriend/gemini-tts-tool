"""List commands for voices and models.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import click

from gemini_tts_tool.core.voices import MODELS, VOICES


@click.command(name="list-voices")
def list_voices() -> None:
    """List all available Gemini TTS voices.

    Shows the 30 available voices that can be used with the --voice option
    in synthesize and multi-voice commands.

    Example:

    \b
        gemini-tts-tool list-voices
    """
    click.echo("Available Gemini TTS Voices (30 total):\n")
    for i, voice in enumerate(VOICES, 1):
        click.echo(f"  {i:2d}. {voice}")
    click.echo("\nDefault voice: Puck")
    click.echo("\nUse with: --voice <name>")


@click.command(name="list-models")
def list_models() -> None:
    """List all available Gemini TTS models.

    Shows the available models and their aliases for use with the --model option.

    Example:

    \b
        gemini-tts-tool list-models
    """
    click.echo("Available Gemini TTS Models:\n")

    for alias, full_name in MODELS.items():
        click.echo(f"  • {alias:5s} → {full_name}")

    click.echo("\nDefault model: flash (gemini-2.5-flash-preview-tts)")
    click.echo("\nModel characteristics:")
    click.echo("  • flash: Fast synthesis (~500ms latency)")
    click.echo("  • pro:   High-quality synthesis (~1-2s latency)")
    click.echo("\nUse with: --model <alias> or --model <full-name>")
