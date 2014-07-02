# 2**15 == 32768 and the sum of its digits is 26. What is the sum of the digits
# of 2**1000?


n = 2**15
def sum_digits(n):
	exp = len(str(n))
	s = 0
	for i in range(exp)[::-1]:
		x = n/10**i
		n -= x*10**i
		s += x
	return s

answer = sum_digits(n)
assert answer == 26, "Sum of digits was {0}".format(answer)

print sum_digits(2**1000)
