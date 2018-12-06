import numpy

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.inf = False
        self.name = x + ',' + y

positions = []
with open('input') as f:
    s = [line.rstrip('\n') for line in f]
    for p in s:
        x = p[0:p.index(',')]
        y = p[p.index(',')+2:]
        positions.append(Position(x, y))

# Calculate distance from cell 
def Distance(position, x, y):
    distance = abs(int(x) - int(position.x)) + abs(int(y) - int(position.y))
    return distance
region_size = 0
size = 400
allowed = 10000
locations = numpy.zeros((size, size), numpy.int8)

for i, row in enumerate(locations):
    for j, value in enumerate(row):
        ranges = 0
        for pos in positions:
            # calculate distance to each position from this location
            # Store information to dict with count of dominated locations
            d = Distance(pos, j, i)
            ranges += d
            if ranges > allowed:
                break
        if ranges < allowed:
            region_size += 1

print(region_size)
