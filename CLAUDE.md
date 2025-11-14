# gemini-tts-tool - Developer Guide

## Overview

A CLI and Python library for Google Gemini Text-to-Speech. Built with modern Python tooling (uv, mise, click, Python 3.14+) and designed for AI agents, automation, and human developers.

**Tech Stack:**
- Python 3.14+
- Click (CLI framework)
- google-genai (Gemini SDK)
- uv (package management)
- ruff (linting/formatting)
- mypy (type checking)
- pytest (testing)

## Architecture

```
gemini-tts-tool/
├── gemini_tts_tool/
│   ├── __init__.py          # Public API exports for library usage
│   ├── cli.py               # CLI entry point (Click group)
│   ├── core/                # Core library (importable, CLI-independent)
│   │   ├── __init__.py
│   │   ├── client.py        # Gemini client management
│   │   ├── synthesizer.py  # TTS synthesis logic
│   │   └── voices.py        # Voice & model catalog
│   ├── commands/            # CLI command implementations
│   │   ├── __init__.py
│   │   ├── synthesize_command.py
│   │   ├── multi_voice_command.py
│   │   └── list_commands.py
│   └── utils.py             # Shared utilities (audio, validation)
├── tests/                   # Test suite (46 tests)
│   ├── __init__.py
│   ├── test_utils.py        # Utility function tests (8 tests)
│   ├── test_voices.py       # Voice & model validation tests (11 tests)
│   ├── test_client.py       # Client authentication tests (10 tests)
│   └── test_synthesizer.py  # TTS synthesis tests (17 tests)
├── pyproject.toml           # Project configuration
├── Makefile                 # Development commands
├── README.md                # User documentation
├── CLAUDE.md                # This file
├── LICENSE                  # MIT License
├── .mise.toml               # mise configuration
└── .gitignore
```

## Key Design Principles

### 1. Separation of Concerns
- **core/**: Pure library functions, no CLI dependencies, importable
- **commands/**: CLI wrappers with Click decorators
- **utils.py**: Shared utilities across core and commands

### 2. Exception-Based Errors
- Core functions raise custom exceptions (e.g., `SynthesisError`, `AuthenticationError`)
- CLI catches exceptions at command boundary and formats for user
- Never use `sys.exit()` in core modules

### 3. Composability
- Audio processing functions are standalone and composable
- Client creation separate from synthesis operations
- Each function does one thing well

### 4. Agent-Friendly Design
- Rich error messages with "What to do" sections
- Examples in error output for quick recovery
- Structured command output (success to stderr, data to stdout)
- Type-safe with comprehensive hints

## Development Commands

### Quick Start
```bash
# Install dependencies
make install

# Run full quality pipeline
make pipeline    # format → lint → typecheck → test → build → install-global
```

### Quality Checks
```bash
make format      # Auto-format with ruff
make lint        # Lint with ruff
make typecheck   # Type check with mypy (strict mode)
make test        # Run pytest suite
make check       # Run all checks (lint + typecheck + test)
```

### Build & Install
```bash
make clean       # Remove build artifacts
make build       # Build wheel
make install-global  # Install globally with uv tool
```

### Run Locally
```bash
# Without installation
uv run gemini-tts-tool [args]

# Or via Makefile
make run ARGS="synthesize 'Hello' -o test.wav"
```

## Code Standards

### Type Safety
- Use Python 3.14+ syntax (`dict/list` not `Dict/List`)
- Type hints required for all functions
- Strict mypy checking (no `Any` unless necessary)
- Use `type: ignore[...]` with comment for unavoidable SDK issues

### Formatting
- Line length: 100 characters
- Follow PEP 8 via ruff
- Imports sorted alphabetically

### Docstrings
- Module-level docstring acknowledging AI generation:
  ```python
  """
  [Module description].

  Note: This code was generated with assistance from AI coding tools
  and has been reviewed and tested by a human.
  """
  ```
- Function docstrings with Args, Returns, Raises sections
- Clear, concise descriptions

### Error Handling
- Custom exceptions for different error types
- Rich error messages with actionable examples
- Agent-friendly validation feedback

## CLI Commands Reference

### synthesize
```bash
gemini-tts-tool synthesize [TEXT] --output FILE [OPTIONS]
```
Convert text to speech with customizable voice and style.

**Options:**
- `TEXT` - Text to synthesize (positional, optional if using --input or --stdin)
- `--input/-i` - Text input (alternative to positional)
- `--stdin/-s` - Read from stdin
- `--output/-o` - Output file path (required)
- `--voice` - Voice name (default: Puck)
- `--model` - Model: flash/pro or full name (default: flash)
- `--style` - Style instructions
- `--verbose/-V` - Verbose output

### multi-voice
```bash
gemini-tts-tool multi-voice --input-file FILE --output FILE [OPTIONS]
```
Synthesize multi-speaker dialogue (up to 2 speakers).

**Options:**
- `--input-file` - Dialogue file with speaker labels (required)
- `--output/-o` - Output file path (required)
- `--speaker1-voice` - First speaker voice (default: Kore)
- `--speaker2-voice` - Second speaker voice (default: Puck)
- `--model` - Model (default: flash)
- `--style` - Style instructions
- `--verbose/-V` - Verbose output

### list-voices / list-models
```bash
gemini-tts-tool list-voices
gemini-tts-tool list-models
```
Display available voices and models.

## Library Usage

### Import and Use
```python
from gemini_tts_tool import (
    create_client,
    synthesize_speech,
    synthesize_multi_voice,
    VOICES,
    MODELS
)

# Create client (reads GEMINI_API_KEY or GOOGLE_API_KEY)
client = create_client()

# Synthesize speech
audio_data = synthesize_speech(
    client=client,
    text="Hello world",
    voice="Kore",
    model="flash",
    system_instruction="Speak professionally"
)

# Save audio
from gemini_tts_tool.utils import save_audio_wav
save_audio_wav(audio_data, "output.wav")

# Multi-voice
dialogue = "Host: Hello!\nGuest: Hi there!"
audio_data = synthesize_multi_voice(
    client=client,
    dialogue=dialogue,
    speaker1_voice="Zephyr",
    speaker2_voice="Puck"
)
```

### Authentication
```python
# Gemini Developer API
client = create_client()  # Uses GEMINI_API_KEY env var

# Explicit API key
client = create_client(api_key="your-key")

# Vertex AI
client = create_client(
    use_vertex=True,
    project="my-project",
    location="us-central1"
)
```

## Testing

### Test Suite (54 Tests)

**Test Coverage by Module:**

1. **test_utils.py** (8 tests)
   - Audio format validation (wav, mp3, ogg, m4a, flac)
   - WAV file creation with PCM headers (24kHz, mono, 16-bit)
   - Path expansion (home directory, environment variables)
   - File reading with error handling

2. **test_voices.py** (11 tests)
   - Voice catalog validation (all 30 voices)
   - Model validation (flash, pro aliases and full names)
   - Error message helpfulness and actionability

3. **test_client.py** (10 tests)
   - Gemini Developer API authentication
   - Vertex AI authentication with environment variables
   - API key precedence (GOOGLE_API_KEY > GEMINI_API_KEY)
   - Environment variable support for Vertex AI config
   - Error handling with helpful messages

4. **test_synthesizer.py** (17 tests)
   - Single-voice speech synthesis
   - Multi-voice dialogue synthesis (with SDK mocking)
   - Empty input validation
   - stdin reading functionality
   - API response parsing with type guards
   - Speaker detection and validation

5. **test_commands.py** (8 tests)
   - WAV output format validation (rejects .mp3, .txt, etc.)
   - Case-insensitive .wav extension checking
   - synthesize command validation
   - multi-voice command validation

### Running Tests

```bash
# Run all tests (46 tests, ~0.2s)
make test

# Run with verbose output
uv run pytest tests/ -v

# Run specific test file
uv run pytest tests/test_client.py

# Run specific test
uv run pytest tests/test_client.py::test_create_client_with_api_key

# Run with coverage
uv run pytest tests/ --cov=gemini_tts_tool

# Watch mode (re-run on changes)
uv run pytest tests/ -f
```

### Testing Strategy

**Unit Tests with Mocking**
- External dependencies (Gemini API) are mocked
- SDK type validation handled via comprehensive mocking
- Tests focus on logic, not API integration

**Type Safety**
- All tests use strict type hints
- pytest fixtures (tmp_path) for file operations
- Type guards for optional values

**Error Testing**
- Validate error messages contain helpful information
- Verify "What to do" sections in validation errors
- Test error recovery paths

### Writing New Tests

**Test Structure:**
```python
"""Tests for gemini_tts_tool.module_name.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import pytest
from unittest.mock import MagicMock, patch

from gemini_tts_tool.module import function_to_test


def test_function_basic_case() -> None:
    """Test basic functionality."""
    result = function_to_test("input")
    assert result == "expected"


def test_function_error_case() -> None:
    """Test error handling."""
    with pytest.raises(ValueError, match="error message pattern"):
        function_to_test("invalid")


def test_function_with_mock() -> None:
    """Test with mocked dependencies."""
    with patch("gemini_tts_tool.module.dependency") as mock_dep:
        mock_dep.return_value = "mocked"
        result = function_to_test()
        assert result == "expected"
        mock_dep.assert_called_once()
```

**Testing Guidelines:**
- One test function per behavior/scenario
- Descriptive test names: `test_<function>_<scenario>`
- Use pytest fixtures for setup (e.g., `tmp_path`)
- Mock external dependencies (API calls, file system when appropriate)
- Test both success and error paths
- Verify error messages contain helpful guidance
- Keep tests fast and independent

## Important Notes

### Dependencies
- **google-genai**: Python SDK for Gemini API ([GitHub](https://github.com/googleapis/python-genai))
- **Click**: CLI framework ([Docs](https://click.palletsprojects.com/))

### Authentication

**Gemini Developer API:**
- Environment variables: `GEMINI_API_KEY` or `GOOGLE_API_KEY`
- `GOOGLE_API_KEY` takes precedence if both are set
- Get API key: https://aistudio.google.com/app/apikey

**Vertex AI:**
- Environment variables:
  - `GOOGLE_GENAI_USE_VERTEXAI=true` (enables Vertex AI)
  - `GOOGLE_CLOUD_PROJECT=your-project-id` (required)
  - `GOOGLE_CLOUD_LOCATION=us-central1` (required)
- Requires: `gcloud auth application-default login`
- Can also pass project/location as parameters to `create_client()`

### Audio Format
- Gemini TTS returns raw PCM data (24kHz, mono, 16-bit)
- `save_audio_wav()` adds WAV header for playback compatibility
- Output format is always WAV (other formats require ffmpeg)

### Model Selection
- **flash**: `gemini-2.5-flash-preview-tts` - Fast synthesis (~500ms)
- **pro**: `gemini-2.5-pro-preview-tts` - High quality (~1-2s)
- Aliases automatically resolve to full model names

### Voice Catalog
- 30 available voices: Zephyr, Puck, Kore, Charon, etc.
- Use `list-voices` command or import `VOICES` constant
- Each voice has unique characteristics (see README.md)

### Version Sync
**CRITICAL**: Keep version consistent across:
- `pyproject.toml` → `[project]` → `version = "1.0.0"`
- `cli.py` → `@click.version_option(version="1.0.0")`
- `__init__.py` → `__version__ = "1.0.0"`

## Known Issues & Future Fixes

### SDK Type Annotations
**Issue**: Multi-speaker voice config has incomplete type annotations in google-genai SDK

**Current Workaround** (synthesizer.py:188-196):
```python
types.MultiSpeakerVoiceConfig(  # type: ignore[call-arg]
    speaker_voice_configs=[
        types.SpeakerVoiceConfig(  # type: ignore[call-arg]
            speaker_name=speaker1_name,
            prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=speaker1_voice)
        ),
        ...
    ]
)
```

**Future Fix**: When SDK types are updated, remove `# type: ignore` comments

## Development Workflow

1. **Feature Development**
   - Create feature branch
   - Implement in core/ (library functions)
   - Add CLI wrapper in commands/
   - Update __init__.py exports if needed
   - Write tests

2. **Quality Assurance**
   ```bash
   make format      # Auto-format
   make check       # All checks
   ```

3. **Build & Test**
   ```bash
   make pipeline    # Full pipeline
   gemini-tts-tool --help  # Test installation
   ```

4. **Commit & Push**
   - Use structured commit messages
   - Include Co-Authored-By: Claude
   - Push to feature branch
   - Create Pull Request

## Quality Metrics

**Current Status (v1.0.0):**
- ✅ 46 tests passing (100% pass rate)
- ✅ Test execution: ~0.2 seconds
- ✅ Ruff linting: All checks passed
- ✅ Mypy type checking: No issues found (strict mode)
- ✅ Code coverage: Core modules fully tested
- ✅ Documentation: Comprehensive README + CLAUDE.md
- ✅ CI/CD: Ready for GitHub Actions integration

**Module Breakdown:**
```
gemini_tts_tool/
├── core/          3 modules (client, synthesizer, voices)
├── commands/      3 commands (synthesize, multi-voice, list)
├── utils.py       4 utility functions
└── cli.py         Click group with 4 commands

tests/             46 tests across 4 modules
```

## Resources

- **Gemini TTS API**: https://ai.google.dev/gemini-api/docs/speech-generation
- **Python SDK**: https://github.com/googleapis/python-genai
- **Click Documentation**: https://click.palletsprojects.com/
- **API Key**: https://aistudio.google.com/app/apikey
- **Project Repository**: https://github.com/dnvriend/gemini-tts-tool

---

**Last Updated**: 2025-01-14 (v1.0.0 - Initial Release with comprehensive test suite)
