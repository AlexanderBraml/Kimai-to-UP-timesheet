import datetime
from typing import Tuple, List

from openpyxl import load_workbook

DATE_INDEX = (5, 12)

TIME_ROW = 12

DATE_COL = 1
START_HOUR_COL = 2
START_MIN_COL = 4
END_HOUR_COL = 7
END_MIN_COL = 9

MAX_ROWS = 31


def write_to_file(target_template: str, target_file: str,
                  times: List[Tuple[datetime.datetime, datetime.datetime]]) -> None:
    assert 0 < len(times) <= 2 * MAX_ROWS

    workbook = load_workbook(filename=target_template)
    sheet = workbook.active

    sheet.cell(*DATE_INDEX).value = times[0][0].replace(day=1)

    for idx, time in enumerate(times):
        row = TIME_ROW + (idx % MAX_ROWS)
        col_offset = 12 if idx >= MAX_ROWS else 0

        sheet.cell(row, DATE_COL + col_offset).value = time[0].strftime("%d.%m.%Y")
        sheet.cell(row, START_HOUR_COL + col_offset).value = time[0].hour
        sheet.cell(row, START_MIN_COL + col_offset).value = time[0].minute
        sheet.cell(row, END_HOUR_COL + col_offset).value = time[1].hour
        sheet.cell(row, END_MIN_COL + col_offset).value = time[1].minute

    workbook.save(target_file)
    workbook.close()
