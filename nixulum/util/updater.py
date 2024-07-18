import requests

def fetch_github_code(repo_url, save_path):
    try:
        # Fetch the code from GitHub
        response = requests.get(repo_url)
        if response.status_code == 200:
            # Save the code to a file
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Code successfully updated and saved to {save_path}")
        else:
            print(f"Failed to fetch code. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
github_repo_url = 'https://raw.githubusercontent.com/sxury999/nixulum/main/nixulum/main.py'
local_save_path = 'main.py'

fetch_github_code(github_repo_url, local_save_path)
