import numpy
import sys

filepath = '/home/jesseik/adventofcode/3/input'

matrix = numpy.zeros((1500, 1500), numpy.int8)
claims = []
# Read input and parse values
# TODO create proper objects and store
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

# Function to check if passed claim contains square inches claimed only here
def check(cid, startX, startY, width, height):
    for y in range(height):
        for x in range(width):
            ypos = startY + y
            xpos = startX + x
            if (matrix[ypos][xpos] > 1):
                return False
    return True

# TODO use objects from list instead of reparsing
with open(filepath) as f:
    for line2 in f:
        cid = int(line2[line2.index('#')+1:line2.index('@')-1])
        startX = int(line2[line2.index('@')+2:line2.index(',')])
        startY = int(line2[line2.index(',')+1:line2.index(':')])
        width = int(line2[line2.index(':')+2:line2.index('x')])
        height = int(line2[line2.index('x')+1:line2.index('\n')])

        if (check(cid, startX, startY, width, height)):
                print("Found!")
                print(cid)
                sys.exit(0)
