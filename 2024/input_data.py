import requests
import os.path
import sys
sys.path.append('../')
from secret import SESSION_ID

def fetch_data(day, year):
    headers = {
        'Cookie': f'session={SESSION_ID}'
    }

    resp = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', headers=headers)
    text = resp.content.decode('utf-8').strip()
    print(text)
    return text

def get_data(day=sys.argv[0].split('.')[0], year=2024, ex=False):
    filename = f"input_{day}.in"
    
    if ex:
        with open(filename.replace('.in', '.ex'), 'rt') as file:
            return file.read()

    if not os.path.isfile(filename):
        text = fetch_data(day, year)
        with open(filename, "wt") as file:
            file.write(text)
    
    with open(filename, 'rt') as file:
        return file.read()
