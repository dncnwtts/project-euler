# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def digs(n):
	s = str(n)
	digs = []
	for i in range(len(s)):
		digs.append(int(s[i]))
	return digs

d = digs(1634)
s = 0
for i in range(len(d)):
	s += d[i]**4

def sum_digs(n, p):
	d = digs(n)
	s = 0
	for i in range(len(d)):
		s += d[i]**p
	return s

assert 1634 == sum_digs(1634,4), "Doesn't work"
assert 8208 == sum_digs(8208,4), "Doesn't work"
assert 9474 == sum_digs(9474,4), "Doesn't work"

def find_eqs(p):
	n = 1
	s = 0
	while n < 500000:
		n += 1
		if n == sum_digs(n, p):
			s += n
	return s

assert find_eqs(4) == 19316, "Big function failed."

print find_eqs(5)
