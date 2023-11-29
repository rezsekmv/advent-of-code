import requests

SESSION_ID = '<<FILL IN WITH YOUR SESSION_ID>>'

def fetch_data(day, year=2023):
    headers = {
        'Cookie': f'session={SESSION_ID}'
    }

    resp = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', headers=headers)
    text = resp.content.decode('utf-8').strip()
    
    with open(f"{year}/input_{day}.in", "wt") as file:
        file.write(text)
    
    return text.splitlines()

