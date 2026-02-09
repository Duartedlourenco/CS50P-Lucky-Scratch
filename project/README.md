# **Lucky Scratch** 

### Video Demo: [CS50P Lucky Scratch](https://youtu.be/Agf83Jbu__I)

## Description

Lucky Scratch is a terminal-based game developed in Python as the final project for CS50's Introduction to Programming with Python. The program simulates scratch-card and risk-based betting mechanics where the player manages a virtual balance, places bets, and plays different mini-games to win or lose money.

The game runs entirely in the terminal and uses menus to guide the user through the available options. The player can deposit or withdraw money, play two different game modes, read information about the project, or exit the program.

The goal of this project is to apply the programming concepts learned throughout the course in a complete, interactive application.

## Game Mechanics

### Classic Mode – Scratch Card System

The Classic mode generates five random symbols and calculates winnings by counting matching symbols and applying predefined multipliers stored in a dictionary. If three or more identical symbols appear, the player wins according to the symbol’s payout value:

```
def calculate_classic_win(symbols, bet, values):
    for s in set(symbols):
        if symbols.count(s) >= 3:
            return bet * values[s]
    return 0
```

**Symbol Values:**
```
Symbol              Multiplier
------------------------------- 
🍋 Lemon               2x 
🍉 Watermelon          3x 
🍒 Cherry              4x 
⭐ Star                6x 
🔥 Fire                10x 
💎 Diamond             20x 
🍀 Clover              50x 
```

### Bomb Mode – Progressive Risk System

In the Bomb mode, the player reveals tiles on a 5x5 grid while avoiding a hidden bomb. Each safe move increases a multiplier that grows the potential prize. The player may cash out at any time or continue risking the bet for higher rewards. Revealing the bomb results in losing the entire bet.

The pot represents the current payout value in order of the bet amount and the number of tiles already revealed:

```
def calculate_bomb_pot(bet, moves, multipliers):
    if moves < 0 or moves >= len(multipliers):
        raise ValueError("Invalid move number!")
    return int(round(bet * multipliers[moves], 3))
```

The multiplers values are stored in a list:

```
multipliers = [0, 1.01, 1.05, 1.10, 1.15, 1.21, 1.27, 1.34, 1.42, 1.51, 1.61, 1.73, 1.86, 2.02, 2.20, 2.42, 2.69, 3.03, 3.46, 4.04, 4.85, 6.06, 8.08, 12.12, 24.24]
```

## Important Libraries

Several Python libraries are used in the program to implement a fully interactive terminal-based betting game. The following libraries were essential to ensure that the program could execute its core mechanics and visuals.

The external library ```pyfiglet``` is used to render ASCII art text in the terminal. It is responsible for displaying the game title “Lucky Scratch” at the top of every screen using a slant font.

A built-in ```random``` library is used to generate different outcomes for both games. In the Classic mode, random symbols are selected to simulate a scratch card. In the Bomb mode, a random grid position is generated to represent the hidden bomb.

The ```time``` library is used to create small delays using the sleep() function. These delays simulate scratching animations, reveal results and errors.

The ```os``` library is used to control the terminal environment. Using ```os.system('cls' if os.name == 'nt' else 'clear')``` allows to clear the terminal between menus and games. This prevents clutter and keeps everything clean and readable.

To exit the program it is used ```sys.exit()``` from the ```sys``` library.

## Program Logic

All menus use a Match Case Statement to catch the desired option and execute the corresponding function.

To play a game, the player must first deposit a desired amount and it was to be higher than 0. After that, the balance will update with the sum of the deposited amount.  

When a player wants to place a bet, either Classic or Bomb mode, it is presented with a bet requirement:

1. If the bet is not a digit / lower or equal to 0 / higher than the current balance, it will return a error message.

2. If the bet is valid it will initiate the selected game. If the player wins, the prize will be calculated based on the bet amount and the specific game multiplier.

In case the player is satisfied with the current amount, a withdraw option is available, following the same principles as the deposit:

1. If the withdraw amount is not a digit / lower or equal to 0 / higher than the current balance, it will return a error message.

2. If the withdraw is valid, the current balance will be subtracted by the withdrew value.

## Project Files

- ```project.py``` is main file of the application.

- ```README.md``` explains how to project works.

- ```requirements.txt``` lists external dependencies required to run the project.

- ```test_project.py``` contains tested functions used in the project.

## TODO

In the project folder install the requirements:

```
pip install -r requirements.txt
```

Run the program:

```
python project.py
```

Test the functions using pytest:

```
pytest test_project.py
```
