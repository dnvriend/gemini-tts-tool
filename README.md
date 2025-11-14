# gemini-tts-tool

[![Python Version](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://github.com/python/mypy)
[![AI Generated](https://img.shields.io/badge/AI-Generated-blueviolet.svg)](https://www.anthropic.com/claude)
[![Claude Sonnet 4.5](https://img.shields.io/badge/Model-Claude_Sonnet_4.5-blue)](https://www.anthropic.com/claude)
[![Built with Claude Code](https://img.shields.io/badge/Built_with-Claude_Code-5A67D8.svg)](https://www.anthropic.com/claude/code)

A CLI and Python library for Google Gemini Text-to-Speech - AI-powered speech synthesis with 30+ voices.

## About

### What is Gemini TTS?

[Google's Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation) is Google's latest evolution in speech synthesis technology that transforms text into natural-sounding audio with **controllable** characteristics. Unlike traditional TTS systems, Gemini TTS enables you to use **natural language** to guide the style, accent, pace, tone, and emotional delivery of synthesized speech.

**Key Differentiators:**
- **Natural Language Control**: Adjust delivery characteristics through simple text instructions (e.g., "Speak cheerfully and energetically")
- **Multi-Speaker Synthesis**: Generate dialogues with up to 2 distinct voices and personalities
- **Dynamic Performance**: Models deliver expressive readings with requested emotions and accents
- **Enhanced Pace Control**: Adjust speaking speed for improved pronunciation accuracy
- **30 Unique Voices**: Each with distinct characteristics - from "Firm" (Kore) to "Excitable" (Fenrir) to "Breezy" (Aoede)

Powered by Gemini 2.5 models (Flash for speed, Pro for quality), the API supports 24 languages with automatic detection and produces high-quality 24kHz mono audio.

**Official Documentation:**
- [Gemini API Speech Generation](https://ai.google.dev/gemini-api/docs/speech-generation)
- [Google Cloud Gemini TTS](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)

### Why This CLI-First Tool?

This tool embraces a **CLI-first design** built specifically for AI agents and automation workflows, transforming Google's powerful Gemini TTS API into a reliable, composable building block for modern development.

**🤖 Agent-Friendly Design**

CLIs provide structured commands with built-in documentation and rich error messages that AI agents can parse and act upon in ReAct (Reasoning and Acting) loops. When an agent encounters an error, our detailed "What to do" sections with examples enable self-correction and continued operation—making this tool superior to standalone scripts for agentic workflows.

**🔗 Composable Architecture**

The design separates concerns: success messages flow to stderr while audio data processing happens independently. This enables seamless piping and integration with other tools—perfect for automation pipelines where different systems need structured operations without interference from diagnostic information.

**🧱 Reusable Building Blocks**

Commands function as discrete, composable units that can be:
- Orchestrated into larger workflows
- Embedded as skills for Claude Code
- Integrated into MCP servers
- Used in shell scripts and automation
- Chained with other CLI tools via pipes

This modularity enables both individual tool use and sophisticated multi-step automation scenarios without modification.

**⚡ Dual-Mode Operation**

The tool operates simultaneously as:
- **CLI Tool**: Direct command-line operations with rich help and examples
- **Python Library**: Programmatic integration with `import gemini_tts_tool`

This flexibility allows teams to choose their integration approach without tool switching, maintaining the same reliable functionality in both modes.

**🏗️ Built for Reliability**

Type safety with strict mypy checking, comprehensive testing, and thorough error handling with actionable feedback ensure both humans and AI agents receive clear guidance. This makes the tool reliable for mission-critical automation workflows where failures must be recoverable.

## Features

- ✅ **30 Unique Voices**: Choose from Puck, Kore, Zephyr, Charon, Aoede, Fenrir, and 24+ more voices
- ✅ **Multi-Speaker Dialogues**: Create conversations with up to 2 distinct voices
- ✅ **Natural Language Style Control**: Adjust tone, pace, emotion with simple text instructions
- ✅ **Dual Authentication**: Supports both Gemini Developer API and Vertex AI
- ✅ **Multiple Models**: Flash (fast ~500ms) and Pro (quality ~1-2s) options
- ✅ **Audio Formats**: WAV output with 24kHz, mono, 16-bit PCM
- ✅ **Type-Safe**: Strict mypy checking, comprehensive type hints
- ✅ **Rich Error Messages**: Agent-friendly validation with actionable examples

## Use Cases

### Content Production
- 📚 **Audiobook Generation** - Transform long-form written content into professionally narrated audiobooks with emotional delivery and natural pacing
- 🎙️ **Podcast Creation** - Generate multi-speaker podcast episodes with distinct voices and personalities for interviews, discussions, or narrative content
- 📰 **News & Media** - Create professional news broadcasts with appropriate tone and delivery style

### AI & Automation Workflows
- 🤖 **AI Agent Outputs** - Convert AI-generated text into audio files automatically - perfect for agents that need to produce spoken content
- 🔄 **Text-to-Audio Pipelines** - Integrate into automation workflows where text content needs audio representation
- 📊 **Report Narration** - Automatically generate spoken summaries of data reports, analytics, or system notifications

### Accessibility & Communication
- 🔊 **Content Accessibility** - Make written content accessible to visually impaired users with natural-sounding speech
- 💻 **Voice Interfaces** - Build speaking applications, voice assistants, and conversational AI systems
- 📱 **Interactive Applications** - Add voice capabilities to apps, dashboards, or customer-facing systems

### Customer Support & Training
- 🎯 **IVR & Support Systems** - Generate dynamic voice responses for customer support automation
- 📖 **E-Learning Content** - Create engaging educational audio with controlled pacing and emotional delivery
- 🎓 **Training Materials** - Produce consistent, professional narration for training videos and tutorials

### Creative & Marketing
- 🎬 **Video Narration** - Generate voiceovers for marketing videos, explainer content, or product demos
- 📣 **Advertisement Production** - Create dynamic ad copy with specific emotional tones and delivery styles
- 🎮 **Game Audio** - Generate character dialogue and narration for interactive experiences

## Installation

### Prerequisites

- Python 3.14 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Install Globally

```bash
# Install with uv (recommended)
uv tool install gemini-tts-tool

# Verify installation
gemini-tts-tool --version
```

### Install from Source

```bash
# Clone repository
git clone https://github.com/dnvriend/gemini-tts-tool.git
cd gemini-tts-tool

# Install globally
uv tool install .
```

## Configuration

### Gemini Developer API (Recommended)

Set `GEMINI_API_KEY` or `GOOGLE_API_KEY`. The client automatically picks up these variables. If both are set, `GOOGLE_API_KEY` takes precedence.

```bash
export GEMINI_API_KEY='your-api-key'
```

**Get your API key:**
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create or select a project
3. Generate an API key
4. Set the environment variable

### Gemini API on Vertex AI

For Vertex AI, set the following environment variables:

```bash
export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT='your-project-id'
export GOOGLE_CLOUD_LOCATION='us-central1'
```

**Prerequisites:**
- Google Cloud project with Vertex AI API enabled
- Proper IAM permissions for Vertex AI
- Authenticated with `gcloud auth application-default login`

## Usage

### Quick Start

```bash
# Basic text-to-speech
gemini-tts-tool synthesize "Hello world" -o greeting.wav

# With custom voice
gemini-tts-tool synthesize "Welcome!" -o welcome.wav --voice Zephyr

# With style control
gemini-tts-tool synthesize "Breaking news!" -o news.wav \
    --style "Speak in a professional news anchor tone"

# Multi-speaker dialogue
gemini-tts-tool multi-voice --input-file dialogue.txt -o podcast.wav
```

### Podcast Creation Workflow

Creating a professional podcast is straightforward with Gemini TTS. Here's a complete workflow:

**1. Create Your Dialogue File**

Create a text file (e.g., `podcast-script.txt`) with speaker labels:

```
Host: Welcome to today's podcast! We're exploring the exciting world of AI-powered text-to-speech technology.
Guest: Thanks for having me! I'm thrilled to discuss how Gemini TTS is revolutionizing voice synthesis.
Host: Let's dive right in. What makes Gemini TTS different from traditional text-to-speech systems?
Guest: Great question! The key differentiator is natural language control. You can guide the style, emotion, and delivery using simple text instructions.
Host: That's fascinating! Can you give us an example?
Guest: Absolutely! Instead of adjusting sliders and parameters, you simply say "speak cheerfully and energetically" and the AI adapts its delivery accordingly.
```

**2. Generate Your Podcast**

```bash
# Fast generation with flash model (recommended for most podcasts)
gemini-tts-tool multi-voice --input-file podcast-script.txt -o my-podcast.wav

# High-quality generation with pro model
gemini-tts-tool multi-voice --input-file podcast-script.txt -o my-podcast-hq.wav --model pro

# With emotional style control
gemini-tts-tool multi-voice --input-file podcast-script.txt -o my-podcast-styled.wav \
    --model pro \
    --style "Make Host sound professional and authoritative, Guest sound friendly and enthusiastic"

# Custom voices for distinct personalities
gemini-tts-tool multi-voice --input-file podcast-script.txt -o my-podcast-custom.wav \
    --speaker1-voice Kore \
    --speaker2-voice Zephyr \
    --model pro
```

**3. Model Comparison**

- **Flash Model** (~500ms generation): Fast, great for drafts and quick iterations
- **Pro Model** (~1-2s generation): Higher quality, more natural intonation, recommended for final production

**Podcast Tips:**
- Use descriptive speaker labels (Host, Guest, Interviewer, Expert) for clarity
- Keep each dialogue segment concise for natural pacing
- Use style instructions to differentiate speaker personalities
- The pro model delivers more expressive and nuanced performances
- Test with flash first for speed, then generate final version with pro

### Synthesize Command

Convert text to speech with customizable voice and style.

```bash
gemini-tts-tool synthesize [TEXT] --output FILE [OPTIONS]
```

**Options:**
- `TEXT` - Text to synthesize (positional argument)
- `--input/-i` - Alternative way to provide text
- `--stdin/-s` - Read text from stdin
- `--output/-o` - Output audio file path (required, must end with .wav)
- `--voice` - Voice name (default: Puck)
- `--model` - TTS model: flash (default) or pro
- `--style` - Style instructions (e.g., "Speak cheerfully")
- `--verbose/-V` - Show verbose output

**Note:** Output file must have `.wav` extension. Other formats are not supported.

**Examples:**

```bash
# From positional argument
gemini-tts-tool synthesize "Hello world" -o output.wav

# From file via stdin
cat article.txt | gemini-tts-tool synthesize --stdin -o article.wav

# With pro model for higher quality
gemini-tts-tool synthesize "Premium content" -o pro.wav --model pro

# Different voice with style
gemini-tts-tool synthesize "Exciting news!" -o excited.wav \
    --voice Fenrir --style "Sound very enthusiastic and energetic"
```

### Multi-Voice Command

Create dialogue with multiple speakers (up to 2).

```bash
gemini-tts-tool multi-voice --input-file FILE --output FILE [OPTIONS]
```

**Options:**
- `--input-file` - Dialogue file with speaker labels (required)
- `--output/-o` - Output audio file path (required, must end with .wav)
- `--speaker1-voice` - Voice for first speaker (default: Kore)
- `--speaker2-voice` - Voice for second speaker (default: Puck)
- `--model` - TTS model (default: flash)
- `--style` - Style instructions for both speakers (e.g., "Make Speaker1 sound tired, Speaker2 excited")
- `--verbose/-V` - Show verbose output

**Note:** Output file must have `.wav` extension. Style instructions are embedded in the dialogue prompt for multi-voice synthesis.

**Dialogue File Format:**

```
Host: Welcome to today's show! We have an amazing guest with us.
Guest: Thank you for having me. I'm excited to be here.
Host: Let's dive right into our topic.
Guest: Absolutely! Let me start by explaining...
```

**Examples:**

```bash
# Basic multi-voice
gemini-tts-tool multi-voice --input-file dialogue.txt -o podcast.wav

# Custom voices for each speaker
gemini-tts-tool multi-voice --input-file interview.txt -o interview.wav \
    --speaker1-voice Zephyr --speaker2-voice Aoede

# With style instructions (emotional control)
gemini-tts-tool multi-voice --input-file debate.txt -o debate.wav \
    --style "Make Host sound authoritative, Guest sound thoughtful"

# Emotional delivery example
gemini-tts-tool multi-voice --input-file dialogue.txt -o emotional.wav \
    --style "Make Speaker1 sound tired and bored, Speaker2 sound excited and happy"
```

### List Commands

```bash
# View all available voices
gemini-tts-tool list-voices

# View all available models
gemini-tts-tool list-models
```

## Library Usage

Use `gemini-tts-tool` as a Python library in your applications:

```python
from gemini_tts_tool import create_client, synthesize_speech, VOICES

# Create client
client = create_client()  # Reads from environment variables

# Synthesize speech
audio_data = synthesize_speech(
    client=client,
    text="Hello from Python!",
    voice="Kore",
    model="flash",
    system_instruction="Speak professionally"
)

# Save audio (PCM data)
with open("output.wav", "wb") as f:
    f.write(audio_data)

# Multi-voice synthesis
from gemini_tts_tool import synthesize_multi_voice

dialogue = """
Host: Welcome to the show!
Guest: Thanks for having me!
"""

audio_data = synthesize_multi_voice(
    client=client,
    dialogue=dialogue,
    speaker1_voice="Zephyr",
    speaker2_voice="Puck",
    model="flash",
    system_instruction="Make Host sound professional, Guest sound friendly"
)

# Save as WAV (required format)
from gemini_tts_tool.utils import save_audio_wav
save_audio_wav(audio_data, "podcast.wav")
```

## Available Voices

30 Gemini TTS voices with distinct characteristics:

| Voice | Characteristics | Voice | Characteristics |
|-------|----------------|-------|----------------|
| Zephyr | Bright | Puck | Upbeat |
| Charon | Informative | Kore | Firm |
| Fenrir | Excitable | Leda | Youthful |
| Orus | Firm | Aoede | Breezy |
| Callirrhoe | Easy-going | Autonoe | Bright |
| Enceladus | Breathy | Iapetus | Clear |
| Umbriel | Easy-going | Algieba | Smooth |
| Despina | Smooth | Erinome | Clear |
| Algenib | Gravelly | Rasalgethi | Informative |
| Laomedeia | Upbeat | Achernar | Soft |
| Alnilam | Firm | Schedar | Even |
| Gacrux | Mature | Pulcherrima | Forward |
| Achird | Friendly | Zubenelgenubi | Casual |
| Vindemiatrix | Gentle | Sadachbia | Lively |
| Sadaltager | Knowledgeable | Sulafat | Warm |

## Advanced Documentation

Comprehensive guides are available in the [`./references`](./references) directory for in-depth usage:

### Quick Reference
- **[API Setup & Pricing](./references/api-setup-pricing.md)** - Complete guide to obtaining API keys, secure storage (macOS Keychain, environment variables), pricing information for Gemini TTS models, cost calculations, and billing monitoring

- **[Model Features](./references/model-features.md)** - Detailed overview of Gemini TTS capabilities including 24 language support, 30+ voice options, multi-speaker dialogues, style customization, audio formats, and technical specifications

### Guides & Best Practices
- **[Prompting Guide](./references/prompting-guide.md)** - Comprehensive prompt engineering for TTS including core principles, natural language style control, voice selection strategies, language-specific considerations, and advanced techniques with examples

- **[Voice & Style Guide](./references/voice-and-style-guide.md)** - In-depth voice selection and style prompt engineering with extensive coverage of all 30 voices (Puck, Kore, Zephyr, Charon, Aoede, Fenrir, etc.), systemInstruction usage, emotional control, speaking styles, and practical examples across content types

- **[Advanced Multi-Voice Guide](./references/advanced-multi-voice-guide.md)** - Comprehensive guide for multi-speaker audio including speaker differentiation techniques, dialogue formatting best practices, emotional arcs in conversations, complex scene construction with 3+ speakers (workarounds), and complete examples

### Technical References
- **[Quick Reference Templates](./references/quick-reference-templates.md)** - Fast-access templates for common use cases including content type templates (blog posts, news, tutorials, marketing), emotional tone templates, multi-voice patterns, pacing templates, and ready-to-use CLI examples

- **[Token & Text Limits](./references/token-and-text-limits.md)** - Technical documentation on token limits (8,192 input, 16,384 output), character/word conversion estimates (~32,000 characters, ~5,000-6,500 words), audio duration estimates (~8-9 minutes max), rate limits, and strategies for handling long content

- **[Google Cloud TTS API Overview](./references/google-cloud-tts-api-overview.md)** - Comprehensive API reference with curl/bash integration examples, authentication methods, voice catalog, Gemini TTS models (Flash and Pro), API endpoints, request/response structures, audio configuration, and error handling

## Resources

- **Official Documentation**: [Gemini TTS API](https://ai.google.dev/gemini-api/docs/speech-generation) | [Google Cloud TTS](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)
- **Python SDK**: [google-genai](https://github.com/googleapis/python-genai)
- **API Key**: [Get API Key](https://aistudio.google.com/app/apikey)
- **GitHub Repository**: [gemini-tts-tool](https://github.com/dnvriend/gemini-tts-tool)

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/dnvriend/gemini-tts-tool.git
cd gemini-tts-tool

# Install dependencies
make install

# Show available commands
make help
```

### Available Make Commands

```bash
make install          # Install dependencies
make format           # Format code with ruff
make lint             # Run linting with ruff
make typecheck        # Run type checking with mypy
make test             # Run tests with pytest (54 tests)
make check            # Run all checks (lint, typecheck, test)
make pipeline         # Run full pipeline (format, check, build, install-global)
make build            # Build package
make install-global   # Install globally (with --reinstall for fresh install)
make clean            # Remove build artifacts
```

### Project Structure

```
gemini-tts-tool/
├── gemini_tts_tool/         # Main package
│   ├── __init__.py          # Public API exports
│   ├── cli.py               # CLI entry point (Click group)
│   ├── core/                # Core library (importable)
│   │   ├── client.py        # Gemini client management
│   │   ├── synthesizer.py  # TTS synthesis logic
│   │   └── voices.py        # Voice catalog
│   ├── commands/            # CLI command implementations
│   │   ├── synthesize_command.py
│   │   ├── multi_voice_command.py
│   │   └── list_commands.py
│   └── utils.py             # Shared utilities
├── tests/                   # Test suite
├── pyproject.toml           # Project configuration
├── Makefile                 # Development commands
├── README.md                # This file
└── CLAUDE.md                # Development documentation
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the full pipeline (`make pipeline`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all functions
- Write docstrings for public functions
- Format code with `ruff`
- Pass all linting and type checks

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Dennis Vriend**

- GitHub: [@dnvriend](https://github.com/dnvriend)

## Acknowledgments

- Built with [Click](https://click.palletsprojects.com/) for CLI framework
- Powered by [Google Gemini TTS API](https://ai.google.dev/gemini-api)
- Developed with [uv](https://github.com/astral-sh/uv) for fast Python tooling

---

**Note**: This project was developed with assistance from [Claude Code](https://www.anthropic.com/claude/code), an AI-powered development tool by [Anthropic](https://www.anthropic.com/).

Made with ❤️ using Python 3.14
