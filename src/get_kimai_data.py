import csv
import datetime
from typing import List, Tuple

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
