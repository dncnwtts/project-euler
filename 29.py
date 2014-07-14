# Consider all integer combinations a**b for 2\leq a\leq 5 and 2\leq b\leq 5. There should be 15 distinct terms.

# How many are there for 2\leq a,b\leq 100?

def dist_pows(a,b):
	l = []
	for i in range(2,a+1):
		print i
		for j in range(2, b+1):
			l.append(i**j)
	l = list(set(l))
	return len(l)

ans = dist_pows(5,5)
assert ans == 15, "Doesn't work for small numbers, {0}".format(ans)

import time
t0 = time.time()
ans = dist_pows(100,100)
print time.time()-t0
print ans
