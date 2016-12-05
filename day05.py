#!/usr/bin/env python

import md5
import re

ID = 'ffykfhsq'

def decrypt_part1(door_id):
  code = ''
  cnt = 0
  while len(code) < 8:
    md5_hash = md5.new(door_id+str(cnt)).hexdigest()
    if md5_hash[:5] == '00000':
      code += md5_hash[5]
      print code
    cnt += 1
  return code

def decrypt_part2(door_id):
  code = [' ' for i in range(8)]
  cnt = 0
  while ' ' in code:
    md5_hash = md5.new(door_id+str(cnt)).hexdigest()
    if re.search(r'^0{5}[0-7].*', md5_hash[:6]):
      print md5_hash[:7]
      if code[int(md5_hash[5])] == ' ':
        code[int(md5_hash[5])] = md5_hash[6]
      print code
    cnt += 1
  return ''.join(code)

print decrypt_part2(ID)