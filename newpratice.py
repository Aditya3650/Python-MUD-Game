"""
Your name: Aditya Singh Attri
Your student number: A01276335

All of your code must go in this file.
"""

import random
import itertools

"""
A little game.
"""


def make_board(rows: int, columns: int) -> dict:
    """
    Make a game board with coordinates and their descriptions.

    A function which takes rows and columns as inputs and creates a game board with random description for each of the
    coordinates.

    :param rows: A positive int
    :param columns: A positive int
    :precondition: Both the parameters must be positive integers equal to or greater than twenty five.
    :postcondition: Return a dictionary with all the coordinates till 1 less than the specified rows and columns in a
    tuple as keys. Their values are cycled through a list of preset room descriptions. Also, the first and last set of
    coordinates are given some other unique values.
    :return: A dictionary of board coordinates as keys and room description as values.
    """
    room_types = ['the streets of Stormwind', 'over the ashes of Outland', 'outside the Scholomance Academy',
                  'lost in the catacombs of Uldum']
    iterator = itertools.cycle(room_types)
    board_map = {}
    for x_coordinate in range(rows):
        for y_coordinate, room in zip(range(columns), iterator):
            board_map[(x_coordinate, y_coordinate)] = room
    board_map[(0, 0)] = "on the way to find Gul'dan, the Warlock"
    board_map[(rows - 1, columns - 1)] = "at the foot of the Blackrock Mountain, the lair of Gul'dan"
    return board_map


def opening_line():
    """
    Print the opening line of the game.
    """
    print("""\nYou are in search of Gul'dan the Warlock, the leader of the Horde, who destroyed your clan. He was last 
seen at the top of the Blackrock Mountain, preparing for his next raid. You have trained all your life 
to defeat him. This is your chance to seek revenge for what he did.\n""")


def make_character():
    """
    Assign character information to a variable.

    A function to assign character information which include X-coordinate, Y-coordinate, Level, Current-XP and
    Level-Up-XP as keys of the character.

    :postcondition: Assign a dictionary with keys of X and Y coordinates, the level set as 1, the current XP set to
    0 and the level up XP set to 1000.
    :return: A dictionary of X and Y coordinates, level, current XP and level up XP.

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
    """
    character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
    return character_info


def input_name(character: dict):
    """
    Input the character name from the user.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level for the character.
    """
    character['Name'] = input("Enter the name for your Champion: ")


def choose_class() -> int:
    """
    Choose the class of your champion.

    A function to take input from the user to choose the class of the champion of the user.

    :postcondition: Print a set of description for each class and assigning a number to each one. After the user selects
    a number, print the confirmation for the character the user selects. If the input is not a valid number, the
    function repeats itself till the user inputs a valid number.
    :return: The input type-converted to an integer.
    """
    print("""Type the class you want to choose

    Type 1 for Paladin : Paladins are the servants of Light. The Light grants them the strength to fight and makes them 
    very resilient in battles.. Their passive power 'Blessing of the Light' heals them during a battle.

    Type 2 for Warrior : Warriors are seasoned fighters. They have mastery over an arsenal of weaponry and armour. Their
    passive power 'Bloodlust' gives them increased damage during a fight.

    Type 3 for Shaman : Shamans are master of the primal elements. Their mastery over the nature can change the tide of 
    battle at any moment. Their passive power 'Lightning Bolt' decreases the Health of their opponents over time.

    Type 4 for Rogue : Rogues are the assassins of the shadow. Their unseen blade, blinding speed, and subtle poison
     gives them an advantage over any foe. Their passive power 'Poisoned Daggers' decreases the damage output of their
     opponents.""")
    while True:
        class_choice = input()
        if class_choice == "1":
            print("You are a Paladin, the Servant of Light")

            break
        elif class_choice == "2":
            print("You are a Warrior, Lord of War")

            break
        elif class_choice == "3":
            print("You are a Shaman, Master of Nature")

            break
        elif class_choice == "4":
            print("You are a Rogue, Assassin of the Dark")

            break
        else:
            print("Enter a valid number to choose a class")
    return int(class_choice)


def set_class(class_name: int, character: dict):
    """
    Set the class name in the character dictionary according to the choice of the user.

    :param class_name: A positive int
    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level for the character. The class_name parameter must be a positive integer between 1 and 4. It
    will represent the 4 classes.
    :postcondition: Add a 'Class' key to the character dictionary with the value depending upon the choice made by the
    user.

    >>> character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
    >>> class_number = 2
    >>> set_class(class_number, character_info)
    >>> character_info
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, 'Class': 'Warrior'}

    >>> character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
    >>> class_number = 4
    >>> set_class(class_number, character_info)
    >>> character_info
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, 'Class': 'Rogue'}
    """
    if class_name == 1:
        character['Class'] = 'Paladin'
    elif class_name == 2:
        character['Class'] = 'Warrior'
    elif class_name == 3:
        character['Class'] = 'Shaman'
    elif class_name == 4:
        character['Class'] = 'Rogue'


def set_health(character: dict):
    """
    Set the health and the max health in the character dictionary according to the choice of the user.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, and the class for the character.
    :postcondition: Add 'Health' and 'Max_Health' key to the character dictionary with the value depending upon the
    class of the character.

     >>> character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
     'Class': 'Warrior'}
     >>> set_health(character_info)
     >>> character_info
     {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, 'Class': 'Warrior', \
'Health': 1200, 'Max_Health': 1200}

     >>> character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
     'Class': 'Shaman'}
     >>> set_health(character_info)
     >>> character_info
     {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, 'Class': 'Shaman', \
'Health': 900, 'Max_Health': 900}
    """
    if character['Class'] == 'Paladin':
        character['Health'] = 1000
        character['Max_Health'] = 1000
    elif character['Class'] == 'Warrior':
        character['Health'] = 1200
        character['Max_Health'] = 1200
    elif character['Class'] == 'Shaman':
        character['Health'] = 900
        character['Max_Health'] = 900
    elif character['Class'] == 'Rogue':
        character['Health'] = 800
        character['Max_Health'] = 800


def set_damage_and_passive(character: dict):
    """
    Set the health and the max health in the character dictionary according to the choice of the user.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, and the class for the character.
    :postcondition: Add 'Damage' and 'Passive_Power' key to the character dictionary with the value depending upon the
    class of the character.

    >>> character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
    'Class': 'Shaman', 'Health': 900, 'Max_Health': 900}
    >>> set_damage_and_passive(character_info)
    >>> character_info
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, 'Class': 'Shaman', \
'Health': 900, 'Max_Health': 900, 'Damage': 110, 'Passive_Power': 'Lightning Bolt'}

     >>> character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
    'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000}
    >>> set_damage_and_passive(character_info)
    >>> character_info
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, 'Class': 'Paladin', \
'Health': 1000, 'Max_Health': 1000, 'Damage': 95, 'Passive_Power': 'Blessing of the Light'}
    """
    if character['Class'] == 'Paladin':
        character['Damage'] = 95
        character['Passive_Power'] = 'Blessing of the Light'
    elif character['Class'] == 'Warrior':
        character['Damage'] = 80
        character['Passive_Power'] = 'Bloodlust'
    elif character['Class'] == 'Shaman':
        character['Damage'] = 110
        character['Passive_Power'] = 'Lightning Bolt'
    elif character['Class'] == 'Rogue':
        character['Damage'] = 120
        character['Passive_Power'] = 'Poisoned Daggers'


def class_level(character: dict):
    """
    Set the class title according to the level of the character.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, and the class for the character.
    :postcondition: Set the value of the class title key in the character dictionary according to the level of the
    character in the same dictionary.

    >>> character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
    'Class': 'Paladin'}
    >>> class_level(character_info)
    >>> character_info
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, 'Class': 'Paladin', \
'Class_Level': 'Squire'}

    >>> character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 0, 'Level-Up-XP': 1000, \
    'Class': 'Paladin'}
    >>> class_level(character_info)
    >>> character_info
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 3, 'Current-XP': 0, 'Level-Up-XP': 1000, 'Class': 'Paladin', \
'Class_Level': 'Prince'}
    """
    paladin = ['Squire', 'Commander', 'Prince']
    warrior = ['Recruit', 'Taskmaster', 'Warlord']
    shaman = ['Novice', 'Windlord', 'Deathseer']
    rogue = ['Thief', 'Assassin', 'Nightslayer']
    if character['Class'] == 'Paladin':
        character['Class_Level'] = paladin[character['Level'] - 1]
    elif character['Class'] == 'Warrior':
        character['Class_Level'] = warrior[character['Level'] - 1]
    elif character['Class'] == 'Shaman':
        character['Class_Level'] = shaman[character['Level'] - 1]
    elif character['Class'] == 'Rogue':
        character['Class_Level'] = rogue[character['Level'] - 1]


def passive_effect(character: dict, enemy: dict):
    """
    Activate the passive effect depending upon the class of the character.

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character.
    :postcondition: Activate the passive effect depending upon the class of the character. Print the name of the passive
    and the effect it does.

    >>> character_info =  {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
    'Class': 'Paladin', 'Health': 100, 'Max_Health': 1000, 'Damage': 95, 'Passive_Power': 'Blessing of the Light'}
    >>> enemy_info = {}
    >>> passive_effect(character_info, enemy_info)
    <BLANKLINE>
    You invoke 'Blessing of Light' and the Lady Liadrin blesses you with the prism of life. You gain Health amounting \
to 33
    >>> character_info
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
'Class': 'Paladin', 'Health': 133, 'Max_Health': 1000, 'Damage': 95, 'Passive_Power': 'Blessing of the Light'}

    # Does not increase health more than max health
    >>> character_info =  {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
    'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95, 'Passive_Power': 'Blessing of the Light'}
    >>> enemy_info = {}
    >>> passive_effect(character_info, enemy_info)
    <BLANKLINE>
    You invoke 'Blessing of Light' and the Lady Liadrin blesses you with the prism of life. You gain Health amounting \
to 33
    >>> character_info
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95, 'Passive_Power': 'Blessing of the Light'}
    """
    if character['Class'] == 'Paladin':
        character['Health'] += round(character['Max_Health'] / 30)
        print(f"\nYou invoke 'Blessing of Light' and the Lady Liadrin blesses you with the prism of life. "
              f"You gain Health amounting to {round(character['Max_Health'] / 30)}")
    elif character['Class'] == 'Warrior':
        character['Damage'] += round(character['Damage'] / 10)
        print(f"\nYou invoke 'Bloodlust' and the your body goes into a frenzy. "
              f"You gain Damage amounting to {round(character['Damage'] / 10)}")
    elif character['Class'] == 'Shaman':
        enemy['Enemy_Health'] -= round(character['Max_Health'] / 20)
        print(f"\nYou invoke 'Lightning Bolt' and the thunder breaks the sky as your power reaches the elements. "
              f"You decrease the Health of your enemy by {round(character['Max_Health'] / 20)}")
    elif character['Class'] == 'Rogue':
        enemy['Enemy_Damage'] -= round(character['Damage'] / 10)
        print(f"\nYou invoke 'Poisoned Daggers' and the venom starts spreading in your opponent. "
              f"You decrease the Damage of your enemy by {round(character['Damage'] / 10)} ")
    health_cap(character)


def xp_checker(character: dict):
    """
    Level up the character when the experience points reach above a certain threshold.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character.
    :postcondition: Check the current XP of the character and if it is above the level up XP, increase the level,
    health, max health, damage and reset the current XP.

    >>> character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 1001, 'Level-Up-XP': 1000, \
    'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95, 'Class_Level': 'Squire', \
    'Passive_Power': 'Blessing of the Light'}
    >>> xp_checker(character_info)
    <BLANKLINE>
    You have levelled up
    You are now level 2
    Your champion is now a Commander
    Your current Health is 1100
    Your maximum Health is 1100
    Your damage is 105
    XP required to level up is 999
    >>> character_info
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 2, 'Current-XP': 1, 'Level-Up-XP': 1000, 'Class': 'Paladin', \
'Health': 1100, 'Max_Health': 1100, 'Damage': 105, 'Class_Level': 'Commander', 'Passive_Power': 'Blessing of the Light'}

    # When Current-XP < Level-Up-XP
    >>> character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 101, 'Level-Up-XP': 1000, \
    'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95, 'Class_Level': 'Squire', \
    'Passive_Power': 'Blessing of the Light'}
    >>> xp_checker(character_info)
    >>> character_info
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 101, 'Level-Up-XP': 1000, 'Class': 'Paladin', \
'Health': 1000, 'Max_Health': 1000, 'Damage': 95, 'Class_Level': 'Squire', 'Passive_Power': 'Blessing of the Light'}
    """
    if character['Current-XP'] > character['Level-Up-XP']:
        character['Level'] += 1
        character['Current-XP'] -= 1000
        character['Health'] += round(character['Health'] / 10)
        character['Max_Health'] += round(character['Max_Health'] / 10)
        character['Damage'] += round(character['Damage'] / 10)
        class_level(character)
        print(f"""\nYou have levelled up
You are now level {character['Level']}
Your champion is now a {character['Class_Level']}
Your current Health is {round(character['Health'])}
Your maximum Health is {round(character['Max_Health'])}
Your damage is {round(character['Damage'])}
XP required to level up is {character['Level-Up-XP'] - character['Current-XP']}""")
        if character['Level'] == 3:
            print("\nYou sense the boss at the edge of the Barrens, on top of the Blackrock Mountain. "
                  "You must make your there to finally taste the sweet revenge you have longed for. ")


def health_cap(character: dict):
    """
    Check if the health is not more than the max health of the character.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character.
    :postcondition: Check the health of the character and if it is above the max health, reset it back equal to the max
    health.

    >>> character_info =  {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
    'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95, 'Passive_Power': 'Blessing of the Light'}
    >>> health_cap(character_info)
    >>> character_info
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95, 'Passive_Power': 'Blessing of the Light'}

    >>> character_info =  {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
    'Class': 'Paladin', 'Health': 1200, 'Max_Health': 1000, 'Damage': 95, 'Passive_Power': 'Blessing of the Light'}
    >>> health_cap(character_info)
    >>> character_info
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000, \
'Class': 'Paladin', 'Health': 1000, 'Max_Health': 1000, 'Damage': 95, 'Passive_Power': 'Blessing of the Light'}
    """
    if character['Health'] > character['Max_Health']:
        character['Health'] = character['Max_Health']


def show_score(character: dict):
    """
    Print the current stats of the character.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character.
    :postcondition: Print the name, level, class, class level, passive, health, max health, current XP and XP required
    for level up for the character.
    """
    print(f"Name: {character['Name']}, Level: {character['Level']}, Class: {character['Class']}, "
          f"Class_Level: {character['Class_Level']}, Passive: {character['Passive_Power']}, "
          f"Health: {character['Health']}, Max Health: {character['Max_Health']}, "
          f"Current XP: {character['Current-XP']}, "
          f"XP Required For Level Up: {character['Level-Up-XP'] - character['Current-XP']} ")


def is_alive(character: dict) -> bool:
    """
    Checks if the health of the character is not below zero.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character.
    :postcondition: Print the current health and return True if health is above 0. Else print a death message and return
    False.
    :return: A boolean value

    >>> gamer = {'X-coordinate': 0, 'Y-coordinate': 0, 'Health': 5}
    >>> is_alive(gamer)
    Your current Health is 5
    True

    >>> gamer = {'X-coordinate': 0, 'Y-coordinate': 0, 'Health': 0}
    >>> is_alive(gamer)
    You have succumbed to your injuries. Your skills could not match your resolve
    False
    """
    if character['Health'] > 0:
        print(f"Your current Health is {round(character['Health'])}")
        return True
    else:
        print("You have succumbed to your injuries. Your skills could not match your resolve")
        return False


def describe_current_location(board: dict, character: dict):
    """
    Describe the current location of the character.

    A function to give the room description and the current coordinates of the character.

    :param board: A dictionary
    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character. The board parameter must be
    a dictionary of the coordinates as keys and the room description as values.
    :postcondition: Print the charcter name, the current coordinates and the description of the room.

    # Only 2 cases where the rooms are not random
    >>> game_board = make_board(10, 10)
    >>> gamer = {'Name': 'Babu', 'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 2}
    >>> describe_current_location(game_board, gamer)
    Babu is on the way to find Gul'dan, the Warlock at (0, 0)

    >>> game_board_2 = make_board(10, 10)
    >>> character_info = {'Name': 'Sabu', 'X-coordinate': 9, 'Y-coordinate': 9, 'HP': 2}
    >>> describe_current_location(game_board_2, character_info)
    Sabu is at the foot of the Blackrock Mountain, the lair of Gul'dan at (9, 9)
    """
    current_coordinates = (character['X-coordinate'], character['Y-coordinate'])
    champion_name = character['Name']
    print(f"{champion_name} is {board[current_coordinates]} at {current_coordinates}")


def get_user_choice() -> str:
    """
    Take user input for the direction.

    A function to take input from the user for selecting the direction the character will move.

    :postcondition: Print a set of instructions assigning a number to each direction. After the user selects a number,
    print the direction the character moves. Stop the loop if the user inputs 'score' or 'quit'. If the input is not a
    valid number, the function repeats itself till the user inputs a valid number.
    :return: The string entered by the user.
    """
    print("""\nEnter the direction you wish to go 
    Press 1 to go East 
    Press 2 to go South 
    Press 3 to go West 
    Press 4 to go North
    Type 'score' to check out your stats
    Type 'quit' to stop playing, for now ;)""")
    while True:
        user_choice = input()
        if user_choice == "1":
            print("You are moving East")
            break
        elif user_choice == "2":
            print("You are moving South")
            break
        elif user_choice == "3":
            print("You are moving West")
            break
        elif user_choice == "4":
            print("You are moving North")
            break
        elif user_choice.lower() == "score":
            break
        elif user_choice.lower() == "quit":
            break
        else:
            print("Enter a valid number")

    return user_choice


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Check if the requested move can be performed or not

    A function to check if the move requested by the user stays in the boundary of the already established board.

    :param board: A dictionary
    :param character: A dictionary
    :param direction: A positive int
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character. The board parameter must be
    a dictionary of the coordinates as keys and the room description as values. The direction parameter must be a
    positive integer between 1 and 4. It represents the 4 directions.
    :postcondition: Return the boolean value True if the requested move is possible and False if it is not.
    :return: A boolean value

    >>> game_board = make_board(3, 3)
    >>> gamer = make_character()
    >>> direction_move = "3"
    >>> validate_move(game_board, gamer, direction_move)
    False

    >>> game_board = make_board(3, 3)
    >>> gamer = make_character()
    >>> direction_move = "1"
    >>> validate_move(game_board, gamer, direction_move)
    True

    """
    fake_character = character.copy()
    if direction == "1":
        fake_character['Y-coordinate'] += 1
    elif direction == "2":
        fake_character['X-coordinate'] += 1
    elif direction == "3":
        fake_character['Y-coordinate'] -= 1
    elif direction == "4":
        fake_character['X-coordinate'] -= 1
    return True if (fake_character['X-coordinate'], fake_character['Y-coordinate']) in board.keys() else False


def invalid_move():
    """
    Print a random response when the move requested by the user is invalid.

    :postcondition: Print a random response from a given list of responses whenever a move requested by the user is not
    possible. Attach a common suggestion after a random reason each time to the print statement.
    """
    invalid_reasons = ['Oh no, there is a wall there.', 'You stand at the edge of a cliff.', 'You are at a dead-end.',
                       'You are in front of a deadly swamp']
    print(random.choice(invalid_reasons) + " Move in some other direction.")


def move_character(character: dict, direction: str):
    """
    Update the character information whenever a valid move is made.

    A function to update the stored coordinates of the character in character information whenever a valid move is made
    by the user.

    :param character: A dictionary
    :param direction: A positive int
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character. The direction parameter
    must be a positive integer between 1 and 4. It representx the 4 directions.
    :postcondition: Change the coordinates according to the move made by the user. Increase the health of the character
    by 5 and the XP by 20.
    dictionary.

    >>> gamer = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current-XP': 20, 'Level-Up-XP': 1000, 'Health': 100}
    >>> direction_move = "2"
    >>> move_character(gamer, direction_move)
    >>> gamer
    {'X-coordinate': 1, 'Y-coordinate': 0, 'Current-XP': 0, 'Level-Up-XP': 1000, 'Health': 105}


    >>> gamer = {'X-coordinate': 0, 'Y-coordinate': -1, 'Current-XP': 20, 'Level-Up-XP': 1000, 'Health': 100}
    >>> direction_move = "3"
    >>> move_character(gamer, direction_move)
    >>> gamer
    {'X-coordinate': 0, 'Y-coordinate': -1, 'Current-XP': 0, 'Level-Up-XP': 1000, 'Health': 105}
    """
    if direction == "1":
        character['Y-coordinate'] += 1
    elif direction == "2":
        character['X-coordinate'] += 1
    elif direction == "3":
        character['Y-coordinate'] -= 1
    elif direction == "4":
        character['X-coordinate'] -= 1
    character['Health'] += 5
    character['Current-XP'] += 20


def check_for_foes(character: dict) -> bool:
    """
    Check if there is an enemy on the coordinate.

    A function to randomly generate an enemy on a set of coordinates. The chances for generating the enemy is a 25%.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character.
    :postcondition: Generate an enemy on the coordinate. There is a one in four chance for the enemy to generate. Print
    a dialogue and return True if the enemy is generated and the coordinate is not on the list of preset coordinates
    in guess_coordinates. Otherwise, return False.
    :return: A boolean value
    """
    foe_checker = random.randint(1, 5)
    coordinates_list = guess_coordinates()
    character_coordinates = (character['X-coordinate'], character['Y-coordinate'])
    if foe_checker == 1 and character_coordinates not in coordinates_list:
        print("""\nAlas, you have encountered a foe in the wild.
You do not wish to harm any being other than Gul'dan, but you have no choice now.""")
        return True
    else:
        return False


def fight_or_flee() -> bool:
    """
    Ask the user if he wants to continue to fight or flee the foe.

    :postcondition: Print a statement assigning numbers to the two options. Print the selected choice to fight and
    return True if the user selects 1. Otherwise, print the selected choice to flee and return False.
    :return: A boolean value
    """
    print("""\nDo you wish to fight the foe?
    Press 1 to Fight
    Press 2 to Flee""")
    while True:
        user_choice = input()
        if user_choice == "1":
            print("You decide to fight the foe")
            break
        elif user_choice == "2":
            print("You decide to flee from the foe")
            break
        else:
            print("Enter a valid number to fight or flee from the foe")
    return True if user_choice == '1' else False


def guessing_game_select(character: dict):
    """
    Guess the number.

    A function to ask the user to guess a number between 1 and 3.

    :param character: A dictionary
   :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character. The value entered must be
    between 1 and 3.
    :postcondition: Print different set of statements if the user correctly guesses the answer or not. The character
    loses 100 health if the answer is incorrect and the gains 200 health when it is correct.
    """
    secret_number = random.randint(1, 3)
    guess = int(input(f"Enter an option between 1 and 3 to guess the correct side:\n "))
    if guess == secret_number:
        print("\nYou're right! The Bloodmage blesses your soul with the gift of life. "
              "You gain 200 Health")
        character['Health'] += 200
    else:
        character['Health'] -= 100
        print(f"""\nWrong option! The correct side was option {secret_number} 
You feel your soul getting tapped and vitality being removed.
You lose 100 Health""")
    health_cap(character)
    print(f"Your current health is {round(character['Health'])}")


def guessing_game(character: dict):
    """
    Play the game of guessing.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character.
    :postcondition: Print an introductory dialogue and ask the user if they want to continue playing or not after each
    game. Print the choice they select. Also, the character gains 300 XP after each game.
    """
    print("""You come across the Bloodmage Thalnos. 
In order to commence on your quest, you have to play the Trade of Souls.
Answer correctly and gain the elixir of life,
Answer wrong and pay with your soul.\n
The Bloodmage flips The Three Headed Dice of Hrakkar""")
    while character['Health'] != 0:
        guessing_game_select(character)
        if character['Health'] == 0:
            break
        print("""\nDo you still wish to play the Soul Trade with Thalnos?
    Press 1 to Continue Playing
    Press 2 to Stop Playing""")
        user_choice = input()
        if user_choice == "1":
            print("You decide to continue playing the Trade of Souls")
        else:
            print("You decide to stop playing the Trade of Souls")
            break
    character['Current-XP'] += 300


def enemy_flee() -> bool:
    """
    Check if the Ogre fled from you or not.

    :postcondition: Check if the Ogre has ran away or not. There is a one in 5 chance for it to run away. Print a
    dialogue and return True if it flees. Otherwise, return False.
    :return: A boolean value
    """
    flee = random.randint(1, 5)
    if flee == 1:
        print("The Ogre has fled from your wrath. Continue your journey in search of Gul'dan")
        return True
    else:
        return False


def make_game_enemy(character: dict) -> dict:
    """
    Create the enemy for the fight.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character.
    :postcondition: Return the enemy health and enemy damage depending upon the character health and character damage
    respectively.
    :return: A dictionary
    """
    return {'Enemy_Health': character['Max_Health'] / 2, 'Enemy_Damage': character['Damage'] / 2}


def fighting_game_damage(character: dict, enemy: dict):
    """
    Fight the enemy.

    A function to simulate the fight between the character and enemy.

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character. The enemy parameter must be
    a dictionary with keys of enemy health and enemy damage.
    :postcondition: A number is randomly selected between 0 to 3. The character and enemy deal damage to each other
    depending upon the number selected. The health of the character and the enemy is printed after each bout.
    """
    hit_chances = random.randint(0, 3)
    if hit_chances == 0:
        enemy['Enemy_Health'] -= round(character['Damage'])
        character['Health'] -= round(enemy['Enemy_Damage'])
        print("You both attack each other")
    elif hit_chances == 1:
        enemy['Enemy_Health'] -= round(character['Damage'])
        print("Your enemy misses an attack but you hurt him")
    elif hit_chances == 2:
        character['Health'] -= round(enemy['Enemy_Damage'])
        print("You miss your attack but your enemy lands a blow")
    elif hit_chances == 3:
        print("Both of you miss your attacks")
    health_cap(character)
    print(f"Your health is {round(character['Health'])} and your enemy has {round(enemy['Enemy_Health'])} remaining.")


def enemy_flee_damage(character: dict, enemy: dict):
    """
    Chance to take damage from the enemy while fleeing.

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character. The enemy parameter must be
    a dictionary with keys of enemy health and enemy damage.
    :postcondition: Take damage in 1 out of 5 scenarios when the user flees from the enemy. Print a dialogue when the
    damage is dealt.
    """
    flee = random.randint(1, 5)
    if flee == 1:
        character['Health'] -= enemy['Enemy_Damage']
        print("You were damaged while fleeing the battle")


def fighting_game(character: dict, enemy: dict):
    """
    Play the game of fighting the enemy.

    A function to simulate the whole scenario of confronting an enemy and fighting it.

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character. The enemy parameter must be
    a dictionary with keys of enemy health and enemy damage.
    :postcondition: Print a introductory dialogue. The game continues until the health of either the character or the
    enemy goes below zero or until the enemy flees. Ask the user if they want to continue the game after each bout.
    Print the choice they select. Also, the character gains 400 XP after each game.
    """
    print("You face a Boulderfist Ogre. This should not be a problem for a strong Champion like you.")
    while character['Health'] > 0 and enemy['Enemy_Health'] > 0:
        passive_effect(character, enemy)
        fighting_game_damage(character, enemy)
        check_enemy_flee = enemy_flee()
        if check_enemy_flee or character['Health'] <= 0:
            break
        if enemy['Enemy_Health'] <= 0:
            print("\nYou have defeated the Ogre")
            break
        print("""\nDo you still wish to fight the Ogre?
    Press 1 to Continue Fighting
    Press 2 to Flee""")
        user_choice = input()
        if user_choice == "1":
            print("You decide to continue to fight the Ogre")
        else:
            enemy_flee_damage(character, enemy)
            print("You decide to flee from the Ogre. Live to fight another day!")
            break
    character['Current-XP'] += 400


def make_game_boss(character: dict) -> dict:
    """
    Create the enemy for the fight.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character.
    :postcondition: Print a dialogue and return the boss health and boss damage depending upon the character health and
    character damage respectively.
    :return: A dictionary
    """
    print("You face the leader of the Horde, Gul'dan")
    return {'Enemy_Health': round(character['Max_Health'] * 2.5), 'Enemy_Damage': round(character['Damage'] * 1.25)}


def boss_game(character: dict, boss: dict):
    """
    Play the game of fighting the enemy.

    A function to simulate the whole scenario of confronting an enemy and fighting it.

    :param character: A dictionary
    :param boss: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character. The boss parameter must be
    a dictionary with keys of boss health and boss damage.
    :postcondition: The game continues until the health of either the character or the enemy goes below zero. Ask the
    user if they want to continue the game after each bout. Print the choice they select.
    """
    while character['Health'] > 0 and boss['Enemy_Health'] > 0:
        passive_effect(character, boss)
        fighting_game_damage(character, boss)
        if character['Health'] <= 0 or boss['Enemy_Health'] <= 0:
            break
        print("""\nDo you still wish to fight the foe?
    Press 1 to Fight
    Press 2 to Flee""")
        user_choice = input()
        if user_choice == "1":
            print("You decide to continue to fight")
        else:
            print("You decide to flee from Gul'dan's sorcery. Train and come back stronger!")
            break


def boss_dead(character: dict, boss: dict) -> bool:
    """
    Check if the health of the boss is below zero or not.

    :param character: A dictionary
    :param boss: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character. The boss parameter must be
    a dictionary with keys of boss health and boss damage.
    :postcondition: Check if the health of the boss is below or equal to zero while at the same time the health of the
    character is above zero. Print a dialogue and return True if the condition is true. Otherwise, return False.
    :return: A boolean value
    """
    if boss['Enemy_Health'] <= 0 and character['Health'] > 0:
        print("Gul'dan is dead. Your soul is at peace finally.")
        return True
    else:
        return False


def check_if_reached_boss(rows: int, columns: int, character: dict) -> bool:
    """
    Check if the character has reached the final coordinates.

    :param rows: A positive int
    :param columns: A positive int
    :param character: A dictionary
    :precondition: Both the rows and columns parameters must be positive integers equal to or greater than twenty five.
    The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and the XP required
    to level up, the class, health, max health and damage for the character.
    :postcondition: Return True if the character has reached the final coordinates. Otherwise, return False.
    :return: A boolean value

    >>> board_rows = 3
    >>> board_columns = 3
    >>> gamer = make_character()
    >>> check_if_reached_boss(board_rows, board_columns, gamer)
    False

    >>> board_rows = 3
    >>> board_columns = 3
    >>> gamer = {'X-coordinate': 2, 'Y-coordinate': 2, 'HP': 5}
    >>> check_if_reached_boss(board_rows, board_columns, gamer)
    True
    """
    if character['X-coordinate'] == rows - 1 and character['Y-coordinate'] == columns - 1:
        return True
    else:
        return False


def final_message_finish():
    """
    Print the final line of the game.
    """
    print("Congratulations! You have completed your quest for vengeance. Thanks for playing the game!")


def final_game_not_finish():
    """
    Print the line when the user quits the game in between.
    """
    print("Thanks for playing this game, come again later!")


def guess_coordinates() -> list:
    """
    Return a list of coordinates.

    :postcondition: Return a list of preset coordinates.
    :return: A list
    """
    guess_coordinate_list = [(4, 4), (4, 9), (4, 15), (4, 20), (9, 4), (9, 9), (9, 15), (9, 20), (15, 4), (15, 9),
                             (15, 15), (15, 20), (20, 4), (20, 9), (20, 15), (20, 20)]
    return guess_coordinate_list


def guessing_game_runner(character: dict):
    """
    Check if the character is on the preset list of coordinates.

    A function to run the guessing_game function if the character is on the preset list of coordinates.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character.
    :postcondition: If the character is on the preset list of coordinates, run the guessing_game function.
    """
    guess_coordinate_list = guess_coordinates()
    character_coordinates = (character['X-coordinate'], character['Y-coordinate'])
    if character_coordinates in guess_coordinate_list:
        guessing_game(character)


def make_map(rows: int, columns: int, character: dict):
    """
    Print the map of the game.

    :param rows: A positive int
    :param columns: A positive int
    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level up, the class, health, max health and damage for the character. Both the rows and columns
    parameters must be positive integers equal to or greater than twenty five.
    :postcondition: Print the map showing the character position, the position of the guessing_game locations and the
    boss after the character reaches level three.
    """
    room_coord = guess_coordinates()
    char_coordinates = (character['X-coordinate'], character['Y-coordinate'])
    boss_coordinates = ((rows - 1), (columns - 1))
    for row in range(rows):
        print("")
        for column in range(columns):
            coordinates = (row, column)
            if char_coordinates == coordinates:
                print("|_#_", end='')
            elif coordinates == boss_coordinates and character['Level'] == 3:
                print("|_\U0001F480_", end='')
            elif coordinates in room_coord:
                print("|_\U0001F54E", end='')
            else:
                print("|___", end='')
        print("|", end='')
    print("\n")


def game_setup(character: dict):
    """
    Setup the character dictionary.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate, level, current XP and
    the XP required to level for the character.
    :postcondition: Run all the necessary functions to setup the character dictionary.
    """
    opening_line()
    input_name(character)
    class_name = choose_class()
    set_class(class_name, character)
    class_level(character)
    set_health(character)
    set_damage_and_passive(character)


def game():
    """Drive the main game loop."""
    rows = 25
    columns = 25
    board = make_board(rows, columns)
    character = make_character()
    game_setup(character)
    describe_current_location(board, character)
    achieved_goal = False
    while is_alive(character) and not achieved_goal:
        xp_checker(character)
        guessing_game_runner(character)
        direction = get_user_choice()
        if direction == "quit":
            final_game_not_finish()
            break
        elif direction == "score":
            show_score(character)
            continue
        valid_move = validate_move(board, character, direction)
        make_map(rows, columns, character)
        if valid_move:
            move_character(character, direction)
            there_is_a_challenger = check_for_foes(character)
            health_cap(character)
            if there_is_a_challenger and not check_if_reached_boss(rows, columns, character):
                choice_to_fight = fight_or_flee()
                if choice_to_fight:
                    enemy = make_game_enemy(character)
                    fighting_game(character, enemy)
            elif check_if_reached_boss(rows, columns, character):
                choice_to_fight = fight_or_flee()
                if choice_to_fight:
                    boss = make_game_boss(character)
                    boss_game(character, boss)
                    achieved_goal = boss_dead(character, boss)
            if character['Health'] <= 0:
                continue
            describe_current_location(board, character)
        else:
            invalid_move()
    if achieved_goal:
        final_message_finish()


def main():
    """Drives the program."""
    game()


if __name__ == "__main__":
    main()
