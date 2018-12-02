import urllib.request

filepath = '/home/jesseik/advent/1/input'
frequency = 0

with open(filepath) as f:
    for line in f:
        frequency += int(line)

print(frequency)
