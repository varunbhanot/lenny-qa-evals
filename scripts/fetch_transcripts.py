#!/usr/bin/env python3
"""Download the 30 starter-pack episodes used by this eval kit.

Source: https://github.com/LennysNewsletter/lennys-newsletterpodcastdata
License: personal, non-commercial use OK. Do NOT redistribute the raw files
(see that repo's LICENSE.md). Keep transcripts/ gitignored.
"""
from __future__ import annotations

import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EPISODES = ROOT / "episodes.json"
OUT = ROOT / "transcripts"
BASE = "https://raw.githubusercontent.com/LennysNewsletter/lennys-newsletterpodcastdata/main/podcasts"

def main() -> None:
    eps = json.loads(EPISODES.read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    for ep in eps:
        name = ep["file"]
        url = f"{BASE}/{name}"
        dest = OUT / name
        print(f"fetch {name}")
        with urllib.request.urlopen(url) as r:
            body = r.read().decode("utf-8")
        header = (
            f"EPISODE_FILE: {name}\n"
            f"GUEST: {ep['guest']}\n"
            f"TITLE: {ep['title']}\n"
            f"DATE: {ep.get('date', '')}\n"
            f"POST_URL: {ep.get('post_url', '')}\n\n"
        )
        dest.write_text(header + body)
    print(f"Done. {len(eps)} files in {OUT}")

if __name__ == "__main__":
    main()
