##  A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
##  
##  012   021   102   120   201   210
##  
##  What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
##  
import time

def fact(n):
	if n == 1:
		return n
	else:
		return n*fact(n-1)

def lex_perm(nums):
	nums.sort()
	if len(nums) == 2:
		return [ [nums[0], nums[1]], [nums[1],nums[0]]]
	else:
		all_nums = []
		for i in range(len(nums)):
			new_nums = list(nums)
			base = new_nums[i]
			new_nums.pop(i)
			res = lex_perm(new_nums)
			for j in range(len(res)):
				all_nums.append([base] + res[j])
		return all_nums


test_answer = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]
test = lex_perm([0,1,2])
assert test == test_answer, 'Test failed, we get {0}'.format(test)
t0 = time.time()
answer = lex_perm(range(10))
print 'Takes {0} seconds'.format(time.time()-t0)
print answer[999999]
