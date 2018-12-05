import string 
filepath = '/home/jesseik/adventofcode/5/input'
alphabets = list(string.ascii_lowercase)

original = ''
with open(filepath) as f:
    for line in f:
        original = line[0:line.index('\n')]

def Collapse(polymer):
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
                return len(polymer)


# Dict that stores length with each alphabet
lengths = {}
# This is slow af..
for letter in alphabets:
    polymer = original.replace(letter, "")
    polymer = polymer.replace(letter.upper(), "")
    lengths[letter] = Collapse(polymer)

best = min(lengths, key=lengths.get)
print("Best is " + str(best))
print(lengths[best])
