import requests
from datetime import datetime, timedelta
import time
import sys

BIGEST_TIMESTAMP = 2147483647

def timestampToString(ts):
    if ts == BIGEST_TIMESTAMP:
        return '--------'
    return (datetime.utcfromtimestamp(int(ts))+timedelta(hours = 1)).strftime('%H:%M:%S')

def wirteScoresToFile(data, day):    
    sortedData = sorted(data, key = lambda x: (-int(x[1]['stars'])))
    for ps in sortedData:
        p = ps[1]
        if day not in p['completion_day_level']:
            p['completion_day_level'][day] = {'1': {'get_star_ts': BIGEST_TIMESTAMP}, '2': {'get_star_ts': BIGEST_TIMESTAMP}}
        else:
            if '1' not in p['completion_day_level'][day]:
                p['completion_day_level'][day] = {'1': {'get_star_ts': BIGEST_TIMESTAMP}}
            if '2' not in p['completion_day_level'][day]:
                p['completion_day_level'][day] = {'2': {'get_star_ts': BIGEST_TIMESTAMP}}
        
    sortedData = sorted(sortedData, key = lambda x: (int(x[1]['completion_day_level'][day]['2']['get_star_ts'])))

    filename = f'leaderboard/{day}.txt'
    with open(filename, 'w', encoding="utf-8") as f:
        f.write('1st star \t 2nd star \t name\n')
        f.write('===================================\n')
        for person in sortedData:
            person = person[1]
            if person['name'] is not None and day in person['completion_day_level']:
                if person['completion_day_level'][day]['1'] is not None:
                    f.write(timestampToString(person['completion_day_level'][day]['1']['get_star_ts']) + '\t')
                if person['completion_day_level'][day]['2'] is not None:
                    f.write(timestampToString(person['completion_day_level'][day]['2']['get_star_ts']) + '\t')
                f.write(person['name'] + '\n')
        f.close()
    print('File created: ' + filename)

def fetchApi():
    url = 'https://adventofcode.com/2022/leaderboard/private/view/1318392.json'
    leaderboardJson = None
    try:
        f = open('session_cookie.txt', 'rt')
        headers = {'cookie': f.read()}
        response = requests.get(url, headers=headers)
        leaderboardJson = response.json()
        return leaderboardJson['members'].items()
    except:
        print('Please provide session_cookie.txt')
        sys.exit()


def main():
    print('Create a session_cookie.txt file with your cookie value\n')
    print('Commands:')
    print('Type in the date to get the scores for that date (empty is today)')
    print('Type r to refresh data')
    print('Type quit if you want to leave\n')

    data = fetchApi()

    day = time.strftime('%d').lstrip("0")
    
    key = None
    while key != 'quit':
        key = input('Command: ')
        
        if key == 'quit' or key == 'exit':
            print('bye')
        elif key == 'r':
            data = fetchApi()
            print('data fetched')
        elif key == '0' or key == '':
            wirteScoresToFile(data, day)
        elif '1' <= key <= day:
            wirteScoresToFile(data, key)
        else:
            print('Please enter valid command')

main()