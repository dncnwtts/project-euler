# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 
import time

# I modified this code from a previous problem to set an upper limit on the prime factorization. There's no need to get
# all of the primes, but I want to have a large enough number to increment so that the code doesn't take forever.
# Incidentally, there seems to be a tradeoff in the value of max_prime, with the best value being around 100. It
# increases the time spent running the code if I decrease or increase much more.
def pfs(n, max_prime = 50):
        maxn = int(n**0.5)
        base = n
        pfs = []
	i = 2
	while i < max_prime:
                while base % i == 0:
                        pfs.append(i)
                        base = base/i
		i += 1
        return pfs


def smallest(nmax):
	test = True
	smallest_factor = 1
	for i in range(1,nmax+1):
		smallest_factor *= i
	primes = list(set(pfs(smallest_factor)))
	base = 1
	for prime in primes:
		base *= prime
	smallest = base
	while test:
		smallest += base
		for i in range(2,nmax+1):
			if smallest % i != 0:
				break
		if i == nmax:
			return smallest

answer = smallest(10)

assert answer == 2520, "Test failed, I got {0}".format(answer)

t0 = time.time()
answer = smallest(20)
total = time.time() - t0
print answer, '{0} seconds'.format(total)
