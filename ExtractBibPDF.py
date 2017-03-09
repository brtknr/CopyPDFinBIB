#!/usr/bin/env python
import argparse
import re
import shutil

# Read arguments
parser = argparse.ArgumentParser('Extract PDF files out of bib files exported from programs like Mendeley.')
parser.add_argument('--bibFile')
parser.add_argument('--extractTo')
args = parser.parse_args()
print (args)

# Extract reference to files
regex = r"(?<=:)(.*)(?=:pdf)"
files = list()
with open(args.bibFile) as file:
    for line in file:
        matches = re.finditer(regex, line)
        for match in matches:
            files.extend('/{}'.format(m) for m in match.group().split(':pdf;:'))

# Move the list of 
success = list()
failure = list()

for f in files:
    try:
        shutil.copyfile(f, '{}/{}'.format(args.extractTo, f.split('/')[-1]))
        success.append(f)
    except FileNotFoundError:
        failure.append(f)

# Results
print ('Success')
for s in success:
    print('-', s)
print ('---\n')
print ('Failure')
for m in failure:
    print('-', m)
print ('NOTE: Copy may fail due to special characters in the file name.')


