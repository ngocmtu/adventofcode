s = ['5 1 9 5','2 4 6 8','7 5 3']

def solve(s):
  sorted_rows = [sorted(list(map(int,row.split()))) for row in s]
  checksum_list = [(int(row[-1]) - int(row[0])) for row in sorted_rows]
  return sum(checksum_list)

print(solve(s))
