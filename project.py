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
                classic_game(balance)
            case "2":
                bomb_game(balance)
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
            print(f"\n\t\t\tCurrent Balance: ${balance} 💰\n\n\t\t\tPress Ctrl + C to return")
            bet = int(input("\n\t\t\tBet amount: "))
            if bet > balance:
                title()
                print("\n\t\t\tInsufficient balance!")
                time.sleep(1)
                continue
            if bet <= 0: 
                raise ValueError
            break
        except ValueError: 
            title()
            print("\n\t\t\t Invalid amount!")
            time.sleep(1)
        except KeyboardInterrupt: 
            return balance

    balance -= bet
    symbols = ["🍋", "🍉", "🍒", "⭐", "🔥", "💎", "🍀"]
    values = {"🍋": 2, "🍉": 3, "🍒": 4, "⭐": 6, "🔥": 10, "💎": 20, "🍀": 50}
    
    result = [random.choice(symbols) for _ in range(6)]
    title()
    print("\n\t\tScratching...")
    time.sleep(1)
    print(f"\n\t\t[ {' '.join(result)} ]")
    
    # Verifica se há 3 iguais
    win = 0
    for s in set(result):
        if result.count(s) >= 3:
            win = bet * values[s]
            break
            
    if win > 0:
        print(f"\n\t\t🎉 YOU WON ${win}!"); balance += win
    else:
        print("\n\t\tNo luck this time.")
    
    time.sleep(2)
    return balance



def bomb_game(balance):
    while True:
        try:
            title()
            print(f"\t\tBalance: ${balance} 💰")
            bet = int(input("\t\tEnter bet for Bomb field: "))
            if bet > balance: print("\t\tInsufficient!"); time.sleep(1); continue
            balance -= bet
            break
        except: return balance

    grid_size = 6
    bomb_pos = (random.randint(1, 6), random.randint(1, 6))
    revealed = []
    multiplier = 1.0

    while True:
        title()
        current_pot = round(bet * multiplier, 2)
        print(f"\t\tPOT: ${current_pot}  |  Next Multiplier: {round(multiplier + 0.4, 1)}x")
        
        # Desenha o Tabuleiro
        print("\n\t\t    1  2  3  4  5  6")
        for r in range(1, 7):
            print(f"\t\t{r} ", end="")
            for c in range(1, 7):
                if (r, c) in revealed: print(" ✅", end="")
                else: print(" ⬛", end="")
            print()
            
        move = input("\n\t\tEnter (row col) or 'S' to Cash Out: ").upper()
        if move == 'S':
            balance += current_pot
            print(f"\t\tWise choice! You cashed out ${current_pot}"); time.sleep(2)
            break
        
        try:
            r, c = map(int, move.split())
            if (r, c) == bomb_pos:
                title(); print("\n\t\t💥 BOOM! You lost everything."); time.sleep(2); break
            elif (r, c) in revealed or not (1 <= r <= 6 and 1 <= c <= 6):
                continue
            else:
                revealed.append((r, c))
                multiplier += 0.4
        except: continue
    return balance

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
            title()
            print(f"\n\t\t\tCurrent Balance: ${balance} 💰\n\n\t\t\tPress Ctrl + C to return\n\n\t\t\tEnter the amount to be deposited: ")
            amount = int(input("\n\t\t\t➡  "))
            if amount <= 0:
                raise ValueError
            break
        except ValueError:
            title()
            print("\nPlease enter a valid amount.")
            time.sleep(1)
        except KeyboardInterrupt:
            return balance
        
    balance += amount

    title()
    print(f"\n\t\t Successfully added ${amount} to balance!")
    time.sleep(1)
    return balance



def withdraw(balance):
    while True:
        try:
            title()
            title()
            print(f"\n\t\t\tCurrent Balance: ${balance} 💰\n\n\t\t\tPress Ctrl + C to return")
            amount = int(input("\n\t\t\tEnter the amount to be withdrawn: "))
            if amount <= 0:
                raise ValueError
            elif amount > balance:
                raise ValueError
            break
        except ValueError:
            title()
            print("\n\t\t    Please enter a valid amount.")
            time.sleep(1)
        except KeyboardInterrupt:
            return balance 

    balance -= amount

    title()
    print(f"\n\t\t     Successfully withdrawn ${amount}!")
    time.sleep(1)
    return balance



#************************************************************************************************************#

# INFORMATION OF THE GAME AND PROJECT

def information():
    title()
    print("""
    HOW TO PLAY:
    
    🎰 SCRATCH (Classic):
    Match 3 symbols to win. Each symbol has a different 
    multiplier. The Lucky Clover (🍀) pays 50x!
    
    💣 BOMB:
    A 6x6 grid with 1 hidden bomb. Each safe square 
    increases your multiplier. Cash out (S) any time 
    or lose it all if you hit the bomb!
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
                sys.exit("Come back soon!")
            case _:
                print("\n\t\t    Please choose a valid option!")
                time.sleep(1)




if __name__ == "__main__":
    main()