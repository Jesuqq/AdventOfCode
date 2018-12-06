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

size = 400
locations = numpy.zeros((size, size), numpy.int8)
shortests = {}

for i, row in enumerate(locations):
    for j, value in enumerate(row):
        closest = ''
        dist = 1e5
        multiple = False
        for pos in positions:
            # calculate distance to each position from this location
            # Store information to dict with count of dominated locations
            d = Distance(pos, j, i)
            # Shortest was found for sure with 0
            if d == 0:
                closest = pos
                multiple = False
                break
            if d < dist:
                closest = pos
                multiple = False
                dist = d
                continue
            if d == dist:
                # This location belongs to no position!
                multiple = True
                continue

        if closest.name in shortests:
            if not multiple:
                shortests[closest.name] += 1
        else:
            if not multiple:
                shortests[closest.name] = 1
        
        # Set inf flag for position if we are at some of the outermost rows of our grid 
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            closest.inf = True

shortest = ''
dist = 0
for key, value in shortests.items():
    if value > dist:
        obj = next((x for x in positions if x.name == key), None)
        if not obj.inf:
            dist = value
            shortest = obj

print(shortest.name)
print(dist)
