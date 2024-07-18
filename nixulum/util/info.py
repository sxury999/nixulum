
import requests
from colorama import Fore
import os
def tokenInfo(token):
    print('STATUS : [TOKEN INFO]')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f'''
            [{Fore.RED}User ID{Fore.RESET}]         {userID}
            [{Fore.RED}User Name{Fore.RESET}]       {userName}
            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}
            [{Fore.RED}Email{Fore.RESET}]           {email}
            [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ""}
            [{Fore.RED}Token{Fore.RESET}]           {token}
            ''')
        input()
    else:
        print(f"Failed to retrieve user information. Status code: {r.status_code}")
        input("Press any key to exit...")

# Call the tokenInfo function with the token provided by the user
print("""███╗   ██╗██╗██╗  ██╗██╗   ██╗██╗     ██╗   ██╗███╗   ███╗    ██╗███╗   ██╗███████╗ ██████╗ 
████╗  ██║██║╚██╗██╔╝██║   ██║██║     ██║   ██║████╗ ████║    ██║████╗  ██║██╔════╝██╔═══██╗
██╔██╗ ██║██║ ╚███╔╝ ██║   ██║██║     ██║   ██║██╔████╔██║    ██║██╔██╗ ██║█████╗  ██║   ██║
██║╚██╗██║██║ ██╔██╗ ██║   ██║██║     ██║   ██║██║╚██╔╝██║    ██║██║╚██╗██║██╔══╝  ██║   ██║
██║ ╚████║██║██╔╝ ██╗╚██████╔╝███████╗╚██████╔╝██║ ╚═╝ ██║    ██║██║ ╚████║██║     ╚██████╔╝
╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝""")
token = input("Enter your Discord token: ")
tokenInfo(token)
