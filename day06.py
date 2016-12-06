#!/usr/bin/env python

def linesToColumns(data):
  columns = []
  for line in data:
    line = line.rstrip()
    for i, c in enumerate(line):
      if len(columns) <= i:
        columns.append('')
      columns[i] += c
  return columns

def part1(data, reversed=True):
  result = ''
  for i, col in enumerate(linesToColumns(data)):
    tab = {c: col.count(c) for c in set(list(col))}
    result += sorted(tab.iteritems(), key=lambda x: x[1], reverse=reversed)[0][0]
  return result

def part2(data):
  return part1(data, reversed=False)

data = open('data/day06.txt', 'r').readlines()
print part2(data)