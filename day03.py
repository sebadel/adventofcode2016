#!/usr/bin/env python

import re

def valid(edges):
  max_edge = edges.pop(edges.index(max(edges)))
  return edges[0] + edges[1] > max_edge

def part1(data):
  valid_triangles = 0
  for d in data:
    edges = [int(x) for x in re.split('\s+', d.strip())]
    if valid(edges):
      valid_triangles += 1
  return valid_triangles

def part2(data):
  buf = []
  valid_triangles = 0
  for d in data:
    buf.append([int(x) for x in re.split('\s+', d.strip())])
    if len(buf) == 3:
      print buf
      for col in range(3):
        edges = [buf[0][col], buf[1][col], buf[2][col]]
        if valid(edges):
          valid_triangles += 1
      buf = []
  return valid_triangles

data = open('data/day03.txt', 'r').readlines()
print part2(data)