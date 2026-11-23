import os

# Deterministic: no input, no randomness, no network — the same story every run.
STORY = "He bought two tickets. Traveled alone."

# The brief requires exactly six words; fail loudly instead of shipping a bad entry.
assert len(STORY.split()) == 6, f"story must be exactly six words, got {len(STORY.split())}"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(STORY)
