import os
import sys
import requests
import webbrowser

# Replace these values with your GitHub repository details
repo_owner = 'CodeSoftGit'
repo_name = 'pyterm'
python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
pyterm_version = 1.0

def get_latest_release_version():
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        latest_version = data['tag_name']
        return latest_version
    else:
        print(f"Failed to fetch the latest release version. Status Code: {response.status_code}")
        return None

def compare_versions(user_version, latest_version):
    # Split the version strings into lists of integers
    user_version_numbers = list(map(int, user_version.split('.')))
    latest_version_numbers = list(map(int, latest_version.lstrip('v').split('.')))

latest_version = get_latest_release_version()

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"Python {python_version}")
    print(f"pyterm {pyterm_version}")
    try:
        if float(pyterm_version) < float(latest_version):
            print("A newer version is availible! Run update() to open the releases page.")
    except Exception as e:
        pass
    print("Use help() for other commands")

def help():
    print("Other commands:")
    print("clear(): Clear the terminal screen")
    print("help(): View other commands")

def update():
    webbrowser.open("https://github.com/CodeSoftGit/pyterm")

clear()


while True:
    try:
        code = input("py $ ")
        exec(code)
    except Exception as e:
        print(e)