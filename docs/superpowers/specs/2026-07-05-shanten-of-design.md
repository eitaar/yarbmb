# shanten_of design

## Problem

`src/yarbmb/shanten.py` is a stub: it has a broken import (`Sequence` unused/missing),
a bare `import mahjong`, and a function signature with no body.

## Approach

Wrap the `mahjong` library's existing shanten calculator rather than reimplementing
the algorithm:

- `shanten_of(hand: Sequence[Tile]) -> int` builds a 34-length tile-count array from
  `hand` using each `Tile.to_id()` (the encoding `tiles.py` already defines), then
  calls `mahjong.shanten.Shanten.calculate_shanten()` on it and returns the result.
- `calculate_shanten` already covers regular, chiitoitsu, and kokushi hand shapes
  (both enabled by default) and returns -1 for a complete hand, 0 for tenpai, and a
  positive shanten count otherwise.
- Imports: `from collections.abc import Sequence`, `from mahjong.shanten import Shanten`,
  and `from tiles import Tile` (flat import, matching the existing convention in
  `tiles.py`, which has no package `__init__.py` and is itself run as a flat script).
- No extra validation is added. Invalid hand sizes (e.g. not 1,2,4,5,7,8,10,11,13,14
  tiles) raise `ValueError` from inside the library; that's left to propagate.

## Out of scope

- No custom/original shanten algorithm (decided: reuse the library).
- No test file added this round (decided: skip for now).
