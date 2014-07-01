# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?
# 
import time

def nth_prime(n):
	# i is the number of primes
	i = 0
	primes = [2]
	num = 3
	while i < n-1:
		isprime = 1
		for p in primes:
			if num % p == 0:
				num += 1
				isprime = 0
		if isprime == 1:
			i += 1
			primes.append(num)
	return num

answer = nth_prime(6)

assert answer == 13, "Answer was {0}".format(answer)

t0 = time.time()
answer = nth_prime(10001)
t = time.time() - t0
print answer, 'Took {0} seconds'.format(t)
