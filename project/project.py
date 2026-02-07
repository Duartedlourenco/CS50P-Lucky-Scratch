from pyfiglet import Figlet
import os
import sys
import random
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def title():
    clear()
    f = Figlet(font='slant')
    print("\n🍒 🍋 🍉 ⭐ 💎 🍀 🔥 🍒 🍋 🍉 ⭐ 💎 🍀 🔥 🍒 🍋 🍉 ⭐ 💎 🍀 🔥 🍒 🍋 🍉")
    print(f.renderText('Lucky Scratch'), end="")
    print("\n🍒 🍋 🍉 ⭐ 💎 🍀 🔥 🍒 🍋 🍉 ⭐ 💎 🍀 🔥 🍒 🍋 🍉 ⭐ 💎 🍀 🔥 🍒 🍋 🍉")

def main_menu(balance):
    print(f"""
                  Welcome to the Lucky Scratch game!
            
                        Current balance: ${balance} 💰

                    * * * * * * * * * * * * * * *  
                    *                           *
                    *   1. 🎰 Scratch           *
                    *                           *
                    *   2. 💵 Manage Balance    *
                    *                           *
                    *   3. ℹ️  Information       *
                    *                           *
                    *   4. 🏃 Exit              *
                    *                           *
                    * * * * * * * * * * * * * * * 
    """)

    number = input("\t\t\t➡  ")
    return number

#************************************************************************************************************#

# SCRATCH MENU OPTIONS

def scratch_menu(balance):
    print(f"""
                Please choose one of the following modes:
              
                        Current balance: ${balance} 💰

                    * * * * * * * * * * * * * * *  
                    *                           *
                    *   1. 🍀 Classic           *
                    *                           *
                    *   2. 💣 Bomb              *
                    *                           *
                    *   3. ↩️  Return            *
                    *                           *
                    * * * * * * * * * * * * * * * 
        """)

    number = input("\t\t\t➡  ")
    return number



def scratch(balance):
    while True:
        title()
        option = scratch_menu(balance)
        match option:
            case "1":
                balance = classic_game(balance)
            case "2":
                balance = bomb_game(balance)
            case "3":
                break
            case _:
                title()
                print("\n\t\t    Please choose a valid option!")
                time.sleep(1)
    return balance



def classic_game(balance):
    while True:
        try:
            title()
            bet = input(f"\n\t\t\tCurrent Balance: ${balance} 💰\n\n\t\t\tPress Ctrl + C to return\n\n\t\t\tBet amount: ")
            
            if not bet.isdigit():
                raise TypeError("Please enter digits only!")
            
            bet = int(bet)
            validate_bet(bet, balance)
            break

        except (TypeError, ValueError) as e:
            title()
            print(f"\n\t\t\t{e}")
            time.sleep(1)
        except KeyboardInterrupt: 
            return balance

    balance -= bet
    symbols = ["🍋", "🍉", "🍒", "⭐", "🔥", "💎", "🍀"]
    values = {"🍋": 2, "🍉": 3, "🍒": 4, "⭐": 6, "🔥": 10, "💎": 20, "🍀": 50}
    
    result = [random.choice(symbols) for _ in range(5)]
    title()
    for dots in [".", "..", "..."]:
        print(f"\n\t\t\t   Scratching{dots}")
        time.sleep(0.5)
        title()
    print(f"\n\t\t\t[ {' |'.join(result)} ]")
    
    win = calculate_classic_win(result, bet, values)

    if win > 0:
        balance += win
        input(f"\n\t\t\t🎉 YOU WON ${win}!\n\n\t\t\tPress Enter to return...")
    else:
        input("\n\t\t\tNo luck this time.\n\n\t\t\tPress Enter to return...")

    
    return balance

def calculate_classic_win(symbols, bet, values):
    for s in set(symbols):
        if symbols.count(s) >= 3:
            return bet * values[s]
    return 0

def validate_bet(bet, balance):
    if bet <= 0:
        raise ValueError("Invalid bet amount!")
    if bet > balance:
        raise ValueError("Insufficient balance!")
    return True


def bomb_game(balance):
    while True:
        try:
            title()
            bet = input(f"\n\t\t\tCurrent Balance: ${balance} 💰\n\n\t\t\tPress Ctrl + C to return\n\n\t\t\tBet amount: ")
            
            if not bet.isdigit():
                raise TypeError("Please enter digits only!")
            
            bet = int(bet)
            validate_bet(bet, balance)
            break

        except (TypeError, ValueError) as e:
            title()
            print(f"\n\t\t\t{e}")
            time.sleep(1)

        except KeyboardInterrupt: 
            return balance

    balance -= bet

    bomb_pos = (random.randint(1, 5), random.randint(1, 5))
    revealed = []
    current_move = 0
    multipliers = [0, 1.01, 1.05, 1.10, 1.15, 1.21, 1.27, 1.34, 1.42, 1.51, 1.61,
                  1.73, 1.86, 2.02, 2.20, 2.42, 2.69, 3.03, 3.46, 4.04, 4.85,
                  6.06, 8.08, 12.12, 24.24]

    while True:
        title()
        pot = calculate_bomb_pot(bet, current_move, multipliers)

        if len(revealed) == 24:  
            title()       
            print(f"\n\t\t🎉 CONGRATULATIONS! You revealed all safe tiles!!\n\n\t\t💰 Cashing out with ${pot}")
            balance += pot
            time.sleep(2)
            return balance

        else:
            print(f"\n\t\t\tPOT: ${pot}")
            print(f"\t\t\tNext Multiplier: {multipliers[current_move + 1]}x")

            print("\n\t\t\t    1  2  3  4  5")
            for r in range(1, 6):
                print(f"\t\t\t{r} ", end="")
                for c in range(1, 6):
                    print(" ✅" if (r, c) in revealed else " ⬛", end="")
                print()

            move = input("\n\t\t\t(Row Col) or 'C' to Cash Out: ").upper()

            if move == 'C':
                balance += pot
                print(f"\n\t\t\t💰 You cashed out ${pot}!")
                time.sleep(2)
                return balance

            try:
                r, c = map(int, move.split())
                if not (1 <= r <= 5 and 1 <= c <= 5):
                    continue

                if (r, c) in revealed:
                    continue

                if is_bomb_hit((r, c), bomb_pos):
                    title()
                    print("\n\t\t💥 BOOM! You lost everything!")
                    time.sleep(2)
                    return balance

                revealed.append((r, c))
                current_move += 1

            except ValueError:
                continue

def calculate_bomb_pot(bet, moves, multipliers):
    if moves < 0 or moves >= len(multipliers):
        raise ValueError("Invalid move number!")
    return int(round(bet * multipliers[moves], 3))

def is_bomb_hit(position, bomb_position):
    return position == bomb_position

#************************************************************************************************************#

# MANAGE BALANCE MENU OPTIONS

def manage_menu(balance):
    print(f"""
                
                        Current balance: ${balance} 💰

                    * * * * * * * * * * * * * * *  
                    *                           *
                    *   1. 📥 Deposit           *
                    *                           *
                    *   2. 📤 Withdraw          *
                    *                           *
                    *   3. ↩️  Return            *
                    *                           *
                    * * * * * * * * * * * * * * * 
        """)

    number = input("\t\t\t➡  ")
    return number



def manage(balance):
    
    while True:
        title()
        options = manage_menu(balance)
        match options:
            case "1":
                balance = deposit(balance)
            case "2":
                balance = withdraw(balance)
            case "3":
                break
            case _:
                title()
                print("\n\t\t    Please choose a valid option!")
                time.sleep(1)
    
    return balance



def deposit(balance):
    while True:
        try:
            title()
            print(f"\n\t\t\tCurrent Balance: ${balance} 💰\n\n\t\t\tPress Ctrl + C to return\n\n\t\t\tEnter the amount to be deposited: ")
            amount = input("\n\t\t\t➡  ")

            if not amount.isdigit():
                raise TypeError("Please enter digits only!")
            
            amount = int(amount)
            balance = deposit_balance(balance, amount)

            title()
            print(f"\n\t\t Successfully added ${amount} to balance!")
            time.sleep(1)
            return balance
        
        except (TypeError, ValueError) as e:
            title()
            print(f"\n\t\t\t{e}")
            time.sleep(1)

        except KeyboardInterrupt:
            return balance

def deposit_balance(balance, amount):
    if amount <= 0:
        raise ValueError("Invalid deposit amount!")
    return balance + amount



def withdraw(balance):
    while True:
        try:
            title()
            print(f"\n\t\t\tCurrent Balance: ${balance} 💰\n\n\t\t\tPress Ctrl + C to return\n\n\t\t\tEnter the amount to be withdrawn: ")
            amount = input("\n\t\t\t➡  ")

            if not amount.isdigit():
                raise TypeError("Please enter digits only!")
            
            amount = int(amount)
            balance = withdraw_balance(balance, amount)

            title()
            print(f"\n\t\t     Successfully withdrawn ${amount}!")
            time.sleep(1)
            return balance

        except (TypeError, ValueError) as e:
            title()
            print(f"\n\t\t\t{e}")
            time.sleep(1)

        except KeyboardInterrupt:
            return balance

def withdraw_balance(balance, amount):
    if amount <= 0:
        raise ValueError("Invalid withdraw amount!")
    if amount > balance:
        raise ValueError("Insufficient balance!")
    return balance - amount

#************************************************************************************************************#

# INFORMATION OF THE GAME AND PROJECT

def information():
    title()
    print("""
────────────────────────────────────────────────────────────
📚 PROJECT INFORMATION - CS50P
────────────────────────────────────────────────────────────

Lucky Scratch is a terminal-based game developed as a final
project for the CS50P - Introduction to Programming with Python
course offered by Harvard University.

The main goal of this project is to apply core programming
concepts such as:

- Control flow
- Functions
- Dictionaries and lists
- Randomness
- Error handling
- User interaction in terminal environments

────────────────────────────────────────────────────────────
🎮 GAME MODES
────────────────────────────────────────────────────────────

🍀 CLASSIC MODE (Scratch Game)

In Classic mode, you place a bet and scratch 5 symbols.
To win, you must match AT LEAST 3 identical symbols.

SYMBOL VALUES:
────────────────
🍋 Lemon      →  2x Bet
🍉 Watermelon →  3x Bet
🍒 Cherry     →  4x Bet
⭐ Star       →  6x Bet
🔥 Fire       →  10x Bet
💎 Diamond    →  20x Bet
🍀 Clover     →  50x Bet 

          
💣 BOMB MODE (Risk Strategy Game)

In Bomb mode, you place a bet and face a 5x5 grid.
One of the tiles hides a bomb.

✔ Each safe tile you reveal increases your multiplier  
✔ You can CASH OUT at any time  
✖ Hitting the bomb means losing the entire bet

The game automatically ends when ALL safe tiles
are revealed successfully. 

────────────────────────────────────────────────────────────
⚠️  IMPORTANT NOTE
────────────────────────────────────────────────────────────
This game is for educational purposes only and simulates
casino-style mechanics to demonstrate probability, risk,
and reward concepts in programming.

────────────────────────────────────────────────────────────
    """)
    input("\n\t\tPress Enter to return...")


#************************************************************************************************************#
    
# MAIN MENU OPTIONS

def main():
    balance = 0
    while True:
        title()
        option = main_menu(balance)
        match option:
            case "1":
                balance = scratch(balance)      
            case "2":    
                balance = manage(balance)
            case "3":
                information()
            case "4":
                title()
                sys.exit("\n\t\t\tCome back soon!\n")
            case _:
                title()
                print("\n\t\t    Please choose a valid option!")
                time.sleep(1)


if __name__ == "__main__":
    main()