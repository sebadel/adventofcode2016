#!/usr/bin/env python

import re

def abba(s):
  i = 0
  while i+3 < len(s):
    if s[i] != s[i+1] and s[i] == s[i+3] and s[i+1] == s[i+2]:
      return True
    i += 1
  return False

def hypernets(s):
  return re.findall(r'\[(.*?)\]', s)

def supernets(s):
  h = []
  while '[' in s:
    h.append(s[:s.index('[')])
    s = s[s.index(']')+1:]
  h.append(s)
  return h

def valid_tls(s):
  for hypernet in hypernets(s):
    if abba(hypernet):
      return False
  for supernet in supernets(s):
    if abba(supernet):
      return True
  return False

def abas(s):
  i = 0
  t = []
  while i+2 < len(s):
    if s[i] != s[i+1] and s[i] == s[i+2]:
      t.append(s[i:i+3])
    i += 1
  return t

def valid_ssl(s):
  for supernet in supernets(s):
    for aba in abas(supernet):
      for hypernet in hypernets(s):
        for bab in abas(hypernet):
          if aba[0] == bab[1] and aba[1] == bab[0]:
            return True
  return False

def part1(ips):
  cnt = 0
  for ip in ips:
    if valid_tls(ip):
      cnt += 1
  return cnt

def part2(ips):
  cnt = 0
  for ip in ips:
    if valid_ssl(ip):
      cnt += 1
  return cnt

ips = open('data/day07.txt', 'r').readlines()
print part2(ips)

