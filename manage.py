from datetime import datetime
import os.path
from argparse import ArgumentParser

def construct_day_title():
    date = [datetime.now().year, datetime.now().month, datetime.now().day]
    file_name = "-".join(str(e) for e in date) + '.md'
    return file_name

def construct_entry_timestamp():
    now = datetime.now()
    timestamp = [now.hour, now.minute]
    timestamp = [str(e) for e in timestamp]
    timestamp = ':'.join(timestamp)
    return timestamp

def space_entry(entry, timestamp):
    entry.write('\n')
    entry.write("(" + timestamp + ")")
    entry.write('\n\n')

def new_entry(content=''):
    file_name = construct_day_title()
    timestamp = construct_entry_timestamp()

    if os.path.isfile(file_name):
        with open(file_name, 'a') as entry:
            space_entry(entry, timestamp)
            entry.write(content)
    else:
        with open(file_name, 'w') as entry:
            space_entry(entry, timestamp)
            entry.write(content)

parser = ArgumentParser(description='Process journal entry commands.')
parser.add_argument('-e', '--entry', action="store_true",
                    help="appends a timestamp to today's journal entry")
parser.add_argument('-t', '--template', type=str, choices=['morning', 'evening'],
                    help="appends template to today's entry")


args = parser.parse_args()

if args.entry:
    new_entry()
    print("entry timestamped")

if args.template:

    with open('./templates/%s' % args.template + '.md') as template:
        new_entry(template.read())
