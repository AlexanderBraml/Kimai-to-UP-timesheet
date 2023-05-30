import csv
import datetime
from typing import List, Tuple

import requests
from dateutil.parser import parse

DATE_INDEX = 0
START_TIME_INDEX = 1
END_TIME_INDEX = 2


def read_csv(path: str) -> List[Tuple[datetime.datetime, datetime.datetime]]:
    times = []
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Skip header
        for row in reader:
            date = parse(row[DATE_INDEX]).date()
            start = datetime.datetime.combine(date, parse(row[START_TIME_INDEX]).time())
            end = datetime.datetime.combine(date, parse(row[END_TIME_INDEX]).time())
            times.append((start, end))

    return times


def read_api(url: str, user: str, token: str, activity: str, month: int) \
        -> List[Tuple[datetime.datetime, datetime.datetime]]:
    headers = {
        'X-AUTH-USER': user,
        'X-AUTH-TOKEN': token,
    }
    params = {
        'size': 999999,
        'activities': [activity_id(url, user, token, activity)],
    }

    response = requests.get(url + '/api/timesheets', headers=headers, params=params)
    result = response.json()

    times = []
    for entry in result:
        start_date = parse(entry['begin']).replace(tzinfo=None)
        running = entry['end'] is None
        if not running:
            end_date = parse(entry['end']).replace(tzinfo=None)
            if start_date.year == datetime.datetime.now().year and int(start_date.month) == month:
                times.append((start_date, end_date))
    times.sort(key=lambda x: x[0])

    return times


def activity_id(url: str, user: str, token: str, activity: str) -> int:
    headers = {
        'X-AUTH-USER': user,
        'X-AUTH-TOKEN': token,
    }
    params = {
        'size': 999999,
    }

    response = requests.get(url + '/api/activities', headers=headers, params=params)
    result = response.json()

    for entry in result:
        if entry['name'] == activity:
            return entry['id']

    raise ValueError(f'Id of activity {activity} cannot be found.')
