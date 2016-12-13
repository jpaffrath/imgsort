import os, datetime, argparse, re

# returns name of directory based on given date and mode
def getDirname(date, mode):
    dirname = ''

    for c in mode:
        if c == '-':
            dirname += '-'
        elif c == '.':
            dirname += '.'
        elif c == 'y':
            dirname += str(date.year)
        elif c == 'm':
            dirname += str(date.month)
        elif c == 'd':
            dirname += str(date.day)

    return dirname

parser = argparse.ArgumentParser(description='A simple python script for sorting image files in directories')
parser.add_argument('dir', metavar='DIR', type=str, help='Path to your image files')
parser.add_argument('mode', metavar='MODE', type=str, help='Name conventions for sorting directories')
args = parser.parse_args()

directory = args.dir
mode = args.mode

# check if given mode is valid
if not re.match('^[ymd.-]+$', mode):
    print('ERROR: {} is no supported mode!'.format(mode))
    exit()

extensions = ['.jpg', '.png']

# iterate files in given directory
for file in os.listdir(directory):

    # get extension from file
    ext = os.path.splitext(file)[1].lower()

    # process only image files
    if ext in extensions:
        unixdate = os.path.getmtime(file)
        date = datetime.datetime.utcfromtimestamp(unixdate)
        
        dirname = getDirname(date, mode)

        # create directory if it not already exists
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        # move file in new directory
        os.rename(file, '{}/{}/{}'.format(directory, dirname, file))