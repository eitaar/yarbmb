from collections.abc import Sequence

from mahjong.shanten import Shanten

from yarbmb.tiles import Tile


def shanten_of(hand: Sequence[Tile]) -> int:
    tiles_34 = [0] * 34
    for tile in hand:
        tiles_34[tile.to_id()] += 1
    return Shanten.calculate_shanten(tiles_34)
