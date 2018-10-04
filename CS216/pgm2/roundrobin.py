#!/usr/bin/python3
import pprint
from math import sqrt
def helper(arrange, teams, blocksize, iteration):
	# reverse order of teams in each block
	print("iteration=",iteration)
	print("blocksize=",blocksize)
	for i in range(0, teams-blocksize+1, blocksize):
		#rev = [] # like vector in c++
		# created reversed block
		for k in range(i, i+blocksize-2, -1): #i+blocksize-1 (not -2) in c++
			#rev.append(arrange[iteration-1][k])
			arrange[iteration].append(arrange[iteration-1][k])
		# new block in arrange with reversed block
		#for m in range(i, i+blocksize):
			#arrange[iteration].append(rev[m-i])
	# if it's possible to swap more teams...
	if blocksize > 2:
		helper(arrange, teams, int(sqrt(blocksize)), iteration+1)

def main():
	teams = 4
	arrange = [[] for i in range(teams)]
	for i in range(4):
		arrange[0].append(i+1)
	helper(arrange,teams,teams, 1)
	pprint.pprint(arrange)

main()
