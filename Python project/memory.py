# Memory game the objective of the game is to collect most of the pared number.

# Libraries

import random
from tabulate import tabulate
import numpy as np

# global variable

item = ["APPLE", "BANANA", "CHERRY", "ORANGE", "WATERMELON", "BLUEBERRY", "APPLE", "BANANA", "CHERRY", "ORANGE",
        "WATERMELON", "BLUEBERRY"]

board_layout = []


# function for the board

def board():
    random.shuffle(item)
    board_layout.append(item[0:3].copy())
    board_layout.append(item[3:6].copy())
    board_layout.append(item[6:9].copy())
    board_layout.append(item[9:12].copy())

    index_board = list(range(0, len(item)))
    table_index = np.array_split(index_board, 4)

    print("Fruit based table")
    print(tabulate(board_layout))
    print("We are going to use the index value")
    random.shuffle(table_index)

    print(tabulate(table_index))


def game():
    # ORANGE = 1, 6
    # APPLE = 2, 7
    # BANANA = 3, 8
    # CHERRY = 4, 9
    # WATERMELON = 5, 10
    # BLUEBERRY = 0, 11

    lister = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    zero = lister.index(1)
    one = lister.index(1)
    two = lister.index(2)
    three = lister.index(3)
    four = lister.index(4)
    five = lister.index(5)
    six = lister.index(6)
    seven = lister.index(7)
    eight = lister.index(8)
    nine = lister.index(9)
    ten = lister.index(10)
    eleven = lister.index(11)
    life = 3
    count = 0
    player = (input("Enter player name: "))
    while life >= 0:

        firste_number = int(input("player  choice number: "))
        second_number = int(input("player  choice number: "))

        if firste_number == one and second_number == six:
            print("Congrats you found ORANGE")
            count+=1
            lister.remove(1)
            lister.remove(6)
            print(lister)
        elif firste_number == two and second_number == seven:
            print("Congrats you found APPLE")
            count += 1
            lister.remove(2)
            lister.remove(7)
            print(lister)
        elif firste_number == three and second_number == eight:
            print("Congrats you found BANANA")
            count += 1
            lister.remove(3)
            lister.remove(8)
            print(lister)
        elif firste_number == four and second_number == nine:
            print("Congrats you found CHERRY")
            count += 1
            lister.remove(4)
            lister.remove(9)
            print(lister)
        elif firste_number == five and second_number == ten:
            print("Congrats you found WATERMELON")
            count += 1
            lister.remove(5)
            lister.remove(10)
            print(lister)
        elif firste_number == zero and second_number == eleven:
            count += 1
            lister.remove(0)
            lister.remove(11)
            print(lister)
            print("Congrats you found BLUBBERY")
        else:
            print("wrong you have {}".format(life))
            print("you have {} point".format(count))
            print(lister)
            life -= 1


    if len(lister) == 0:
        print("game ended well done {}".format(count))

game()
