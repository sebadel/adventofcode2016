#!/usr/bin/env python

import re

def valid_checksum(room):
  occurrences = {}
  for c in room:
    if c != '-':
      occurrences[c] = room.count(c)
  checksum = [k for k,v in sorted(occurrences.iteritems(),
                                  key = lambda k:(-k[1], k[0]))]
  return ''.join(checksum[:5])

def decipher(code, sector):
  code = list(code)
  for i, c in enumerate(code):
    if c == '-':
      code[i] = ' '
    else:
      code[i] = chr((ord(c) + int(sector)- 97) % 26 + 97)
  return ''.join(code)

def part1(codes):
  valid_codes = []
  sum_sector = 0
  for code in codes:
    (room, sector, checksum) = re.match(
        r'(.*?)-(\d+)\[(.*?)\]', code).groups()
    if valid_checksum(room) == checksum:
      sum_sector += int(sector)
  return sum_sector

def part2(codes):
  for code in codes:
    (room, sector, checksum) = re.match(
        r'(.*?)-(\d+)\[(.*?)\]', code).groups()
    if valid_checksum(room) == checksum:
      print decipher(code, sector)
      if decipher(code, sector) == 'northpole object storage kjnwoetrcyt':
        return sector
  return 'Room not found'


codes = open('data/day04.txt', 'r').readlines()
print part1(codes)
print part2(codes)