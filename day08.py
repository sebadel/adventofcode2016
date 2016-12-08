#!/usr/bin/env python

import curses
import re
import time

DELAY=0.01

class Matrix(object):
  def __init__(self, rows, cols, myscreen=None):
    self.cells = [[0 for c in range(cols)] for r in range(rows)]
    self.myscreen = myscreen
    if self.myscreen:
      curses.start_color()
      curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

  def rect(self, cols, rows):
    for r in range(int(rows)):
      for c in range(int(cols)):
        self.cells[r][c] = 1

  def rotate_row(self, row_idx, offset):
    row = self.cells[row_idx]
    row2 = self.rotate(row, offset)
    self.cells[row_idx] = row2

  def rotate_col(self, col_idx, offset):
    sequence = [r[col_idx] for r in self.cells]
    sequence = self.rotate(sequence,offset)
    for i in range(len(self.cells)):
      self.cells[i][col_idx] = sequence[i]

  def rotate(self, sequence, offset):
    for _ in range(offset):
      a = sequence.pop()
      sequence = [a] + sequence
    return sequence

  def pixel_count(self):
    return sum([sum(r) for r in self.cells])

  def display(self):
    (h, w) = self.myscreen.getmaxyx()
    x = (w / 2) - (len(self.cells[0]) / 2)
    for i, r in enumerate(self.cells):
      if self.myscreen:
        y = (h/2)-(len(self.cells)/2)
        for j, c in enumerate(r):
          self.myscreen.addch(
            y+i, x+j,
            curses.ACS_DIAMOND if c else ' ',
            curses.color_pair(1))
        self.myscreen.refresh()
        time.sleep(DELAY)
      else:
        print ''.join(['.' if c else ' ' for c in r])


def part1(instructions, use_curses=False):
  myscreen = None
  if use_curses:
    myscreen = curses.initscr()
    curses.curs_set(0)
    myscreen.border(0)
  matrix = Matrix(6,50, myscreen)
  for i in instructions:
    if 'rect' in i:
      matrix.rect(*re.search(r'(\d+)x(\d+)', i).groups())
    elif 'rotate row' in i:
      (row_idx, offset) = re.search(r'=(\d+) by (\d+)', i).groups()
      matrix.rotate_row(int(row_idx), int(offset))
    elif 'rotate column' in i:
      (col_idx, offset) = re.search(r'=(\d+) by (\d+)', i).groups()
      matrix.rotate_col(int(col_idx), int(offset))
    matrix.display()
  if use_curses:
    myscreen.getch()
    curses.endwin()
  print matrix.pixel_count()


instructions = open('data/day08.txt', 'r').readlines()
part1(instructions, use_curses=True)
