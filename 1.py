# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(n,k):
	multiples = []
	i = 1
	while i < n:
		if k*i < n:
			multiples.append(k*i)
			i += 1
		else:
			return multiples

m3 = multiples(10,3)
m5 = multiples(10,5)
mults = m3 + m5
answer = sum(set(mults))

assert answer == 23, "Test case failed, I got {0}".format(answer)

m3 = multiples(1000,3)
m5 = multiples(1000,5)
mults = m3 + m5
answer = sum(set(mults))
print(answer)
