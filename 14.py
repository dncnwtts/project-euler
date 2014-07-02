import time

def collatz(n):
	if n % 2 == 0:
		return n/2
	else:
		return 3*n+1

def seq(n):
	i = 1
	while n != 1:
		i += 1
		n = collatz(n)
	return i

assert seq(13) == 10, "The sequence had {0} length".format(seq(13))

t0 = time.time()
maxn = 0
maxstart = 0
for i in range(1,1000000):
	n = seq(i)
	if n > maxn:
		maxn = n
		maxstart = i
print maxstart, "Took {0} seconds".format(time.time()-t0)
