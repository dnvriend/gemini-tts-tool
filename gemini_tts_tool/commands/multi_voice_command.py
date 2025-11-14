"""Multi-voice command implementation.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import sys

import click

from gemini_tts_tool.core.client import AuthenticationError, create_client
from gemini_tts_tool.core.synthesizer import SynthesisError, synthesize_multi_voice
from gemini_tts_tool.core.voices import DEFAULT_MODEL
from gemini_tts_tool.utils import AudioError, expand_path, read_file, save_audio_wav


@click.command(name="multi-voice")
@click.option(
    "--input-file",
    required=True,
    help="Input dialogue file with speaker labels (e.g., 'Host: Hello')",
)
@click.option(
    "--output",
    "-o",
    required=True,
    help="Output audio file path (required)",
)
@click.option(
    "--speaker1-voice",
    default="Kore",
    help="Voice for first speaker (default: Kore)",
)
@click.option(
    "--speaker2-voice",
    default="Puck",
    help="Voice for second speaker (default: Puck)",
)
@click.option(
    "--model",
    default=DEFAULT_MODEL,
    help="TTS model (default: flash). Options: flash, pro, or full model name",
)
@click.option(
    "--style",
    help="Style instructions (e.g., 'Make Speaker1 excited, Speaker2 thoughtful')",
)
@click.option(
    "--verbose",
    "-V",
    is_flag=True,
    help="Show verbose output",
)
@click.pass_context
def multi_voice(
    ctx: click.Context,
    input_file: str,
    output: str,
    speaker1_voice: str,
    speaker2_voice: str,
    model: str,
    style: str | None,
    verbose: bool,
) -> None:
    """Synthesize multi-speaker dialogue using Gemini TTS.

    Creates audio with distinct voices for up to 2 speakers. Speaker names are
    automatically detected from dialogue labels in the format "SpeakerName: text".

    Examples:

    \b
        # Basic multi-voice (speakers auto-detected)
        gemini-tts-tool multi-voice --input-file dialogue.txt -o podcast.wav

    \b
        # Custom voices for each speaker
        gemini-tts-tool multi-voice --input-file dialogue.txt -o audio.wav \\
            --speaker1-voice Zephyr --speaker2-voice Aoede

    \b
        # With style instructions
        gemini-tts-tool multi-voice --input-file dialogue.txt -o styled.wav \\
            --style "Make Speaker1 sound excited, Speaker2 sound thoughtful"

    \b
    Dialogue file format (dialogue.txt):
        Host: Welcome to today's show!
        Guest: Thanks for having me!
        Host: Let's get started.
    """
    try:
        # Validate output format
        if not output.lower().endswith(".wav"):
            raise ValueError(
                f"Output file must end with .wav extension. Got: {output}\n\n"
                "What to do:\n"
                "  Change your output file to have a .wav extension:\n"
                "  • gemini-tts-tool multi-voice --input-file dialogue.txt -o podcast.wav\n"
                "  • gemini-tts-tool multi-voice --input-file dialogue.txt "
                "-o ~/audio/output.wav\n\n"
                "Note: Currently only WAV format is supported."
            )

        # Read dialogue file
        if verbose:
            click.echo(f"Reading dialogue from {input_file}...", err=True)

        input_path = expand_path(input_file)
        dialogue = read_file(input_path)

        # Expand output path
        output_path = expand_path(output)

        if verbose:
            click.echo(f"Model: {model}", err=True)
            click.echo(f"Speaker 1 voice: {speaker1_voice}", err=True)
            click.echo(f"Speaker 2 voice: {speaker2_voice}", err=True)
            if style:
                click.echo(f"Style: {style}", err=True)
            click.echo(f"Dialogue length: {len(dialogue)} characters", err=True)

        # Create client
        client = ctx.obj.get("client") if ctx.obj else None
        if not client:
            client = create_client()

        # Synthesize
        if verbose:
            click.echo("Synthesizing multi-voice dialogue...", err=True)

        audio_data = synthesize_multi_voice(
            client=client,
            dialogue=dialogue,
            speaker1_voice=speaker1_voice,
            speaker2_voice=speaker2_voice,
            model=model,
            system_instruction=style,
        )

        # Save audio
        if verbose:
            click.echo(f"Saving audio to {output_path}...", err=True)

        save_audio_wav(audio_data, output_path)

        # Success message
        click.echo(f"✓ Multi-voice dialogue synthesized successfully: {output_path}", err=True)

    except (
        OSError,
        AuthenticationError,
        SynthesisError,
        AudioError,
        ValueError,
        FileNotFoundError,
    ) as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        if verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)
