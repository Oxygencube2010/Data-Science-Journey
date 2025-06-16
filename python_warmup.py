""" Inspire by Realpython - https://realpython.com/python-dice-roll/ """
import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def parse_input(input_string):
    """Return `input string` as an integer between 1 and 6"""
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number between 1 and 6.")
        raise SystemExit(1)

def roll_dice(num_dice):
    """Return a list of integers with length `num_dice`"""
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

def _get_dice_face(dice_values):
    dice_faces =  []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces

def _generate_dice_faces_rows(dice_faces):
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for dice in dice_faces:
            row_components.append(dice[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows

def generate_dice_faces_diagram(dice_values):
    """ Return an ASCII diagram of dice faces based on `dice_values` """

    # Generate a list of dice faces from DICE_ART
    dice_faces = _get_dice_face(dice_values)
    
    # Generate a list containing the dice faces rows
    dice_face_rows = _generate_dice_faces_rows(dice_faces)
    
    # Generate header with the words `RESULTS` centered
    width = len(dice_face_rows[0])
    diagram_header = "RESULTS".center(width, "~")
    dice_faces_diagram = "\n".join([diagram_header] + dice_face_rows)
    return dice_faces_diagram

# 1. Get and validate user's input
num_dice_input = input("How many dice do you want to roll? (1-6): ")
num_dice = parse_input(num_dice_input)
# 2. Roll the dice
roll_results = roll_dice(num_dice)
# 3. Generate the ASCII diagram of the dice faces
dice_face_diagram = generate_dice_faces_diagram(roll_results)
# 4. Display the diagram
print(f"\n{dice_face_diagram}")
