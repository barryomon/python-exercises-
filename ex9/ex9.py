name = input('Enter file: ')
if len(name) < 1:
    name = 'mbox-short.txt'

handle = open(name)

counts = dict()

for line in handle:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

biggest = None
biggest_count = 0

for email, count in counts.items():
    if count > biggest_count:
        biggest = email
        biggest_count = count

print(biggest, biggest_count)
