#
#  GemUO
#
#  (c) 2005-2010 Max Kellermann <max@duempel.org>
#  (c) 2010 Kai Sassmannshausen <kai@sassie.org>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; version 2 of the License.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#

FLAG_FEMALE = 0x02
FLAG_POISON = 0x04
FLAG_YELLOW = 0x08
FLAG_MOVABLE = 0x20
FLAG_WAR_MODE = 0x40
FLAG_HIDDEN = 0x80

NORTH = 0x0
NORTH_EAST = 0x1
EAST = 0x2
SOUTH_EAST = 0x3
SOUTH = 0x4
SOUTH_WEST = 0x5
WEST = 0x6
NORTH_WEST = 0x7
RUNNING = 0x80

SERIAL_PLAYER = 0x80000000

ITEM_BANDAGE = 0xe21
ITEM_GOLD = 0xeed

ITEM_DRUMS = 0xe9c
ITEM_TAMOURINE = 0xe9d
ITEM_TAMOURINE_TASSEL = 0xe9e
ITEM_LEAP_HARP = 0xeb2
ITEM_HARP = 0xeb1
ITEM_LUTE = 0xeb3
ITEM_BAMBOO_FLUTE = 0x2805

ITEM_CROOK = 0xe81

ITEM_DAGGER = 0xf52
ITEM_BUTCHER_KNIFE1 = 0x13F6
ITEM_BUTCHER_KNIFE2 = 0x13F7

ITEM_WAND1 = 0xDF2
ITEM_WAND2 = 0xDF3
ITEM_WAND3 = 0xDF4
ITEM_WAND4 = 0xDF5

ITEM_RECALL_SCROLL = 0x1f4c
ITEM_MARK_SCROLL = 0x1f59

ITEM_FISH_STEAK = 0x97B

ITEMS_INSTRUMENTS = (
    ITEM_DRUMS,
    ITEM_TAMOURINE,
    ITEM_TAMOURINE_TASSEL,
    ITEM_LEAP_HARP,
    ITEM_HARP,
    ITEM_LUTE,
    ITEM_BAMBOO_FLUTE,
    )
ITEMS_INSTRUMENTS = set(ITEMS_INSTRUMENTS)

ITEMS_SCOLLS = (
    ITEM_RECALL_SCROLL,
    ITEM_MARK_SCROLL,
    )

ITEMS_WEAPONS_FENCING = (
    ITEM_DAGGER,
    )

ITEMS_WEAPONS_SWORD = (
    ITEM_BUTCHER_KNIFE1,
    ITEM_BUTCHER_KNIFE2
    )

ITEMS_WEAPONS_MACE = (
    ITEM_CROOK,
    ITEM_WAND1,
    ITEM_WAND2,
    ITEM_WAND3,
    ITEM_WAND4,
    )

ITEMS_AXE = (
    0xf45, # executioner's axe
    0xf47, 0xf48, # battle axe
    0xf49, 0xf4a, # axe
    0xf4b, 0xf4c, # double axe
    0x13fb, 0x13fa, # large battle axe
    0x1443, # two handed axe
)

ITEMS_WEAPONS = \
    ITEMS_WEAPONS_FENCING + \
    ITEMS_WEAPONS_SWORD + \
    ITEMS_WEAPONS_MACE

ITEMS_FOOD = (
    ITEM_FISH_STEAK,
    )

ITEM_WOOL = 0xdf8

ITEMS_YARN = (
    0xe1d,
    0xe1e,
    0xe1f,
    )

ITEMS_SPINNING_WHEEL = (
    0x1015,
    0x1019,
    0x101c,
    0x10a4,
    )

ITEMS_LOOM = (
    0x105f,
    0x1060,
    0x1061,
    0x1062,
    )


ITEM_GM_ROBE = 0x204f

ITEMS_WOODEN_BOX = (0x9aa, 0xe7d)
ITEMS_MEDIUM_CRATE = (0xe3f, 0xe3e)
ITEMS_LARGE_CRATE = (0xe3c, 0xe3d)
ITEMS_CHEST = (
    0x9ab, 0xe7c, 0xe41, 0xe40, 0xe43, 0xe42,
    0x280b, 0x280c, 0x280d, 0x280e, 0x280f, 0x2810, 0x2813, 0x2814,
)

ITEMS_LOGS = (0x1bdd, 0x1be0)
ITEMS_BOARDS = (0x1bd7, 0x1bda)
ITEMS_CARPENTRY_TOOLS = (
    0x10e4, # draw knife
    0x1030, 0x1031, # jointing plane
    0x1034, 0x1035, # saw
)

ITEMS_CARPENTRY_PRODUCTS = ITEMS_MEDIUM_CRATE + ITEMS_WOODEN_BOX + (
    0x1b7a, # wooden shield
    0x0DC0, # fishing pole
    0xe89, # quarter staff
    0x13F8, # gnarled staff
)

ITEMS_FLETCHING_TOOLS = (
    ITEM_DAGGER,
)

ITEMS_FLETCHING_PRODUCTS = (
    0xf4f, 0xf50, # crossbow
    0x13b1, 0x13b2, # bow
    0x13fc, 0x13fd, # heavy crossbow
)

TREES = (
    0x4CCA, 0x4CCB, 0x4CCC, 0x4CCD, 0x4CD0, 0x4CD3, 0x4CD6, 0x4CD8,
    0x4CDA, 0x4CDD, 0x4CE0, 0x4CE3, 0x4CE6, 0x4CF8, 0x4CFB, 0x4CFE,
    0x4D01, 0x4D41, 0x4D42, 0x4D43, 0x4D44, 0x4D57, 0x4D58, 0x4D59,
    0x4D5A, 0x4D5B, 0x4D6E, 0x4D6F, 0x4D70, 0x4D71, 0x4D72, 0x4D84,
    0x4D85, 0x4D86, 0x52B5, 0x52B6, 0x52B7, 0x52B8, 0x52B9, 0x52BA,
    0x52BB, 0x52BC, 0x52BD,

    0x4CCE, 0x4CCF, 0x4CD1, 0x4CD2, 0x4CD4, 0x4CD5, 0x4CD7, 0x4CD9,
    0x4CDB, 0x4CDC, 0x4CDE, 0x4CDF, 0x4CE1, 0x4CE2, 0x4CE4, 0x4CE5,
    0x4CE7, 0x4CE8, 0x4CF9, 0x4CFA, 0x4CFC, 0x4CFD, 0x4CFF, 0x4D00,
    0x4D02, 0x4D03, 0x4D45, 0x4D46, 0x4D47, 0x4D48, 0x4D49, 0x4D4A,
    0x4D4B, 0x4D4C, 0x4D4D, 0x4D4E, 0x4D4F, 0x4D50, 0x4D51, 0x4D52,
    0x4D53, 0x4D5C, 0x4D5D, 0x4D5E, 0x4D5F, 0x4D60, 0x4D61, 0x4D62,
    0x4D63, 0x4D64, 0x4D65, 0x4D66, 0x4D67, 0x4D68, 0x4D69, 0x4D73,
    0x4D74, 0x4D75, 0x4D76, 0x4D77, 0x4D78, 0x4D79, 0x4D7A, 0x4D7B,
    0x4D7C, 0x4D7D, 0x4D7E, 0x4D7F, 0x4D87, 0x4D88, 0x4D89, 0x4D8A,
    0x4D8B, 0x4D8C, 0x4D8D, 0x4D8E, 0x4D8F, 0x4D90, 0x4D95, 0x4D96,
    0x4D97, 0x4D99, 0x4D9A, 0x4D9B, 0x4D9D, 0x4D9E, 0x4D9F, 0x4DA1,
    0x4DA2, 0x4DA3, 0x4DA5, 0x4DA6, 0x4DA7, 0x4DA9, 0x4DAA, 0x4DAB,
    0x52BE, 0x52BF, 0x52C0, 0x52C1, 0x52C2, 0x52C3, 0x52C4, 0x52C5,
    0x52C6, 0x52C7
)

CREATURE_EAGLE = 0x5
CREATURE_BIRD = 0x6
CREATURE_DIRE_WOLF = 0x17
CREATURE_GREY_WOLF1 = 0x19
CREATURE_GREY_WOLF2 = 0x1a
CREATURE_GREY_WOLF3 = 0x1b
CREATURE_WHITE_WOLF1 = 0x22
CREATURE_WHITE_WOLF2 = 0x23
CREATURE_WHITE_WOLF3 = 0x24
CREATURE_WHITE_WOLF4 = 0x25
CREATURE_TIMBERWOLF = 0xe1
CREATURE_GORILLA = 0x1d
CREATURE_COW1 = 0xD8
CREATURE_COW2 = 0xE7
CREATURE_BULL1 = 0xE8
CREATURE_BULL2 = 0xE9
CREATURE_HORSE1 = 0xC8
CREATURE_HORSE2 = 0xE2
CREATURE_HORSE3 = 0xE4
CREATURE_HORSE4 = 0xCC
CREATURE_RIDEABLE_LLAMA = 0xDC
CREATURE_DESERT_OSTARD = 0xD2
CREATURE_BLACK_BEAR = 0xD3
CREATURE_POLAR_BEAR = 0xD5
CREATURE_FOREST_OSTARD = 0xDB
CREATURE_FRENZIED_OSTARD = 0xDA
CREATURE_WALRUS = 0xdd
CREATURE_NIGHTMARE = 0x74
CREATURE_LLAMA = 0xDC
CREATURE_GOAT = 0xD1
CREATURE_TIMBER_WOLF = 0xE1
CREATURE_HINT = 0xED
CREATURE_RAT = 0xEE
CREATURE_GREAT_HART = 0xCF
CREATURE_SHEEP = 0xCF
CREATURE_PIG = 0xCB
CREATURE_CAT = 0xC9
CREATURE_DOG = 0xD9
CREATURE_RAT = 0xEE

ANIMALS = (
    CREATURE_EAGLE,
    CREATURE_BIRD,
    CREATURE_DIRE_WOLF,
    CREATURE_GREY_WOLF1,
    CREATURE_GREY_WOLF2,
    CREATURE_GREY_WOLF3,
    CREATURE_WHITE_WOLF1,
    CREATURE_WHITE_WOLF2,
    CREATURE_WHITE_WOLF3,
    CREATURE_WHITE_WOLF4,
    #CREATURE_TIMBERWOLF,
    CREATURE_GORILLA,
    CREATURE_COW1,
    CREATURE_COW2,
    CREATURE_BULL1,
    CREATURE_BULL2,
    CREATURE_HORSE1,
    CREATURE_HORSE2,
    CREATURE_HORSE3,
    CREATURE_HORSE4,
    CREATURE_RIDEABLE_LLAMA,
    CREATURE_DESERT_OSTARD,
    CREATURE_BLACK_BEAR,
    CREATURE_POLAR_BEAR,
    CREATURE_FOREST_OSTARD,
    CREATURE_LLAMA,
    CREATURE_GOAT,
    CREATURE_TIMBER_WOLF,
    CREATURE_HINT,
    CREATURE_RAT,
    CREATURE_GREAT_HART,
    CREATURE_SHEEP,
    CREATURE_PIG,
    CREATURE_CAT,
    CREATURE_DOG,
    CREATURE_RAT,
    )
ANIMALS = set(ANIMALS)

MONSTERS = (
    CREATURE_FRENZIED_OSTARD,
    CREATURE_NIGHTMARE
    )
MONSTERS = set(MONSTERS)

MOUNTS = (
    CREATURE_HORSE1,
    CREATURE_HORSE2,
    CREATURE_HORSE3,
    CREATURE_HORSE4,
    CREATURE_RIDEABLE_LLAMA,
    CREATURE_DESERT_OSTARD,
    CREATURE_FOREST_OSTARD,
    CREATURE_FRENZIED_OSTARD,
    CREATURE_NIGHTMARE,
    )
MOUNTS = set(MOUNTS)

MALE_HUMAN = 0x190
FEMALE_HUMAN = 0x191
HUMANS = (MALE_HUMAN, FEMALE_HUMAN)
