#!/usr/bin/env python

import re

def expand_pattern(p):
  result = ''
  g = re.match(r'(.*?)\((\d+)x(\d+)\)(.*)', p)
  if g:
    (prefix, char, multiple, rest) = g.groups()
    n = rest[:int(char)] * int(multiple)
    return prefix + n + rest[int(char):]
  else:
    print "Error: %s" % p
    exit()
#    print len(p)
    return p

def part1(data):
  """data is an array; important for assignment by reference."""
  data[0] = data[0].replace(' ', '')
  while '(' in data[0]:
    data[0] = expand_pattern(data[0])
    print 'Len: %08d Count "(": %04d Count ")": %04d' % (len(data[0]), data[0].count('('), data[0].count(')'))
  print 'LEN: %d' % len(data[0])

data = open('data/day09.txt', 'r').readlines()
part1(data)