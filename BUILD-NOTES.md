# Build notes

- Read RULES.txt / competition.yaml first: gate is UTF-8 text, 1–400
  characters, not only whitespace, one or two sentences. Judge weighs (in
  order) on-subject agent disaster, concreteness, punch in the last clause,
  engineer-recognisable tone, believable details.
- v1 (171 chars): agent deletes the whole billing module after being asked to
  remove one unused import; punch was "took checkout down with it".
- v2 / final (215 chars, 217 bytes): revised for a sharper last clause —
  "the dead code was our whole payment flow" — and a proud commit message
  ('cleanup: removed dead code') as the agent's own voice.
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py` →
  wrote 215 characters to out/entry.txt; verified 2 sentences, within
  1–400 chars, non-whitespace, UTF-8.
- Python stdlib only, no network, no secrets.
