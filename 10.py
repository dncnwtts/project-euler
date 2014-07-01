# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
import time

# This basically implemented the the sieve of Eratosthenes, with the pseudocode on wikipedia.

def sum_primes_under(n):
	big_list = range(n)
	is_prime = [True]*len(big_list)
	is_prime[0] = False
	is_prime[1] = False
	primes = [2]
	for i in range(2,n):
		if is_prime[i]:
			for j in range(i**2,n,i):
				is_prime[j] = False
	primes = []
	for i in range(len(is_prime)):
		if is_prime[i]:
			primes.append(big_list[i])
	return sum(primes)

# Both of these methods are way too slow.
def _sum_primes_under(n):
	s = 0
	primes = []
	nums = range(2,n)
	for i in range(len(nums)):
		t0 = time.time()
		primes.append(nums[0])
		#print primes[-1]
		nums = [x for x in nums if x % nums[0] != 0]
		if len(nums) == 0:
			return sum(primes)
		print time.time() - t0

def __sum_primes_under(n):
	s = 0
	primes = []
	for i in range(2,n):
		t0 = time.time()
		is_prime = 1
		for p in primes:
			if i % p == 0:
				is_prime = 0
				break
		if is_prime == 1:
			primes.append(i)
			print time.time() - t0
	return sum(primes)



answer = sum_primes_under(10)

assert answer == 17, "Answer was {0}".format(answer)

t0 = time.time()
answer = sum_primes_under(2000000)
print answer, "Time is {0} seconds".format(time.time()-t0)
