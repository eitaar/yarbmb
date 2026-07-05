from dataclasses import dataclass

from yarbmb.tiles import Tile, Tile34


@dataclass(frozen=True)
class DiscardOption:
    tile: Tile
    shanten_after: int
    ukeire_count: int
    ukeire_tiles: frozenset[Tile34]
