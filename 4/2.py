import operator

filepath = '/home/jesseik/adventofcode/4/input'

# Data models
class Event:
    def __init__(self, timestamp, event):
        self.timestamp = timestamp
        self.event = event

class Nap:
    def __init__(self, gid, minutes):
        self.gid = gid
        self.minutes = minutes

# Read input into events
events = []
with open(filepath) as f:
    for line in f:
        timestamp = line[1:line.index(']')]
        event = line[line.index(']')+2:line.index('\n')]
        events.append(Event(timestamp, event))

gid = 0
startMin = -1
minutes = []
naps = []
# Sort by timestamp
events.sort(key=lambda x: x.timestamp)
# Parse events into naps
for event in events:
    print(event.timestamp + " : " + event.event)

    # New shift
    if "Guard" in event.event:
        gid = event.event[event.event.index('#')+1:event.event.index('b')-1]
        continue

    if "falls" in event.event:
        startMin = event.timestamp[event.timestamp.index(':')+1:]
        continue

    if "wakes" in event.event:
        endMin = event.timestamp[event.timestamp.index(':')+1:]
        for i in range(int(startMin), int(endMin)):
           minutes.append(i)

    naps.append(Nap(gid, minutes))
    minutes = []

# Parse naps into guard specific objects
guards = {}
for nap in naps:
    if nap.gid not in guards:
        minutes = {}
        for minute in nap.minutes:
            minutes[minute] = 1
        guards[nap.gid] = minutes
        continue

    if nap.gid in guards:
        for minute in nap.minutes:
            if minute in guards[nap.gid]:
                guards[nap.gid][minute] += 1
            else:
                guards[nap.gid][minute] = 1

guard_id = 0
popular_minute = -1
minute_occurances = 0

for guard_key, guard_value in guards.items():
    occurances = 0
    for minutes_key, minutes_value in guard_value.items():
        if minutes_value > minute_occurances:
            guard_id = guard_key
            popular_minute = minutes_key
            minute_occurances = minutes_value

print(guard_id)
print(popular_minute)
answer = int(guard_id) * int(popular_minute)
print("Answer is: " + str(answer))
