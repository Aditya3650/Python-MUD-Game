"""
Your name: Aditya Singh Attri
Your student number: A01276335

All of your code must go in this file.
"""

import random


def make_board(rows, columns):
    """
    Make a game board with coordinates and their descriptions.

    A function which takes rows and columns as inputs and creates a game board with random description for each of the
    coordinates.

    :param rows: A positive int
    :param columns: A positive int
    :precondition: Both the parameters must be positive integers equal to or greater than two.
    :postcondition: The function returns a dictionary with all the coordinates till 1 less than the specified rows and
    columns in a tuple as keys. Their values are random room descriptions from a specified list of room descriptions.
    Also, the first and last set of coordinates are given some other unique values.
    :return: A dictionary of board coordinates as keys and room description as values.
    """
    room_types = ['the student lounge', 'an empty classroom', 'one of the elevators']
    board_map = {}
    for x_coordinate in range(rows):
        for y_coordinate in range(columns):
            board_map[(x_coordinate, y_coordinate)] = random.choice(room_types)
    board_map[(0, 0)] = "the lobby of BCIT"
    board_map[(rows - 1, columns - 1)] = 'the washroom'
    return board_map


def make_character():
    """
    Assign character information to a variable.

    A function to assign character information which include X-coordinate, Y-coordinate and the HP (Hit-Points) as keys
    of the character.

    :postcondition: The function assigns a dictionary of X and Y coordinates and the HP of the character.
    :return: A dictionary of X and Y coordinates and the HP.

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 5}
    """
    character_info = {'X-coordinate': 0, 'Y-coordinate': 0, 'Level': 1, 'Current-XP': 0, 'Level-Up-XP': 1000}
    return character_info


def input_name():
    champion_name = input("Enter the name for your champion: ")
    return champion_name


def choose_class():
    print("""Type the class you want to choose
    Type 1 for Paladin 
    Type 2 for Warrior
    Type 3 for Shaman
    Type 4 for Rogue""")
    while True:
        class_choice = input().lower()
        if class_choice == "1":
            print("You are a Paladin")

            break
        elif class_choice == "2":
            print("You are a Warrior")

            break
        elif class_choice == "3":
            print("You are a Shaman")

            break
        elif class_choice == "4":
            print("You are a Rogue")

            break
        else:
            print("Enter a valid number to choose a class")
    return int(class_choice)


def xp_checker(character, base_health, base_damage):
    if character['Current-XP'] > character['Level-Up-XP']:
        character['Level'] += 1
        character['Current-XP'] -= 1000
        character['Health'] += base_health / 10
        character['Max_Health'] += base_health / 10
        character['Damage'] += base_damage / 10
        print(f"""You have levelled up
You are now level {character['Level']}
Your current Health is {character['Health']}
XP required to level up is {character['Level-Up-XP'] - character['Current-XP']}""")


def health_cap(character):
    if character['Health'] > character['Max_Health']:
        character['Health'] = character['Max_Health']


def set_class(class_name, character):
    if class_name == 1:
        character['Class'] = 'Paladin'
    elif class_name == 2:
        character['Class'] = 'Warrior'
    elif class_name == 3:
        character['Class'] = 'Shaman'
    elif class_name == 4:
        character['Class'] = 'Rogue'


def set_health(character):
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


def set_damage(character):
    if character['Class'] == 'Paladin':
        character['Damage'] = 95
    elif character['Class'] == 'Warrior':
        character['Damage'] = 80
    elif character['Class'] == 'Shaman':
        character['Damage'] = 110
    elif character['Class'] == 'Rogue':
        character['Damage'] = 120


def class_level(character):
    paladin = ['Paladin1', 'Paladin2', 'Paladin3']
    warrior = ['Warrior1', 'Warrior2', 'Warrior3']
    shaman = ['Shaman1', 'Shaman2', 'Shaman3']
    rogue = ['Rogue1', 'Rogue2', 'Rogue3']
    if character['Class'] == 'Paladin':
        character['Class_Level'] = paladin[character['Level'] - 1]
    elif character['Class'] == 'Warrior':
        character['Class_Level'] = warrior[character['Level'] - 1]
    elif character['Class'] == 'Shaman':
        character['Class_Level'] = shaman[character['Level'] - 1]
    elif character['Class'] == 'Rogue':
        character['Class_Level'] = rogue[character['Level'] - 1]


def special_attack(character):
    paladin = ['PaladinAtk1', 'PaladinAtk2', 'PaladinAtk3']
    warrior = ['WarriorAtk1', 'WarriorAtk2', 'WarriorAtk3']
    shaman = ['ShamanAtk1', 'ShamanAtk2', 'ShamanAtk3']
    rogue = ['RogueAtk1', 'RogueAtk2', 'RogueAtk3']
    if character['Class'] == 'Paladin':
        character['Special_Attack'] = paladin[character['Level'] - 1]
    elif character['Class'] == 'Warrior':
        character['Special_Attack'] = warrior[character['Level'] - 1]
    elif character['Class'] == 'Shaman':
        character['Special_Attack'] = shaman[character['Level'] - 1]
    elif character['Class'] == 'Rogue':
        character['Special_Attack'] = rogue[character['Level'] - 1]


def special_attack_effect(character, enemy):
    if character['Class'] == 'Paladin':
        character['Health'] += character['Max_Health'] / 30
    elif character['Class'] == 'Warrior':
        character['Damage'] += character['Damage'] / 10
    elif character['Class'] == 'Shaman':
        enemy['Enemy_Health'] -= character['Max_Health'] / 20
    elif character['Class'] == 'Rogue':
        enemy['Enemy_Damage'] -= character['Damage'] / 10
    character['Health'] += 10


def is_alive(character):
    """
    Checks if the character does not have 0 HP.

    :param character: A dictionary
    :precondition: The parameter must be a dictionary with keys of X and Y coordinate as well as the HP of the
    character.
    :postcondition: Return False if the HP is 0. Otherwise, return True.
    :return: A boolean value

    >>> gamer = {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 5}
    >>> is_alive(gamer)
    True

    >>> gamer = {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 0}
    >>> is_alive(gamer)
    Sorry, you died to over-examination :(
    False
    """
    if character['Health'] != 0:
        print(f"Your current Health is {character['Health']}")
        return True
    else:
        print("Sorry, you died to over-examination :(")
        return False


def describe_current_location(board, character):
    """
    Describe the current location of the character.

    A function to give the room description and the current coordinates of the character.

    :param board: A dictionary
    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate as well as the HP of the
    character. The board parameter must be a dictionary of the coordinates as keys and their description as values.
    :postcondition: The function prints the current coordinates and its description.

    # Only 2 cases where the rooms are not random
    >>> game_board = make_board(3, 3)
    >>> gamer = make_character()
    >>> describe_current_location(game_board, gamer)
    You are in the lobby of BCIT at (0, 0)

    >>> game_board_2 = make_board(4, 4)
    >>> char_info = {'X-coordinate': 3, 'Y-coordinate': 3, 'HP': 2}
    >>> describe_current_location(game_board_2, char_info)
    You are in the washroom at (3, 3)
    """
    current_coordinates = (character['X-coordinate'], character['Y-coordinate'])
    champion_name = character['champion_name']
    print(f"{champion_name} is in {board[current_coordinates]} at {current_coordinates}")


def get_user_choice():
    """
    Take user input for the direction.

    A function to take input from the user for selecting the direction the character will move.

    :postcondition: Print a set of instructions assigning a number to each direction. After the user selects a number,
    print the direction the character moves. If the input is not a valid number, the function repeats itself till the
    user inputs a valid number.
    :return: The user choice type converted to integer.
    """
    print("""\nEnter the direction you wish to go 
    Press 1 to go North 
    Press 2 to go East 
    Press 3 to go South 
    Press 4 to go West
    Type 'quit' to stop playing, for now ;)""")
    while True:
        user_choice = input()
        if user_choice == "1":
            print("You are moving North")
            break
        elif user_choice == "2":
            print("You are moving East")
            break
        elif user_choice == "3":
            print("You are moving South")
            break
        elif user_choice == "4":
            print("You are moving West")
            break
        elif user_choice.lower() == "quit":
            break
        else:
            print("Enter a valid number")
    return user_choice


def validate_move(board, character, direction):
    """
    Check if the requested move can be performed or not

    A function to check if the move requested by the user stays in the boundary of the already established board.

    :param board: A dictionary
    :param character: A dictionary
    :param direction: A positive int
    :precondition: The board parameter must be a dictionary of the coordinates as keys and their description as values.
    The character parameter must be a dictionary with keys of X and Y coordinate as well as the HP of the character. The
    direction parameter must be a positive integer between 1 and 4. It will represent the 4 directions.
    :postcondition: Return the boolean value True if the requested move is possible and False if it is not.
    :return: A boolean value

    >>> game_board = make_board(3, 3)
    >>> gamer = make_character()
    >>> direction_move = 3
    >>> validate_move(game_board, gamer, direction_move)
    True

    >>> game_board = make_board(3, 3)
    >>> gamer = make_character()
    >>> direction_move = 1
    >>> validate_move(game_board, gamer, direction_move)
    False

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
    invalid_reasons = ['Oh no, there is a wall there.', 'The floor is wet there.', 'You are at a dead-end.']
    print(random.choice(invalid_reasons) + " Move in some other direction.")


def move_character(character, direction):
    """
    Update the character information whenever a valid move is made.

    A function to update the stored coordinates of the character in character information whenever a valid move is made
    by the user.

    :param character: A dictionary
    :param direction: A positive int
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate as well as the HP of the
    character. The direction parameter must be a positive integer between 1 and 4. It will represent the 4 directions.
    :postcondition: Change the coordinates according to the move made by the user in the character information
    dictionary.

    >>> gamer = make_character()
    >>> direction_move = 2
    >>> move_character(gamer, direction_move)
    >>> gamer
    {'X-coordinate': 1, 'Y-coordinate': 0, 'HP': 5}


    >>> gamer = make_character()
    >>> direction_move = 3
    >>> move_character(gamer, direction_move)
    >>> gamer
    {'X-coordinate': 0, 'Y-coordinate': 1, 'HP': 5}
    """
    if direction == "1":
        character['Y-coordinate'] += 1
    elif direction == "2":
        character['X-coordinate'] += 1
    elif direction == "3":
        character['Y-coordinate'] -= 1
    elif direction == "4":
        character['X-coordinate'] -= 1
    character['Health'] += 10
    character['Current-XP'] += 20


def check_for_foes():
    """
    Check if there is an enemy on the coordinate.

    A function to randomly generate an enemy on a set of coordinates. The chances for generating the enemy is a 25%.

    :postcondition: Generate an enemy on the coordinate. There is a one in four chance for the enemy to generate. Return
    True if the enemy is generated. Otherwise, return False.
    :return: A boolean value
    """
    foe_checker = random.randint(1, 5)
    if foe_checker == 1:
        print("""\nAlas, you have encountered a foe.
Answer the pop python quiz or lose your life.\n""")
        return True
    else:
        print("There is no one here.")
        return False


def fight_or_flee():
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


def guessing_game_select(character):
    """
    Guess the number.

    A function to ask the user to guess a number between 1 and 5.

    :param character: A dictionary
    :precondition: The character parameter must be a dictionary with keys of X and Y coordinate as well as the HP of the
    character. The value entered must be between 1 and 5.
    :postcondition: Print different set of statements if the user correctly guesses the answer or not. The character
    loses 1 HP if the answer is incorrect.
    """
    secret_number = random.randint(1, 5)
    guess = input(f"Enter an option between 1 and 5 (both inclusive):\n ")
    if guess == secret_number:
        print("\nYou're right! Chris gifts you a LEGO set.")
        character['Health'] += 200
    else:
        character['Health'] -= 100
        print(f"""\nWrong option, the correct answer was option {secret_number}.
Your current health is {character['Health']}""")
    character['Current-XP'] += 100
    health_cap(character)


def guessing_game(character):
    print("""You come across the Bloodmage Thalnos.
    Answer correctly and get life.
    Answer wrongly and pay with blood.\n""")
    while character['Health'] != 0:
        guessing_game_select(character)
        if character['Health'] == 0:
            break
        print("""\nDo you still wish to fight the foe?
Press 1 to Fight
Press 2 to Flee""")
        user_choice = input()
        if user_choice == "1":
            print("You decide to continue to fight the foe")
        else:
            print("You decide to flee from the foe mid-battle")
            break
    character['Current-XP'] += 300


def enemy_flee():
    flee = random.randint(1, 5)
    if flee == 1:
        print("Enemy has fled")
        return True


def make_game_enemy(character):
    return {'Enemy_Health': character['Max_Health'] / 2, 'Enemy_Damage': character['Damage'] / 2}


def fighting_game_damage(character, enemy):
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


def enemy_flee_damage(character, enemy):
    flee = random.randint(1, 5)
    if flee == 1:
        character['Health'] -= enemy['Enemy_Damage']
        print("You were damaged while fleeing the battle")


def fighting_game(character, enemy):
    while character['Health'] != 0 and enemy['Enemy_Health'] != 0:
        special_attack_effect(character, enemy)
        fighting_game_damage(character, enemy)
        check_enemy_flee = enemy_flee()
        if check_enemy_flee:
            break
        if character['Health'] <= 0 or enemy['Enemy_Health'] <= 0:
            break
        print("""\nDo you still wish to fight the foe?
    Press 1 to Fight
    Press 2 to Flee""")
        user_choice = input()
        if user_choice == "1":
            print("You decide to continue to fight the foe")
        else:
            enemy_flee_damage(character, enemy)
            print("You decide to flee from the foe mid-battle")
            break
    character['Current-XP'] += 400


def game_select(character, enemy):
    game_list = [guessing_game, fighting_game]
    random_game = random.choice(game_list)
    if random_game == game_list[0]:
        guessing_game(character)
    else:
        fighting_game(character, enemy)


def make_game_boss(character):
    print("You face the boss")
    return {'Enemy_Health': round(character['Max_Health'] * 2.5), 'Enemy_Damage': round(character['Damage'] * 1.25)}


# def boss_game_damage(character, boss):
#     enemy_hit = random.randint(0, 1)
#     character_hit = random.randint(0, 1)
#     if enemy_hit == 1 and character_hit == 1:
#         boss['Enemy_Health'] -= round(character['Damage'])
#         character['Health'] -= round(boss['Enemy_Damage'])
#         print("You both attack each other")
#     elif enemy_hit == 0 and character_hit == 1:
#         boss['Enemy_Health'] -= round(character['Damage'])
#         print("Your enemy misses an attack but you hurt him")
#     elif enemy_hit == 1 and character_hit == 0:
#         character['Health'] -= round(boss['Enemy_Damage'])
#         print("You miss your attack but your enemy lands a blow")
#     elif enemy_hit == 0 and character_hit == 0:
#         print("Both of you miss your attacks")
#     health_cap(character)
#     print(f"Your health is {round(character['Health'])} and your enemy has {round(boss['Boss_Health'])} remaining.")
#
#
# def boss_flee_damage(character, enemy):
#     flee = random.randint(1, 5)
#     if flee == 1:
#         character['Health'] -= enemy['Boss_Damage'] * 2
#         print("You were damaged while fleeing the battle")
#
#
def boss_game(character, boss):
    while character['Health'] != 0 and boss['Enemy_Health'] != 0:
        special_attack_effect(character, boss)
        fighting_game_damage(character, boss)
        if character['Health'] <= 0 or boss['Enemy_Health'] <= 0:
            break
        print("""\nDo you still wish to fight the foe?
    Press 1 to Fight
    Press 2 to Flee""")
        user_choice = input()
        if user_choice == "1":
            print("You decide to continue to fight the foe")
        else:
            print("You decide to flee from the foe mid-battle")
            break
    character['Current-XP'] += 400


def boss_dead(character, boss):
    if boss['Enemy_Health'] <= 0 and character['Health'] > 0:
        print('Boss is Dead')
        return True
    else:
        return False


def check_if_reached_boss(rows, columns, character):
    """
    Check if the character has reached the final coordinates.

    :param rows: A positive int
    :param columns: A positive int
    :param character: A dictionary
    :precondition: Both the parameters must be positive integers equal to or greater than two. The character parameter
    must be a dictionary with keys of X and Y coordinate as well as the HP of the character.
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
    print("Congratulations, you have found the washroom, finally! Thanks for playing the game!")


def final_game_not_finish():
    print("Thanks for playing this game, come again later!")


def game():
    """Drive the main game loop."""
    print("\nYou have arrived at BCIT but you're feeling queasy. Find your way to the washroom. FAST!")
    rows = 6
    columns = 6
    board = make_board(rows, columns)
    character = make_character()
    character['champion_name'] = input_name()
    class_name = choose_class()
    set_class(class_name, character)
    class_level(character)
    set_health(character)
    set_damage(character)
    base_health = character['Health']
    base_damage = character['Damage']
    special_attack(character)
    print(character)
    describe_current_location(board, character)
    achieved_goal = False
    while is_alive(character) and not achieved_goal:
        xp_checker(character, base_health, base_damage)
        direction = get_user_choice()
        if direction == "quit":
            final_game_not_finish()
            break
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_foes()
            health_cap(character)
            if there_is_a_challenger:
                choice_to_fight = fight_or_flee()
                if choice_to_fight and not check_if_reached_boss(rows, columns, character):
                    enemy = make_game_enemy(character)
                    game_select(character, enemy)
            if check_if_reached_boss(rows, columns, character):
                choice_to_fight = fight_or_flee()
                if choice_to_fight:
                    boss = make_game_boss(character)
                    boss_game(character, boss)
                    achieved_goal = boss_dead(character, boss)
            if character['Health'] == 0:
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
