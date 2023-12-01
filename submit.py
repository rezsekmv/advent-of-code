import requests
from secret import SESSION_ID


def submit(answer, level, day, year):
    headers = {
        'Cookie': f'session={SESSION_ID}'
    }
        
    body = {
        level: level,
        answer: answer
    }

    respText = requests.post(f'https://adventofcode.com/{year}/day/{day}/answer', headers=headers, json=body).content.decode('utf-8').strip()
    
    if ('That\'s the right answer!' in respText):
        print("GOOD")
    else:
        print("BAD")
    
    return respText
