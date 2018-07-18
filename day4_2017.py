import fileinput

# Part 1
# reads from STDIN
count_part1 = 0
for line in fileinput.input():
    count_part1 += 1 if len(line.split()) == len(list(set(line.split()))) else 0

# Part 2
count_part2 = 0
def identify_anagram(words):
    for index,word in enumerate(words):
        for each in words[index+1:]:
            if word == each:
                return True
    return False

for line in fileinput.input():
    words = [sorted(list(word)) for word in line.split()]
    count_part2 += 0 if identify_anagram(words) else 1
    
print(str(count_part1))
print(str(count_part2))
