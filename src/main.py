import argparse
from os.path import expanduser

from get_kimai_data import read_csv
from write_target import write_to_file

parser = argparse.ArgumentParser()

parser.add_argument("--source", help="A csv file containg the times to import.")
parser.add_argument("--target", help="The target xslx file.")
parser.add_argument("--template", help="The template on which the target will be based.")

args = parser.parse_args()

if __name__ == '__main__':
    source = expanduser(args.source)
    target = expanduser(args.target)
    template = expanduser(args.template)
    write_to_file(template, target, read_csv(source))
