import requests
import os

def fetch_and_update_github_code(repo_url, local_save_path):
    try:
        # Fetch the code from GitHub
        response = requests.get(repo_url)
        
        if response.status_code == 200:
            # Read the fetched content
            fetched_content = response.content.decode('utf-8')
            
            # Check if the fetched content is different from the existing file content
            if not is_content_same(local_save_path, fetched_content):
                # Save the fetched code to the existing file (overwrite mode)
                with open(local_save_path, 'wb') as file:
                    file.write(response.content)
                print(f"Code successfully updated and saved to {local_save_path}")
            else:
                print("Code is already up to date. No changes made.")
        else:
            print(f"Failed to fetch code. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def is_content_same(file_path, new_content):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            return False
        
        # Read existing file content
        with open(file_path, 'rb') as file:
            existing_content = file.read().decode('utf-8')
        
        # Compare existing content with new content
        return existing_content == new_content
    
    except Exception as e:
        print(f"Error checking file content: {e}")
        return False

# Example usage:
github_repo_url = 'https://raw.githubusercontent.com/sxury999/nixulum/main/nixulum/main.py'
local_save_path = 'main.py'  # Update this to your existing main.py path

fetch_and_update_github_code(github_repo_url, local_save_path)
