import urllib.request
import sys

filepath = '/home/jesseik/advent/1/input'
frequency = 0
frequencies = []

while True:
    with open(filepath) as f:
        for line in f:
            frequency += int(line)
            if int(frequency) in frequencies:
                print("found!")
                print(frequency)
                sys.exit(0)
            
            frequencies.append(int(frequency))
