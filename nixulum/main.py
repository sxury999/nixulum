import os
import json
import sys
from colorama import init, Fore
from pystyle import Colors, Colorate, Center

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

# Function to load theme from JSON file
def load_theme():
    try:
        with open('theme.json', 'r') as file:
            theme = json.load(file)
        return theme['color']
    except FileNotFoundError:
        return "blue_to_purple"  # Default to blue to purple gradient

# Function to save theme to JSON file
def save_theme(color):
    theme = {'color': color}
    with open('theme.json', 'w') as file:
        json.dump(theme, file)
    print("Theme saved successfully!")

# Function to change and save theme
def change_theme():
    colors = {
        '1': "red_to_yellow",
        '2': "green_to_blue",
        '3': "yellow_to_red",
        '4': "blue_to_purple",
        '5': "cyan_to_green",
        '6': "black_to_white"  # Updated to use valid color
    }

    clear_screen()
    print("Choose a color theme:")
    print("1. Red to Yellow")
    print("2. Green to Blue")
    print("3. Yellow to Red")
    print("4. Blue to Purple")
    print("5. Cyan to Green")
    print("6. Black to White")
    choice = input("Enter the number of your choice: ")

    if choice in colors:
        save_theme(colors[choice])
    else:
        print("Invalid choice. Defaulting to Blue to Purple gradient.")
        save_theme("blue_to_purple")

# Mapping of color themes to Colors attributes
color_mappings = {
    "red_to_yellow": Colors.red_to_yellow,
    "green_to_blue": Colors.green_to_blue,
    "yellow_to_red": Colors.yellow_to_red,
    "blue_to_purple": Colors.blue_to_purple,
    "cyan_to_green": Colors.cyan_to_green,
    "black_to_white": Colors.black_to_white
}

# Function to display main menu
def display_menu(current_color):
    logo = Center.XCenter("""
        ███╗   ██╗██╗██╗  ██╗██╗██╗     ██╗     ██╗   ██╗███╗   ███╗
        ████╗  ██║██║╚██╗██╔╝██║██║     ██║     ██║   ██║████╗ ████║                <made by Jack and Y2K> 
        ██╔██╗ ██║██║ ╚███╔╝ ██║██║     ██║     ██║   ██║██╔████╔██║                theme changer «!» update «+»
        ██║╚██╗██║██║ ██╔██╗ ██║██║     ██║     ██║   ██║██║╚██╔╝██║
        ██║ ╚████║██║██╔╝ ██╗██║███████╗███████╗╚██████╔╝██║ ╚═╝ ██║
        ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ «01» login «06» blank «11» blank «16» blank «21» blank           ┃
    ┃ «02» info  «07» blank «12» blank «17» blank «22» blank           ┃ 
    ┃ «03» nuker «08» blank «13» blank «18» blank «23» blank           ┃                         
    ┃ «04» blank «09» blank «14» blank «19» blank «24» blank           ┃
    ┃ «05» blank «10» blank «15» blank «20» blank «25» blank           ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

    # Apply gradient color to logo
    color_function = color_mappings.get(current_color, Colors.blue_to_purple)
    colored_logo = Colorate.Vertical(color_function, logo)

    clear_screen()  # Clear the screen before printing
    print(colored_logo)

# Main menu function
def main_menu():
    current_color = load_theme()

    while True:
        clear_screen()
        display_menu(current_color)
        choice = input(Fore.RESET + "[?] Choice » ")

        if choice == '1':
            open_login_py()
        elif choice == '2':
            open_info_py()
        elif choice == '3':
            open_nuker_py()
        elif choice == '+':
            open_up_py()
        elif choice == '!':
            change_theme()
            current_color = load_theme()
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
