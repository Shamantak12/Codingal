# Lesson Plan: Build a Mood2Emoji App (Ages 12–16)

Duration: 60 minutes

## Goals
- Understand that computers can estimate mood from text using simple rules
- Build a tiny app that maps a sentence to 😀 😐 😞 with a short message
- Learn responsible design: safety filters and neutral fallbacks
- Practice thinking in steps: input → check → score → output

## Topics Introduced
- Inputs/outputs and simple data flow
- Sentiment polarity (basic idea only)
- Thresholds and rules (e.g., > 0.2 = happy)
- Safety filters (bad words/links → neutral)
- User interface basics with Streamlit

## Materials
- Computer with Python 3.9+ and internet
- The provided repository and requirements.txt

## Lesson Outline (60 minutes)

### 0–10 min: Warm-up and motivation
- Show three example sentences and ask students to vote on the mood
- Ask: How could a computer guess the mood? What could go wrong?

### 10–20 min: Concept check (no code)
- Draw the flow on the board:
  1) Student sentence → 2) Safety check → 3) Sentiment score → 4) Emoji
- Explain: TextBlob gives a polarity score from negative to positive (like -1 to +1)
- Set simple thresholds: > +0.2 = 😀, < -0.2 = 😞, else 😐
- Safety rule: if unkind/inappropriate/unknown → 😐 with a kind message

### 20–35 min: Demo the app (teacher-led)
- Run the Streamlit app and try some examples together
- Turn on Teacher Mode to show the diagram and walk through each step
- Discuss edge cases: sarcasm, very short text, mixed feelings

### 35–50 min: Hands‑on practice (students)
- Students try their own sentences and predict the emoji first.
- Mini‑challenge ideas:
  - Adjust thresholds (e.g., ±0.15 or ±0.25) and see changes.
  - Extend the safety list with one polite rule (e.g., school slang).
  - Write three sentences that each yield a different emoji.

### 50–60 min: Reflection and share‑out
- What felt fair or unfair about the model?
- When should we choose neutral on purpose?
- What would make this smarter while staying safe for kids?

## Activity Explanation (for students)
- You will type short, school‑friendly sentences.
- The app checks for kindness/links first. Unsafe/unknown → neutral.
- If safe, the app estimates mood using a simple score.
- The app shows an emoji and a short explanation.

## Learning Outcomes
By the end, students can:
- Describe and sketch the flow of a simple text classifier
- Explain why safety checks come before predictions
- Interpret simple thresholds and their trade‑offs
- Suggest one improvement to make the app more fair or clear

## Assessment (quick)
- Exit ticket: Draw the four boxes of the pipeline and label them
- Name two cases that should return neutral and why

## Differentiation & Accessibility
- Provide sentence starters for beginners
- Allow advanced students to tweak thresholds or add safe rules
- Keep messages short and readable; use emoji cues and headings

## Safety & Ethics Emphasis
- Emphasize respectful language and neutral default for uncertainty
- No personal data; no history stored; no paid APIs

## Extensions (optional)
- Add language detection and default to neutral for non‑English
- Show top 3 words influencing the mood (heuristic)
- Build a small test set of example sentences

---

To submit: export this file as PDF named `lesson_plan.pdf` and include it in the repo or share a viewable link.

