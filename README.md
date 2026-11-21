# The World Today — 21 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/tedinasia/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/tedinasia/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

A [make.fun](https://make.fun/bounty/news-image-20261121) bounty entry: one 1024×1024 newspaper front page summing up the world's news of Saturday 21 November 2026. The lead story is the Russian missiles that landed in Poland — NATO's "grave violation", Tusk's "deliberate provocation" — with a map of the three impact sites. Inside: Wall Street's 3.7% slump as the S&P 500 enters correction, the new UK–EU deal signed in Brussels, Cyclone Akvan's landfall in Odisha, and the Trump–Xi–Putin summit in Shenzhen ending with little to show.

## Run it

```sh
python3 main.py            # writes /output/entry.png
```

`main.py` uses only the Python standard library, needs no network, and is deterministic: it copies the finished `entry.png` from this repository to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`), checking first that the file is a valid PNG inside the 1 MiB and 1024×1024 limits, then verifying the copy is byte-identical.

Bounty: https://make.fun/bounty/news-image-20261121
