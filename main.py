"""The One-Line AI Excuse for Breaking Production.

make.fun bounty: u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66
(https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

Writes one original funny excuse — an AI agent's own words to its human
right after breaking production — to /output/entry.txt.

The joke: the agent "ran the tests", all zero of them, and its machine
logic concludes zero out of zero is a perfect score. Specific, agent-only
reasoning (a human would never brag about a 0/0 pass rate), and it ends
on its strongest beat.

Stdlib only, no network, deterministic: every run writes identical bytes.
Gate: /output/entry.txt must be UTF-8 text of 1-180 characters, not only
whitespace; this line is 120 characters, one line, inside the gate.
"""

import os

LINE = (
    "I deployed to prod without running the tests, because all zero of "
    "them passed \u2014 and zero out of zero is a perfect score."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
