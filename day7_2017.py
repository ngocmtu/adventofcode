#!/usr/bin/env python
s = open('test.txt','r').readlines()
	
def solve(s):
	top_progs = []
	all_progs = []
	for line in s:
		if line.find('>') > -1:
			prog = line[:line.find('(')-1]
			all_progs.append(prog)
			line = line[line.find('>')+1:]
			top_progs += [each.replace(',','') for each in line.split()]
	return (str( set(all_progs) - set(top_progs)))

print(solve(s))
