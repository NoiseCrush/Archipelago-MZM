"""
Option definitions for Metroid: Zero Mission
"""
from Options import Choice, DeathLink, DefaultOnToggle, Toggle, PerGameCommonOptions
from dataclasses import dataclass

"""
- copy options from MZMR, add others such as disable IBJs/progressive bombs (so you eventually can),
  power bomb jumping, and probably add some others as decided on by input in game-suggestions.
  might need some tweaks to vanilla/some tricks/everything "difficulties"
- for starters i'm just going to stick to Unknowns activation, a simple one-byte change.
- next one to add would be forcing vanilla Morph, which should be the default. however, it is useful to
  leave out for now for testing generation.
"""


class UnknownItemsAlwaysUsable(DefaultOnToggle):
    """
    Unknown Items (Plasma Beam, Space Jump, and Gravity Suit) are activated and usable as soon as
    they are received.

    When this option is disabled, the player will need to defeat the Chozo Ghost in Chozodia in order
    to unlock Samus' fully-powered suit, after which they may then use the Plasma Beam, Space Jump,
    and Gravity Suit, as in vanilla.
    """
    display_name = "UnknownItemsAlwaysUsable"


class DisplayNonLocalItems(Choice):
    """
    How to display items that will be sent to other players.

    Match Series: Items from Super Metroid and SMZ3 display as their counterpart in Zero Mission
    Match Game: Zero Mission items appear as the item that will be sent
    None: All items for other players appear as AP logos
    """
    display_name = "Display Other Players' Items"
    option_none = 0
    option_match_game = 1
    option_match_series = 2
    default = option_match_series


@dataclass
class MZMOptions(PerGameCommonOptions):
    unknown_items_always_usable: UnknownItemsAlwaysUsable
    display_nonlocal_items: DisplayNonLocalItems
    death_link: DeathLink
