import random


def get_user_input() -> int:
    """
    Ask for the user’s input of how many dice they want to roll in the simulation.
    Validates it, and returns it as an integer number if the validation was successful.
    Otherwise, the function will ask for the user’s input again.
    """
    user_input = input("How many dice do you want to roll? [1-6] ")
    while user_input.strip() not in ("1", "2", "3", "4", "5", "6"):
        user_input = input("How many dice do you want to roll? [1-6] ")
    return int(user_input)


def roll_dices(n_dice: int) -> list:
    dices = []
    for _ in range(n_dice):
        roll = random.randint(1, 6)
        dices.append(roll)
    return dices


def print_dices(list_dices):
    """Print the roll dices in ASCII art"""
    DICE_ART = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    o    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  o      │",
            "│         │",
            "│      o  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  o      │",
            "│    o    │",
            "│      o  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  o   o  │",
            "│         │",
            "│  o   o  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  o   o  │",
            "│    o    │",
            "│  o   o  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  o   o  │",
            "│  o   o  │",
            "│  o   o  │",
            "└─────────┘",
        ),
    }
    DIE_HEIGHT = len(DICE_ART[1])
    DIE_FACE_SEPARATOR = " "

    # Generate a list of dice faces from DICE_ART
    dice_faces = []
    for dice in list_dices:
        dice_faces.append(DICE_ART[dice])

    dice_faces_rows = []
    # Generate the list of dice faces rows
    for row_index in range(DIE_HEIGHT):
        row_components = []
        for dice in dice_faces:
            row_components.append(dice[row_index])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    header = " RESULTS ".center(width, "~")

    dice_faces_result = "\n".join([header] + dice_faces_rows)

    return dice_faces_result


if __name__ == "__main__":
    number_dice = get_user_input()
    roll_dices = roll_dices(number_dice)
    print(print_dices(roll_dices))
