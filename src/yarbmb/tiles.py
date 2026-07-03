import re
from dataclasses import dataclass
from enum import Enum
from typing import NewType

Tile34 = NewType("Tile34", int)  # 0-33


class Suit(Enum):
    MAN = "m"
    PIN = "p"
    SOU = "s"
    HONOUR = "z"


@dataclass(frozen=True, slots=True)
class Tile:
    suit: Suit
    num: int
    is_red: bool = False

    def to_id(self) -> Tile34:
        offset = {"m": 0, "p": 9, "s": 18, "z": 27}
        return Tile34(self.num - 1 + offset[self.suit.value])


def parse_tile(s: str) -> Tile:
    if s[0] == "0":
        return Tile(suit=Suit(s[1]), num=5, is_red=True)
    return Tile(suit=Suit(s[1]), num=int(s[0]))


def parse_hand(s: str) -> list[Tile]:
    hand: list[Tile] = []
    nums = re.split(r"[a-z]", s)[:-1]
    suits = [c for c in s if c.isalpha()]
    for i, suit in enumerate(suits):
        for n in nums[i]:
            hand.append(parse_tile(f"{n}{suit}"))
    return hand


print(parse_hand("123p456s567z223m"))
