#   A perfect number is a number for which the sum of its proper divisors is exactly
#   equal to the number. For example, the sum of the proper divisors of 28 would be
#   1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#   
#   A number n is called deficient if the sum of its proper divisors is less than n
#   and it is called abundant if this sum exceeds n.
#   
#   As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
#   number that can be written as the sum of two abundant numbers is 24. By
#   mathematical analysis, it can be shown that all integers greater than 28123 can
#   be written as the sum of two abundant numbers. However, this upper limit cannot
#   be reduced any further by analysis even though it is known that the greatest
#   number that cannot be expressed as the sum of two abundant numbers is less than
#   this limit.
#   
#   Find the sum of all the positive integers which cannot be written as the sum of
#   two abundant numbers.
import time

def get_divisors(n):
	divs = []
	for i in range(int(n**0.5)):
		if (n/(i+1))*(i+1) == n:
			divs.append(i+1)
			divs.append(n/(i+1))
	divs = list(set(divs))
	divs.sort()
	return divs[:-1]

def is_abundant(n):
	s = sum(get_divisors(n))
	if s > n:
		return True
	else:
		return False

def is_sum(num, list_of_nums):
	max_ind = -1
	for i in range(len(list_of_nums)):
		if list_of_nums[i] > num:
			max_ind = i
			break
	list_of_nums = list_of_nums[:max_ind]
	for i in range(len(list_of_nums)):
		if num - list_of_nums[i] in list_of_nums:
			return True
		'''
		for j in range(i):
			if list_of_nums[i] + list_of_nums[j] == num:
				return True
		'''
	return False


abundant_numbers = []
n = 0
while n < 28123:
	n += 1
	if is_abundant(n):
		abundant_numbers.append(n)
assert is_abundant(12), "Abundance is off."
assert is_abundant(24), "Abundance is off..."
assert is_sum(24,abundant_numbers), "Abundance is off..."
assert is_sum(28123, abundant_numbers), "is_sum isn't working."


# We can make a list of all numbers that are sums, and a list of all numbers,
# then remove the first list from the second.
t0 = time.time()
abundant_sums = []
for i in range(len(abundant_numbers)):
	for j in range(0,i+1):
		abundant_sums.append(abundant_numbers[i]+abundant_numbers[j])
abundant_sums = list(set(abundant_sums))
print 'have all sums'

non_abundant = range(28123)
inds = []
for i in range(len(non_abundant)):
	if non_abundant[i] not in abundant_sums:
		inds.append(i)

s = 0
for i in range(len(inds)):
	s += non_abundant[inds[i]]
print s

print "This took {0} seconds".format(time.time()-t0)
