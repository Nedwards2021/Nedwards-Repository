######################################
# Opening Comments
# Author: Nathaniel Edwards
# 3/4/21
# Card Game
######################################

import PySimpleGUI as sg
import random


class Cards:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

class Player:
    def __init__(self, Card, cardsleft, cardswon):
        self.Card = Card
        self.CardsLeft = cardsleft
        self.cardswon = cardswon


class Computer:
    def __init__(self, Ccard, Ccardsleft, Ccardswon):
        self.Ccard = Ccard
        self.Ccardsleft = Ccardsleft
        self.Ccardswon = Ccardswon


layout = [[sg.Text('War Card Game', relief='sunken', font=('Any', 16), enable_events=True, key='-Text-')],
          [sg.MLine(size=(60, 10), key='-Response-', reroute_stdout=True, auto_refresh=True, disabled=True,
                    do_not_clear=True)],
          [sg.Button('submit', bind_return_key=True, key = '-submit-')]]

window = sg.Window('Card Game', layout, finalize=True)

Cardnums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#11=Jack, 12=Queen, 13=King, 14=Ace, 15=Joker
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        window.close()
        break
    if event == '-submit-':
        card1 = random(Cardnums)
        card2 = random(Cardnums)