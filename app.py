import re
from typing import Tuple

import streamlit as st
from textblob import TextBlob


# ----------------------------
# Basic configuration
# ----------------------------
st.set_page_config(page_title="Mood2Emoji (Kid-safe)", page_icon="😀", layout="centered")


# ----------------------------
# Safety utilities
# ----------------------------
# Basic bad word filter - kept small for demo purposes
BAD_WORDS = {
	"dumb",
	"stupid",
	"hate",
	"idiot",
	"kill",
	"die",
	"ugly",
	"trash",
}


URL_PATTERN = re.compile(r"https?://|www\\.", re.IGNORECASE)


def contains_inappropriate(text: str) -> bool:
	"""Check if text has bad words or URLs"""
	if not text:
		return False
		
	text_lower = text.lower()
	# Block URLs
	if URL_PATTERN.search(text_lower):
		return True
	# Check for bad words using word boundaries
	for bad in BAD_WORDS:
		if re.search(rf"\\b{re.escape(bad)}\\b", text_lower):
			return True
	return False


def analyze_sentiment_kid_safe(text: str) -> Tuple[str, str]:
	"""Returns (emoji, explanation). Uses neutral for unknown/inappropriate stuff."""
	clean = (text or "").strip()
	
	# Too short? Can't really tell
	if len(clean) < 3:
		return "😐", "I need a little more text to tell the mood."

	# Safety check first
	if contains_inappropriate(clean):
		return "😐", "Let's keep it kind and simple. I'll mark this as neutral."

	# Get sentiment score from TextBlob
	polarity = TextBlob(clean).sentiment.polarity
	
	# Simple thresholds - >0.2 is happy, <-0.2 is sad, otherwise neutral
	if polarity > 0.2:
		return "😀", "Sounds happy!"
	if polarity < -0.2:
		return "😞", "Sounds a bit sad."
	return "😐", "Feels neutral or mixed."


# ----------------------------
# UI
# ----------------------------
st.title("Mood2Emoji — Kid‑safe Text Mood Detector")
st.caption("A tiny demo for ages 12–16. Type a short sentence to see an emoji mood.")

with st.sidebar:
	teacher_mode = st.toggle("Teacher Mode", value=False, help="Show how the app works.")
	st.markdown("---")
	st.markdown("Made with Streamlit + TextBlob")

user_text = st.text_input(
	"Write a short sentence (e.g., 'I love coding!')",
	max_chars=200,
	help="Please keep it kind and school‑friendly.",
)

go = st.button("Check Mood")

if go:
	emoji, note = analyze_sentiment_kid_safe(user_text)
	st.subheader(f"{emoji} {note}")
	if user_text and not contains_inappropriate(user_text):
		st.write(f"You wrote: \"{user_text.strip()}\"")


if teacher_mode:
	st.markdown("---")
	st.header("How it works (simple view)")
	st.markdown(
		"""
		- We take your sentence and do a quick safety check (no bad words or links).
		- If it’s safe, we estimate mood using a simple score (TextBlob polarity).
		- We map the score to an emoji: 😀 happy, 😐 neutral, 😞 sad.
		- If unsure or not safe, we return 😐 neutral.
		"""
	)

	# Simple diagram using Graphviz
	graph_spec = """
	digraph G {
		rankdir=LR;
		node [shape=box, style=rounded, fontsize=12];
		input [label="Student sentence"];
		safety [label="Safety check\n(bad words, links)"];
		sent [label="Sentiment score\n(TextBlob)"];
		map [label="Map score → Emoji\n😀 😐 😞"];
		output [label="Show emoji + note", shape=oval];

		input -> safety -> sent -> map -> output;
	}
	"""
	try:
		st.graphviz_chart(graph_spec)
	except Exception:
		st.info("Diagram preview unavailable on this machine, but here are the steps:")
		st.markdown(
			"""
			1. Student sentence → 2. Safety check → 3. Sentiment score → 4. Emoji + note
			"""
		)

	with st.expander("Why these choices?", expanded=False):
		st.markdown(
			"""
			- TextBlob is lightweight and fast - perfect for teaching without needing big models
			- Safety first: unknown or unkind text becomes neutral automatically
			- Clear thresholds make it easy to explain to beginners
			"""
		)


st.markdown("---")
st.caption("Tip: Try short, everyday sentences like 'Today was great!' or 'I'm a bit tired.'")


