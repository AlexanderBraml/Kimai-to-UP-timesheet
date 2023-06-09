# Kimai-to-UP-timesheet

Sync kimai data to the [default timesheet](https://www.uni-passau.de/fileadmin/dokumente/beschaeftigte/Personal/Formulare_Internetseite/_VI_4/Stud_Hilfskraefte/Dokumentation_der_taeglichen_Arbeitszeit.xlsx) provided by the University of Passau for student assistants.

## Installation

Clone this repository, then execute:
```shell
pip install -r requirements.txt
```

## Usage

You have two options to sync data. You either export a csv file from kimai and use it as a source for the script, or you
enter your api credentials to sync grab the data directly from kimai without manual exporting.

You always have to specify the following parameters:
- target (the target excel file)
- template (the excel template)

### Using the api

If you're using the api as the data source you have to specify the following additional parameters:
- url
- user
- api password
- activity name
- month

A call could look like this:

```shell
python3 main.py api --url "https://demo.kimai.org" --user john_user --password "api_kitten" --activity "Work" --month 1 --target ~/timesheet.xlsx --template ~/template.xlsx
```

### Using a csv file

If you want to use a csv file as the source, you have to specify the path to it. The following call uses `~/source.csv` as a data source:
```shell
python3 main.py csv --source ~/kimai.csv --target ~/timesheet.xlsx --template ~/template.xlsx
```

## Further help

For further info execute `python3 main.py --help`.
