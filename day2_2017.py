s = ['5 1 9 5','2 4 6 8','7 5 3']

# sort ascendingly each row in s and turn all items into int
# return sum of difference of smallest and largest items in each row
def solve_part1(s):
  sorted_rows = [sorted(list(map(int,row.split()))) for row in s]
  checksum_list = [(int(row[-1]) - int(row[0])) for row in sorted_rows]
  return sum(checksum_list)

# sort descendingly each row in s and turn all items into int
# divide largest item in list with every item smaller than it until finding the perfect divider
def solve_part2(s):
  rows = [sorted(list(map(int,row.split())),reverse=True) for row in s]
  result = 0
  for row in rows:
    for index,item in enumerate(row):
      for divider in row[index+1:]:
        result += item/divider if item%divider == 0 else 0
        continue
  return result
  
print(solve_part1(s))
print(solve_part2(s))
