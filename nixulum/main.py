import json
import os
import sys
import itertools
import threading
from colorama import init, Fore, Back, Style
from time import sleep
import clear

init(autoreset=True)

UTIL_FOLDER = "util"  # Define the name of the folder where the tools are located

def open_login_py():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "login.py"))

def open_info_py():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "info.py"))

def open_nuker_py():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "nuker.py"))
def open_updater_py():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "updater.py"))
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def rainbow_text(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.WHITE, Fore.LIGHTMAGENTA_EX]
    result = ""
    color_cycle = itertools.cycle(colors)
    for char in text:
        result += next(color_cycle) + char
    return result

clear_screen()
def change_theme():
    colors = {
        '1': '\033[31m',  # Red
        '2': '\033[32m',  # Green
        '3': '\033[33m',  # Yellow
        '4': '\033[34m',  # Blue
        '5': '\033[35m',  # Magenta
        '6': '\033[36m',  # Cyan
        '7': '\033[37m',  # White
        
    }

    clear_screen()
    print("Choose a color:")
    print("1. Red")
    print("2. Green")
    print("3. Yellow")
    print("4. Blue")
    print("5. Magenta")
    print("6. Cyan")
    print("7. White")
    

    choice = input("Enter the number corresponding to your choice: ")

    if choice in colors:
        selected_color = colors[choice]
        save_theme(selected_color)
        clear_screen()  # Clear the screen after choosing the color
        return selected_color
    else:
        print("Invalid choice. Using default color.")
        clear_screen()  # Clear the screen even on invalid choice
        return '\033[34m'  # Default to blue

def save_theme(color):
    theme = {'color': color}
    with open('theme.json', 'w') as file:
        json.dump(theme, file)
    print("Theme saved successfully!")

def load_theme():
    try:
        with open('theme.json', 'r') as file:
            theme = json.load(file)
        return theme['color']
        print("theme loaded")
    except FileNotFoundError:
        return '\033[34m'  # Default to blue
clear_screen()
def display_menu(current_color):
    header = """
██╗   ██╗██╗██╗  ██╗██╗██╗     ██╗     ██╗   ██╗███╗   ███╗
████╗  ██║██║╚██╗██╔╝██║██║     ██║     ██║   ██║████╗ ████║                    
██╔██╗ ██║██║ ╚███╔╝ ██║██║     ██║     ██║   ██║██╔████╔██║
██║╚██╗██║██║ ██╔██╗ ██║██║     ██║     ██║   ██║██║╚██╔╝██║
██║ ╚████║██║██╔╝ ██╗██║███████╗███████╗╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝ """
    menu = """<made by Jack and Y2K> 
theme changer «!» update «+»
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ «01» login «06» blank «11» blank «16» blank «21» blank           ┃
┃ «02» info  «07» blank «12» blank «17» blank «22» blank           ┃ 
┃ «03» nuker «08» blank «13» blank «18» blank «23» blank           ┃                         
┃ «04» blank «09» blank «14» blank «19» blank «24» blank           ┃
┃ «05» blank «10» blank «15» blank «20» blank «25» blank           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
    
    if current_color == 'rainbow':
        print(rainbow_text(header))
        print(rainbow_text(menu))
    else:
        print(current_color + header + "\033[0m")
        print(current_color + menu + "\033[0m")

def main_menu():
    current_color = load_theme()

    while True:
        display_menu(current_color)
        choice = input(current_color + "Enter your choice: \033[0m")
        clear_screen()
        if choice == '1':
            open_login_py()
        elif choice == '2':
            open_info_py()
        elif choice == '3':
            open_nuker_py()
        elif choice == '!':
            current_color = change_theme()
            continue 
        elif choice == '!':
           open_updater_py()
        # Return to the menu after changing the theme
        # Handle other choices if needed...

#test hello me

main_menu()
