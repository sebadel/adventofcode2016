#!/usr/bin/env python

moves = 'R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1'.split(', ')
directions = ['N', 'E', 'S', 'W']
direction = 'N'
latitude = 0
longitude = 0
tracks = []
for m in moves:
  if m[0] == 'L':
    if direction == 'N':
      direction = 'W'
    else:
      direction = directions[directions.index(direction)-1]
  else:
      direction = directions[(directions.index(direction)+1) % 4]
  step = 0
  distance = int(m[1:])
  while step <  distance:
    if direction == 'N':
      longitude = longitude - 1
    elif direction == 'S':
      longitude = longitude + 1
    elif direction == 'W':
      latitude = latitude - 1
    else:
      latitude = latitude + 1
    if [latitude, longitude] not in tracks:
      tracks.append([latitude,longitude])
    else:
      print abs(latitude) + abs(longitude)
      break
    step +=1