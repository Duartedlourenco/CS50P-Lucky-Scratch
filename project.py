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

def menu(balance):
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




def scratch(balance):
    while True:
        title()
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
        
        match number:
            case "1":
                classic(balance)
            case "2":
                ...
            case "3":
                break
            case _:
                title()
                print("\n\t\t    Please choose a valid option!")
                time.sleep(1)
    
    return balance


def classic(balance):
    
    symbols = ["🍋", "🍉", "🍒", "⭐", "🔥", "💎", "🍀"]

    lemon_value = 2
    watermelon_value = 3
    cherry_value = 4
    star_value = 5
    fire_value = 6
    diamond_value = 7
    lucky_value = 10 
    
    while True:
        try:
            title()
            print(f"""      
                         Current balance: ${balance} 💰
                  
                        To return press Ctrl + C 
                  """)
            amount = int(input("\t\t\tPlace your bet amount: "))
            if amount <= 0:
                raise ValueError
            elif amount > balance:
                title()
                print("\n\t\t Your bet exceeds your available balance.")
                time.sleep(1)
            elif amount <= 0:
                raise ValueError
            break
        except ValueError:
            title()
            print("\n\t\t    Please enter a valid amount.")
            time.sleep(1)
        except KeyboardInterrupt:
            return balance

    balance -= amount

    


def manage(balance):
    
    while True:
        title()
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
        
        match number:
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
            print(f"""      
                         Current balance: ${balance} 💰
                  
                        To return press Ctrl + C 
                  """)
            amount = int(input("\t\t   Enter the amount to be deposited: "))
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
            print(f"""      
                         Current balance: ${balance} 💰
                  
                        To return press Ctrl + C 
                  """)
            amount = int(input("\t\t   Enter the amount to be withdrawn: "))
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




def information():
    ...




def main():
    balance = 0
    while True:
        clear()
        title()
        option = menu(balance)
        match option:
            case "1":
                scratch(balance)      
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