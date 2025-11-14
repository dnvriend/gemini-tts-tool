# Google Cloud Text-to-Speech API - Comprehensive Overview

**Research Date**: 2025-11-03
**Focus**: Bash/curl integration for CLI implementation
**Target**: Practical implementation guide for Google TTS including Gemini models

---

## Table of Contents

1. [Authentication & Setup](#authentication--setup)
2. [Voice Catalog](#voice-catalog)
3. [Gemini TTS Models](#gemini-tts-models)
4. [API Integration (curl/bash)](#api-integration-curlbash)
5. [Audio Configuration](#audio-configuration)
6. [Error Handling](#error-handling)
7. [Working Examples](#working-examples)

---

## Authentication & Setup

### 1. API Key Setup

#### Option A: API Key (Simplest for CLI tools)

```bash
# Set your API key as environment variable
export GOOGLE_API_KEY="your-api-key-here"

# Or use in requests directly
API_KEY="your-api-key-here"
```

**Getting an API Key:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create or select a project
3. Enable the "Cloud Text-to-Speech API"
4. Navigate to "APIs & Services" → "Credentials"
5. Click "Create Credentials" → "API Key"
6. Copy and secure your API key

#### Option B: Service Account (Production)

```bash
# Set service account credentials
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"

# Get access token
ACCESS_TOKEN=$(gcloud auth application-default print-access-token)
```

### 2. Enable Cloud Text-to-Speech API

```bash
# Using gcloud CLI
gcloud services enable texttospeech.googleapis.com --project=YOUR_PROJECT_ID

# Verify API is enabled
gcloud services list --enabled --project=YOUR_PROJECT_ID | grep texttospeech
```

### 3. Security Best Practices

- **Never commit API keys** to version control
- **Use environment variables** for API keys
- **Restrict API key usage** to specific APIs and IP addresses (in Google Cloud Console)
- **Rotate keys regularly**
- **Use service accounts** for production deployments
- **Store keys securely** (e.g., macOS Keychain, HashiCorp Vault)

```bash
# Store in macOS Keychain
security add-generic-password -a "$USER" -s "google-tts-api-key" -w "your-api-key"

# Retrieve from macOS Keychain
GOOGLE_API_KEY=$(security find-generic-password -a "$USER" -s "google-tts-api-key" -w)
```

---

## Voice Catalog

### Voice Categories

Google Cloud TTS offers four main voice categories:

1. **Standard** - Basic quality, lowest cost
2. **WaveNet** - High quality, DeepMind technology
3. **Neural2** - Latest generation, most natural
4. **Studio** - Professional voice acting quality
5. **Gemini TTS** - AI-powered, expressive synthesis (Preview)

### Available Voices by Type

#### Neural2 Voices (Recommended for Most Use Cases)

**English (US)**
- `en-US-Neural2-A` - Male
- `en-US-Neural2-C` - Female
- `en-US-Neural2-D` - Male
- `en-US-Neural2-E` - Female
- `en-US-Neural2-F` - Female
- `en-US-Neural2-G` - Female
- `en-US-Neural2-H` - Female
- `en-US-Neural2-I` - Male
- `en-US-Neural2-J` - Male

**English (UK)**
- `en-GB-Neural2-A` - Female
- `en-GB-Neural2-B` - Male
- `en-GB-Neural2-C` - Female
- `en-GB-Neural2-D` - Male
- `en-GB-Neural2-F` - Female

**Other Major Languages**
- Dutch: `nl-NL-Neural2-A` (Female), `nl-NL-Neural2-B` (Male), `nl-NL-Neural2-C` (Male), `nl-NL-Neural2-D` (Female), `nl-NL-Neural2-E` (Female)
- German: `de-DE-Neural2-A` (Female), `de-DE-Neural2-B` (Male), `de-DE-Neural2-C` (Female), `de-DE-Neural2-D` (Male), `de-DE-Neural2-F` (Female)
- French: `fr-FR-Neural2-A` (Female), `fr-FR-Neural2-B` (Male), `fr-FR-Neural2-C` (Female), `fr-FR-Neural2-D` (Male), `fr-FR-Neural2-E` (Female)
- Spanish: `es-ES-Neural2-A` (Female), `es-ES-Neural2-B` (Male), `es-ES-Neural2-C` (Female), `es-ES-Neural2-D` (Female), `es-ES-Neural2-E` (Female), `es-ES-Neural2-F` (Male)
- Italian: `it-IT-Neural2-A` (Female), `it-IT-Neural2-C` (Male)
- Japanese: `ja-JP-Neural2-B` (Female), `ja-JP-Neural2-C` (Male), `ja-JP-Neural2-D` (Male)

#### Studio Voices (Premium Quality)

**English (US)**
- `en-US-Studio-M` - Male
- `en-US-Studio-O` - Female
- `en-US-Studio-Q` - Male

#### WaveNet Voices (High Quality)

Available for 30+ languages with naming pattern: `{language-code}-Wavenet-{A-F}`

Example:
- `en-US-Wavenet-A` through `en-US-Wavenet-J`
- `nl-NL-Wavenet-A` through `nl-NL-Wavenet-E`

#### Standard Voices (Basic Quality)

Available for 40+ languages with naming pattern: `{language-code}-Standard-{A-D}`

### Voice Characteristics and Use Cases

| Voice Type | Quality | Naturalness | Cost | Best For |
|------------|---------|-------------|------|----------|
| Standard | Basic | Low | $ | Testing, high-volume |
| WaveNet | High | Medium-High | $$ | General purpose |
| Neural2 | Very High | Very High | $$$ | Professional content |
| Studio | Premium | Highest | $$$$ | Marketing, audiobooks |
| Gemini TTS | AI-Powered | Variable | Preview | Experimental, expressive |

### Getting Voice List via API

```bash
# List all available voices
curl -X GET \
  "https://texttospeech.googleapis.com/v1/voices?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" | jq '.'

# Filter for Neural2 voices
curl -X GET \
  "https://texttospeech.googleapis.com/v1/voices?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" | \
  jq '.voices[] | select(.name | contains("Neural2"))'

# Filter by language
curl -X GET \
  "https://texttospeech.googleapis.com/v1/voices?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" | \
  jq '.voices[] | select(.languageCodes[] | contains("en-US"))'
```

---

## Gemini TTS Models

### Overview

Gemini TTS models use generative AI to produce highly expressive and natural-sounding speech. These models are currently in **Preview** and accessed through the Generative Language API (not Cloud TTS API).

### Available Models

#### 1. gemini-2.5-flash-preview-tts

**Characteristics:**
- **Speed**: Fastest synthesis
- **Quality**: Good quality, natural intonation
- **Use Case**: Interactive applications, real-time synthesis
- **Latency**: Low latency (~500ms)
- **Cost**: Lower cost tier

**Best For:**
- Chatbots and virtual assistants
- Real-time voice responses
- High-volume synthesis needs
- Development and testing

#### 2. gemini-2.5-pro-preview-tts

**Characteristics:**
- **Speed**: Moderate synthesis speed
- **Quality**: Highest quality, most expressive
- **Use Case**: Premium content, professional applications
- **Latency**: Higher latency (~1-2s)
- **Cost**: Higher cost tier

**Best For:**
- Audiobook narration
- Professional video voiceovers
- Marketing content
- High-quality content creation

### Model Comparison

| Feature | Flash | Pro |
|---------|-------|-----|
| Speed | Fast (500ms) | Moderate (1-2s) |
| Quality | Good | Excellent |
| Expressiveness | Natural | Highly expressive |
| Cost | Lower | Higher |
| Best Use | Interactive | Premium content |
| Voice Control | Basic | Advanced |
| Style Prompts | Supported | Enhanced support |

### Gemini TTS API Endpoint

```
POST https://generativelanguage.googleapis.com/v1beta/{model}:generateContent?key=API_KEY
```

**Key Differences from Cloud TTS:**
- Uses Generative Language API (not Cloud TTS API)
- Different endpoint structure
- Unified API for text and speech generation
- Style prompts for emotional control
- Context-aware synthesis

### Model Availability

- **Status**: Preview/Beta
- **Access**: Requires API key with Generative Language API enabled
- **Regions**: Global availability
- **Pricing**: Preview pricing, subject to change

---

## API Integration (curl/bash)

### Endpoint URLs

#### Cloud Text-to-Speech API (Standard/WaveNet/Neural2/Studio)

```bash
# Base URL
BASE_URL="https://texttospeech.googleapis.com/v1"

# Text synthesis endpoint
SYNTHESIZE_URL="${BASE_URL}/text:synthesize"

# Voice list endpoint
VOICES_URL="${BASE_URL}/voices"
```

#### Generative Language API (Gemini TTS)

```bash
# Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Gemini Flash TTS
FLASH_URL="${BASE_URL}/models/gemini-2.5-flash-preview-tts:generateContent"

# Gemini Pro TTS
PRO_URL="${BASE_URL}/models/gemini-2.5-pro-preview-tts:generateContent"
```

### Request Structure (Cloud TTS)

#### Basic Request Body

```json
{
  "input": {
    "text": "Hello, world! This is Google Cloud Text-to-Speech."
  },
  "voice": {
    "languageCode": "en-US",
    "name": "en-US-Neural2-C",
    "ssmlGender": "FEMALE"
  },
  "audioConfig": {
    "audioEncoding": "MP3",
    "speakingRate": 1.0,
    "pitch": 0.0,
    "volumeGainDb": 0.0
  }
}
```

#### Request with SSML Input

```json
{
  "input": {
    "ssml": "<speak>Hello <break time=\"500ms\"/> world!</speak>"
  },
  "voice": {
    "languageCode": "en-US",
    "name": "en-US-Neural2-C"
  },
  "audioConfig": {
    "audioEncoding": "MP3"
  }
}
```

### Request Structure (Gemini TTS)

```json
{
  "contents": [
    {
      "parts": [
        {
          "text": "Hello! This is Gemini TTS speaking with natural expression."
        }
      ]
    }
  ],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "voiceConfig": {
        "prebuiltVoiceConfig": {
          "voiceName": "Puck"
        }
      }
    }
  }
}
```

### Response Format

#### Cloud TTS Response

```json
{
  "audioContent": "base64-encoded-audio-data-here..."
}
```

#### Gemini TTS Response

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "inlineData": {
              "mimeType": "audio/wav",
              "data": "base64-encoded-audio-data-here..."
            }
          }
        ]
      }
    }
  ]
}
```

### Extracting Audio Content

```bash
# Cloud TTS - Extract and decode
curl -X POST "${SYNTHESIZE_URL}?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @request.json | \
  jq -r '.audioContent' | \
  base64 --decode > output.mp3

# Gemini TTS - Extract and decode
curl -X POST "${FLASH_URL}?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @request.json | \
  jq -r '.candidates[0].content.parts[0].inlineData.data' | \
  base64 --decode > output.wav
```

### Common HTTP Status Codes

| Code | Meaning | Common Causes |
|------|---------|---------------|
| 200 | Success | Request completed successfully |
| 400 | Bad Request | Invalid JSON, missing required fields |
| 401 | Unauthorized | Invalid or missing API key |
| 403 | Forbidden | API not enabled, quota exceeded |
| 404 | Not Found | Invalid endpoint or voice name |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Error | Google server error |
| 503 | Unavailable | Service temporarily unavailable |

---

## Audio Configuration

### Audio Encodings

#### Available Formats

| Encoding | Extension | Quality | Size | Use Case |
|----------|-----------|---------|------|----------|
| MP3 | .mp3 | Good | Small | Web, mobile, general |
| LINEAR16 | .wav | Excellent | Large | Professional, editing |
| OGG_OPUS | .ogg | Good | Small | Web, streaming |
| MULAW | .wav | Basic | Small | Telephony |
| ALAW | .wav | Basic | Small | Telephony |

#### Format Details

**MP3** (Recommended for CLI tools)
```json
{
  "audioEncoding": "MP3",
  "sampleRateHertz": 24000  // Optional: 8000-48000
}
```

**LINEAR16** (Uncompressed WAV)
```json
{
  "audioEncoding": "LINEAR16",
  "sampleRateHertz": 24000  // Required for LINEAR16
}
```

**OGG_OPUS** (Web streaming)
```json
{
  "audioEncoding": "OGG_OPUS",
  "sampleRateHertz": 24000  // Optional
}
```

### Voice Parameters

#### Speaking Rate

Controls speech speed (0.25 to 4.0, default: 1.0)

```json
{
  "audioConfig": {
    "speakingRate": 1.25  // 25% faster
  }
}
```

**Recommendations:**
- `0.75` - Slow, clear (educational content)
- `1.0` - Normal (default)
- `1.25` - Slightly faster (efficient)
- `1.5` - Fast (time-sensitive)

#### Pitch

Adjusts voice pitch (-20.0 to 20.0 semitones, default: 0.0)

```json
{
  "audioConfig": {
    "pitch": -5.0  // Lower pitch
  }
}
```

**Recommendations:**
- `-5.0` - Lower, more authoritative
- `0.0` - Natural (default)
- `5.0` - Higher, more energetic

#### Volume Gain

Adjusts audio volume (-96.0 to 16.0 dB, default: 0.0)

```json
{
  "audioConfig": {
    "volumeGainDb": 3.0  // Increase volume by 3dB
  }
}
```

**Recommendations:**
- `-6.0` - Quieter background audio
- `0.0` - Normal (default)
- `3.0` - Louder, clear foreground

### Style Prompts (Gemini TTS)

Gemini TTS supports style prompts for emotional and contextual control:

```json
{
  "contents": [
    {
      "parts": [
        {
          "text": "I'm so excited to tell you about this!"
        }
      ]
    }
  ],
  "generationConfig": {
    "speechConfig": {
      "voiceConfig": {
        "prebuiltVoiceConfig": {
          "voiceName": "Puck"
        }
      }
    }
  },
  "systemInstruction": {
    "parts": [
      {
        "text": "Speak with enthusiasm and excitement, as if sharing great news with a friend."
      }
    ]
  }
}
```

**Style Examples:**
- "Speak professionally and clearly, like a news anchor"
- "Use a warm, friendly tone, like talking to a close friend"
- "Sound authoritative and confident, like an expert"
- "Express sadness and empathy"
- "Sound excited and energetic"

### Output Format Considerations

**For CLI Tools:**
- Use **MP3** for best size/quality balance
- Use **LINEAR16** if further audio processing needed
- Sample rate: 24000 Hz (good balance)

**For Web Applications:**
- Use **OGG_OPUS** for streaming
- Use **MP3** for broader compatibility

**For Telephony:**
- Use **MULAW** or **ALAW**
- Sample rate: 8000 Hz

---

## Error Handling

### Common Error Responses

#### Invalid API Key

```json
{
  "error": {
    "code": 401,
    "message": "Request had invalid authentication credentials.",
    "status": "UNAUTHENTICATED"
  }
}
```

**Fix:** Check API key, ensure no extra spaces

#### API Not Enabled

```json
{
  "error": {
    "code": 403,
    "message": "Cloud Text-to-Speech API has not been used in project...",
    "status": "PERMISSION_DENIED"
  }
}
```

**Fix:** Enable API in Google Cloud Console

#### Invalid Voice Name

```json
{
  "error": {
    "code": 400,
    "message": "Invalid voice name",
    "status": "INVALID_ARGUMENT"
  }
}
```

**Fix:** Check voice name spelling, verify voice exists

#### Rate Limit Exceeded

```json
{
  "error": {
    "code": 429,
    "message": "Quota exceeded",
    "status": "RESOURCE_EXHAUSTED"
  }
}
```

**Fix:** Implement exponential backoff, request quota increase

### Error Handling Pattern (Bash)

```bash
#!/bin/bash

synthesize_speech() {
    local text="$1"
    local output_file="$2"

    # Create request
    local request=$(cat <<EOF
{
  "input": {"text": "${text}"},
  "voice": {"languageCode": "en-US", "name": "en-US-Neural2-C"},
  "audioConfig": {"audioEncoding": "MP3"}
}
EOF
)

    # Make request
    local response=$(curl -s -w "\n%{http_code}" -X POST \
        "https://texttospeech.googleapis.com/v1/text:synthesize?key=${GOOGLE_API_KEY}" \
        -H "Content-Type: application/json" \
        -d "${request}")

    # Split response and status code
    local body=$(echo "$response" | head -n -1)
    local status=$(echo "$response" | tail -n 1)

    # Handle errors
    if [ "$status" -ne 200 ]; then
        local error_msg=$(echo "$body" | jq -r '.error.message // "Unknown error"')
        echo "ERROR (HTTP $status): $error_msg" >&2
        return 1
    fi

    # Extract audio
    echo "$body" | jq -r '.audioContent' | base64 --decode > "$output_file"

    if [ $? -eq 0 ]; then
        echo "Audio saved to: $output_file"
        return 0
    else
        echo "ERROR: Failed to decode audio content" >&2
        return 1
    fi
}

# Usage
synthesize_speech "Hello, world!" "output.mp3"
```

### Retry Logic with Exponential Backoff

```bash
#!/bin/bash

retry_with_backoff() {
    local max_attempts=5
    local attempt=1
    local delay=1

    while [ $attempt -le $max_attempts ]; do
        echo "Attempt $attempt of $max_attempts..." >&2

        if synthesize_speech "$1" "$2"; then
            return 0
        fi

        if [ $attempt -lt $max_attempts ]; then
            echo "Retrying in ${delay}s..." >&2
            sleep $delay
            delay=$((delay * 2))
        fi

        attempt=$((attempt + 1))
    done

    echo "ERROR: All retry attempts failed" >&2
    return 1
}

# Usage
retry_with_backoff "Hello, world!" "output.mp3"
```

---

## Working Examples

### Example 1: Basic Synthesis (Cloud TTS)

```bash
#!/bin/bash

GOOGLE_API_KEY="your-api-key-here"
API_URL="https://texttospeech.googleapis.com/v1/text:synthesize"

# Create request JSON
REQUEST_JSON=$(cat <<'EOF'
{
  "input": {
    "text": "Hello! This is a test of Google Cloud Text-to-Speech."
  },
  "voice": {
    "languageCode": "en-US",
    "name": "en-US-Neural2-C",
    "ssmlGender": "FEMALE"
  },
  "audioConfig": {
    "audioEncoding": "MP3"
  }
}
EOF
)

# Make request and save audio
curl -X POST "${API_URL}?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "${REQUEST_JSON}" | \
  jq -r '.audioContent' | \
  base64 --decode > output.mp3

echo "Audio saved to output.mp3"
```

### Example 2: Dutch Voice with Custom Parameters

```bash
#!/bin/bash

GOOGLE_API_KEY="your-api-key-here"
API_URL="https://texttospeech.googleapis.com/v1/text:synthesize"

REQUEST_JSON=$(cat <<'EOF'
{
  "input": {
    "text": "Hallo! Dit is een test van Google Cloud Text-to-Speech in het Nederlands."
  },
  "voice": {
    "languageCode": "nl-NL",
    "name": "nl-NL-Neural2-A",
    "ssmlGender": "FEMALE"
  },
  "audioConfig": {
    "audioEncoding": "MP3",
    "speakingRate": 0.9,
    "pitch": 0.0,
    "volumeGainDb": 0.0
  }
}
EOF
)

curl -X POST "${API_URL}?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "${REQUEST_JSON}" | \
  jq -r '.audioContent' | \
  base64 --decode > dutch_output.mp3

echo "Dutch audio saved to dutch_output.mp3"
```

### Example 3: SSML with Breaks and Emphasis

```bash
#!/bin/bash

GOOGLE_API_KEY="your-api-key-here"
API_URL="https://texttospeech.googleapis.com/v1/text:synthesize"

REQUEST_JSON=$(cat <<'EOF'
{
  "input": {
    "ssml": "<speak>Welcome to <emphasis level=\"strong\">Google Cloud</emphasis> Text-to-Speech. <break time=\"500ms\"/> This technology is <emphasis level=\"moderate\">amazing</emphasis>!</speak>"
  },
  "voice": {
    "languageCode": "en-US",
    "name": "en-US-Neural2-D"
  },
  "audioConfig": {
    "audioEncoding": "MP3"
  }
}
EOF
)

curl -X POST "${API_URL}?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "${REQUEST_JSON}" | \
  jq -r '.audioContent' | \
  base64 --decode > ssml_output.mp3

echo "SSML audio saved to ssml_output.mp3"
```

### Example 4: Gemini Flash TTS

```bash
#!/bin/bash

GOOGLE_API_KEY="your-api-key-here"
API_URL="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-tts:generateContent"

REQUEST_JSON=$(cat <<'EOF'
{
  "contents": [
    {
      "parts": [
        {
          "text": "Hello! I'm using Gemini Flash TTS for fast, natural-sounding speech synthesis."
        }
      ]
    }
  ],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "voiceConfig": {
        "prebuiltVoiceConfig": {
          "voiceName": "Puck"
        }
      }
    }
  }
}
EOF
)

curl -X POST "${API_URL}?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "${REQUEST_JSON}" | \
  jq -r '.candidates[0].content.parts[0].inlineData.data' | \
  base64 --decode > gemini_flash.wav

echo "Gemini Flash audio saved to gemini_flash.wav"
```

### Example 5: Gemini Pro TTS with Style Prompt

```bash
#!/bin/bash

GOOGLE_API_KEY="your-api-key-here"
API_URL="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro-preview-tts:generateContent"

REQUEST_JSON=$(cat <<'EOF'
{
  "contents": [
    {
      "parts": [
        {
          "text": "I'm absolutely thrilled to announce this groundbreaking development!"
        }
      ]
    }
  ],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "voiceConfig": {
        "prebuiltVoiceConfig": {
          "voiceName": "Puck"
        }
      }
    }
  },
  "systemInstruction": {
    "parts": [
      {
        "text": "Speak with great enthusiasm and excitement, as if announcing major news to a large audience."
      }
    ]
  }
}
EOF
)

curl -X POST "${API_URL}?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "${REQUEST_JSON}" | \
  jq -r '.candidates[0].content.parts[0].inlineData.data' | \
  base64 --decode > gemini_pro.wav

echo "Gemini Pro audio saved to gemini_pro.wav"
```

### Example 6: List Available Voices

```bash
#!/bin/bash

GOOGLE_API_KEY="your-api-key-here"
API_URL="https://texttospeech.googleapis.com/v1/voices"

# List all voices
curl -X GET "${API_URL}?key=${GOOGLE_API_KEY}" | jq '.'

# List Neural2 voices only
curl -X GET "${API_URL}?key=${GOOGLE_API_KEY}" | \
  jq '.voices[] | select(.name | contains("Neural2")) | {name: .name, gender: .ssmlGender, languages: .languageCodes}'

# List Dutch voices
curl -X GET "${API_URL}?key=${GOOGLE_API_KEY}" | \
  jq '.voices[] | select(.languageCodes[] | contains("nl-NL")) | {name: .name, gender: .ssmlGender}'
```

### Example 7: Complete CLI Tool Template

```bash
#!/bin/bash
# tts-cli.sh - Google Cloud TTS CLI Tool

set -euo pipefail

# Configuration
GOOGLE_API_KEY="${GOOGLE_API_KEY:-}"
API_URL="https://texttospeech.googleapis.com/v1/text:synthesize"
DEFAULT_VOICE="en-US-Neural2-C"
DEFAULT_LANGUAGE="en-US"
DEFAULT_ENCODING="MP3"

# Usage
usage() {
    cat <<EOF
Usage: $0 [OPTIONS] TEXT OUTPUT_FILE

Google Cloud Text-to-Speech CLI Tool

Arguments:
  TEXT          Text to synthesize (or use --input-file)
  OUTPUT_FILE   Output audio file path

Options:
  -k, --api-key KEY        Google API key (or set GOOGLE_API_KEY env var)
  -v, --voice NAME         Voice name (default: $DEFAULT_VOICE)
  -l, --language CODE      Language code (default: $DEFAULT_LANGUAGE)
  -e, --encoding FORMAT    Audio encoding: MP3|LINEAR16|OGG_OPUS (default: $DEFAULT_ENCODING)
  -r, --rate FLOAT         Speaking rate 0.25-4.0 (default: 1.0)
  -p, --pitch FLOAT        Pitch -20.0 to 20.0 (default: 0.0)
  -g, --gain FLOAT         Volume gain -96.0 to 16.0 dB (default: 0.0)
  -i, --input-file FILE    Read text from file
  -s, --ssml               Input is SSML (default: plain text)
  -h, --help               Show this help

Examples:
  $0 "Hello world" output.mp3
  $0 -v nl-NL-Neural2-A "Hallo wereld" dutch.mp3
  $0 -r 0.75 -p -2 "Slow and low" slow.mp3
  $0 -i input.txt -o output.mp3

EOF
    exit 0
}

# Parse arguments
TEXT=""
OUTPUT_FILE=""
VOICE="$DEFAULT_VOICE"
LANGUAGE="$DEFAULT_LANGUAGE"
ENCODING="$DEFAULT_ENCODING"
RATE="1.0"
PITCH="0.0"
GAIN="0.0"
INPUT_FILE=""
USE_SSML=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help) usage ;;
        -k|--api-key) GOOGLE_API_KEY="$2"; shift 2 ;;
        -v|--voice) VOICE="$2"; shift 2 ;;
        -l|--language) LANGUAGE="$2"; shift 2 ;;
        -e|--encoding) ENCODING="$2"; shift 2 ;;
        -r|--rate) RATE="$2"; shift 2 ;;
        -p|--pitch) PITCH="$2"; shift 2 ;;
        -g|--gain) GAIN="$2"; shift 2 ;;
        -i|--input-file) INPUT_FILE="$2"; shift 2 ;;
        -s|--ssml) USE_SSML=true; shift ;;
        -*) echo "Unknown option: $1" >&2; exit 1 ;;
        *)
            if [ -z "$TEXT" ]; then
                TEXT="$1"
            elif [ -z "$OUTPUT_FILE" ]; then
                OUTPUT_FILE="$1"
            else
                echo "Too many arguments" >&2
                exit 1
            fi
            shift
            ;;
    esac
done

# Validate
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "ERROR: API key required (set GOOGLE_API_KEY or use --api-key)" >&2
    exit 1
fi

if [ -n "$INPUT_FILE" ]; then
    if [ ! -f "$INPUT_FILE" ]; then
        echo "ERROR: Input file not found: $INPUT_FILE" >&2
        exit 1
    fi
    TEXT=$(cat "$INPUT_FILE")
fi

if [ -z "$TEXT" ]; then
    echo "ERROR: Text required (provide as argument or --input-file)" >&2
    exit 1
fi

if [ -z "$OUTPUT_FILE" ]; then
    echo "ERROR: Output file required" >&2
    exit 1
fi

# Build request
if [ "$USE_SSML" = true ]; then
    INPUT_JSON="{\"ssml\": $(echo "$TEXT" | jq -Rs .)}"
else
    INPUT_JSON="{\"text\": $(echo "$TEXT" | jq -Rs .)}"
fi

REQUEST_JSON=$(cat <<EOF
{
  "input": $INPUT_JSON,
  "voice": {
    "languageCode": "$LANGUAGE",
    "name": "$VOICE"
  },
  "audioConfig": {
    "audioEncoding": "$ENCODING",
    "speakingRate": $RATE,
    "pitch": $PITCH,
    "volumeGainDb": $GAIN
  }
}
EOF
)

# Make request
echo "Synthesizing speech..." >&2
response=$(curl -s -w "\n%{http_code}" -X POST \
    "${API_URL}?key=${GOOGLE_API_KEY}" \
    -H "Content-Type: application/json" \
    -d "${REQUEST_JSON}")

body=$(echo "$response" | head -n -1)
status=$(echo "$response" | tail -n 1)

if [ "$status" -ne 200 ]; then
    error_msg=$(echo "$body" | jq -r '.error.message // "Unknown error"')
    echo "ERROR (HTTP $status): $error_msg" >&2
    exit 1
fi

# Extract and save audio
echo "$body" | jq -r '.audioContent' | base64 --decode > "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
    file_size=$(stat -f%z "$OUTPUT_FILE" 2>/dev/null || stat -c%s "$OUTPUT_FILE" 2>/dev/null)
    echo "Success! Audio saved to: $OUTPUT_FILE (${file_size} bytes)" >&2
else
    echo "ERROR: Failed to save audio" >&2
    exit 1
fi
```

### Example 8: Batch Processing Multiple Texts

```bash
#!/bin/bash
# batch-tts.sh - Batch process multiple texts

GOOGLE_API_KEY="your-api-key-here"
API_URL="https://texttospeech.googleapis.com/v1/text:synthesize"
VOICE="en-US-Neural2-C"

# Read texts from file (one per line)
input_file="texts.txt"
output_dir="output"

mkdir -p "$output_dir"

line_num=1
while IFS= read -r text; do
    [ -z "$text" ] && continue

    output_file="${output_dir}/audio_${line_num}.mp3"

    echo "Processing line $line_num: $text"

    request=$(cat <<EOF
{
  "input": {"text": "$text"},
  "voice": {"languageCode": "en-US", "name": "$VOICE"},
  "audioConfig": {"audioEncoding": "MP3"}
}
EOF
)

    curl -s -X POST "${API_URL}?key=${GOOGLE_API_KEY}" \
        -H "Content-Type: application/json" \
        -d "$request" | \
        jq -r '.audioContent' | \
        base64 --decode > "$output_file"

    echo "  Saved to: $output_file"

    line_num=$((line_num + 1))

    # Rate limiting: sleep between requests
    sleep 0.5
done < "$input_file"

echo "Batch processing complete!"
```

---

## Summary

### Quick Start Checklist

1. **Setup**
   - Get API key from Google Cloud Console
   - Enable Cloud Text-to-Speech API
   - Store API key securely

2. **Choose Voice Type**
   - Neural2: Best quality/cost balance (recommended)
   - Studio: Premium quality
   - WaveNet: High quality
   - Gemini TTS: AI-powered, expressive (preview)

3. **Basic Request**
   ```bash
   curl -X POST "https://texttospeech.googleapis.com/v1/text:synthesize?key=${API_KEY}" \
     -H "Content-Type: application/json" \
     -d '{"input":{"text":"Hello"},"voice":{"languageCode":"en-US","name":"en-US-Neural2-C"},"audioConfig":{"audioEncoding":"MP3"}}' | \
     jq -r '.audioContent' | base64 --decode > output.mp3
   ```

4. **Handle Errors**
   - Check HTTP status codes
   - Parse error messages
   - Implement retry logic

### Key Takeaways

- **Cloud TTS**: Standard, WaveNet, Neural2, Studio voices via `texttospeech.googleapis.com`
- **Gemini TTS**: AI-powered synthesis via `generativelanguage.googleapis.com` (preview)
- **Audio Formats**: MP3 (recommended for CLI), LINEAR16 (professional), OGG_OPUS (web)
- **Voice Control**: Speaking rate, pitch, volume gain
- **SSML Support**: Advanced control with breaks, emphasis, prosody
- **Style Prompts**: Gemini TTS supports emotional/contextual instructions

### Resources

- [Cloud TTS Documentation](https://cloud.google.com/text-to-speech/docs)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Voice List](https://cloud.google.com/text-to-speech/docs/voices)
- [SSML Reference](https://cloud.google.com/text-to-speech/docs/ssml)
- [Pricing](https://cloud.google.com/text-to-speech/pricing)
- [Quotas & Limits](https://cloud.google.com/text-to-speech/quotas)

---

**Research Completed**: 2025-11-03
**Status**: Comprehensive overview with working curl/bash examples
**Next Steps**: Implement CLI tool using patterns and examples provided
