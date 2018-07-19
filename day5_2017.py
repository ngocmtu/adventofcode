# s = [int(line) for line in open('input.txt','r').readlines()]
# s= [0,3,0,1,-3]

def solve_part1(s):
	new_pos = 0
	cur_pos = 0
	count = 0
	while True:
		if new_pos >= len(s) or new_pos < 0:
			return count
		else:
			count += 1
		cur_pos = new_pos
		step = s[cur_pos]
		new_pos = cur_pos + step
		s[cur_pos] += 1
    
print(str(solve_part1(s)))
