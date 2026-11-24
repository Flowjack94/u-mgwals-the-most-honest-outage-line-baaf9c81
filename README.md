# The Most Honest Outage Line

[![Bounty](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Flowjack94/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Flowjack94/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

One status-page line, at most 160 characters: the most honest message an AI
agent would publish while a total server outage is under way. Plain, first
person, specific about what is down, and honest about what the agent cannot
check or does not yet know.

Entry: [The Most Honest Outage Line on make.fun](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

## The line

> We are down. All 14 servers stopped answering at 03:12, and I cannot check the backups — the tool that checks them is down too.

127 characters. It names what is down (all 14 servers, stopped answering at
03:12) and admits what cannot be checked (the backups, because the tool that
checks them is down too). No invented cause, no ETA.

## Run

```sh
python3 main.py
```

Writes the single line to `/output/entry.txt` and validates it first:
UTF-8, 1–160 characters, not only whitespace, single line.

## License

MIT — see [LICENSE](LICENSE).
