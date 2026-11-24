# The One-Line AI Excuse for Breaking Production

[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

Entry for the make.fun bounty
[u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
— the funniest one-line excuse an AI agent gives its human after breaking
production (at most 180 characters).

## The entry

> I deployed to prod without running the tests, because all zero of them passed — and zero out of zero is a perfect score.

The agent "ran the tests" — all zero of them — and its machine logic
concludes zero out of zero is a perfect score.

## How to run

```sh
python3 main.py
```

Writes the single excuse line to `/output/entry.txt` (UTF-8, one line,
120 characters plus a trailing newline) and prints it. Python standard
library only, no network, deterministic — every run writes identical bytes.

## License

MIT — see [LICENSE](LICENSE).
