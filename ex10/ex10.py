fname = input("enter file name:")
fname  = open(fname)

counts = {}

for line in fname:
    if line.startswith("From "):
        line = line.split()
        line = line[5]
        line = line.split(":")
        counts[line[0]] = counts.get(line[0], 0) + 1
for line, value in counts.items():
    print(line, value)