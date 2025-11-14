# Advanced Multi-Voice Techniques for Gemini TTS

Comprehensive guide for creating compelling multi-speaker audio content with Gemini 2.5 TTS models.

## Table of Contents

1. [Multi-Voice Fundamentals](#multi-voice-fundamentals)
2. [Speaker Differentiation Techniques](#speaker-differentiation-techniques)
3. [Dialogue Formatting Best Practices](#dialogue-formatting-best-practices)
4. [Emotional Arcs in Conversations](#emotional-arcs-in-conversations)
5. [Complex Scene Construction](#complex-scene-construction)
6. [Common Pitfalls and Solutions](#common-pitfalls-and-solutions)
7. [Complete Multi-Voice Examples](#complete-multi-voice-examples)

---

## Multi-Voice Fundamentals

### How Gemini TTS Handles Multiple Voices

Gemini TTS uses contextual understanding to create vocal distinctions between speakers based on:

1. **Speaker labels** (e.g., "Host:", "Guest:")
2. **Character descriptions** in systemInstruction
3. **Dialogue content and word choice**
4. **Context clues** (emotion tags, action descriptions)

**Important:** Unlike traditional multi-voice TTS that assigns different models to different speakers, Gemini synthesizes all voices in a single pass, creating subtle but perceptible differences through contextual modulation.

### Capabilities and Limitations

**What Works Well:**
- ✅ 2-3 distinct speakers with clear personality differences
- ✅ Conversational dialogue (interviews, discussions)
- ✅ Emotional variation between characters
- ✅ Maintaining speaker consistency throughout dialogue
- ✅ Natural turn-taking and conversational flow

**Limitations:**
- ⚠️ More than 4 speakers becomes difficult to distinguish
- ⚠️ Extreme vocal differences (child vs adult) less effective than moderate differences
- ⚠️ Requires well-structured text formatting
- ⚠️ Same language across all speakers (no multilingual mixing in single synthesis)

### Model Selection for Multi-Voice

| Scenario | Recommended Model | Reason |
|----------|------------------|--------|
| Simple dialogue (2 speakers) | Flash | Fast, sufficient quality |
| Complex conversation (3+ speakers) | Pro | Better speaker distinction |
| Emotional character scenes | Pro | Subtle vocal nuance |
| Long-form dialogue (>1000 words) | Pro | Better consistency |
| Real-time applications | Flash | Lower latency |

---

## Speaker Differentiation Techniques

### 1. Personality-Based Differentiation

Create distinct speakers through personality traits that naturally affect speech patterns.

**Example systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "This is a conversation between Alex and Jordan. Alex is confident and energetic—speaks quickly with enthusiasm and uses expressive language. Jordan is thoughtful and measured—speaks slowly with careful word choice and reflective pauses. Make their contrasting personalities clear through vocal delivery."
    }]
  }
}
```

**Character Dimensions to Vary:**

| Dimension | Energetic Character | Calm Character |
|-----------|-------------------|----------------|
| Speed | Fast, rapid-fire | Slow, deliberate |
| Energy | High, animated | Low, measured |
| Pitch variation | Wide range | Narrow range |
| Pauses | Brief, minimal | Long, contemplative |
| Vocabulary | Casual, colorful | Formal, precise |

### 2. Role-Based Differentiation

Leverage professional or social roles to create natural distinctions.

**Examples:**

**Teacher vs Student:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Dialogue between Teacher and Student. Teacher speaks with patient authority and clarity—explaining concepts slowly. Student speaks with curiosity and occasional uncertainty—asking questions with genuine interest. Differentiate through confidence levels and pacing."
    }]
  }
}
```

**CEO vs Reporter:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Interview between CEO and Reporter. CEO speaks with polished professionalism—measured, strategic responses. Reporter speaks with journalistic directness—crisp questions with investigative tone. Show power dynamic through vocal confidence."
    }]
  }
}
```

**Doctor vs Patient:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Medical consultation. Doctor speaks with calm expertise and reassurance. Patient speaks with concern and questions—voice reflects anxiety diminishing to relief as conversation progresses. Show emotional journey clearly."
    }]
  }
}
```

### 3. Age-Based Differentiation

While extreme age differences (child vs elder) are less effective, moderate age distinctions work well.

**Young Professional vs Senior Executive:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Business meeting between Junior Analyst (mid-20s, eager, slightly nervous, speaks quickly) and Senior VP (50s, seasoned, calm authority, speaks deliberately). Age difference should come through confidence level and speech patterns, not pitch alone."
    }]
  }
}
```

### 4. Emotional State Differentiation

Use contrasting emotional states to create immediate distinction.

**Optimist vs Pessimist:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Debate between Optimist and Pessimist. Optimist speaks with hopeful energy and enthusiasm. Pessimist speaks with skeptical caution and concern. Make worldview differences clear through vocal tone."
    }]
  }
}
```

### 5. Cultural/Regional Markers (within same language)

Reference speaking style characteristics without attempting accents.

**Examples:**
```
"Speaker A has New York directness—fast, to-the-point, energetic."
"Speaker B has Southern warmth—slower, more measured, hospitable."
```

**Note:** Avoid requesting specific accents ("British accent," "Australian accent"). Instead, describe speaking style traits.

---

## Dialogue Formatting Best Practices

### Standard Format

```
Speaker Name: Dialogue text.

Different Speaker: Response text.

Speaker Name: Follow-up text.
```

**Key Rules:**
- Use consistent speaker labels throughout
- Include line break between speakers
- Maintain consistent punctuation style
- Use colon after speaker name

### Enhanced Format with Context

Add minimal context tags for clarity:

```
Alex [excited]: I can't believe we actually did it!

Jordan [cautious]: Let's not celebrate too early. We still need approval.

Alex [reassuring]: Come on, the data speaks for itself!
```

**Context Tags:**
- Keep brief (1-2 words)
- Use brackets or parentheses
- Focus on emotion or manner
- Don't overuse (2-3 per conversation)

### Handling Interruptions and Overlap

```
Speaker A: I think we should consider—

Speaker B [interrupting]: Wait, before you continue, did you see the latest numbers?

Speaker A: Actually, yes, that's exactly what I was about to—

Speaker B: Sorry, go ahead.

Speaker A: Thanks. As I was saying, the numbers suggest we're on the right track.
```

**Techniques:**
- Use em-dash (—) for interrupted speech
- Add [interrupting] tag for clarity
- Show natural conversational flow
- Include acknowledgment of interruption

### Action Beats Between Dialogue

Minimal action descriptions can enhance delivery:

```
Host: Welcome back to the show!

[pause]

Guest: Thanks for having me.

Host [laughing]: We're thrilled you're here.
```

**Guidelines:**
- Use sparingly
- Keep to basic actions: [pause], [laughing], [sighs]
- Bracket format to distinguish from dialogue
- Don't include lengthy stage directions

---

## Emotional Arcs in Conversations

### Technique: Progressive Emotional Shift

Guide speakers through emotional journeys within single conversation.

**Example: Customer Frustration → Resolution**

**Text:**
```
Customer [frustrated]: I've been trying to reach someone for two hours! This is completely unacceptable!

Agent [calm, empathetic]: I completely understand your frustration, and I sincerely apologize for the wait. Let me help you right now.

Customer [still upset]: Well, I hope so. I've wasted my entire morning on this!

Agent [reassuring]: I'm going to make sure we resolve this quickly. Can you tell me what's happening?

Customer [calming slightly]: It's my account. I can't access it, and I have an important payment due today.

Agent [confident]: I see the issue here, and I can fix this immediately. Give me just one moment.

Customer [hopeful]: Really? You can fix it now?

Agent: Yes, absolutely. Unlocking your account right now... done. Try logging in.

Customer [relieved]: Oh! It worked! Thank you so much!

Agent [warm]: You're very welcome. I'm glad we could resolve this for you today.
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Customer service call with clear emotional progression. Customer starts very frustrated and angry—sharp tone, fast pace. Gradually shift to cautious hope, then relief and gratitude—softer tone, slower pace. Agent remains consistently calm and professional throughout—reassuring and empathetic. Show Customer's emotional journey clearly through vocal changes."
    }]
  }
}
```

### Technique: Mirrored Energy

Speakers influence each other's energy levels.

**Example: Building Excitement Together**

```
Host: So tell us about this breakthrough!

Scientist [starting calm]: Well, we've been working on this for five years—

Host [enthusiastic]: Five years! That's incredible dedication!

Scientist [warming up]: Yes! And just last month, everything finally clicked.

Host [excited]: What happened?

Scientist [now enthusiastic too]: We ran the simulation, and—I still get chills thinking about it—the results were beyond what we'd hoped for!

Host [thrilled]: This is amazing!

Scientist [matching enthusiasm]: It really is! This could change everything!
```

**systemInstruction:**
```
"Podcast interview where enthusiasm is contagious. Scientist starts calm and measured but catches Host's energy—progressively becoming more animated. Host consistently enthusiastic—drawing Scientist out. Show energy building between them naturally."
```

### Technique: Contrasting Emotional Responses

Same situation, different reactions.

**Example: Risk Assessment Discussion**

```
Optimist: This is our big opportunity! We have to take this chance!

Realist [measured]: Let's look at the data first. What's the actual success rate?

Optimist [impassioned]: Sometimes you have to take risks! The potential is enormous!

Realist [analytical]: The potential loss is also enormous. I'm seeing a 40% failure rate here.

Optimist [insistent]: But a 60% success rate! That's better than half!

Realist [firm]: With $2 million at stake, I need better than "better than half."
```

**systemInstruction:**
```
"Business meeting debate. Optimist speaks with passion and conviction—faster pace, higher energy. Realist speaks with calm analysis—slower pace, deliberate tone. Maintain contrast throughout—emotional vs analytical approaches to same problem."
```

---

## Complex Scene Construction

### Multi-Character Scenes (3+ Speakers)

**Best Practices:**
1. Limit to 3-4 speakers maximum
2. Give each distinct personality
3. Have clear "primary" and "secondary" characters
4. Use speaker variety for different roles

**Example: Podcast with Two Hosts and Guest**

**Text:**
```
Sarah [enthusiastic]: Welcome to Tech Talk! I'm Sarah—

Mike [equally enthusiastic]: And I'm Mike! Today we have an incredible guest!

Sarah: Dr. Chen, thanks for joining us!

Dr. Chen [warm but professional]: Thanks for having me. Happy to be here.

Mike: So, Dr. Chen, explain quantum computing like we're five years old.

Dr. Chen [chuckling]: Okay! Imagine a maze...

Sarah [interjecting]: I love this already!

Dr. Chen [continuing]: A regular computer tries one path at a time. A quantum computer? Tries them all at once.

Mike [amazed]: Whoa.

Sarah: That's... that's actually brilliant!

Dr. Chen: Right? It's like having infinite versions of yourself exploring simultaneously.

Mike: My mind is officially blown.
```

**systemInstruction:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Podcast with three distinct voices. Sarah: energetic, curious, frequently interjects—fast pace, high energy. Mike: enthusiastic but slightly more laid-back than Sarah—conversational warmth. Dr. Chen: knowledgeable but approachable—explains clearly with occasional humor, more measured than hosts. Create clear distinction: Sarah fastest/highest energy, Mike moderate, Dr. Chen most measured."
    }]
  }
}
```

### Nested Dialogue (Story within Story)

When characters tell stories containing other dialogue:

**Format:**
```
Narrator: She told me what happened that night.

Character (recounting): I walked up to him and said, "We need to talk." And he just looked at me and replied, "Not now." Can you believe that?

Narrator: I could see she was still upset about it.
```

**systemInstruction Tips:**
- Clearly differentiate narrator from characters
- Use "recounting" or "remembering" tags for embedded dialogue
- Keep embedded dialogue brief

### Group Conversations with Dynamics

**Example: Team Meeting with Power Dynamics**

```
Manager: Let's hear everyone's thoughts. Alex, what do you think?

Alex [confident]: I think we should move forward. The data supports it.

Manager: Good. Jordan?

Jordan [hesitant]: I... I have some concerns about the timeline.

Alex [dismissive]: The timeline is fine.

Manager [firm]: Let Jordan finish.

Jordan [more confident now]: Thank you. My concern is that we're underestimating implementation complexity.

Manager [thoughtful]: That's a valid point. Let's discuss this.
```

**systemInstruction:**
```
"Meeting with clear hierarchy. Manager speaks with authority and control—decisive. Alex speaks confidently, sometimes interrupting—eager to impress. Jordan starts hesitant but gains confidence when supported—shows growth. Demonstrate power dynamics through vocal confidence and interruption patterns."
```

---

## Common Pitfalls and Solutions

### Pitfall 1: Speakers Sound Too Similar

**Symptoms:**
- Can't distinguish who's speaking
- All dialogue has same energy
- Personalities don't come through

**Solutions:**
- ✅ Increase personality contrast in systemInstruction
- ✅ Vary speaking pace more dramatically
- ✅ Give speakers contrasting emotional states
- ✅ Use role-based differences (professional vs casual)
- ✅ Add more context tags
- ✅ Switch to Pro model for better differentiation

**Before:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Conversation between two people."
    }]
  }
}
```

**After:**
```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Conversation between two contrasting personalities. Alex is energetic and rapid-fire—speaks quickly with enthusiasm. Morgan is contemplative and measured—speaks slowly with thoughtful pauses. Make their different approaches to communication obvious through pacing and energy."
    }]
  }
}
```

### Pitfall 2: Inconsistent Speaker Characteristics

**Symptoms:**
- Speaker sounds different in different parts
- Personality traits fade mid-conversation
- Energy levels fluctuate randomly

**Solutions:**
- ✅ Keep systemInstruction focused on key traits
- ✅ Reinforce characteristics periodically in text
- ✅ Use Pro model for longer dialogues
- ✅ Break very long conversations into consistent chunks
- ✅ Maintain consistent speaker labels

### Pitfall 3: Over-Complicated Formatting

**Symptoms:**
- Lengthy action descriptions confuse synthesis
- Too many context tags
- Unclear who is speaking

**Solutions:**
- ✅ Simplify to essential speaker labels
- ✅ Remove lengthy stage directions
- ✅ Use minimal, brief context tags
- ✅ Let dialogue and systemInstruction carry emotion
- ✅ Format consistently

**Too Complex:**
```
[Sarah, speaking with rising anxiety and fidgeting with her coffee cup, looks directly at Mark before speaking in a hushed, urgent whisper]: We need to leave. Now.
```

**Better:**
```
Sarah [urgent whisper]: We need to leave. Now.
```

### Pitfall 4: Unclear Turn-Taking

**Symptoms:**
- Dialogue runs together
- Hard to tell when speakers change
- Loss of conversational rhythm

**Solutions:**
- ✅ Always use line breaks between speakers
- ✅ Maintain consistent speaker labels
- ✅ Use proper punctuation (periods, not commas between speakers)
- ✅ Include brief pauses for natural turn-taking

**Unclear:**
```
Alex: What do you think? Jordan: I'm not sure. Alex: Come on, you must have an opinion.
```

**Clear:**
```
Alex: What do you think?

Jordan: I'm not sure.

Alex: Come on, you must have an opinion.
```

### Pitfall 5: Too Many Speakers

**Symptoms:**
- More than 4 speakers become indistinguishable
- Listener confusion about who's speaking
- Decreased audio quality

**Solutions:**
- ✅ Limit to 3-4 speakers maximum
- ✅ Have 1-2 primary speakers and others as brief participants
- ✅ Use clear role distinctions ("Moderator:", "Panelist 1:", etc.)
- ✅ Consider breaking into multiple audio files if more speakers needed

---

## Complete Multi-Voice Examples

### Example 1: Technical Interview (2 Speakers)

**Use Case:** Software engineering podcast

**Full Implementation:**

```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Technical podcast interview. Host is enthusiastic and curious—asks questions with genuine interest, conversational warmth. Engineer is knowledgeable but approachable—explains clearly without jargon, thoughtful and measured. Host faster and more animated; Engineer more deliberate and explanatory."
    }]
  },
  "voiceName": "Zephyr",
  "languageCode": "en-US"
}
```

**Text:**
```
Host: Welcome back to Code & Coffee! Today I'm talking with Jamie Chen, a senior engineer at DataFlow. Jamie, thanks for being here!

Jamie: Thanks for having me! Excited to chat.

Host: So, let's dive right in. You recently led the migration of your entire infrastructure to Kubernetes. That sounds... terrifying?

Jamie [laughing]: It was! But also incredibly rewarding. Let me break down how we approached it.

Host: Please do! Our listeners are definitely interested.

Jamie: The key was incremental migration. We didn't try to move everything at once. Instead, we started with our least critical services first.

Host: Oh, that's smart! So you could test without major risk.

Jamie: Exactly. We learned a lot from those initial migrations—mistakes we could afford to make with low-stakes services.

Host: What was the biggest lesson?

Jamie [thoughtful pause]: Honestly? The importance of observability. You need to know what's happening in your cluster at all times. We invested heavily in monitoring before migrating critical services.

Host: That makes sense. What about developer buy-in? Did your team resist the change?

Jamie: Some did initially. Change is hard. But we ran training sessions, created comprehensive documentation, and most importantly, we listened to concerns.

Host: And it paid off?

Jamie: Absolutely. Now the team loves it. Deployments are faster, scaling is automated, and developers have more control over their services.

Host: Jamie, this has been fantastic. Where can people learn more about your work?

Jamie: Check out our engineering blog at dataflow.tech/blog. We've documented the entire migration journey.

Host: Perfect! Thanks again for sharing your insights!

Jamie: My pleasure!
```

### Example 2: Customer Support Call (2 Speakers with Emotional Arc)

**Use Case:** Training material for support teams

**Full Implementation:**

```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Customer support call demonstrating emotional de-escalation. Customer starts very frustrated—sharp tone, fast speech, elevated stress. Gradually calms to relief and gratitude—softer tone, slower pace. Agent maintains calm professionalism throughout—empathetic, reassuring, patient. Show customer's emotional journey clearly while agent remains steady anchor."
    }]
  },
  "voiceName": "Kore",
  "languageCode": "en-US"
}
```

**Text:**
```
Agent: Thank you for calling TechSupport Plus. My name is Alex. How can I help you today?

Customer [frustrated]: Finally! I've been on hold for twenty minutes! My entire system is down, and I have a presentation in two hours!

Agent [calm, empathetic]: I completely understand how stressful that must be, and I apologize for the wait. Let's get your system back up right away. Can you tell me what's happening?

Customer [still upset]: The application won't even open! I click it, and nothing happens. I've tried restarting three times!

Agent [reassuring]: Okay, that does sound frustrating. I see your account here, and I have a few ideas. Are you on Windows or Mac?

Customer: Windows. Please tell me you can fix this quickly.

Agent [confident]: I'm going to walk you through a solution that should resolve this. First, let's check if the application service is running. Can you open Task Manager for me?

Customer [slightly calmer]: Okay, it's open.

Agent: Perfect. Click on the Services tab and look for "TechApp Service." Is it there?

Customer: Yes... it says "Stopped."

Agent: That's exactly what I suspected. Right-click on it and select "Start."

Customer [pause]: Okay... it's starting...

Agent: Now try opening the application.

Customer [relieved]: It's opening! Oh thank goodness!

Agent [warm]: Excellent! I'm so glad that worked. Your presentation is saved.

Customer [grateful]: Thank you so much. I'm sorry I was frustrated earlier.

Agent: No apology needed. I completely understand. Glad I could help. Is there anything else I can assist you with?

Customer: No, that was it. You're a lifesaver!

Agent: Happy to help! Good luck with your presentation!
```

### Example 3: Narrative Fiction with Multiple Characters (3 Speakers)

**Use Case:** Audiobook excerpt

**Full Implementation:**

```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Fiction audiobook with narrator and two distinct characters. Narrator: warm, engaging storytelling voice with measured pacing. Detective Reeves: serious, authoritative, lower register—speaks deliberately with professional gravitas. Witness Sarah: nervous, higher pitch, faster speech—voice trembles slightly with anxiety. Make clear distinction between all three voices while maintaining narrative flow."
    }]
  },
  "voiceName": "Aoede",
  "languageCode": "en-US"
}
```

**Text:**
```
Narrator: Detective Reeves entered the interrogation room at exactly 9 PM. The witness, Sarah Martinez, sat at the metal table, her hands clasped tightly together.

Detective Reeves [serious]: Ms. Martinez. Thank you for coming in. I know this isn't easy.

Sarah [nervous]: I... I want to help. I just don't know if I saw anything useful.

Narrator: The detective pulled out a worn notebook and clicked his pen.

Detective Reeves: Why don't you tell me what you remember? Start from the beginning.

Sarah [trembling]: I was walking home from the store. It was around seven. I heard shouting from the building.

Detective Reeves [gentle but probing]: What kind of shouting? Could you make out words?

Sarah: Someone yelled, "Don't!" or maybe "Stop!" I couldn't tell. It was muffled.

Narrator: She paused, her eyes distant, reliving the moment.

Sarah [quiet]: Then I heard the crash. Glass breaking. And then... silence.

Detective Reeves: Did you see anyone leaving the building?

Sarah [hesitant]: Maybe. There was a car. Dark sedan. It drove away fast.

Detective Reeves: License plate?

Sarah [regretful]: I didn't think to look. I'm sorry.

Detective Reeves [reassuring]: You're doing fine. Every detail helps. What happened next?

Narrator: Sarah took a deep breath, gathering courage.

Sarah [stronger now]: I called 911. Then I waited until the police arrived.

Detective Reeves: That was exactly the right thing to do. Ms. Martinez, you may have saved someone's life tonight.
```

### Example 4: Business Negotiation (2 Speakers with Power Dynamic)

**Use Case:** MBA case study, training material

**Full Implementation:**

```json
{
  "systemInstruction": {
    "parts": [{
      "text": "Business negotiation between Buyer and Seller. Buyer speaks with confident assertiveness—direct, slightly aggressive, controlled. Seller speaks with diplomatic professionalism—measured, strategic, carefully choosing words. Show power dynamic through vocal confidence and pacing. Buyer slightly faster and more forceful; Seller more deliberate and tactical."
    }]
  },
  "voiceName": "Charon",
  "languageCode": "en-US"
}
```

**Text:**
```
Buyer: Let's get to the point. Your asking price is 30% above market value.

Seller [calm]: I appreciate your directness. However, our valuation accounts for proprietary technology and established client relationships.

Buyer: Technology that's three years old. And clients you'll lose if you don't have capital to serve them properly.

Seller [unfazed]: Our technology has been continuously updated. As for capital, we have multiple interested parties.

Buyer [skeptical]: Do you? Because I've heard otherwise.

Seller [measured pause]: What I can tell you is that you're sitting at this table because you recognize the strategic value we bring.

Buyer: The value I recognize is opportunity—for me. You need a buyer more than I need to buy.

Seller [slight edge]: We need the right buyer. There's a difference.

Buyer: Fine. Here's my offer: 20 million. Final.

Seller [pause, then]: That's interesting. Let me counter: 32 million, and I'll include our development team for two years.

Buyer [considering]: The team is valuable. But the price needs to be 25 million.

Seller: 28 million, and we have a deal.

Buyer [pause]: 27 million. Not a dollar more.

Seller [slight smile in voice]: Deal.
```

---

## Testing and Iteration for Multi-Voice

### A/B Testing Framework

Test variations systematically:

```
Test: Customer Service Dialogue
Base Text: [same script]

Version A:
- systemInstruction: "Basic customer service tone"
- Result: Speakers too similar

Version B:
- systemInstruction: "Customer frustrated, agent calm"
- Result: Better distinction but emotional arc unclear

Version C:
- systemInstruction: "Customer progresses from frustrated to relieved. Agent calm throughout."
- Result: ✅ WINNER - Clear emotional journey and distinction

Winner: Version C
Key Learning: Specify emotional progression for better character arc
```

### Evaluation Criteria

Rate each synthesis on:

- [ ] Can you distinguish speakers without labels?
- [ ] Do personalities match systemInstruction intent?
- [ ] Does emotional arc progress naturally?
- [ ] Is pacing appropriate for each speaker?
- [ ] Do speakers maintain consistency throughout?
- [ ] Does dialogue sound natural and conversational?
- [ ] Are interruptions and overlaps handled well?

---

## Advanced Tips

1. **Use Pro Model for Complex Scenes:** When you have 3+ characters or subtle emotional work, Pro model delivers better results

2. **Front-Load Character Descriptions:** Put most important character traits early in systemInstruction

3. **Test Short Samples First:** Generate 30-second samples before committing to full-length dialogues

4. **Document What Works:** Save successful systemInstruction patterns for reuse

5. **Consider Audio Editing:** For critical productions, small adjustments in post-production can enhance voice distinctions

6. **Limit Extreme Contrasts:** Moderate personality differences work better than extreme opposites

7. **Use Dialogue to Reinforce Character:** Let word choice and sentence structure reflect personality

8. **Strategic Use of Context Tags:** One well-placed emotion tag can guide entire scene delivery

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Companion Guides:** voice-and-style-guide.md, quick-reference-templates.md
