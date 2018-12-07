import sys

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

while True:
    # Find possible steps that can be solves
    possible = []
    for step in steps:
        if len(deps[step]) == 0:
            possible.append(step)
    solved = sorted(possible)[0]
    for key, value in deps.items():
        if solved in value:
            value.remove(solved)

    steps.remove(solved)
    deps.pop(solved)
    completed.append(solved)
    if len(steps) == 0:
        print(''.join(completed))
        sys.exit(0)
