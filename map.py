import itertools
import random

# def guess_list():
#     guess_coordinate_list = [(4, 4), (4, 9), (4, 15), (4, 20), (9, 4), (9, 9), (9, 15), (9, 20), (15, 4), (15, 9),
#                              (15, 15), (15, 20), (20, 4), (20, 9), (20, 15), (20, 20)]
#     return guess_coordinate_list
#
#
# def guess_2():
#     guess_lists = [4, 9, 15, 20]
#     guess_coordinates_list = itertools.product(guess_lists, guess_lists)
#     return list(guess_coordinates_list)

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
    room_types = ['on the streets of Stormwind', 'over the ashes of Outland', 'outside the Scholomance Academy',
                  'lost in the catacombs of Uldum']
    board_map = {(x_coordinate, y_coordinate): random.choice(room_types) for x_coordinate in range(rows)
                 for y_coordinate in range(columns)}
    # for x_coordinate in range(rows):
    #     for y_coordinate in range(columns):
    #         board_map[(x_coordinate, y_coordinate)] = random.choice(room_types)
    board_map[(0, 0)] = "on the way to find Gul'dan, the Warlock"
    board_map[(rows - 1, columns - 1)] = "at the foot of the Blackrock Mountain, the lair of Gul'dan"
    return board_map


def main():
    """Drives the program."""

    print(make_board(5, 5))


if __name__ == "__main__":
    main()
