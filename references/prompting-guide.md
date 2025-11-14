# Prompting Guide for Gemini TTS

This guide provides strategies and best practices for crafting effective text inputs for Google's Gemini Text-to-Speech API.

**Official Documentation**: 
- [Gemini TTS Documentation](https://cloud.google.com/text-to-speech/docs/gemini-tts)
- [Speech Generation Guide](https://ai.google.dev/gemini-api/docs/speech-generation)

## Core Prompting Principles

### 1. Clear and Natural Text

Use natural, well-formed sentences for best results:

**Good:**
```
"The weather today is sunny and warm, perfect for outdoor activities."
```

**Less Effective:**
```
"weather today sunny warm perfect outdoor activities"
```

### 2. Proper Punctuation

Use correct punctuation to guide natural speech patterns:

**Good:**
```
"Hello! How are you? I'm doing great."
```

**Less Effective:**
```
"Hello how are you im doing great"
```

### 3. Contextual Clarity

Provide enough context for proper pronunciation and emphasis:

**Good:**
```
"The lead content writer will lead the meeting."
```

**Less Effective:**
```
"The lead will lead the meeting."
```

## Style Instructions

### Natural Language Style Control

Gemini TTS supports natural language style instructions to control tone and emotion:

**Format**: "Say [style]: [text]"

**Emotional Tones:**
- `"Say cheerfully: Have a wonderful day!"`
- `"Say excitedly: This is amazing news!"`
- `"Say calmly: Don't worry, everything will be fine."`
- `"Say confidently: I believe we can accomplish this."`
- `"Say sadly: I'm sorry to hear about your loss."`

**Speaking Styles:**
- `"Say in a whisper: This is a secret."`
- `"Say formally: Good evening, distinguished guests."`
- `"Say conversationally: Hey, what's up?"`
- `"Say dramatically: In a world where..."`

### Combining Style and Content

**Example 1: Professional Announcement**
```
"Say in a clear, professional tone: Welcome to today's meeting. We have several important topics to discuss."
```

**Example 2: Friendly Greeting**
```
"Say warmly and cheerfully: Thank you for calling! How can I help you today?"
```

**Example 3: Dramatic Narration**
```
"Say with excitement and energy: The hero stood before the ancient door, knowing that behind it lay the answers to all mysteries."
```

## Voice Selection Strategies

### Matching Voice to Content Type

| Content Type | Recommended Voice | Reasoning |
|-------------|------------------|-----------|
| **Educational Content** | Charon | Clear, informative, easy to understand |
| **Energetic Marketing** | Puck | Upbeat, engaging, attention-grabbing |
| **Professional Business** | Kore | Firm, authoritative, trustworthy |
| **Friendly Customer Service** | Zephyr | Warm, approachable, welcoming |
| **Neutral Narration** | Echo | Balanced, versatile, works for most content |

### Example Voice Selection

```go
// Professional announcement
voice = "Kore"
text = "Say in a firm, clear tone: Attention all staff, meeting begins in 5 minutes."

// Friendly greeting
voice = "Zephyr"
text = "Say cheerfully: Welcome to our store! How can I assist you today?"

// Educational content
voice = "Charon"
text = "Today we'll learn about the fundamentals of quantum physics."
```

## Language-Specific Considerations

### English (en-US)

- Use standard spelling and grammar
- Include pronunciation hints for uncommon words: "The word 'quinoa' (KEEN-wah) is..."
- Use phonetic spelling for emphasis: "The answer is clearly 'NO' (emphasize the word)"

### Numbers and Dates

**Good Formatting:**
```
"The meeting is scheduled for March 15th, 2025 at 3:30 PM."
```

**Avoid Ambiguity:**
```
"The meeting is 3/15/25 at 3:30." // Can be unclear
```

### Abbreviations and Acronyms

**Spell Out When Needed:**
```
"The NASA (N-A-S-A) mission was successful."
```

**Provide Context:**
```
"The CEO (Chief Executive Officer) announced the merger."
```

## Text Formatting Best Practices

### Paragraphs and Structure

Break long text into paragraphs for natural pauses:

**Good:**
```
"This is the first paragraph. It contains complete thoughts.

This is the second paragraph. It provides additional information."
```

### Emphasis and Pauses

Use punctuation for natural pauses:
- Commas for brief pauses
- Periods for longer pauses
- Exclamation points for emphasis
- Question marks for questioning tone

**Example:**
```
"Stop, look, and listen before crossing the street."
```

### Handling Special Characters

**Currency:**
```
"The price is ten dollars and fifty cents."
// Better than: "The price is $10.50"
```

**Email Addresses:**
```
"Contact us at support at example dot com."
// Better than: "Contact us at support@example.com"
```

## Advanced Techniques

### Multi-Speaker Dialogues

Gemini TTS supports generating audio with multiple distinct voices in a single dialogue. This is ideal for:
- Conversations between characters
- Interviews and Q&A sessions
- Multi-character storytelling
- Training simulations with multiple roles
- Podcast-style content

#### Basic Format for Multi-Speaker Text

Use speaker aliases (alphanumeric, no spaces) followed by a colon:

**Format:**
```
SpeakerAlias1: Text for first speaker.
SpeakerAlias2: Text for second speaker.
SpeakerAlias1: Response from first speaker.
```

**Example:**
```
Speaker1: Hello, how are you today?
Speaker2: I'm doing well, thank you! How about you?
Speaker1: Great! I'm excited about our project.
```

#### Speaker Alias Rules

**✅ Valid Aliases:**
- `Speaker1`, `Speaker2`, `Narrator`, `Customer`, `Agent`
- `Alice`, `Bob`, `Charlie123`
- Alphanumeric characters only, no spaces

**❌ Invalid Aliases:**
- `Speaker 1` (contains space)
- `Speaker-1` (contains hyphen)
- `Speaker_1` (contains underscore)

#### Complete Multi-Speaker Example

**Text Input:**
```
Narrator: Once upon a time, in a distant kingdom...

Hero: I must find the ancient artifact!

Narrator: And so, the hero's journey began.

Villain: You'll never succeed!

Hero: We'll see about that!
```

#### Voice Mapping Configuration

In your code, map each speaker alias to a specific voice:

**Go Example (Cloud TTS Client):**
```go
multiSpeakerVoiceConfig := &texttospeechpb.MultiSpeakerVoiceConfig{
    SpeakerVoiceConfigs: []*texttospeechpb.MultispeakerPrebuiltVoice{
        {
            SpeakerAlias: "Narrator",
            SpeakerId:    "Charon",  // Informative voice
        },
        {
            SpeakerAlias: "Hero",
            SpeakerId:    "Kore",    // Firm, confident voice
        },
        {
            SpeakerAlias: "Villain",
            SpeakerId:    "Puck",    // Energetic, could be menacing
        },
    },
}
```

#### Adding Style to Multi-Speaker Dialogues

You can combine speaker aliases with style instructions:

**Format:**
```
Speaker1: Say cheerfully: Hello there!
Speaker2: Say formally: Good morning.
Speaker1: Say excitedly: Great to see you!
```

**Example Dialogue with Styles:**
```
Customer: Say cheerfully: Hi, I need help with my order.
Agent: Say professionally: Hello! I'd be happy to assist you.
Customer: Say worried: It hasn't arrived yet.
Agent: Say reassuringly: Don't worry, let me check that for you.
```

#### Best Practices for Multi-Speaker Dialogues

1. **Use Clear Speaker Names**
   - Use descriptive but short aliases: `Narrator`, `Hero`, `Customer`
   - Avoid generic names that could be confusing: `Person1`, `A`, `B`

2. **Assign Appropriate Voices**
   - Match voice characteristics to character traits
   - Use contrasting voices for different characters
   - Consider voice gender and tone for character consistency

3. **Maintain Speaker Consistency**
   - Use the same alias throughout for each character
   - Don't switch aliases for the same character
   - Keep voice mappings consistent across sessions

4. **Structure Dialogues Clearly**
   - One line per speaker turn
   - Use line breaks between different speakers
   - Keep turns reasonably short for natural flow

**Example of Well-Structured Dialogue:**
```
Teacher: Welcome to today's science class. Today we're studying photosynthesis.

Student1: That sounds interesting! Can you explain how it works?

Teacher: Absolutely. Photosynthesis is the process by which plants convert sunlight into energy.

Student2: So plants eat sunlight?

Teacher: In a way, yes. They use sunlight to create glucose, which is their food.
```

#### Character Voice Recommendations

**Narrators:**
- `Charon` - Informative, clear, educational
- `Echo` - Neutral, balanced, versatile

**Main Characters (Heroes/Protagonists):**
- `Kore` - Firm, confident, authoritative
- `Zephyr` - Bright, friendly, approachable

**Supporting Characters:**
- `Puck` - Upbeat, energetic
- `Aria` - Melodic, expressive

**Antagonists/Villains:**
- `Kore` - Firm (can sound authoritative/commanding)
- Custom combinations with style instructions

**Example Character Mapping:**
```
// Educational podcast
Host: Charon
Guest: Kore

// Storytelling
Narrator: Charon
Protagonist: Zephyr
Antagonist: Kore (with style: Say in a commanding tone)

// Customer service training
Customer: Zephyr
Agent: Kore
Supervisor: Charon
```

#### Limitations and Constraints

**Text Limits:**
- Each dialogue prompt: Maximum 4,000 bytes
- Combined dialogue: Maximum 4,000 bytes
- Total characters across all speakers: 4,000 bytes

**Audio Limits:**
- Maximum output duration: ~655 seconds (~10.9 minutes)
- Audio will be truncated if exceeded

**Speaker Limits:**
- Number of unique speakers: Typically 2-10 speakers per dialogue
- Each speaker must have a unique alias

#### Example: Customer Service Dialogue

**Text:**
```
Customer: Say concerned: Hi, my order hasn't arrived yet.
Agent: Say professionally: I'm sorry to hear that. Can you provide your order number?
Customer: Say relieved: Sure, it's ORD-12345.
Agent: Say confidently: Thank you. Let me check on that for you right away.
Customer: Say grateful: Thank you so much!
Agent: Say warmly: You're welcome. I've found your order - it's scheduled for delivery tomorrow.
```

**Voice Mapping:**
```go
{
    {SpeakerAlias: "Customer", SpeakerId: "Zephyr"}, // Friendly, warm
    {SpeakerAlias: "Agent", SpeakerId: "Kore"},       // Professional, firm
}
```

#### Example: Educational Dialogue

**Text:**
```
Teacher: Today we're going to learn about the water cycle.
Student1: What is the water cycle?
Teacher: Great question! The water cycle describes how water moves through our environment.
Student2: Does it always rain?
Teacher: Not always, but precipitation is one part of the cycle. Can anyone name another part?
Student1: Evaporation?
Teacher: Excellent! Evaporation is when water turns into vapor and rises into the air.
```

**Voice Mapping:**
```go
{
    {SpeakerAlias: "Teacher", SpeakerId: "Charon"},   // Informative, clear
    {SpeakerAlias: "Student1", SpeakerId: "Zephyr"},  // Bright, curious
    {SpeakerAlias: "Student2", SpeakerId: "Puck"},    // Upbeat, engaged
}
```

### Character Consistency

For multi-character narratives, assign consistent voices:
- **Narrator**: Charon (informative, clear)
- **Main Character**: Kore (firm, confident) or Zephyr (friendly)
- **Supporting Character**: Puck (upbeat) or Aria (expressive)
- **Antagonist**: Kore with style instructions for commanding tone

### Emotional Arc

Build emotional progression through style instructions:

```
"Say calmly: The journey began quietly.

Say with growing excitement: But as we traveled further, things became more interesting.

Say with urgency: Suddenly, danger appeared!"
```

## Common Prompt Patterns

### Greetings and Introductions

**Professional:**
```
"Say in a warm, professional tone: Good morning! Welcome to our company. My name is [Name], and I'll be assisting you today."
```

**Casual:**
```
"Say cheerfully: Hey there! How's it going? Thanks for joining us."
```

### Instructions and Guidance

**Clear Instructions:**
```
"Say in a clear, instructional tone: First, press the power button. Then, wait for the light to turn green. Finally, select your option."
```

**Step-by-Step:**
```
"Say clearly and slowly: Step one: Gather your materials. Step two: Follow the instructions. Step three: Verify your results."
```

### Narrations

**Storytelling:**
```
"Say in a storytelling voice with appropriate pacing: Long ago, in a kingdom far away, a young princess discovered a mysterious door. She hesitated for a moment, then reached for the handle."
```

**Educational:**
```
"Say in an informative, clear tone: Photosynthesis is the process by which plants convert sunlight into energy. This process occurs in two main stages."
```

### Announcements

**Public Announcements:**
```
"Say loudly and clearly: Attention all passengers: Flight 123 is now boarding at gate 7."
```

**Quiet Notifications:**
```
"Say softly: You have a new message."
```

## What to Avoid

### ❌ Overly Technical Language Without Context

**Avoid:**
```
"The API endpoint returns JSON with nested objects."
```

**Better:**
```
"The API endpoint returns data in JSON format, which contains nested information structures."
```

### ❌ Excessive Punctuation

**Avoid:**
```
"Wow!!! This is amazing!!!!!!"
```

**Better:**
```
"Say excitedly: Wow! This is amazing!"
```

### ❌ Unclear Abbreviations

**Avoid:**
```
"Check the FAQ for more info."
```

**Better:**
```
"Check the frequently asked questions, or FAQ, for more information."
```

### ❌ Missing Context for Ambiguous Words

**Avoid:**
```
"The bass was caught in the bass."
```

**Better:**
```
"The bass fish was caught in the bass guitar."
```

## Prompt Templates

### Template 1: Customer Service Greeting

```
"Say [tone]ly: [Greeting]. [Company name] customer service. How may I assist you today?"
```

**Example:**
```
"Say warmly: Good afternoon. Acme Corporation customer service. How may I assist you today?"
```

### Template 2: Educational Content

```
"[Introduction]. Today we'll learn about [topic]. [Content]. Let's begin with [first point]."
```

**Example:**
```
"Say in a clear, instructional tone: Welcome to our learning module. Today we'll learn about data structures. Data structures are ways of organizing information in computer programs. Let's begin with arrays."
```

### Template 3: Story Narration

```
"Say in a [style] voice: [Story text with appropriate pacing]"
```

**Example:**
```
"Say in a storytelling voice with dramatic pauses: In the depths of the forest, where shadows danced and whispers echoed, the ancient secret lay hidden. For generations, none had dared to seek it out."
```

## Testing and Iteration

### Test Different Styles

Try multiple style variations to find the best fit:

1. Generate with different voices
2. Try various style instructions
3. Compare outputs
4. Select the best match for your use case

### Refinement Process

1. **Start Simple**: Begin with basic text-to-speech
2. **Add Style**: Incorporate style instructions
3. **Refine Voice**: Select appropriate voice
4. **Adjust Pacing**: Use punctuation and structure for natural flow
5. **Test Output**: Listen and refine based on results

## Best Practices Summary

1. ✅ **Use natural language** - Write as you would speak
2. ✅ **Include proper punctuation** - Guide natural speech patterns
3. ✅ **Add style instructions** - Control tone and emotion naturally
4. ✅ **Choose appropriate voices** - Match voice to content type
5. ✅ **Provide context** - Help with pronunciation and emphasis
6. ✅ **Structure clearly** - Use paragraphs and formatting
7. ✅ **Test and iterate** - Refine based on audio output

## References

- [Gemini TTS Documentation](https://cloud.google.com/text-to-speech/docs/gemini-tts)
- [Speech Generation Guide](https://ai.google.dev/gemini-api/docs/speech-generation)
- [Cloud Text-to-Speech Best Practices](https://cloud.google.com/text-to-speech/docs/best-practices)

