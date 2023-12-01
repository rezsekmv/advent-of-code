import requests
import os.path
from secret import SESSION_ID

def fetch_data(day, year):
    headers = {
        'Cookie': f'session={SESSION_ID}'
    }

    resp = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', headers=headers)
    text = resp.content.decode('utf-8').strip()
    
    return text

def get_data(day, year=2023):
    filename = f"{year}/input_{day}.in"

    if not os.path.isfile(filename):
        text = fetch_data(day, year)
        with open(filename, "wt") as file:
            file.write(text)
    
    with open(filename, 'rt') as file:
        return file.read()
