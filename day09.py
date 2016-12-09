#!/usr/bin/env python

import re

def expand_pattern(p):
  result = ''
  g = re.match(r'(.*?)\((\d+)x(\d+)\)(.*)', p)
  if g:
    (prefix, char, multiple, rest) = g.groups()
    n = rest[:int(char)] * int(multiple)
    return prefix + expand_pattern(n) + expand_pattern(rest[int(char):])
  else:
#    print len(p)
    return p

def part1(data):
  """data is an array; important for assignment by reference."""
  data[0].replace(' ', '')
  print len(expand_pattern(data[0]))

data = open('data/day09.txt', 'r').readlines()
part1(data)