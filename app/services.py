SKIN_OILS = {
    "dry": ["Jojoba Oil", "Argan Oil", "Rosehip Oil"],
    "oily": ["Grapeseed Oil", "Hemp Seed Oil", "Jojoba Oil"],
    "sensitive": ["Calendula Oil", "Chamomile Oil", "Jojoba Oil"],
    "combination": ["Squalane", "Jojoba Oil", "Rosehip Oil"]
}

CONCERN_BOOSTERS = {
    "aging": ["Bakuchiol", "Vitamin E"],
    "acne": ["Tea Tree", "Niacinamide"],
    "redness": ["Centella", "Bisabolol"],
    "dehydration": ["Hyaluronic Acid", "Vitamin E"]
}

BASE_PERCENTAGES = {
    1: [60, 25, 15],
    2: [50, 30, 20],
    3: [40, 35, 25]
}

BOOSTER_PERCENTAGES = {
    1: [3, 2],
    2: [6, 4],
    3: [8, 6]
}


def generate_formula(skin_type, concern, intensity):
    oils = SKIN_OILS[skin_type.lower()]
    boosters = CONCERN_BOOSTERS[concern.lower()]
    base = BASE_PERCENTAGES[intensity]
    active = BOOSTER_PERCENTAGES[intensity]

    return {
        "base_oils": [
            f"{oils[0]}: {base[0]}%",
            f"{oils[1]}: {base[1]}%",
            f"{oils[2]}: {base[2]}%"
        ],
        "active_boosters": [
            f"{boosters[0]}: {active[0]}%",
            f"{boosters[1]}: {active[1]}%"
        ]
    }