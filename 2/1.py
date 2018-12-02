import sys

filepath = '/home/jesseik/advent/2/input'
twice = 0
thrice = 0

with open(filepath) as f:
    for line in f:
        findings = {}
        for char in line:
            if char not in findings:
                findings[char] = 1
            else:
                findings[char] = findings[char] + 1
        # Check if any number was twice or thrice here
        if 2 in findings.values():
            twice += 1
        if 3 in findings.values():
            thrice += 1


print(twice * thrice)
