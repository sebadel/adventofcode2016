#!/usr/bin/env python

INPUT='01110110101001000'
LENGTH_PART1=272
LENGTH_PART2=35651584

def checksum(a):
  cs = ''
  i = 0
  while i < len(a):
    if a[i] == a[i+1]:
      cs += '1'
    else:
      cs += '0'
    i += 2
  if len(cs) % 2:
    return cs
  return checksum(cs)

def next_sequence(a):
  i = ''.join([str(abs(int(c)-1)) for c in a])
  b = a + '0' + i[::-1]
  return b

def run(a, length):
  while len(a) < length:
    a = next_sequence(a)
  a = a[:length]
  print checksum(a)

run(INPUT, LENGTH_PART1)
#run(INPUT, LENGTH_PART2)
