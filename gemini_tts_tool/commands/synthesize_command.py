"""Synthesize command implementation.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import sys

import click

from gemini_tts_tool.core.client import AuthenticationError, create_client
from gemini_tts_tool.core.synthesizer import SynthesisError, read_stdin, synthesize_speech
from gemini_tts_tool.core.voices import DEFAULT_MODEL, DEFAULT_VOICE
from gemini_tts_tool.utils import AudioError, expand_path, save_audio_wav


@click.command(name="synthesize")
@click.argument("text", required=False)
@click.option(
    "--input",
    "-i",
    "input_text",
    help="Text to synthesize (alternative to positional arg)",
)
@click.option(
    "--stdin",
    "-s",
    is_flag=True,
    help="Read text from stdin",
)
@click.option(
    "--output",
    "-o",
    required=True,
    help="Output audio file path (required)",
)
@click.option(
    "--voice",
    default=DEFAULT_VOICE,
    help=f"Voice name (default: {DEFAULT_VOICE})",
)
@click.option(
    "--model",
    default=DEFAULT_MODEL,
    help="TTS model (default: flash). Options: flash, pro, or full model name",
)
@click.option(
    "--style",
    help="Style instructions (e.g., 'Speak cheerfully and energetically')",
)
@click.option(
    "--verbose",
    "-V",
    is_flag=True,
    help="Show verbose output",
)
@click.pass_context
def synthesize(
    ctx: click.Context,
    text: str | None,
    input_text: str | None,
    stdin: bool,
    output: str,
    voice: str,
    model: str,
    style: str | None,
    verbose: bool,
) -> None:
    """Synthesize speech from text using Gemini TTS.

    TEXT is the text to synthesize (optional if using --input or --stdin).

    Examples:

    \b
        # Basic synthesis
        gemini-tts-tool synthesize "Hello world" -o greeting.wav

    \b
        # With custom voice and style
        gemini-tts-tool synthesize "Welcome!" -o welcome.wav \\
            --voice Zephyr --style "Speak cheerfully"

    \b
        # From stdin
        echo "Hello" | gemini-tts-tool synthesize --stdin -o output.wav

    \b
        # Using pro model
        gemini-tts-tool synthesize "High quality" -o pro.wav --model pro
    """
    try:
        # Validate output format
        if not output.lower().endswith(".wav"):
            raise ValueError(
                f"Output file must end with .wav extension. Got: {output}\n\n"
                "What to do:\n"
                "  Change your output file to have a .wav extension:\n"
                "  • gemini-tts-tool synthesize 'Hello' -o output.wav\n"
                "  • gemini-tts-tool synthesize 'Hello' -o ~/audio/greeting.wav\n\n"
                "Note: Currently only WAV format is supported."
            )

        # Determine input source (priority: stdin > input_text > text)
        input_text_final: str | None = None
        if stdin:
            if verbose:
                click.echo("Reading from stdin...", err=True)
            input_text_final = read_stdin()
        elif input_text:
            input_text_final = input_text
        elif text:
            input_text_final = text
        else:
            raise click.UsageError(
                "No input provided. Provide TEXT argument, use --input, or use --stdin"
            )

        if not input_text_final or not input_text_final.strip():
            raise ValueError("Input text cannot be empty")

        # Expand output path
        output_path = expand_path(output)

        if verbose:
            click.echo(f"Model: {model}", err=True)
            click.echo(f"Voice: {voice}", err=True)
            if style:
                click.echo(f"Style: {style}", err=True)
            click.echo(f"Text length: {len(input_text_final)} characters", err=True)

        # Create client from context or create new one
        client = ctx.obj.get("client") if ctx.obj else None
        if not client:
            client = create_client()

        # Synthesize
        if verbose:
            click.echo("Synthesizing speech...", err=True)

        audio_data = synthesize_speech(
            client=client,
            text=input_text_final,
            voice=voice,
            model=model,
            system_instruction=style,
        )

        # Save audio
        if verbose:
            click.echo(f"Saving audio to {output_path}...", err=True)

        save_audio_wav(audio_data, output_path)

        # Success message
        click.echo(f"✓ Speech synthesized successfully: {output_path}", err=True)

    except (AuthenticationError, SynthesisError, AudioError, ValueError) as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        if verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)
