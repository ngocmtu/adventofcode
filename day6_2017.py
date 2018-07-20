# s = [10,3,15,10,5,15,5,15,9,2,5,8,5,2,3,6]
# s = [0, 2, 7, 0]
		
def solve(s):
	all_combo = []
	while True:
		all_combo.append(''.join([str(each) for each in s]))
		largest_idx = sorted([idx for idx,val in enumerate(s) if val == max(s)])[0]
		largest_num = s[largest_idx]
		s[largest_idx] = 0
		while largest_num > 0:
			largest_idx += 1 if largest_idx < len(s)-1 else -(len(s)-1)
			s[largest_idx] += 1
			largest_num -= 1
		if ''.join([str(each) for each in s]) in all_combo:
			return len(all_combo)
	
print(str(solve(s)))
