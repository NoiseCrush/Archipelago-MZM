"""
Classes and functions related to AP items for Metroid: Zero Mission
"""
import typing
from enum import IntEnum
from BaseClasses import Item, ItemClassification
from typing import Dict

AP_MZM_ID_BASE = 261300

progression = ItemClassification.progression
filler = ItemClassification.filler
useful = ItemClassification.useful
trap = ItemClassification.trap


class ItemType(IntEnum):
    tank = 0
    major = 1
    beam = 2


class MZMItem(Item):
    game: str = "Metroid Zero Mission"


class ItemData:
    name: str
    code: int
    id: int
    progression: ItemClassification
    type: ItemType  # used for determining the memory address to write bits to as each go somewhere different
    bits: typing.Optional[int]  # bit to flip when adding this item to Samus' equipment

    def __init__(self, name: str, id: int, progression: ItemClassification, type: ItemType, bits: int) -> None:
        self.name = name
        self.id = id
        self.code = id + AP_MZM_ID_BASE
        self.progression = progression
        self.type = type
        self.bits = bits


# assignments lifted from BioSpark's MZM Randomizer for now, may reorganize later
item_data_table: Dict[str, ItemData] = {
    "Energy Tank": ItemData("Energy Tank", 0, progression, ItemType.tank, None),
    "Missile Tank": ItemData("Missile Tank", 1, filler, ItemType.tank, None),
    "Super Missile Tank": ItemData("Super Missile Tank", 2, filler, ItemType.tank, None),
    "Power Bomb Tank": ItemData("Power Bomb Tank", 3, filler, ItemType.tank, None),
    "Long Beam": ItemData("Long Beam", 4, progression, ItemType.beam, 0x1),
    "Charge Beam": ItemData("Charge Beam", 5, useful, ItemType.beam, 0x10),
    "Ice Beam": ItemData("Ice Beam", 6, progression, ItemType.beam, 0x2),
    "Wave Beam": ItemData("Wave Beam", 7, progression, ItemType.beam, 0x4),
    "Plasma Beam": ItemData("Plasma Beam", 8, progression, ItemType.beam, 0x8),
    "Bomb": ItemData("Bomb", 9, progression, ItemType.beam, 0x80),  # regular bomb is stored with beams
    "Varia Suit": ItemData("Varia Suit", 10, progression, ItemType.major, 0x10),
    "Gravity Suit": ItemData("Gravity Suit", 11, progression, ItemType.major, 0x20),
    "Morph Ball": ItemData("Morph Ball", 12, progression, ItemType.major, 0x40),
    "Speed Booster": ItemData("Speed Booster", 13, progression, ItemType.major, 0x2),
    "Hi-Jump": ItemData("Hi-Jump", 14, progression, ItemType.major, 0x1),
    "Screw Attack": ItemData("Screw Attack", 15, progression, ItemType.major, 0x8),
    "Space Jump": ItemData("Space Jump", 16, progression, ItemType.major, 0x4),
    "Power Grip": ItemData("Power Grip", 17, progression, ItemType.major, 0x80),
    "Nothing": ItemData("Nothing", 18, filler, None, None),
    "AP Item (Filler)": ItemData("AP Item", 19, filler, None, None),
    "AP Item (Progression)": ItemData("AP Item", 20, progression, None, None),
    "AP Item (Useful)": ItemData("AP Item", 21, useful, None, None),
    "AP Item (Trap)": ItemData("AP Item", 22, trap, None, None),
}

def get_major_items():
    return (name for name, data in item_data_table.items() if data.type in (ItemType.beam, ItemType.major))
