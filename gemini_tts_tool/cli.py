"""CLI entry point for gemini-tts-tool.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import click

from gemini_tts_tool.utils import get_greeting


@click.command()
@click.version_option(version="0.1.0")
def main() -> None:
    """Convert text into natural-sounding speech using Google's Gemini Text-to-Speech (TTS)"""
    click.echo(get_greeting())


if __name__ == "__main__":
    main()
