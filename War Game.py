# War
# Dev1
# Robert Ball
# Object oriented program to play the classic card game of war


import random


class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    # The two values of None were inserted so that the numbers would agree with their place in the list
    # for example "2" is in position 2 and "3" is in 3 and so on.
    values = [None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    # Standard init
    def __init__(self, v, s):
        self.value = v
        self.suit = s

    # This allows you to over ride the value so you can directly print the object
    def __repr__(self):
        v = self.values[self.value] + \
            " of " + \
            self.suits[self.suit]
        return v

    # Override the less than function
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        else:
            return False

    # Override the greater than function
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        else:
            return False


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    def deal(self, p1, p2):
        if len(self.cards) == 0:  # this should never happen
            return False
        while len(self.cards) > 1:
            print(len(self.cards))
            p1.addCard(self.cards.pop())
            print(len(self.cards))
            p2.addCard(self.cards.pop())
        return True


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)

    def cardsLeft(self):
        return len(self.hand)

    def playCard(self):
        if len(self.hand) == 0:
            print("Error hand should not be empty")
        return self.hand.pop(0)  # default is -1, the end of the list, 0 forces it to be from the front

def War():
    if player1.cardsLeft() < 4 or player2.cardsLeft() < 4:
        if player1.cardsLeft() == 3 or player2.cardsLeft() == 3:
            Pwc1 = player1.playCard()
            Pwc2 = player1.playCard()
            Pwc3 = player1.playCard()
            Cwc1 = player2.playCard()
            Cwc2 = player2.playCard()
            Cwc3 = player2.playCard()
            if Pwc3 > Cwc3:
                player1.addCard(p1C)
                player1.addCard(p2C)
                player1.addCard(Pwc1)
                player1.addCard(Pwc2)
                player1.addCard(Pwc3)
                player1.addCard(Cwc1)
                player1.addCard(Cwc2)
                player1.addCard(Cwc3)
                print(f"{p1Name} took this one. {p1Name} got a {Pwc3} and {p2Name} got a {Cwc3}")
            elif Cwc3 > Pwc3:
                player2.addCard(p1C)
                player2.addCard(p2C)
                player2.addCard(Pwc1)
                player2.addCard(Pwc2)
                player2.addCard(Pwc3)
                player2.addCard(Cwc1)
                player2.addCard(Cwc2)
                player2.addCard(Cwc3)
                print(f"{p2Name} took this one. {p2Name} got a {Cwc3} and {p1Name} got a {Pwc3}")
            else:
                player1.addCard(p1C)
                player2.addCard(p2C)
                player1.addCard(Pwc1)
                player1.addCard(Pwc2)
                player1.addCard(Pwc3)
                player2.addCard(Cwc1)
                player2.addCard(Cwc2)
                player2.addCard(Cwc3)
                print(f"It's another tie!! Each player will get their own cards back."
                      f" {p1Name} got a {Pwc3} and {p2Name} got a {Cwc3}.")

        elif player1.cardsLeft() == 2 or player2.cardsLeft() == 2:
            Pwc1 = player1.playCard()
            Pwc2 = player1.playCard()
            Cwc1 = player2.playCard()
            Cwc2 = player2.playCard()
            if Pwc2 > Cwc2:
                player1.addCard(p1C)
                player1.addCard(p2C)
                player1.addCard(Pwc1)
                player1.addCard(Pwc2)
                player1.addCard(Cwc1)
                player1.addCard(Cwc2)
                print(f"{p1Name} took this one. {p1Name} got a {Pwc2} and {p2Name} got a {Cwc2}")
            elif Cwc2 > Pwc2:
                player2.addCard(p1C)
                player2.addCard(p2C)
                player2.addCard(Pwc1)
                player2.addCard(Pwc2)
                player2.addCard(Cwc1)
                player2.addCard(Cwc2)
                print(f"{p2Name} took this one. {p2Name} got a {Cwc2} and {p1Name} got a {Pwc2}")
            else:
                player1.addCard(p1C)
                player2.addCard(p2C)
                player1.addCard(Pwc1)
                player1.addCard(Pwc2)
                player2.addCard(Cwc1)
                player2.addCard(Cwc2)
                print(f"It's another tie!! Each player will get their own cards back."
                      f" {p1Name} got a {Pwc2} and {p2Name} got a {Cwc2}.")
        else:
            Pwc = player1.playCard()
            Cwc = player2.playCard()
            if Pwc > Cwc:
                player1.addCard(p1C)
                player1.addCard(p2C)
                player1.addCard(Pwc)
                player1.addCard(Cwc)
                print(f"{p1Name} took this one. {p1Name} got a {Pwc} and {p2Name} got a {Cwc}")
            elif Cwc > Pwc:
                player2.addCard(p1C)
                player2.addCard(p2C)
                player2.addCard(Pwc)
                player2.addCard(Cwc)
                print(f"{p2Name} took this one. {p2Name} got a {Cwc} and {p1Name} got a {Pwc}")
            else:
                player1.addCard(p1C)
                player2.addCard(p2C)
                player1.addCard(Pwc)
                player2.addCard(Cwc)
                print(f"It's another tie!! Each player will get their own cards back."
                      f" {p1Name} got a {Pwc} and {p2Name} got a {Cwc}.")
    else:
        Pwc1 = player1.playCard()
        Pwc2 = player1.playCard()
        Pwc3 = player1.playCard()
        Pwc4 = player1.playCard()
        Cwc1 = player2.playCard()
        Cwc2 = player2.playCard()
        Cwc3 = player2.playCard()
        Cwc4 = player2.playCard()
        if Pwc4 > Cwc4:
            player1.addCard(p1C)
            player1.addCard(p2C)
            player1.addCard(Pwc1)
            player1.addCard(Pwc2)
            player1.addCard(Pwc3)
            player1.addCard(Pwc4)
            player1.addCard(Cwc1)
            player1.addCard(Cwc2)
            player1.addCard(Cwc3)
            player1.addCard(Cwc4)
            print(f"{p1Name} took this one. {p1Name} got a {Pwc4} and {p2Name} got a {Cwc4}")
        elif Cwc4 > Pwc4:
            player2.addCard(p1C)
            player2.addCard(p2C)
            player2.addCard(Pwc1)
            player2.addCard(Pwc2)
            player2.addCard(Pwc3)
            player2.addCard(Pwc4)
            player2.addCard(Cwc1)
            player2.addCard(Cwc2)
            player2.addCard(Cwc3)
            player2.addCard(Cwc4)
            print(f"{p2Name} took this one. {p2Name} got a {Cwc4} and {p1Name} got a {Pwc4}")
        else:
            player1.addCard(p1C)
            player2.addCard(p2C)
            player1.addCard(Pwc1)
            player1.addCard(Pwc2)
            player1.addCard(Pwc3)
            player1.addCard(Pwc4)
            player2.addCard(Cwc1)
            player2.addCard(Cwc2)
            player2.addCard(Cwc3)
            player2.addCard(Cwc4)
            print(f"It's another tie!! Each player will get their own cards back."
                  f" {p1Name} got a {Pwc4} and {p2Name} got a {Cwc4}.")



myDeck = Deck()
player1 = Player('Bob')
player2 = Player('Computer')

myDeck.deal(player1, player2)

p1Name = player1.name
p2Name = player2.name

print(f"Welcome {p1Name}, you are playing against the computer \n")
print('Shuffling..........')
print('Dealing.............')
while player1.cardsLeft() > 0 and player2.cardsLeft() > 0:
    response = input('Press Enter to Continue, Q to quit')
    p1C = player1.playCard()
    p2C = player2.playCard()
    if response.upper() == 'Q':
        break

    if p1C > p2C:
        player1.addCard(p1C)
        player1.addCard(p2C)
        print(f"{p1Name} took this one. {p1Name} got a {p1C} and {p2Name} got a {p2C}")
    elif p2C > p1C:
        player2.addCard(p1C)
        player2.addCard(p2C)
        print(f"{p2Name} took this one. {p2Name} got a {p2C} and {p1Name} got a {p1C}")
    else:
        print(f"It was a Tie!! {p1Name} got a {p1C} and {p2Name} got a {p2C}. Time for a War!")
        War()

    print(f"{p1Name} has {player1.cardsLeft()} cards left, {p2Name} has {player2.cardsLeft()}")
