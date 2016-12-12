#!/usr/bin/env python

import re

def part1(data):
  if '(' in data:
    g = re.match(r'^(.*?)\((\d+)x(\d+)\)', data)
    if g:
      (prefix, char, multiple) = g.groups()
      rest = data[len(prefix) + len(char)+len(multiple)+3+int(char):]
      return len(prefix) + (int(char) * int(multiple)) + part1(rest)
  else:
    return len(data)

def part2(data):
  if '(' in data:
    g = re.match(r'^(.*?)\((\d+)x(\d+)\)(.*)', data)
    if g:
      (prefix, char, multiple, rest) = g.groups()
      expanded_pattern = part2(rest[:int(char)]) * int(multiple)
      rest = rest[int(char):]
      return len(prefix) + expanded_pattern + part2(rest)
  else:
    return len(data)

data = open('data/day09.txt', 'r').readlines()
#data = ['(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN']
#print part1(data[0])
print part2(data[0])
