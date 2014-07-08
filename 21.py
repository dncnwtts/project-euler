##  Let d(n) be defined as the sum of proper divisors of n (numbers less than n
##  which divide evenly into n).
##  If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
##  each of a and b are called amicable numbers.
##  
##  For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
##  and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
##  142; so d(284) = 220.
##  
##  Evaluate the sum of all the amicable numbers under 10000.
##  
import time

def get_proper_divisors(n):
	r'''
	get_proper_divisors(220) = [1,2,4,5,10,11,20,22,44,55,110]
	'''
	divs = []
	for i in range(int(n**0.5)):
		div = i+1
		if (n/div)*div == n:
			divs.append(div)
			divs.append(n/div)
	divs = list(set(divs))
	divs.sort()

	return divs[:-1]

def d(n):
	divs  = get_proper_divisors(n)
	return sum(divs)


assert d(284) == 220, "Sum of proper divisors is incorrect"
assert d(220) == 284, "Sum of proper divisors is incorrect"


def amicable(n):
	if (d(d(n)) == n) & (d(n) != n):
		return True
	else:
		return False

assert amicable(284), "Amicable function doesn't work"
assert amicable(220), "Amicable function doesn't work"

n = 1
s = 0
t0 = time.time()
while n < 10000:
	n += 1
	if amicable(n):
		s += n
t = time.time()
print s, 'Took {0} seconds'.format(t-t0)
