# 10! = 3628800 and the sum of these digits is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!.

def fact(n):
	if n == 1:
		return n
	else:
		return n*fact(n-1)

def count(n):
	numdigs = len(str(n))
	val = 0
	for i in range(numdigs)[::-1]:
		dig = n/10**i
		val += dig
		n -= dig*10**i
	return val


assert fact(10) == 3628800, "Factorial function is incorrect, {0}".format(fact(10))
assert count(fact(10)) == 27, "Sum of digits function is incorrect, {0}".format(count(fact(10)))

n = fact(100)
#print fact(100)
print count(n)
