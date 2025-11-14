# Gemini 2.5 TTS Voice and Style Prompt Engineering Guide

**Last Updated:** 2025-11-03
**Models:** gemini-2.5-flash-preview-tts, gemini-2.5-pro-preview-tts
**Author:** Research compiled for curl-gemini-tts CLI

## Table of Contents

1. [Overview](#overview)
2. [Voice Selection Guide](#voice-selection-guide)
3. [Style Control with systemInstruction](#style-control-with-systeminstruction)
4. [Single Voice Synthesis](#single-voice-synthesis)
5. [Multi-Voice Scenarios](#multi-voice-scenarios)
6. [Emotional Control](#emotional-control)
7. [Speaking Styles](#speaking-styles)
8. [Advanced Prompt Patterns](#advanced-prompt-patterns)
9. [Model-Specific Guidance](#model-specific-guidance)
10. [Practical Examples](#practical-examples)
11. [Best Practices](#best-practices)
12. [Troubleshooting](#troubleshooting)

---

## Overview

Gemini 2.5 TTS models support sophisticated voice synthesis through a combination of:

- **Voice selection** via `voiceName` parameter (Puck, Kore, Zephyr, Charon, Aoede, Fenrir)
- **Style prompts** via `systemInstruction` for emotional tone, pacing, and delivery
- **Text formatting** for emphasis, pauses, and structure
- **Multi-voice support** through structured prompt formatting

### Key Capabilities

- Natural-sounding speech with emotional nuance
- Multiple distinct voices in single synthesis
- Style control without explicit SSML markup
- Context-aware delivery based on content type
- Support for 100+ languages

### Model Selection

| Model | Best For | Latency | Quality |
|-------|----------|---------|---------|
| gemini-2.5-flash-preview-tts | Quick responses, real-time apps | Low | High |
| gemini-2.5-pro-preview-tts | Complex scenarios, subtle nuance | Medium | Very High |

---

## Voice Selection Guide

### Available Voices

| Voice | Characteristics | Best For |
|-------|----------------|----------|
| **Puck** | Energetic, youthful, upbeat | Marketing, entertainment, casual content |
| **Kore** | Professional, clear, neutral | News, business, educational content |
| **Zephyr** | Warm, friendly, conversational | Podcasts, storytelling, guides |
| **Charon** | Deep, authoritative, serious | Documentaries, formal announcements |
| **Aoede** | Expressive, dynamic, theatrical | Character dialogue, audiobooks |
| **Fenrir** | Calm, soothing, measured | Meditation, ASMR, bedtime stories |

### Voice Selection Matrix

```
Content Type          | Primary Choice | Alternative
---------------------|----------------|-------------
News Article         | Kore           | Charon
Blog Post            | Zephyr         | Puck
Product Demo         | Puck           | Zephyr
Tutorial             | Kore           | Zephyr
Audiobook Fiction    | Aoede          | Zephyr
Audiobook Non-Fiction| Zephyr         | Kore
Podcast Host         | Zephyr         | Puck
Corporate Training   | Kore           | Charon
Marketing Ad         | Puck           | Aoede
Meditation Guide     | Fenrir         | Zephyr
Character Dialogue   | Aoede          | Puck
Technical Docs       | Kore           | Charon
Storytelling         | Aoede          | Zephyr
Interview/Convo      | Zephyr         | Puck
```

### Language-Specific Recommendations

For non-English content, voice characteristics remain but pronunciation adapts:

- **Spanish/Portuguese:** Puck, Zephyr (best naturalness)
- **French/German:** Kore, Charon (clarity and formality)
- **Japanese/Korean:** Aoede, Zephyr (expressiveness)
- **Mandarin/Cantonese:** Kore, Fenrir (tonal accuracy)

---

## Style Control with systemInstruction

### How systemInstruction Works

The `systemInstruction` field provides high-level guidance to the TTS model about:

- Overall tone and emotion
- Speaking style and pacing
- Target audience and context
- Delivery emphasis

**Key Principle:** systemInstruction sets the "mood" and "context" without specifying exact phonetic details.

### Basic Structure

```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are a [role]. Speak with [tone/style]. The audience is [target]. [Additional guidance]."
      }
    ]
  }
}
```

### Effective systemInstruction Components

1. **Role Definition:** "You are a professional news anchor" / "You are an excited product reviewer"
2. **Tone Specification:** "enthusiastic" / "calm and measured" / "warm and friendly"
3. **Pacing Guidance:** "speak slowly and clearly" / "energetic pace" / "conversational tempo"
4. **Emphasis Hints:** "emphasize key technical terms" / "build excitement for reveals"
5. **Audience Context:** "explaining to beginners" / "professional business audience"

### systemInstruction Examples

#### Professional News Delivery
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are a professional broadcast journalist. Speak with clarity, authority, and objectivity. Maintain a measured pace suitable for news delivery. Emphasize important facts without sensationalism."
      }
    ]
  },
  "voiceName": "Kore"
}
```

#### Enthusiastic Product Demo
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are an energetic product demonstrator at a tech event. Show genuine excitement about features. Build anticipation before revealing key points. Speak conversationally but maintain high energy throughout."
      }
    ]
  },
  "voiceName": "Puck"
}
```

#### Soothing Bedtime Story
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are reading a bedtime story to children. Speak softly and soothingly with a calm, gentle pace. Add slight dramatic flair for character dialogue but keep overall energy relaxing. Create a peaceful, sleepy atmosphere."
      }
    ]
  },
  "voiceName": "Fenrir"
}
```

---

## Single Voice Synthesis

### Basic Prompt Structure

For single-voice synthesis, focus on:

1. Clear, well-structured text
2. Natural punctuation for pauses
3. Appropriate systemInstruction for context

### Example 1: Professional Tutorial

**Text:**
```
Welcome to our advanced JavaScript tutorial. Today, we'll explore closures.

A closure is a function that has access to variables in its outer lexical scope, even after the outer function has returned. Let's see this in action.

Consider this example: when we define a function inside another function, the inner function maintains access to the outer function's variables. This powerful feature enables data privacy and factory patterns.
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are a patient programming instructor teaching intermediate developers. Speak clearly with slight pauses after technical terms to allow comprehension. Use a friendly but professional tone. Emphasize code concepts when mentioned."
      }
    ]
  },
  "voiceName": "Kore"
}
```

### Example 2: Engaging Blog Post

**Text:**
```
Here's something fascinating: the human brain processes visual information 60,000 times faster than text!

That's exactly why infographics work so incredibly well. They combine the speed of visual processing with the clarity of written content.

Think about it—when was the last time you chose to read a 2,000-word article over an engaging infographic covering the same topic? I'm guessing... never?
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are a charismatic blogger sharing interesting insights. Speak conversationally with natural enthusiasm. Pause briefly before revealing surprising facts for effect. Include slight emphasis on numbers and statistics. Sound like you're talking to a friend over coffee."
      }
    ]
  },
  "voiceName": "Zephyr"
}
```

### Example 3: Meditation Script

**Text:**
```
Close your eyes... and take a deep breath in.

Hold it for a moment.

And slowly release.

Feel your body beginning to relax. Notice any tension in your shoulders... and let it go.

With each breath, you're becoming more and more peaceful. More and more calm.

There's nowhere you need to be. Nothing you need to do. Just breathe... and be present in this moment.
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are a gentle meditation guide. Speak very slowly and softly with long natural pauses. Your voice should be calming and peaceful. Each word should feel like a gentle invitation to relax. Maintain a consistently soothing, hypnotic tone throughout."
      }
    ]
  },
  "voiceName": "Fenrir"
}
```

---

## Multi-Voice Scenarios

### Structured Format for Multiple Speakers

Gemini TTS can synthesize multiple distinct voices in a single request using speaker labels and systemInstruction guidance.

### Format Pattern

```
[Speaker Name]: Dialogue text

[Different Speaker]: Response text
```

### Key Techniques

1. **Clear speaker labels:** Use consistent naming (e.g., "Alex:", "Jordan:")
2. **Character descriptions in systemInstruction:** Define each voice's characteristics
3. **Distinct personalities:** Make speaker differences clear in description
4. **Contextual cues:** Include brief action or emotion hints

### Example 4: Podcast Interview

**Text:**
```
Host: Welcome back to Tech Insights! I'm thrilled to have Dr. Sarah Chen with us today. Sarah, thanks for joining us!

Guest: Thanks for having me! It's great to be here.

Host: So, let's dive right in. You've just published groundbreaking research on quantum computing. Can you explain it in terms our listeners can understand?

Guest: Absolutely! Imagine trying to find your way out of a massive maze. A classical computer would try one path at a time. But a quantum computer? It explores all possible paths simultaneously. That's the real superpower here.

Host: Wow, that's fascinating! And this has practical applications right now?

Guest: Yes! We're already seeing breakthroughs in drug discovery, encryption, and climate modeling. The future is incredibly exciting.
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "This is a podcast conversation between two people. Host is an enthusiastic interviewer with an engaging, warm voice—speak with genuine curiosity and energy. Guest is a knowledgeable scientist—speak with authority but remain approachable and conversational. Both should sound natural and relaxed, with the Host slightly more animated than the Guest."
      }
    ]
  },
  "voiceName": "Zephyr"
}
```

### Example 5: Customer Service Call

**Text:**
```
Agent: Thank you for calling TechSupport Plus. My name is Morgan. How can I help you today?

Customer: Hi, yes, I'm having trouble with my account login. It keeps saying my password is incorrect, but I know it's right!

Agent: I completely understand how frustrating that must be. Let me help you resolve this. First, can you confirm the email address associated with your account?

Customer: Sure, it's john.doe@email.com.

Agent: Perfect. I see your account here. It looks like your account was temporarily locked after several login attempts. That's actually a security feature to protect you. I can unlock it right now.

Customer: Oh! That makes sense. I was trying different passwords thinking I forgot it.

Agent: Totally understandable! I've unlocked your account. You should be able to log in now with your original password. Give it a try?

Customer: Yes! It worked! Thank you so much!

Agent: Wonderful! Is there anything else I can help you with today?
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "This is a customer service call. Agent speaks professionally with warmth and empathy—calm, helpful, and reassuring. Customer starts slightly frustrated but becomes relieved—voice should reflect this emotional journey from annoyance to gratitude. Make the conversation sound natural with slight overlaps in energy between speakers."
      }
    ]
  },
  "voiceName": "Kore"
}
```

### Example 6: Character Dialogue Scene

**Text:**
```
Detective: [serious, low voice] The evidence doesn't lie, Mr. Harrison. Your fingerprints were found at the scene.

Mr. Harrison: [nervous, defensive] That's impossible! I wasn't anywhere near that building!

Detective: [pause, leaning in] Then explain this security footage. That's you entering at 10:47 PM. Right around the time of the incident.

Mr. Harrison: [panicked] I... I can explain! I was just—

Detective: [interrupting, firm] Save it. We both know you're lying. The question is: are you going to tell me the truth, or do I need to make this harder for you?

Mr. Harrison: [defeated, quiet] Fine. I'll tell you everything.
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "This is a dramatic interrogation scene. Detective speaks with authority and intensity—measured, calculated, slightly threatening. Use lower pitch and deliberate pacing. Mr. Harrison is increasingly anxious—voice should tremble slightly, speed up when panicked, and become subdued when defeated. Include emotional nuance through vocal tension."
      }
    ]
  },
  "voiceName": "Aoede"
}
```

---

## Emotional Control

### Primary Emotions Supported

Gemini TTS responds well to emotional direction in systemInstruction:

- **Joy/Excitement:** "enthusiastic," "delighted," "energetic"
- **Sadness/Melancholy:** "somber," "reflective," "subdued"
- **Anger/Frustration:** "intense," "sharp," "forceful"
- **Fear/Anxiety:** "nervous," "hesitant," "worried"
- **Calm/Peace:** "tranquil," "soothing," "measured"
- **Surprise/Wonder:** "amazed," "curious," "astonished"
- **Confidence/Authority:** "commanding," "assured," "powerful"
- **Warmth/Affection:** "tender," "caring," "gentle"

### Emotional Intensity Scale

Use modifiers to control intensity:

- **Light:** "slightly," "gently," "subtly"
- **Moderate:** (no modifier)
- **Strong:** "very," "intensely," "deeply"

### Example 7: Joyful Product Announcement

**Text:**
```
We did it! After two years of development, countless iterations, and your incredible feedback... we're finally ready!

Introducing the Phoenix 5—our most advanced, most beautiful, most powerful device ever created. And honestly? We couldn't be more excited to share it with you!

Every feature, every detail, every pixel was crafted with one goal: making your life easier and more delightful. This is more than just an upgrade. This is a revolution.
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are announcing an exciting product launch with genuine joy and pride. Speak with building enthusiasm—start energetic and crescendo to even more excitement. Emphasize superlatives naturally. Let your voice convey the passion and celebration of this moment. Sound like you're bursting with happiness to share this news."
      }
    ]
  },
  "voiceName": "Puck"
}
```

### Example 8: Somber Memorial

**Text:**
```
Today, we remember.

We remember the lives lost. The families forever changed. The heroes who gave everything.

Twenty years have passed, but the memories remain vivid. The pain, still real. The courage, still inspiring.

We gather not in sorrow alone, but in gratitude—for those who served, for those who sacrificed, and for the resilience of the human spirit that refuses to be broken by tragedy.

We will never forget.
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are delivering a memorial speech with deep respect and solemnity. Speak slowly with purposeful pauses. Your voice should convey profound sadness but also quiet strength. Each word carries weight. Maintain dignity and restraint—avoid over-dramatization. Let the gravity of the moment speak through measured, heartfelt delivery."
      }
    ]
  },
  "voiceName": "Charon"
}
```

### Example 9: Building Suspense

**Text:**
```
The hallway was empty. Too empty.

Sarah's footsteps echoed against the marble floor as she approached the door at the end. The door she'd been warned never to open.

Her hand trembled as she reached for the handle. Cold metal against her palm.

From inside... a sound. A whisper? Or just the wind?

She turned the handle.

The door creaked open.

And what she saw inside... would change everything.
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are narrating a suspenseful thriller scene. Start with quiet tension and gradually build unease. Use strategic pauses to create anticipation. Lower your pitch slightly for ominous moments. Speak deliberately—each sentence should add to the mounting dread. End with emphasis and a slight dramatic pause after 'everything.'"
      }
    ]
  },
  "voiceName": "Aoede"
}
```

---

## Speaking Styles

### Style Categories

1. **Conversational:** Natural, relaxed, like talking to friends
2. **Professional:** Clear, articulate, business-appropriate
3. **Narrative:** Storytelling, engaging, descriptive
4. **Instructional:** Patient, clear, educational
5. **Dramatic:** Theatrical, expressive, performative
6. "Promotional:** Enthusiastic, persuasive, energetic
7. **Documentary:** Authoritative, informative, measured

### Example 10: Conversational Podcast Style

**Text:**
```
So here's the thing about morning routines—everyone tells you to wake up at 5 AM, meditate, journal, exercise, make a green smoothie, and probably learn a new language before breakfast. Right?

But honestly? That's exhausting just thinking about it!

Here's what actually works: pick ONE thing. Just one. Maybe it's making your bed. Maybe it's ten minutes of stretching. Whatever feels doable.

Because here's the secret nobody tells you: consistency beats perfection every single time.
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You're hosting a casual, relatable podcast. Speak like you're chatting with a friend—natural rhythm, occasional verbal emphasis, conversational pauses. Include slight vocal variety to maintain engagement. Sound authentic and approachable, not scripted. Let personality shine through."
      }
    ]
  },
  "voiceName": "Zephyr"
}
```

### Example 11: Documentary Narration

**Text:**
```
The Amazon Rainforest. Spanning over 5.5 million square kilometers across nine countries, it stands as Earth's largest tropical rainforest.

But this isn't just a forest—it's a living, breathing system. Home to ten percent of all species on the planet. Producer of twenty percent of the world's oxygen.

Indigenous peoples have thrived here for over 10,000 years, developing deep knowledge of this complex ecosystem. Their wisdom, passed down through generations, holds secrets modern science is only beginning to understand.

Yet this irreplaceable treasure faces unprecedented threats. Every minute, an area the size of four football fields is cleared. The clock is ticking.
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are narrating a nature documentary with David Attenborough-style gravitas. Speak with authority and wonder. Use measured pacing that allows facts to resonate. Build tension when describing threats. Convey both the majesty of nature and the urgency of conservation. Voice should inspire awe and respect."
      }
    ]
  },
  "voiceName": "Charon"
}
```

### Example 12: Sales Pitch / Promotional

**Text:**
```
Tired of spending hours on repetitive tasks? Frustrated watching your productivity slip away on busy work?

What if I told you there's a better way?

Introducing TaskFlow Pro—the automation tool that saves teams an average of 15 hours every week. That's right. Fifteen hours you get back to focus on what actually matters.

No complex setup. No coding required. Just smart automation that works the way you work.

Join over 50,000 teams who've already made the switch. Your future self will thank you.

Try TaskFlow Pro free for 30 days. What do you have to lose—except all that wasted time?
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are delivering a compelling sales pitch with confident energy. Start by relating to pain points, then build excitement about the solution. Emphasize key benefits and numbers with natural enthusiasm. Sound persuasive but genuine—not pushy. Create urgency without pressure. Your voice should inspire action while building trust."
      }
    ]
  },
  "voiceName": "Puck"
}
```

---

## Advanced Prompt Patterns

### Pattern 1: Emotional Journey

Structure content to guide TTS through emotional transitions.

**Before (Flat Emotion):**
```
Our company has decided to close the office. This affects everyone. We'll provide support during the transition. More details will follow.
```

**After (Emotional Journey):**
```
I have some difficult news to share, and I want to be completely transparent with you.

[pause] After careful consideration, we've made the incredibly hard decision to close our office location. I know this impacts each and every one of you, and I don't take that lightly.

But I want you to know: we're committed to supporting you through this transition. You're not alone in this. We'll provide comprehensive resources, placement assistance, and continued benefits.

More details are coming, but today, I first wanted to speak with you personally. Your contributions matter. You matter.
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are a CEO delivering difficult news with empathy and sincerity. Start serious and somber. Speak slowly with genuine concern. Show compassion when discussing impact. Shift to reassuring and supportive tone when offering help. End with warmth and personal connection. Let your voice convey that you genuinely care."
      }
    ]
  }
}
```

### Pattern 2: Emphasis Through Repetition

**Example:**
```
This isn't just about speed. It's not just about power. It's not just about design.

It's about all three. Together. Perfectly balanced. For the first time ever.

That's what makes this revolutionary.
```

**systemInstruction:** "Build emphasis with each repetition, then deliver final line with confident conviction."

### Pattern 3: Question-Answer Flow

**Example:**
```
What's the secret to great writing?

Is it vocabulary? Partly.

Grammar? That helps.

Reading widely? Absolutely.

But the real secret? It's simple: write every single day. Even when you don't feel like it. Even when it's terrible. Especially when it's terrible.

Because you can't edit a blank page.
```

**systemInstruction:** "Pose questions with genuine curiosity. Answer conversationally as if thinking aloud. Build to confident conclusion."

### Pattern 4: Contrast and Comparison

**Example:**
```
Traditional project management: rigid timelines, endless meetings, delayed feedback, frustrated teams.

Agile methodology: flexible sprints, quick stand-ups, continuous iteration, empowered teams.

See the difference? One fights change. The other embraces it.
```

**systemInstruction:** "Present first option with slight disapproval and slower pace. Present second option with enthusiasm and energy. Emphasize contrast in final statement."

### Pattern 5: Statistical Storytelling

**Example:**
```
Ninety-three percent. Let that sink in.

Ninety-three percent of communication is non-verbal. Your body language, your tone, your facial expressions—that's what people actually hear.

So when you're in that next meeting, that next presentation, that next difficult conversation... remember: it's not just what you say. It's how you say it.

Those words? They're only seven percent of your message. Make the other ninety-three count.
```

**systemInstruction:** "Emphasize statistics with deliberate pacing. Pause after numbers for impact. Build from factual to motivational. End with inspirational energy."

---

## Model-Specific Guidance

### gemini-2.5-flash-preview-tts

**Best For:**
- Real-time applications
- Shorter content (< 500 words)
- Simple emotional ranges
- Conversational styles
- Quick prototyping

**Optimization Tips:**
- Keep systemInstruction concise (1-2 sentences)
- Focus on primary emotion/style
- Avoid overly complex emotional nuances
- Works best with natural, flowing text
- Faster processing = slight trade-off in subtle vocal control

**Example Prompt (Flash-Optimized):**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "Professional news delivery with clear, authoritative tone."
      }
    ]
  },
  "voiceName": "Kore"
}
```

### gemini-2.5-pro-preview-tts

**Best For:**
- Complex emotional narratives
- Longer content (500+ words)
- Subtle vocal nuances
- Multi-character scenes
- Audiobook production
- High-quality final output

**Optimization Tips:**
- Use detailed systemInstruction (3-5 sentences)
- Specify subtle emotional transitions
- Include character personality details for dialogue
- Take advantage of superior context understanding
- Better at maintaining consistency over longer passages

**Example Prompt (Pro-Optimized):**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are a seasoned broadcast journalist with 20 years of experience. Deliver this news story with professional gravitas, emphasizing key facts with subtle vocal stress. Maintain objective neutrality but allow appropriate emotional inflection for human interest elements. Pace should be measured—approximately 150 words per minute—with strategic pauses between major story segments."
      }
    ]
  },
  "voiceName": "Kore"
}
```

### Performance Comparison

| Feature | Flash | Pro |
|---------|-------|-----|
| Emotional Subtlety | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Multi-Character Distinction | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Long-Form Consistency | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Complex Instruction Following | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Cost Efficiency | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

---

## Practical Examples

### Example 13: News Anchor Style

**Use Case:** Daily news podcast opening

**Text:**
```
Good morning. I'm Alex Rivera, and this is your Friday briefing.

Top story: The Federal Reserve has announced a quarter-point interest rate cut, marking the third reduction this year. Markets responded positively, with the S&P 500 climbing two percent in early trading.

In technology news: the European Union has finalized new AI regulations, requiring transparency in algorithmic decision-making. Companies have 18 months to comply.

And in science: researchers at MIT have developed a new battery technology that could double electric vehicle range. The breakthrough involves a novel lithium-metal compound.

We'll have complete coverage of these stories and more right after this break.
```

**Full Configuration:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are a professional news anchor delivering the morning headlines. Speak with clarity, authority, and neutral objectivity. Maintain consistent pacing suitable for broadcast—measured but engaging. Emphasize important facts and figures naturally. Transition smoothly between stories with appropriate vocal cues."
      }
    ]
  },
  "voiceName": "Kore",
  "languageCode": "en-US"
}
```

### Example 14: Audiobook Narration

**Use Case:** Fiction audiobook sample

**Text:**
```
Chapter Seven: The Decision

Eleanor stood at the window, watching rain streak down the glass in thin, shimmering lines. Behind her, the grandfather clock ticked—each second another reminder that time was running out.

She'd promised herself she'd never return to Willow Creek. Too many memories. Too much pain.

But the letter changed everything.

"Eleanor?" Her sister's voice drifted from the hallway, tentative, hopeful. "Have you decided?"

Eleanor closed her eyes, her hand pressed against the cold window pane. After ten years, the answer should have been easy.

It wasn't.

"Yes," she finally whispered. "Book two tickets. We leave tomorrow."
```

**Full Configuration:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are narrating a character-driven fiction novel. Use a warm, engaging narrative voice with subtle emotional inflection that reflects Eleanor's internal conflict. For dialogue, differentiate characters slightly: Eleanor sounds resolved but conflicted, Sister sounds hopeful and uncertain. Maintain storytelling pacing with natural pauses for scene transitions. Create atmosphere through vocal tone—melancholy but with underlying tension."
      }
    ]
  },
  "voiceName": "Aoede",
  "languageCode": "en-US"
}
```

### Example 15: Marketing Ad (30-second spot)

**Use Case:** Radio/streaming audio advertisement

**Text:**
```
Feeling overwhelmed by your inbox? You're not alone.

The average person receives 121 emails every single day. That's 121 interruptions. 121 distractions. 121 reasons you can't focus on actual work.

InboxZero changes that. Smart filters. AI-powered prioritization. One-click unsubscribe.

Take back your day. Try InboxZero free.

Because your time is worth more than spam.
```

**Full Configuration:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are voicing a concise radio advertisement with relatable, conversational energy. Start by connecting to listener's pain point with empathy. Emphasize the staggering number (121) with appropriate concern. Shift to confident, solution-focused tone when introducing the product. End with motivational conviction. Pace briskly but clearly—30 seconds total. Sound authentic and trustworthy, not overly sales-y."
      }
    ]
  },
  "voiceName": "Puck",
  "languageCode": "en-US"
}
```

### Example 16: Educational Content

**Use Case:** Online course lesson

**Text:**
```
Welcome to Lesson 3: Understanding Functions in Python.

In programming, a function is like a recipe. You give it ingredients—we call those parameters—and it follows steps to create something new. That's your return value.

Let's look at a simple example:

def greet underscore user, name in parentheses, colon, return, quote, Hello, comma, quote, plus name.

When we call greet underscore user, quote, Alice, quote, the function receives Alice as the name parameter, combines it with our greeting, and returns, quote, Hello comma Alice, quote.

See how reusable this is? We can greet any user without rewriting code. That's the power of functions.

In the next video, we'll explore parameters in depth. See you there!
```

**Full Configuration:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are an patient, enthusiastic programming instructor teaching beginners. Speak clearly and deliberately, especially when explaining code concepts. Use friendly, encouraging tone that reduces intimidation. Pause briefly after technical terms to allow mental processing. When describing code, slow down slightly and enunciate syntax elements. End with warm invitation to continue learning. Sound like the supportive teacher everyone wishes they had."
      }
    ]
  },
  "voiceName": "Kore",
  "languageCode": "en-US"
}
```

### Example 17: Motivational Speech

**Use Case:** Corporate training, personal development

**Text:**
```
Let me tell you something about failure.

Every single person you admire—every entrepreneur, athlete, artist, leader—they've failed. Repeatedly. Often spectacularly.

J.K. Rowling was rejected by twelve publishers. Michael Jordan was cut from his high school basketball team. Steve Jobs was fired from his own company.

But here's what they understood that changed everything: failure isn't the opposite of success. It's part of success.

Every failure teaches. Every setback strengthens. Every mistake makes you wiser.

So the question isn't: will you fail? The question is: what will you do when you do?

Will you quit? Or will you learn, adapt, and come back stronger?

Your next great success might be waiting on the other side of your next failure.

Don't fear it. Embrace it. Because that's where growth lives.
```

**Full Configuration:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are delivering an inspiring motivational speech to a live audience. Start with bold confidence. Build energy progressively. Emphasize powerful statements with conviction. Use strategic pauses to let key ideas resonate. When listing examples, maintain rhythmic pacing. Crescendo to peak inspirational energy toward the end. Your voice should ignite motivation and belief. Sound like Tony Robbins meets Brené Brown—powerful but authentic."
      }
    ]
  },
  "voiceName": "Charon",
  "languageCode": "en-US"
}
```

### Example 18: Guided Workout

**Use Case:** Fitness app, workout video

**Text:**
```
Alright, let's do this! High knees—GO!

Drive those knees up! Pump your arms! You've got this!

Feel that energy! Feel that power! This is YOUR time!

Ten more seconds! Push through! Don't slow down now!

Five! Four! Three! Two! One!

And rest. Shake it out. Catch your breath.

Beautiful work. You just pushed yourself, and your body is thanking you for it.

Grab some water if you need it. When you're ready, we've got burpees next.

I know, I know—everyone's favorite! But remember: strong body, strong mind. You're building both right now.

Let's go!
```

**Full Configuration:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are an energetic fitness coach leading a high-intensity workout. Speak with maximum enthusiasm and encouragement during active sets—loud, motivating, rapid-fire energy. Use countdown with increasing intensity. During rest periods, lower energy to supportive and warm—give people a moment to breathe. Balance push with compassion. Sound like you genuinely believe in their potential. High energy but never annoying—authentically supportive."
      }
    ]
  },
  "voiceName": "Puck",
  "languageCode": "en-US"
}
```

### Example 19: Bedtime Story

**Use Case:** Children's content, sleep apps

**Text:**
```
Once upon a time, in a peaceful forest where the trees whispered gentle lullabies, there lived a small rabbit named Luna.

Every evening, as the sun painted the sky in soft shades of pink and gold, Luna would hop to her favorite spot by the stream.

She would sit very still... and listen.

Listen to the water bubbling softly over smooth stones. Listen to the wind rustling through leaves. Listen to the crickets beginning their evening song.

And as the stars began to appear, one by one, twinkling like tiny lanterns in the sky, Luna would close her eyes and make a wish.

She wished for peaceful dreams. For gentle sleep. For tomorrow to be as beautiful as today.

And then, with a happy sigh, Luna would hop home to her cozy burrow, curl up in her soft bed, and drift into the most wonderful dreams.

Just like you will soon.

Goodnight, little one. Sweet dreams.
```

**Full Configuration:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are reading a bedtime story to help a child fall asleep. Speak very softly and slowly with a warm, gentle tone. Use long, natural pauses that encourage relaxation. Each word should feel calm and soothing. Gradually slow your pace even more as the story progresses. End with a whispered, loving goodnight. Create a sleepy, peaceful atmosphere throughout. Think ASMR-style gentleness."
      }
    ]
  },
  "voiceName": "Fenrir",
  "languageCode": "en-US"
}
```

### Example 20: Comedy Podcast Intro

**Use Case:** Entertainment, comedy content

**Text:**
```
[upbeat energy] Hey hey HEY! Welcome to "Technically Speaking"—the podcast where we explain complicated tech stuff... badly!

I'm your host, Jamie, and boy oh boy, do we have a doozy for you today.

We're talking about blockchain. You know, that thing your uncle won't stop talking about at Thanksgiving? Yeah. THAT blockchain.

Now, I know what you're thinking: "Jamie, I've heard seventeen explanations of blockchain, and I still have no idea what it is."

SAME. Same, friend. Same.

But here's the difference: we're gonna explain it using only references to 90s boy bands and pizza. You're welcome.

Stick around—this is gonna get weird.
```

**Full Configuration:**
```json
{
  "systemInstruction": {
    "parts": [
      {
        "text": "You are hosting a comedic, irreverent podcast with high energy and personality. Speak casually and expressively with lots of vocal variety. Emphasize punchlines with timing. Sound genuinely amused by your own jokes. Use conversational rhythms with quick pace. Include slight exaggeration for comedic effect. Engaging and charismatic—make listeners feel like they're hanging out with a funny friend. Not afraid to be silly."
      }
    ]
  },
  "voiceName": "Puck",
  "languageCode": "en-US"
}
```

---

## Best Practices

### 1. Text Preparation

#### DO:
- ✅ Use natural punctuation for pacing (periods, commas, dashes)
- ✅ Write how you want it spoken (contractions, conversational flow)
- ✅ Break long paragraphs into shorter segments
- ✅ Use ellipses (...) for longer pauses
- ✅ Spell out numbers under ten; use digits for 10+
- ✅ Include pronunciation hints in parentheses if needed

#### DON'T:
- ❌ Write in all caps (except for emphasis sparingly)
- ❌ Over-use exclamation points!!!!
- ❌ Include stage directions like [pause] or *sighs* (use systemInstruction instead)
- ❌ Use complex nested sentences that are hard to parse
- ❌ Mix multiple topics without clear transitions

### 2. systemInstruction Crafting

#### DO:
- ✅ Be specific about role, tone, and context
- ✅ Mention target audience if relevant
- ✅ Specify pacing (slow, measured, energetic, etc.)
- ✅ Describe emotional journey if content has arc
- ✅ Reference real-world speaking styles ("like a TED talk," "like a friend giving advice")
- ✅ Include 2-4 key directives for best results

#### DON'T:
- ❌ Write overly long instructions (>100 words)
- ❌ Use conflicting directions ("enthusiastic but monotone")
- ❌ Specify phonetic details (that's the model's job)
- ❌ Include unrelated context or backstory
- ❌ Forget to consider the entire content when setting tone

### 3. Voice Selection

#### DO:
- ✅ Match voice characteristics to content type (see Voice Selection Matrix)
- ✅ Consider target audience age/demographic
- ✅ Test multiple voices for subjective preference
- ✅ Use the same voice for consistent brand identity
- ✅ Adjust systemInstruction to complement voice choice

#### DON'T:
- ❌ Choose solely based on gender/pitch preference
- ❌ Switch voices mid-project without strategic reason
- ❌ Ignore language-specific voice performance
- ❌ Assume one voice works for all content types

### 4. Multi-Voice Content

#### DO:
- ✅ Use clear, consistent speaker labels
- ✅ Describe each character's personality in systemInstruction
- ✅ Make dialogue distinct through word choice and rhythm
- ✅ Include minimal context tags (e.g., "[surprised]")
- ✅ Format with line breaks between speakers

#### DON'T:
- ❌ Have more than 4-5 distinct characters (gets muddy)
- ❌ Use ambiguous speaker labels ("Person A," "Speaker 1")
- ❌ Expect extreme vocal differentiation (it's subtle)
- ❌ Include lengthy action descriptions between dialogue

### 5. Iteration and Testing

#### DO:
- ✅ Generate multiple versions with slight systemInstruction variations
- ✅ Test with representative sample of your content first
- ✅ Listen on target playback device (phone, speaker, headphones)
- ✅ Get feedback from target audience
- ✅ Document what works for reuse

#### DON'T:
- ❌ Settle for first generation
- ❌ Test only on high-quality studio monitors
- ❌ Skip A/B testing different approaches
- ❌ Forget to save successful prompt patterns

### 6. Content Length Optimization

| Content Length | Recommended Model | Notes |
|---------------|-------------------|-------|
| < 100 words | Flash | Quick responses, real-time |
| 100-500 words | Flash | Most standard use cases |
| 500-2000 words | Pro | Better consistency |
| 2000+ words | Pro | Break into chunks if possible |

### 7. Quality Checklist

Before finalizing your audio:

- [ ] Emotional tone matches content intent
- [ ] Pacing is appropriate for content type
- [ ] Emphasis falls on correct words/phrases
- [ ] Multi-voice characters are distinguishable
- [ ] No awkward pauses or rushed sections
- [ ] Pronunciation is correct (especially names, technical terms)
- [ ] Overall energy level matches brand/context
- [ ] Ending doesn't sound abrupt or cut off

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Monotone or Flat Delivery

**Symptoms:** Audio sounds robotic or lacks emotional nuance

**Solutions:**
- ✅ Add more descriptive emotion words to systemInstruction
- ✅ Include personality details ("enthusiastic," "warm," "energetic")
- ✅ Vary sentence structure in text (questions, exclamations, statements)
- ✅ Try a more expressive voice (Aoede, Puck)
- ✅ Break text into shorter, more dynamic segments

**Before:**
```json
{
  "systemInstruction": {
    "parts": [{"text": "Read this professionally."}]
  }
}
```

**After:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "You are an enthusiastic teacher sharing exciting discoveries. Speak with genuine warmth and curiosity. Let your passion for the subject shine through naturally."
    }]
  }
}
```

#### Issue 2: Too Fast or Too Slow

**Symptoms:** Pacing doesn't match content needs

**Solutions:**
- ✅ Explicitly mention pacing in systemInstruction ("speak slowly," "measured pace," "energetic tempo")
- ✅ Adjust punctuation (more commas = more pauses)
- ✅ Break long sentences into shorter ones
- ✅ Use ellipses (...) for deliberate pauses
- ✅ Add words that naturally slow speech ("Now... let's consider...")

**Example:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Speak slowly and deliberately with strategic pauses. Aim for approximately 130 words per minute—slower than typical conversation to ensure comprehension."
    }]
  }
}
```

#### Issue 3: Incorrect Emphasis

**Symptoms:** Wrong words are emphasized, changing meaning

**Solutions:**
- ✅ Restructure sentences to naturally emphasize key words
- ✅ Use formatting (italics sometimes helps: *really* important)
- ✅ Specify what to emphasize in systemInstruction
- ✅ Add brief parenthetical hints: "the KEY insight here"
- ✅ Test different text variations

**Before:**
```
We need to increase sales revenue by next quarter.
```

**After:**
```
We need to increase sales revenue by NEXT quarter.
```

Or in systemInstruction:
```
"Emphasize temporal deadlines and specific targets."
```

#### Issue 4: Multi-Voice Characters Sound Too Similar

**Symptoms:** Can't distinguish between speakers in dialogue

**Solutions:**
- ✅ Provide distinct personality descriptions for each character
- ✅ Use contrasting speaking styles (formal vs casual, energetic vs calm)
- ✅ Give characters different speech patterns and vocabulary
- ✅ Limit to 2-3 main speakers for clarity
- ✅ Consider using Pro model (better differentiation)

**Example:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "This is a conversation between two distinct people. Alex is young, energetic, and speaks quickly with casual slang. Dr. Martinez is older, measured, formal, and speaks slowly with professional vocabulary. Make their vocal differences clear."
    }]
  }
}
```

#### Issue 5: Awkward Pauses or Rushed Sections

**Symptoms:** Unnatural breaks or sections that run together

**Solutions:**
- ✅ Review punctuation (periods vs commas vs dashes)
- ✅ Add paragraph breaks for natural pauses
- ✅ Use ellipses for intentional longer pauses
- ✅ Break run-on sentences into shorter segments
- ✅ Test with different text formatting

**Before:**
```
The results are clear we need to act now the data shows significant improvement is possible but only if we implement these changes immediately without delay starting next week.
```

**After:**
```
The results are clear. We need to act now.

The data shows significant improvement is possible—but only if we implement these changes immediately.

Starting next week.
```

#### Issue 6: Mispronunciation

**Symptoms:** Names, technical terms, or foreign words pronounced incorrectly

**Solutions:**
- ✅ Spell phonetically in parentheses: "Dr. Nguyen (NEW-win)"
- ✅ Use more common spelling if acceptable: "GitHub" vs "Git Hub"
- ✅ Add pronunciation guidance to systemInstruction
- ✅ Test variations: "SQL" vs "S-Q-L" vs "sequel"
- ✅ Consider respelling: "GIF" → "JIF" or "GHIF"

**Example:**
```
Meet our CTO, Xiomara (see-oh-MAR-ah) Chen (CHEN).
```

#### Issue 7: Inconsistent Quality in Long Content

**Symptoms:** Audio quality or style drifts in longer passages

**Solutions:**
- ✅ Use Pro model for content > 500 words
- ✅ Break very long content into logical chunks
- ✅ Maintain consistent systemInstruction throughout
- ✅ Ensure each section has clear context
- ✅ Test full audio end-to-end before finalizing

#### Issue 8: Ending Sounds Abrupt

**Symptoms:** Audio cuts off too quickly after final word

**Solutions:**
- ✅ Add a concluding sentence or phrase
- ✅ End with ellipses to extend final pause
- ✅ Include a natural closing ("That's all for today," "Thank you")
- ✅ Ensure final punctuation is a period (not comma)

**Before:**
```
...and that's how quantum computing will change cryptography
```

**After:**
```
...and that's how quantum computing will change cryptography forever.

Thank you for listening.
```

### Advanced Debugging

#### Test Systematically

1. **Isolate variables:** Change one element at a time (voice, systemInstruction, text)
2. **Create minimal examples:** Test with simple text first
3. **Compare models:** Try both Flash and Pro
4. **Document findings:** Keep notes on what works

#### A/B Testing Template

```
Version A:
- Voice: Kore
- systemInstruction: "Professional tone"
- Result: [Your observation]

Version B:
- Voice: Kore
- systemInstruction: "Professional broadcast journalist with authority and warmth"
- Result: [Your observation]

Winner: Version B
Reason: More engaging while maintaining professionalism
```

---

## Additional Resources

### Official Documentation

- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Audio Generation Guide](https://ai.google.dev/gemini-api/docs/audio)
- [API Reference](https://ai.google.dev/api/generate-content)

### Related Tools

- **curl-gemini-tts CLI:** Command-line tool for Gemini TTS (this project)
- **Gemini AI Studio:** Web interface for testing prompts
- **Google Cloud Speech:** Alternative TTS services

### Prompt Engineering Resources

- [Google AI Prompt Engineering Guide](https://ai.google.dev/gemini-api/docs/prompting-intro)
- [Best Practices for Generative AI](https://ai.google.dev/gemini-api/docs/best-practices)

### Community Examples

Check the [examples/](../examples/) directory for:
- Ready-to-use prompt templates
- Industry-specific examples
- Multi-voice conversation scripts
- Emotional range demonstrations

---

## Conclusion

Effective prompt engineering for Gemini TTS combines:

1. **Strategic voice selection** matched to content type and audience
2. **Descriptive systemInstruction** that sets tone, emotion, and style
3. **Well-formatted text** with natural punctuation and structure
4. **Iterative testing** to refine and optimize results

Remember:

- **Start simple:** Basic prompts work well for most use cases
- **Iterate:** Test variations to find what works best
- **Be specific:** Clear instructions yield better results
- **Match context:** Consider content type, audience, and delivery platform
- **Document success:** Save patterns that work for reuse

With these techniques, you can create professional, engaging audio content for any use case—from news delivery to character dialogue to meditation guides.

Happy prompting! 🎙️

---

**Document Version:** 1.0
**Last Updated:** 2025-11-03
**Maintained By:** curl-gemini-tts project
**Feedback:** Submit issues or suggestions via project repository
