import argparse
from os.path import expanduser

from src.get_kimai_data import read_csv, read_api
from src.write_target import write_to_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('mode', help='The source of the export.', choices=['api', 'csv'])

    parser.add_argument('--target', help='The target xslx file.', required=True)
    parser.add_argument('--template', help='The template on which the target will be based.', required=True)

    parser.add_argument('--source', help='A csv file containg the times to import.')

    parser.add_argument('--url', help='The url of your kimai instance.')
    parser.add_argument('--user', help='Your kimai username.')
    parser.add_argument('--password', help='Your kimai api password, not your regular password.')
    parser.add_argument('--activity', help='The id of the activity to be exported.')
    parser.add_argument('--month', help='The month to export.')

    args = parser.parse_args()

    times = []
    if args.mode == 'api':
        if any(a is None for a in [args.url, args.user, args.password, args.activity, args.month]):
            raise ValueError('The following arguments are required when using api as source: --url --user '
                             '--password --activity --month')

        times = read_api(args.url, args.user, args.password, int(args.activity), int(args.month))
    elif args.mode == 'csv':
        if args.source is None:
            raise ValueError('The following arguments are required when using csv as source: --source')

        times = read_csv(expanduser(args.source))
    write_to_file(expanduser(args.template), expanduser(args.target), times)
