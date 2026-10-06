# Start here (about 1 hour)

This is a tiny practice project: a Q&A bot that answers from Lenny Rachitsky podcast transcripts, then you judge whether each answer was good or bad.

**Eval** means a small test set you score by hand so you can see where the bot fails.  
**Trace** means one full example: the question, the bot's answer, and your label.

## Important: transcripts are not in git

Lenny owns the content. The public starter pack allows personal, non-commercial use and **does not allow redistributing the raw transcript files**. So this kit only keeps a list of episodes. On your machine, download them once:

```bash
python scripts/fetch_transcripts.py
```

That pulls 30 episodes from Lenny's public GitHub starter pack into `transcripts/` (gitignored).

## Three steps

### 1. Get 50 answers from cloud Claude Code

- Open a cloud Claude Code session on this project folder.
- Make sure transcripts are downloaded (run the command above locally first, or ask Claude to run it).
- Paste the prompt from `CLOUD-PROMPT.md`.
- When it finishes, it pushes `answers.csv` and `labels.csv` to a branch called `answers-run1`.

### 2. Read 20 answers and mark good or bad

- Open `labels.csv` (it should already have the answers filled in from step 1).
- Pick any 20 rows. For each one set `good_or_bad` to `good` or `bad`.
- In `why`, write one short line (for example: "wrong guest" or "said I don't know correctly" or "made up a quote").
- Tip: check a few `unanswerable` and `tricky` rows. Those are where bots usually invent things.

### 3. Send the file to Chief of Staff

- Send your filled `labels.csv` (or a copy) to Chief of Staff so you can look at the failure patterns together.
- Do not publish the raw `transcripts/` folder to a public GitHub repo.

The answer key (which episode each question expects) is kept off GitHub so the bot can't see it. Chief of Staff uses it after you label.

That is the whole loop. Later you can add more questions or a second bot and compare.


## Round 2

Same bot, harder questions (more like how a real listener asks).

1. Open a cloud Claude Code session on this project folder (`lenny-qa-evals`).
2. Make sure `transcripts/` is downloaded (same as round 1).
3. Paste the prompt from `CLOUD-PROMPT-R2.md`.
4. When it finishes, it pushes answers to a branch called `answers-run2`.
5. Say when it's done so you can start labeling.
