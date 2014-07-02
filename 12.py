# What is the first triangle number to have over five hundred divisors?
import time

def triangle(n):
	num = n*(n+1)/2	
	return num

def num_divisors(n):
	divisors = []
	for i in range(1,int(n**0.5)+1):
		div1 = n/i
		if div1*i == n:
			divisors.append(div1)
			divisors.append(n/div1)
	return len(set(divisors))

def first_over(n):
	i = 0
	test = 0
	while test < n:
		test = num_divisors(triangle(i))
		if test > n:
			return triangle(i)
		else:
			i += 1


answer = first_over(5)
assert num_divisors(15) == 4, "Number of divisors is {0}".format(num_divisors(15))
assert answer == 28, "My answer was {0}".format(answer)

t0 = time.time()
answer = first_over(500)
t = time.time()-t0
print answer, "Over in {0} seconds".format(t)
