#!/usr/bin/env python

import re
import sys
import time


class Bot(object):
  def __init__(self, bot_id):
    self.id = bot_id
    self.low = None
    self.high = None
    self.content = []

  def give(self, other_bot, value):
    if value in self.content:
      self.content.pop(self.content.index(value))
      other_bot.receive(value)

  def receive(self, value):
    self.content.append(value)
    self.behave()

  def behave(self):
    if len(self.content) == 2 and 'BOT_' in self.id and self.low and self.high:
      if 17 in self.content and 61 in self.content:
        print 'WINNING BOT %s' % self.id
      self.give(bots[self.low], min(self.content))
      self.give(bots[self.high], max(self.content))
      self.content = []


RE_BEHAVIOR = re.compile(r'bot (\d+) gives low to (.*?) (\d+) and high to (.*?) (\d+)')
RE_VALUE = re.compile(r'value (\d+) goes to bot (\d+)')
actions = []
def read_instruction(i):
  if RE_VALUE.match(i):
    (value, bot) = RE_VALUE.match(i).groups()
    bot_id = 'BOT_%03d' % int(bot)
    if bot_id not in bots:
      bots[bot_id] = Bot(bot_id)
    bots[bot_id].receive(int(value))
  elif RE_BEHAVIOR.match(i):
    (bot, low_type, low_value, high_type, high_value) = RE_BEHAVIOR.match(i).groups()
    low = '%s_%03d' % (low_type.upper(), int(low_value))
    high = '%s_%03d' % (high_type.upper(), int(high_value))
    bot_id = 'BOT_%03d' % int(bot)
    for b in [bot_id, low, high]:
      if b not in bots:
        bots[b] = Bot(b)
    bots[bot_id].high = high
    bots[bot_id].low = low
    bots[bot_id].behave()

def part1(data):
  for d in data:
    read_instruction(d.rstrip())

def part2():
  for k, v in bots.iteritems():
    if 'OUTPUT' in k:
      print '%s: [%s]' % (k, ','.join(map(str, v.content)))
#  for o in ['OUTPUT_001', 'OUTPUT_002', 'OUTPUT_003']:
#    print bots[o].content

bots = {}
data = open('data/day10.txt', 'r').readlines()
part1(data)
part2()