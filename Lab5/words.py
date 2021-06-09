import os

filename = 'nilsholg.txt'
filepath = os.path.join(os.path.dirname(__file__), filename)
for line in open(filepath):
    print(line)