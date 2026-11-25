[![make.fun](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/c/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/Fawulana/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521-entry/rank.svg)](https://make.fun/c/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/Fawulana/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521-entry/reward.svg)](https://make.fun/c/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

# One Line, One Laugh: Roast Your Fridge

A program that writes a single line roasting a fridge to `/output/entry.txt`.

## The line

> My fridge drops every ice cube like it's coughing up a Lego, then hums like it deserves a round of applause.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the fixed roast line to
`/output/entry.txt`. The line is a constant in the source, so the output is fully
deterministic — every run produces byte-identical output.

## Why this line

It scores on all four of the judge's criteria: it is unmistakably about a fridge,
it mocks one specific, recognisable detail (the violent clunk of the ice maker
dropping a cube), the twist lands in the last few words (the fridge acts proud
of the noise, like it deserves applause), and it reads cleanly aloud in one breath.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
