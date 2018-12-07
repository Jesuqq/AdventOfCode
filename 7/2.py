import sys
import string

steps = []
deps = {}
with open('input') as f:
    for line in f:
        dependency = line[5:6]
        step = line[36:37]
        # Collect all steps in puzzle
        if step not in steps:
            steps.append(step)
            deps[step] = []
        if dependency not in steps:
            steps.append(dependency)
            deps[dependency] = []
        if step not in deps:
            deps[step] = [dependency]
        else:
            deps[step].append(dependency)

completed = []
alphabet = string.ascii_uppercase
# Key = step name, value = t of completion
progress = {}
workers = 5
available_w = workers
t = 0

while True:
    # Find possible steps that can be solves
    possible = []

    # Move completed steps from to completed list and remove from deps
    for key, value in progress.copy().items():
        if t == value or t > value:
            available_w += 1
            completed.append(key)
            progress.pop(key)
        
            for key1, value1 in deps.items():
                if key in value1:
                    value1.remove(key)

            steps.remove(key)

    for step in steps:
        if len(deps[step]) == 0:
            possible.append(step)

    possible = sorted(possible)
    # Items from possible are free to distribute as work
    dist = 0
    for i in range(available_w):
        if len(possible) > 0:
            task = next((x for x in possible if x not in progress), None)
            if task != None:
                possible.remove(task)
                progress[task] = t + alphabet.index(task) + 1 + 60
                dist += 1
            else:
                break
    available_w -= dist

    if len(steps) == 0 and len(progress) == 0:
        break
    t += 1

print(t)
