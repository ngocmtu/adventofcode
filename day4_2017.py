import fileinput

# Part 1
# reads from STDIN
count_part1 = 0
for line in fileinput.input:
    count += 1 if len(line.split()) == len(list(set(line.split()))) else 0

print(str(count_part1))
