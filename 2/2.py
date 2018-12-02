import sys

filepath = '/home/jesseik/advent/2/input'

with open(filepath) as f:
    # Read input into array
    lines = f.readlines()

for line in lines:
    for target in lines:
        if line == target:
            break
        # Compare line and target char by char
        # Break out if more than 1 chars differ
        differcount = 0
        index = 0
        for char in line:
            if differcount > 1:
                # No match, break out
                break
            if char != target[index]:
                differcount += 1

            index += 1
        if differcount == 1:
            print("Match found!")
            # Find and print common letters
            loopindex = 0
            common = ""
            for char1 in line:
                if char1 == target[loopindex]:
                    common += char1
                loopindex += 1
            print(common)
            sys.exit(0)
