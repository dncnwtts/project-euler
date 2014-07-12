# Euler discovered the remarkable quadratic formula:
# 
# Considering quadratics of the form:
# 
#     n^2 + an + b, where |a| < 1000 and |b| < 1000
# 
#     where |n| is the modulus/absolute value of n
#     e.g. |11| = 11 and |-4| = 4
# 
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
# 

def is_prime(n):
	prime = True
	i = 1
	if n < 0:
		return False
	while (i <  int(n**0.5)) and prime:
		i += 1
		if n % i == 0:
			prime = False
	return prime

def quad(n,a,b):
	return n**2 + a*n + b

assert is_prime(1601), "Prime function wrong"
assert not is_prime(1681), "Prime function has false positives."

for n in range(80):
	p = n**2 - 79*n +1601
	assert is_prime(p), "Prime function is off, {0}".format(n,p)

max_primes = 0
max_prod = [0,0,0]
for a in range(-999,1000):
	if a % 250 == 0:
		print a
	for b in range(-999,1000):
		n = 0
		consec_primes = True
		while consec_primes:
			if is_prime(quad(n,a,b)):
				n += 1
			else:
				consec_primes = False
		if n > max_primes:
			max_primes = n
			max_prod = [a,b,a*b]
print max_prod	
