# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

def pfs(n):
	maxn = int(n**0.5)
	base = n
	pfs = []
	potential_factors = range(maxn)[2:] # cutting of 1 and 2.
	for i in potential_factors:
		while base % i == 0:
			pfs.append(i)
			base = base/i
	return pfs


answer = pfs(13195)

assert answer == [5,7,13,29], "Test case failed with pfs = {0}".format(answer)

answer = max(pfs(600851475143))
print answer
