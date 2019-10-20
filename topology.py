#!/usr/bin/env python3

import random
import datetime
import time
import json
import sys
import os
import re
import glob

def create_lattice(x_count, y_count, diag = False):
    links = []
    offset = 0
    if x_count < 1 or y_count < 1:
        return links

    def connect(x1, y1, x2, y2):
        # validate coordinates
        if (x2 < x_count) and (y2 < y_count):
            a = offset + x1 * y_count + y1
            b = offset + x2 * y_count + y2
            links.append({'source': a, 'target': b})

    for x in range(0, x_count):
        for y in range(0, y_count):
            if diag:
                connect(x, y, x + 1, y + 1)
                if y > 0:
                    connect(x, y, x + 1, y - 1)
            connect(x, y, x, y + 1)
            connect(x, y, x + 1, y)

    return links


if len(sys.argv) != 4:
    print("Usage: {} [lattice4|lattice8] <n> <output-file>".format(sys.argv[0]))
    exit(1)

geometry = sys.argv[1]
number = int(sys.argv[2])
path = sys.argv[3]
links = []

if geometry == 'lattice4':
	links = create_lattice(number, number, False)
elif geometry == 'lattice8':
	links = create_lattice(number, number, True)
else:
    print('unknown geometry: {}'.format(geometry))
    exit(1)

if os.path.isfile(path):
    print('File already exists: {}'.format(path))
    exit(1)

with open(path, "w") as file:
    json.dump({'links': links}, file)
    print('Wrote {}'.format(path))
