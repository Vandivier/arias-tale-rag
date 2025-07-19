def create_horse_fact() -> str:
    """
    Return a random fact about horses.
    """
    facts = []
    facts.append("Horses cannot sleep.")
    facts.append(
        "Horses have a unique way of communicating with each other through body language."
    )
    facts.append("The fastest recorded speed of a horse is 55 mph (88.5 km/h).")

    return facts[0]


def roll_a_dice() -> int:
    """
    Simulate rolling a six-sided dice.
    """
    import random

    return random.randint(1, 6)
