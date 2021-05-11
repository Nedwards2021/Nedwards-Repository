######################################
# Opening Comments
# Author: Nathaniel Edwards
# 3/18/21
#Dice Game
######################################

import random
import time
import os

def CheckDiceRolls(PlayerRoll,ComputerRoll):
    if PlayerRoll == 1:
        PlayerDiceCount['1'] = PlayerDiceCount['1'] + 1
    elif PlayerRoll == 2:
        PlayerDiceCount['2'] = PlayerDiceCount['2'] + 1
    elif PlayerRoll == 3:
        PlayerDiceCount['3'] = PlayerDiceCount['3'] + 1
    elif PlayerRoll == 4:
        PlayerDiceCount['4'] = PlayerDiceCount['4'] + 1
    elif PlayerRoll == 5:
        PlayerDiceCount['5'] = PlayerDiceCount['5'] + 1
    else:
        PlayerDiceCount['6'] = PlayerDiceCount['6'] + 1

    if ComputerRoll == 1:
        ComputerDiceCount['1'] = ComputerDiceCount['1'] + 1
    elif ComputerRoll == 2:
        ComputerDiceCount['2'] = ComputerDiceCount['2'] + 1
    elif ComputerRoll == 3:
        ComputerDiceCount['3'] = ComputerDiceCount['3'] + 1
    elif ComputerRoll == 4:
        ComputerDiceCount['4'] = ComputerDiceCount['4'] + 1
    elif ComputerRoll == 5:
        ComputerDiceCount['5'] = ComputerDiceCount['5'] + 1
    else:
        ComputerDiceCount['6'] = ComputerDiceCount['6'] + 1


PlayerDiceCount = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}
ComputerDiceCount = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}
WinLose = {'Player':0, 'Computer':0}

while True:
    Answer = input('Would you like to play/continue? (Y)es or (N)o? You may also (D)isplay the current stats')
    Response = Answer.upper()
    if Response == 'Y':
        PlayerRoll = random.randint(1, 6)
        ComputerRoll = random.randint(1, 6)
        if PlayerRoll > ComputerRoll:
            print(f'The Player won. The Player rolled a {PlayerRoll} and the Computer rolled a {ComputerRoll}')
            WinLose['Player'] = WinLose['Player']+1
            CheckDiceRolls(PlayerRoll, ComputerRoll)
        elif ComputerRoll > PlayerRoll:
            print(f'The Computer won. The Player rolled a {PlayerRoll} and the Computer rolled a {ComputerRoll}')
            WinLose['Computer'] = WinLose['Computer'] + 1
            CheckDiceRolls(PlayerRoll, ComputerRoll)
        else:
            print(f'It\'s a Tie!! The player rolled a {PlayerRoll} and the Computer rolled a {ComputerRoll}')
            CheckDiceRolls(PlayerRoll, ComputerRoll)

        print(f"The Player has won {WinLose.get('Player')} time(s) and the computer has won {WinLose.get('Computer')}"
              f" time(s)")
        print(f"The Player has rolled a 1: {PlayerDiceCount.get('1')} time(s), a 2: {PlayerDiceCount.get('2')} time(s), "
              f"a 3: {PlayerDiceCount.get('3')} time(s), a 4: {PlayerDiceCount.get('4')} time(s), "
              f"a 5: {PlayerDiceCount.get('5')} time(s) and a 6: {PlayerDiceCount.get('6')} time(s).")
        print(f"The Computer has rolled a 1: {ComputerDiceCount.get('1')} time(s), a 2: {ComputerDiceCount.get('2')} time(s),"
              f"a 3: {ComputerDiceCount.get('3')} time(s), a 4: {ComputerDiceCount.get('4')} time(s), "
              f"a 5: {ComputerDiceCount.get('5')} time(s) and a 6: {ComputerDiceCount.get('6')} time(s).")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif Response == 'N':
        print('Thank you for playing.')
        break
    elif Response == 'D':
        print(f"The Player has won {WinLose.get('Player')} time(s) and the computer has won {WinLose.get('Computer')}"
              f" time(s)")
        print(
            f"The Player has rolled a 1: {PlayerDiceCount.get('1')} time(s), a 2: {PlayerDiceCount.get('2')} time(s), "
            f"a 3: {PlayerDiceCount.get('3')} time(s), a 4: {PlayerDiceCount.get('4')} time(s), "
            f"a 5: {PlayerDiceCount.get('5')} time(s) and a 6: {PlayerDiceCount.get('6')} time(s).")
        print(
            f"The Computer has rolled a 1: {ComputerDiceCount.get('1')} time(s), a 2: {ComputerDiceCount.get('2')} time(s),"
            f"a 3: {ComputerDiceCount.get('3')} time(s), a 4: {ComputerDiceCount.get('4')} time(s), "
            f"a 5: {ComputerDiceCount.get('5')} time(s) and a 6: {ComputerDiceCount.get('6')} time(s).")
        time.sleep(10)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('Please input either a Y or N to play/continue or a D to see the current stats.')
        os.system('cls' if os.name == 'nt' else 'clear')