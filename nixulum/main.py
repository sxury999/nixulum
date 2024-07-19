import os
import json
import sys
import itertools
from colorama import init, Fore, Back, Style

# Initialize colorama for colored terminal output
init(autoreset=True)

# Define the folder where the tools are located
UTIL_FOLDER = "util"

# List of dependencies to install
imports = ['requests', 'colorama', 'websocket', 'websocket-client', 'uuid', 'datetime', 'tls_client', 'colorist']

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to update terminal title
def update_title(text):
    os.system(f'title {text}')

# Function to install dependencies
def install_dependencies():
    update_title('Test - Installing dependencies')
    total_dependencies = len(imports)
    
    for i, _import in enumerate(imports, start=1):
        clear_screen()
        print(f"Installing dependencies... ({i}/{total_dependencies})")
        print(f"Installing {_import}")
        result = os.system(f'pip install {_import} > nul')
        
        if result != 0:
            print(f"Failed to install {_import}. Please check your internet connection and try again.")
            input("Press Enter to exit...")
            return False
    
    clear_screen()
    print('Finishing up...')
    clear_screen()
    return True

# Function to generate rainbow text
def rainbow_text(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.WHITE, Fore.LIGHTMAGENTA_EX]
    result = ""
    color_cycle = itertools.cycle(colors)
    
    for char in text:
        result += next(color_cycle) + char
    
    return result

# Function to change and save theme
def change_theme():
    colors = {
        '1': Fore.RED,      # Red
        '2': Fore.GREEN,    # Green
        '3': Fore.YELLOW,   # Yellow
        '4': Fore.BLUE,     # Blue
        '5': Fore.MAGENTA,  # Magenta
        '6': Fore.CYAN,     # Cyan
        '7': Fore.WHITE     # White
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
        clear_screen()
        return selected_color
    else:
        print("Invalid choice. Using default color.")
        clear_screen()
        return Fore.BLUE  # Default to blue

# Function to save theme to JSON file
def save_theme(color):
    theme = {'color': color}
    with open('theme.json', 'w') as file:
        json.dump(theme, file)
    print("Theme saved successfully!")

# Function to load theme from JSON file
def load_theme():
    try:
        with open('theme.json', 'r') as file:
            theme = json.load(file)
        return theme['color']
    except FileNotFoundError:
        return Fore.BLUE  # Default to blue

# Function to display main menu
def display_menu(current_color):
    header = """
██╗    ██╗██╗██╗  ██╗██╗██╗     ██╗     ██╗   ██╗███╗   ███╗
████╗  ██║██║╚██╗██╔╝██║██║     ██║     ██║   ██║████╗ ████║                <made by Jack and Y2K> 
██╔██╗ ██║██║ ╚███╔╝ ██║██║     ██║     ██║   ██║██╔████╔██║                theme changer «!» update «+»
██║╚██╗██║██║ ██╔██╗ ██║██║     ██║     ██║   ██║██║╚██╔╝██║
██║ ╚████║██║██╔╝ ██╗██║███████╗███████╗╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝ """
    
    menu = """
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
        print(current_color + header)
        print(current_color + menu)

# Main menu function
def main_menu():
    current_color = load_theme()

    while True:
        display_menu(current_color)
        choice = input(current_color + "Enter your choice: ")

        if choice == '1':
            open_login_py()
        elif choice == '2':
            open_info_py()
        elif choice == '3':
            open_nuker_py()
        elif choice == '!':
            current_color = change_theme()
        elif choice == '+':
            open_up_py()
        else:
            clear_screen()
            print("Invalid choice. Please enter a valid option.")

# Placeholder functions for opening Python scripts
def open_login_py():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "login.py"))

def open_info_py():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "info.py"))

def open_nuker_py():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "nuker.py"))

def open_up_py():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "up.py"))

# Script entry point
if __name__ == "__main__":
    if install_dependencies():
        main_menu()
