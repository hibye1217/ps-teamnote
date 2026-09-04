# TeamNote
My version of the teamnote. Use at your own risk, because god this code is terrible

Also we assume `#include <bits/stdc++.h>` and `using namespace std` for every code.

## Build
Edit the `teamnote_option.sty`'s variables as you like. My personal choices for the variables are:
- `TrustedOnly`: `false` as the untrusted parts are already notated so I can ignore it myself.
- `ShowIndicator`: `true` to see which parts are completed.
- `HideEasy`: `true` if I use this in ICPC which have 25 page restriction.
- `HideHard`: `false` unless I want to distribute more beginner-friendly version.
- `HideVariable`: `true` if I use this for myself, `false` otherwise.
- `HideExplanation`: `true` if I use this for myself, `false` otherwise.
- `ExtraInfo`: `false` unless debugging.

Then compile the TeX as usual. I use `pdflatex`.

## Notation
### Indicator Notation
- Completed (Blue): You can freely use this code.
- To Revise (Green): This code does work, but the style might not match my current one.
- To Test (Yellow): This code is not tested. Use at your own risk.
- To Add (Orange): I did learned this, I just didn't added this because I'm too lazy.
- To Learn (Red): I need to learn this later.

### Gray Text
Anything that are written in gray texts are untested statements i.e. might be false.

### Difficulty
- Easy: I can write this code myself w/o reference.
- Normal: This is not Easy nor Hard.
- Hard: I don't know how to properly use this.
- Show: This have to be shown at all cost.
- Hide: I want to temporary hide this.

## References
Every code is written by me, though some of them is basically the rewritten version of the others' code.
- [`teamnote.sty`](https://github.com/ho94949/teamnote.sty) by ho94949
- [Edited version of `teamnote.sty`](https://github.com/justiceHui/icpc-teamnote/tree/master) by jhnah917
- [Topic List](https://youkn0wwho.academy/topic-list) by youkn0wwho