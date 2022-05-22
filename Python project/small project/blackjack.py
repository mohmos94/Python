import random

card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
player_card = []
computer_card = []

computer_money = 200

player_money = int(input("Enter your money: "))
bet = int(input("how much do you wanna bet on this round: "))


def deck():
    copy_card_list = card.copy() * 3

    card.extend(copy_card_list)

    random.shuffle(card)


deck()


def extra_cards():
    more_cards = input("do you want more card? Enter yes or no: ")
    if more_cards == "yes":
        cards = random.choice(card)
        card.remove(cards)
        player_card.append(cards)
        print(player_card)
        extra_cards()
    else:
        return -1


# game player and computer
def player_hand():
    print("player hands")

    # choice a random card from the list

    firste_card = random.choice(card)
    second_card = random.choice(card)

    # delete the card from the list

    card.remove(firste_card)
    card.remove(second_card)

    # send it inside the list

    player_card.append(firste_card)
    player_card.append(second_card)

    print(player_card)

    for element in range(len(player_card)):
        if player_card[element] == 11:
            card_value = int(input("enter 1 or 11 to change A value: "))
            player_card[element] = card_value
            print(player_card)

    extra_cards()

    player_value = 0

    for elements in player_card:
        player_value += elements

    print(player_value)

    return player_value


# computer turn
def computer_hand():
    print("computer hands")

    # choice a random card from the list

    firste_computer_card = random.choice(card)
    second_computer_card = random.choice(card)

    # delete the card from the list

    card.remove(firste_computer_card)
    card.remove(second_computer_card)

    # send it inside the list

    computer_card.append(firste_computer_card)
    computer_card.append(second_computer_card)

    print(computer_card)

    # value from the card

    computer_value = firste_computer_card + second_computer_card

    print(computer_value)

    for element in range(len(computer_card)):
        if computer_card[element] == 11:
            computer_answer = int(input("enter 1 or 11 to for A value: "))
            computer_card[element] = computer_answer
            print(computer_card)

    return computer_value


while True:
    print("lets play black jack")

    player_hands_value = player_hand()

    computer_hands_value = computer_hand()

    if player_hands_value == 21 and computer_hands_value != 21:
        computer_money -= bet
        player_money += bet
        print("player wins {} player has {} total".format(bet, player_money))
    elif computer_hands_value < player_hands_value <= 21:
        computer_money -= bet
        player_money += bet
        print("player wins {} player has {} total".format(bet, player_money))
    elif computer_hands_value > 21:
        computer_money -= bet
        player_money += bet
        print("player wins {} player has {} total".format(bet, player_money))
    elif player_hands_value > 21:
        computer_money += bet
        player_money -= bet
        print("computer wins {} computer has {} total".format(bet, computer_money))
    elif player_hands_value < computer_hands_value <= 21:
        computer_money += bet
        player_money -= bet
        print("computer wins {} computer has {} total".format(bet, computer_money))
    elif computer_hands_value == 21 and computer_hands_value != 21:
        computer_money += bet
        computer_hands_value -= bet
        print("computer wins {} computer has {} total".format(bet, computer_money))
    elif player_hands_value == 21 and computer_hands_value == 21:
        print("draw wins")

    answer = input("do you wanna play one more round yes or no: ")

    if answer == "yes":
        player_card.clear()
        computer_card.clear()
        print("thank you your total value right know is: ".format(player_money))
    else:
        exit()
