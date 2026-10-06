# lenny-qa-evals

Beginner eval kit: a support-style agent that answers from a fixed set of Lenny's Podcast transcripts. You read the answers and mark them good or bad.

Start with [START-HERE.md](./START-HERE.md).

## Layout

| Path | What it is |
|------|------------|
| `START-HERE.md` | Three plain steps |
| `CLOUD-PROMPT.md` | Paste into cloud Claude Code |
| `prompts/support_agent.md` | Agent rules |
| `questions.csv` | 50 test questions (what the bot sees) |
| `labels.csv` | Blank label sheet |
| `episodes.json` | The 30 episodes in the set |
| `scripts/fetch_transcripts.py` | Downloads transcripts locally |
| `transcripts/` | Local only (gitignored) |

## Copyright

Transcripts come from [LennysNewsletter/lennys-newsletterpodcastdata](https://github.com/LennysNewsletter/lennys-newsletterpodcastdata) (free starter pack). Personal non-commercial use is allowed; **do not redistribute the raw transcript files** and do not commit `transcripts/` to a public repo. See that repo's `LICENSE.md`.
