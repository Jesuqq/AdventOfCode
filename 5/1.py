import sys
filepath = '/home/jesseik/adventofcode/5/input'

polymer = ''
with open(filepath) as f:
    for line in f:
        polymer = line[0:line.index('\n')]

while True:
    index = 0
    for letter in polymer:
        pair = polymer[index+1]
        uppercase = letter.istitle()
        if uppercase:
            # pair has to be lowercase
            if pair == letter.lower():
                # Remove letter and pair
                polymer = polymer[:index] + polymer[index+2:]
                break
        else:
            # pair has to be uppercase
            if pair == letter.upper():
                # Remove letter and pair
                polymer = polymer[:index] + polymer[index+2:]
                break
        index += 1
        if index + 1 == len(polymer):
            print(len(polymer))
            sys.exit(0)
