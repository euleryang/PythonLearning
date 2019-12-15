'''
read csv type of file

version: 0.1
Author: SamYang
Date: 2019-12-15

'''

import csv

filename = 'example.csv'

try:
    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print('Cannot open this file:', filename)
else:
    for item in data:
        print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))