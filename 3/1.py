import numpy
filepath = '/home/jesseik/adventofcode/3/input'

matrix = numpy.zeros((1500, 1500), numpy.int8)
with open(filepath) as f:
    for line in f:
        startX = int(line[line.index('@')+2:line.index(',')])
        startY = int(line[line.index(',')+1:line.index(':')])
        width = int(line[line.index(':')+2:line.index('x')])
        height = int(line[line.index('x')+1:line.index('\n')])

        for y in range(height):
            for x in range(width):
                ypos = startY + y
                xpos = startX + x
                matrix[ypos][xpos] += 1

dups = 0
for y in range(1500):
    for x in range(1500):
        if matrix[y][x] > 1:
            dups += 1

print(dups)
