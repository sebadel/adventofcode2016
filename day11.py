#!/usr/bin/env python

import copy

initial_state  = {
  1: ['TG', 'TM', 'PG', 'SG'],
  2: ['PM', 'SM'],
  3: ['EG', 'EM', 'RG', 'RM'],
  4: []
}

final_state = {
  1: [],
  2: [],
  3: [],
  4: ['EG', 'EM', 'PG', 'PM', 'RG', 'RM', 'SG', 'SM', 'TG', 'TM']
}

_initial_state  = {
  1: ['HM', 'LM'],
  2: ['HG'],
  3: ['LG'],
  4: []
}

_xsfinal_state = {
  1: [],
  2: [],
  3: [],
  4: ['HG', 'HM', 'LG', 'LM']
}

def safe_floor(floor):
  if len(floor) > 1:
    for o in floor:
      if (o[1] == 'M' and
          not '%sG' % o[0] in floor and
          'G' in [x[1] for x in floor]):
        return False
  return True

def pairs(floor):
  p = []
  if len(floor) < 2:
    return []
  for a in floor:
    for b in floor:
      if b != a and sorted([a,b]) not in p:
        p.append(sorted([a,b]))
  return p


class State(object):
  """nb_floors if empty
     status otherwise: {1:['a', 'b', 'c'], 2:[...]}
  """
  def __init__(self, floors, number_moves=0,
               elevator_level=0, previous=None):
    self.floors = floors
    self.number_moves = number_moves
    self.elevator_level = elevator_level
    self.previous = previous

  def __eq__(self, other_state):
    for floor_id in self.floors:
      if sorted(self.floors[floor_id]) != sorted(other_state.floors[floor_id]):
        return False
    return True

  def __ne__(self, other_state):
    return (not self.__eq__(other_state))

  def __hash__(self):
    return hash(self.__repr__()[8:])

  def __repr__(self):
    output = []
    for k, v in self.floors.iteritems():
      output.append('[%s: %32s]' % (k, ' '.join(sorted(v))))
    return '[[%4d]]' % self.number_moves + ' '.join(output)

  @property
  def nb_floors(self):
    return len(self.floors)

  def safe(self):
    for floor_id, floor in self.floors.iteritems():
      if not safe_floor(floor):
        return False
    return True


  def safe_elevator_trip(self, elevator_content,
    floor_origin, floor_destination):
    start = min([floor_origin, floor_destination])
    stop = max([floor_origin, floor_destination])
    for floor_id in range(start,stop+1):
      floor = self.floors[floor_id]
      if not safe_floor(floor + elevator_content):
        return False
    return True

  @property
  def possible_moves(self):
    moves = []
    for floor_id in [self.elevator_level]:  # self.floors:
      floor = self.floors[floor_id]
      if floor:
        for obj in floor:
          for new_floor_id in self.floors:
            if new_floor_id != floor_id:
              new_state = State(
                copy.deepcopy(self.floors),
                number_moves=(
                  self.number_moves +
                  abs(self.elevator_level - floor_id) +
                  abs(new_floor_id - floor_id)),
                elevator_level=new_floor_id,
                previous=self)
              o = new_state.floors[floor_id].pop(floor.index(obj))
              if new_state.safe_elevator_trip([o], floor_id, new_floor_id):
                new_state.floors[new_floor_id].append(o)
                if new_state.safe():
                  moves.append(new_state)

        for p in pairs(floor):
          for new_floor_id in self.floors:
            if new_floor_id != floor_id:
              new_state = State(
                copy.deepcopy(self.floors),
                number_moves=(
                  self.number_moves +
                  abs(self.elevator_level - floor_id) +
                  abs(new_floor_id - floor_id)),
                elevator_level=new_floor_id,
                previous=self)

              new_state.floors[floor_id].pop(new_state.floors[floor_id].index(p[0]))
              new_state.floors[floor_id].pop(new_state.floors[floor_id].index(p[1]))
              if new_state.safe_elevator_trip(p, floor_id, new_floor_id):
                new_state.floors[new_floor_id].extend(p)
                if new_state.safe():
#                  print new_state
                  moves.append(new_state)

    self.moves = moves
    return self.moves


def part1(initial_state, final_state):
  state = State(floors=initial_state, number_moves=0, elevator_level=1)
  final = State(final_state)
  found = False
  len_states = 0
  states = set([state])
  while True:  # not found:
    if len_states == len(states):
      break
    len_states = len(states)
    print len(states)
    new_states = set()
    for state in states:
      new_states.update(set(state.possible_moves))
    if final in new_states:
      found = True
      for i in new_states:
        if i == final:
          print '%d steps' % i.number_moves
          while i.previous:
            print i
            i = i.previous
          print
    states.update(new_states)
  print max([x.number_moves for x in states])


def try2(initial_state, final_state):
  state = State(floors=initial_state, number_moves=0, elevator_level=1)
  final = State(floors=final_state, number_moves=0, elevator_level=4)
  found = False
  states = set([state])
  finals = set([final])
  while not found:
    print '%d - %d' % (len(states), len(finals))
 #   print max([x.number_moves for x in states])
    new_states = set()
    new_final_states = set()
    for state in states:
      new_states = new_states.union(set(state.possible_moves))
    for final in finals:
      new_final_states = new_final_states.union(set(final.possible_moves))
    if (states.intersection(new_final_states) or
       finals.intersection(new_states)):
      print '\n'.join([x for x in states.intersection(new_final_states)])
      found = True
    states = states.union(new_states)
    finals = finals.union(new_final_states)
  print max([x.number_moves for x in states])


#s1 = State(initial_state)
s1 = State(initial_state)
s2 = State(initial_state)
s3 = State(final_state)
#set1 = set([s3])
#print s1 in set1
#set1.update(set([s2]))
#print s1 in set1
part1(initial_state, final_state)