import os

# Deterministic: no input, no randomness, no network — the same story every run.
STORY = "He bought two tickets. Traveled alone."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(STORY)
