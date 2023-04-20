# Kimai-to-UP-timesheet

Sync kimai data to the default timesheet provided by the University of Passau for student assistants.

## Installation

Clone this repository, then execute:
```shell
pip install -r requirements.txt
```

## Usage

Write the data in `~/kimai.csv` to `~/template.xlsx` as `~/timesheet.xlsx`:
```shell
python3 main.py --source ~/kimai.csv --target ~/timesheet.xlsx --template ~/template.xlsx
```

For further info execute `python3 main.py --help`.
